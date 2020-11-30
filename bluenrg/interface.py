import json
import logging
import Queue

from . import codes, commands, events
from .util import WorkerThread


log = logging.getLogger(__name__)


class Interface(object):

    def __init__(self, conn):
        self._conn = conn

        conn.event_callback = self.__on_event
        
        self._event_queue = Queue.Queue()
        self._dispatcher_thread = None
        self._event_listeners = {}

        self._gatt_services = {}

        self._command_history = []
        self._event_history = [] 

    @property
    def is_running(self):
        return self._conn.is_open \
            and self._conn._receiver_thread != None and self._conn._receiver_thread.is_alive() \
            and self._dispatcher_thread != None and self._dispatcher_thread.is_alive()

    @property
    def command_history(self):
        return self._command_history

    @property
    def event_history(self):
        return self._event_history

    @property
    def gatt_services(self):
        return self._gatt_services

    def add_gatt_service(self, name, *args, **kwargs):
        if name in self._gatt_services:
            raise ValueError("GATT service with name '{:}' already exists".format(name))

        ret = GATTService(self, name, *args, **kwargs)
        self._gatt_services[name] = ret

        return ret

    @property
    def event_listeners(self):
        return self._event_listeners

    def add_event_listener(self, event, func):
        self._event_listeners.setdefault(event, []).append(func)

    def mac_address(self):
        res = self._conn.exec_sync(commands.ACI_HAL_READ_CONFIG_DATA(
            Offset=0x80
        ))

        return ":".join(format(b, "02X") for b in bytearray(reversed(res.Data)))

    def start(self):
        if log.isEnabledFor(logging.DEBUG):
            log.debug("Starting interface...")

        # Ensure connection is open
        if not self._conn.is_open:
            self._conn.open()

        # Start dispatcher thread if not alive
        if not self._dispatcher_thread or not self._dispatcher_thread.is_alive():
            self._dispatcher_thread = WorkerThread(target=self.__dispatch_event)
            self._dispatcher_thread.start()

        log.info("Interface started")

    def stop(self):
        if log.isEnabledFor(logging.DEBUG):
            log.debug("Stopping interface...")
        
        # Kill dispatcher thread
        if self._dispatcher_thread:
            self._dispatcher_thread.kill()
            self._dispatcher_thread = None
        
        # Close connection
        if self._conn.is_open:
            self._conn.close()

        log.info("Interface stopped")

    def clear(self):
        self._gatt_services = {}

        self._command_history = []
        self._event_history = [] 

    def __on_event(self, event):
        if isinstance(event, events.HCI_COMMAND_COMPLETE_EVENT):
            self._command_history.append(event)
        else:
            self._event_history.append(event)

            self._event_queue.put_nowait(event)

    def __dispatch_event(self):

        if self._event_queue.empty():

            # No event - wait for termination or timeout interval
            if self._dispatcher_thread.wait():
                if log.isEnabledFor(logging.DEBUG):
                    log.debug("Event dispatcher terminated during wait")

            return

        try:
            event = self._event_queue.get(block=False)
        except Queue.Empty:
            return

        # Invoke event listeners
        if log.isEnabledFor(logging.DEBUG):
            log.debug("Invoking listener(s) for event {:}".format(event))

        for listener in self._event_listeners.get(type(event), []):
            try:
                listener(event)
            except:
                log.exception("Error in event listener {:}".format(listener))


class GATTService(object):

    def __init__(self, interface, name, handle=None):
        self._interface = interface
        self._name = name
        self._handle = handle
        self._characteristics = {}
        self._characteristic_value_handles = {}

        # Listen for characteristic modified events
        interface.add_event_listener(events.ACI_GATT_ATTRIBUTE_MODIFIED_EVENT, self.__attribute_modified_listener)

    @property
    def characteristics(self):
        return self._characteristics

    def add_characteristic(self, name, *args, **kwargs):
        if name in self._characteristics:
            raise ValueError("Characteristic with name '{:}' already exists")

        ret = self.Characteristic(self, name, *args, **kwargs)
        self._characteristics[name] = ret
        self._characteristic_value_handles[ret.value_handle] = ret

        return ret

    def __attribute_modified_listener(self, event):

        # Find characteristic by handle
        char = self._characteristic_value_handles.get(event.Attr_Handle, None)
        if char == None:
            log.warning("No registered characteristic found for attribute modified event {:}".format(event))

            return

        if char.value_callback:
            char.value_callback(event.Attr_Data)
        else:
            log.info("No characteristic value callback function defined to handle attribute modified event {:}".format(event))

    class Characteristic(object):

        def __init__(self, service, name, handle=None, value_callback=None, value=None):
            self._service = service
            self._name = name
            self._handle = handle
            self._value_callback = value_callback
            if value != None:
                self.update_value(value)

        @property
        def name(self):
            return self._name

        @property
        def handle(self):
            return self._handle

        @property
        def value_handle(self):
            return self._handle + 1

        @property
        def value_callback(self):
            return self._value_callback

        def read_value(self):
            raise NotImplementedError()

        def update_value(self, data):
            if not self._handle:
                raise ValueError("No handle defined for characteristic '{:}'".format(self._name))

            log.info("Updating characteristic '{:}' with value '{:}'".format(self._name, data))

            self._service._interface._conn.exec_sync(commands.ACI_GATT_UPDATE_CHAR_VALUE(
                Service_Handle=self._service._handle,
                Char_Handle=self._handle,
                Char_Value_Length=len(data),
                Char_Value=data
            ))


