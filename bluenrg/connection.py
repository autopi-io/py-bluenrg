import logging
import serial
import threading

from .packet import Packet, EventPacket
from .util import ResultMatcher, WorkerThread


log = logging.getLogger(__name__)


class TimeoutException(Exception):
    pass


class SerialConnection(object):

    def __init__(self, device="", baudrate=115200, timeout=1, event_callback=None):
        self._serial = serial.Serial(
            baudrate=baudrate,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=timeout)
        if device:
            self._serial.port = device

        self._receiver_thread = None
        self._reply_matcher = ResultMatcher()

        self.event_callback = event_callback

    @property
    def device(self):
        return self._serial.port

    @device.setter
    def device(self, value):
        self._serial.port = value

    @property
    def baudrate(self):
        return self._serial.baudrate

    @baudrate.setter
    def baudrate(self, value):
        self._serial.baudrate = value

    @property
    def timeout(self):
        return self._serial.timeout

    @baudrate.setter
    def timeout(self, value):
        self._serial.timeout = value

    @property
    def is_open(self):
        return self._serial.is_open

    def open(self):
        if log.isEnabledFor(logging.DEBUG):
            log.debug("Opening connection...")

        # Open serial port and flush buffers
        self._serial.open()
        self._serial.reset_input_buffer()
        self._serial.reset_output_buffer()

        # Start receiver thread if not alive
        if not self._receiver_thread or not self._receiver_thread.is_alive():
            self._receiver_thread = WorkerThread(target=self.__recv_event)
            self._receiver_thread.start()

        log.info("Connection opened")

    def close(self):
        if log.isEnabledFor(logging.DEBUG):
            log.debug("Closing connection...")

        # Kill receiver thread
        if self._receiver_thread:
            self._receiver_thread.kill()
            self._receiver_thread = None

        # Close serial port
        self._serial.close()

        log.info("Connection closed")

    def exec_async(self, cmd):
        self.__send(cmd)

    def exec_sync(self, cmd, reply="HCI_COMMAND_COMPLETE_EVENT", raise_on_error=True, timeout=1):

        res_cls = getattr(cmd.__class__, reply, None)
        if res_cls == None:
            raise ValueError("No reply class found for command {:}".format(cmd))

        # Setup result matcher
        res = self._reply_matcher.setup(lambda r: r.__class__ == res_cls)

        # Send command
        self.__send(cmd)

        # Wait for reply or until timeout reached
        res = self._reply_matcher.wait(timeout)
        if res == None:
            raise TimeoutException("No {:} result matched within timeout of {:} second(s)".format(res_cls, timeout))

        # Check for exception in result
        if isinstance(res, Exception):
            raise res

        # Check status parameter in packet
        if raise_on_error:
            status = getattr(res, "Status", 0)
            if status != 0x00:
                desc = bluenrg.codes.STATUS_ERROR_CODES.get(status, "Unknown")
                raise Exception("{:} (status code 0x{:02x})".format(desc, status))

        return res

    def __send(self, cmd):
        data = cmd.pack() if isinstance(cmd, Packet) else cmd

        if log.isEnabledFor(logging.DEBUG):
            log.debug("TX: {:}".format(" ".join(format(d, "02x") for d in data)))

        self._serial.write(data)

    def __recv(self, length):
        data = self._serial.read(length)
        if not data:
            raise TimeoutException("No data received within timeout of {:} second(s)".format(self._serial.timeout))
        if len(data) < length:
            raise TimeoutException("Partial data received ({:}/{:} bytes) received within timeout of {:} second(s)".format(len(data), length, self._serial.timeout))

        return data

    def __recv_event(self):

        # First check for pending data
        if not self._serial.in_waiting:

            # No data - wait for termination or timeout interval
            if self._receiver_thread.wait():
                if log.isEnabledFor(logging.DEBUG):
                    log.debug("Event receiver terminated during wait")

            return

        data = bytearray()
        try:

            # Receive header
            data.extend(self.__recv(3))
            if data[EventPacket.OFFSET_TYPE] != EventPacket.TYPE:
                raise Exception("Got invalid event packet type {:02x}".format(data[EventPacket.OFFSET_TYPE]))

            # Receive payload
            length = int(data[EventPacket.OFFSET_DATA_LENGTH])
            if length > 0:
                data.extend(self.__recv(length))

            # Unpack data
            event = EventPacket.unpack(data)

            # Call reply matcher
            is_reply = self._reply_matcher.match(event)

            # Perform callback
            if self.event_callback:
                try:
                    self.event_callback(event)
                except:
                    log.exception("Error in event callback function")
            else:
                if not is_reply:
                    log.warning("No callback function registered to handle event packet {:}".format(event))

        except Exception as ex:
            log.exception("Failed to receive event packet: {:}".format(" ".join(format(d, "02x") for d in data)))

            self._reply_matcher.fail(ex)

            # Flush any remaining data in read buffer
            self._serial.reset_input_buffer()

        finally:

            if log.isEnabledFor(logging.DEBUG) and data:
                log.debug("RX: {:}".format(" ".join(format(d, "02x") for d in data)))