class GATTTerminalInterface(Interface):

    SERV_TERM = "terminal"
    CHAR_AUTH = "authentication"
    CHAR_CMD = "command"
    CHAR_RES = "result"

    CODE_SUCCESS            = 0
    CODE_AUTH_REQUIRED      = 1
    CODE_AUTH_EXPIRED       = 2
    CODE_AUTH_FAILED        = 3
    CODE_CMD_INVALID        = 6
    CODE_CMD_FAILED         = 7
    CODE_INACTIVITY_TIMEOUT = 9

    def __init__(self, conn):
        super(GATTTerminalInterface, self).__init__(conn)

        self._auth_token = ""
        self._last_interaction = None  # TODO HN: Auto disconnect after inactivity?

        self._service = None
        self._result_char = None

        self.on_authenticate = None
        self.on_execute = None

        self.add_event_listener(events.HCI_LE_CONNECTION_COMPLETE_EVENT, self.__client_connect)
        self.add_event_listener(events.HCI_DISCONNECTION_COMPLETE_EVENT, self.__client_disconnect)

    @property
    def is_running(self):
        return super(GATTTerminalInterface, self).is_running and self._service != None

    def start(self):
        super(GATTTerminalInterface, self).start()

        if self._service == None:

            # Get GATT service handles from device
            res = self._conn.exec_sync(commands.APP_GATT_GET_TERMINAL_HANDLES())

            # Build GATT service model for terminal interaction
            self._service = self.add_gatt_service(self.SERV_TERM, handle=res.Service_Handle)
            self._service.add_characteristic(self.CHAR_AUTH, handle=res.Auth_Char_Handle, value_callback=self.__recv_auth_token)
            self._service.add_characteristic(self.CHAR_CMD, handle=res.Command_Char_Handle, value_callback=self.__exec_cmd)
            self._result_char = self._service.add_characteristic(self.CHAR_RES, handle=res.Result_Char_Handle)

            # Initially reset authentication
            self.__reset_auth(self.CODE_AUTH_REQUIRED)

    def stop(self):
        super(GATTTerminalInterface, self).stop()

        self.clear()

        self._service = None
        self._result_char = None

        self._auth_token = ""

    def __client_connect(self, event):
        self.__reset_auth(self.CODE_AUTH_REQUIRED)

    def __client_disconnect(self, event):

        # Clear authentication token
        self._auth_token = ""

    def __reset_auth(self, code):

        # Clear authentication token
        self._auth_token = ""

        # Set result code
        self.__result(code)

    def __result(self, code, data=None):
        res = {
            "code": code
        }

        if data:
            res["data"] = data

        self._result_char.update_value(json.dumps(res, separators=(",", ":")))

    def __recv_auth_token(self, val):
        self._auth_token += val

    def __exec_cmd(self, val):

        # Check for authentication token
        if not self._auth_token:
            log.warning("Attempted to execute command without authentication token: {:}".format(val))

            self.__reset_auth(self.CODE_AUTH_REQUIRED)

            return

        # Perform authentication
        try:
            if not self.on_authenticate(self._auth_token):
                log.warning("Expired authentication token when attempting to execute command: {:}".format(val))

                self.__reset_auth(self.CODE_AUTH_EXPIRED)

                return

        except:
            log.exception("Failed to authenticate token of length {:} when attempting to execute command: {:}".format(len(self._auth_token), val))

            self.__reset_auth(self.CODE_AUTH_FAILED)

            return

        # Parse command
        try:
            cmd = json.loads(val)
        except:
            log.exception("Invalid command: {:}".format(val))
            
            # Set error result
            self.__result(self.CODE_CMD_INVALID)

            return

        # Execute command
        try:
            res = self.on_execute(cmd["cmd"], *cmd.get("args", []), **cmd.get("kwargs", {}))
        except:
            log.exception("Failed to execute command: {:}".format(cmd))

            # Set error result
            self.__result(self.CODE_CMD_FAILED)

            return

        # Set successful result
        self.__result(self.CODE_SUCCESS, data=res)

        log.info("Successfully executed command: {:}".format(cmd))
