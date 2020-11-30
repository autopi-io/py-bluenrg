import logging
import struct

from collections import OrderedDict

from .util import cached_inheritors, set_attr_default


log = logging.getLogger(__name__)


class Parameter(object):
    """
    See: https://docs.python.org/2/howto/descriptor.html#properties
    """

    VALUES_KEY = "_parameter_values"

    def __init__(self, order=0, size=1, choices={}, multi_choice=False, ranges={}):
        self.order = order
        self.size = size
        self.choices = choices
        self.multi_choice = multi_choice
        self.ranges = ranges

    def __get__(self, obj, objtype=None):
        return set_attr_default(obj, self.VALUES_KEY, {}).get(self, None)

    def __set__(self, obj, val):
        self.validate(obj, val)

        set_attr_default(obj, self.VALUES_KEY, {})[self] = val

    def actual_sizes(self, obj):
        ret = self.size

        # Check for variable size(s)
        if isinstance(self.size, Parameter):
            ret = set_attr_default(obj, self.VALUES_KEY, {}).get(self.size, 0)

        return ret if isinstance(ret, tuple) else (ret,)

    def validate(self, obj, val):
        if not self.validate_size(obj, val):
            raise ValueError("Invalid size")

        if self.choices and self.ranges:
            if not self.validate_choice(val) and not self.validate_range(val):
                raise ValueError("Invalid {:} and out of range".format("multi choice" if self.multi_choice else "choice"))
        elif self.choices and not self.validate_choice(val):
            raise ValueError("Invalid multi choice" if self.multi_choice else "Invalid choice")
        elif self.ranges and not self.validate_range(val):
            raise ValueError("Out of range")  

    def validate_size(self, obj, val):
        ret = False

        # Validate multiple sizes
        for size in self.actual_sizes(obj):
            if isinstance(val, int):
                ret = val.bit_length() <= size * 8
            elif isinstance(val, str):
                ret = len(bytearray(val)) == size

            if ret:
                break

        return ret

    def validate_choice(self, val):
        if self.multi_choice:
            # Validate bitmask
            return min(self.choices.keys()) <= val <= sum(self.choices.keys())
        else:
            return val in self.choices

    def validate_range(self, val):
        ret = False

        # Validate multiple ranges
        for rang, desc in self.ranges.iteritems():
            ret = rang[0] <= val <= rang[1]
            if ret:
                break

        return ret


class Packet(object):
    """
    """

    OFFSET_TYPE = 0x00

    def __init__(self, **kwargs):

        # Sort by parameter order
        params = self.all_parameters(sort_by="order")
        for key in sorted(kwargs.keys(), key=lambda k: getattr(params.get(k), "order", 0)):
            if not hasattr(self, key):
                raise ValueError("Unknown parameter '{:}'".format(key))

            try:
                setattr(self, key, kwargs[key])
            except ValueError as ve:
                raise ValueError("Cannot set parameter '{:}' value {:}: {:}".format(key, repr(kwargs[key]), ve))

    def __str__(self):
        return "<object '{:}.{:}'({:})>".format(
            self.__class__.__module__,
            self.__class__.__name__,
            ", ".join(["{:}={:}".format(n, repr(self.value_of(p))) for n, p in self.all_parameters(sort_by="order").iteritems()])
        )

    def value_of(self, parameter, default=0):
        """
        Gets actual value for a given parameter object.
        """

        return getattr(self, Parameter.VALUES_KEY, {}).get(parameter, default)

    def as_dict(self):
        """
        Converts object to dictionary.
        """

        return {n: self.value_of(p) for n, p in self.all_parameters(sort_by="order").iteritems()}

    def pack(self):
        """
        Packs entire packet into byte array.
        """

        ret = bytearray()

        if log.isEnabledFor(logging.DEBUG):
            log.debug("Packing {:} to {:}".format(self, type(ret)))

        # Add type
        ret.append(struct.pack("<B", self.__class__.TYPE))  # Unsigned char (1 byte)

        # Add code
        if self.__class__.OFFSET_DATA_LENGTH > 2:
            ret.extend(struct.pack("<H", self.__class__.CODE))  # Unsigned short (2 bytes)
        else:
            ret.extend(struct.pack("<B", self.__class__.CODE))  # Unsigned char (1 byte)

        # Add empty length (will be updated later)
        ret.append(0x00)  # Unsigned char (1 byte)
        length_index = len(ret) - 1
        length_total = 0

        # Add all parameters sorted by order
        for name, parameter in self.all_parameters(sort_by="order").iteritems():
            value = self.value_of(parameter)

            # Ensure is valid
            try:
                parameter.validate(self, value)
            except ValueError as ve:
                raise ValueError("Cannot pack parameter '{:}' value {:}: {:}".format(name, repr(value), ve))

            sizes = parameter.actual_sizes(self)
            # TODO HN: Support use multiple sizes?
            size = sizes[0]

            # Skip if size is zero
            if size == 0:
                log.info("Skipping pack of parameter '{:}' because size is zero".format(name))

                continue

            # Pack value
            if isinstance(value, int):
                if size == 2:
                    ret.extend(struct.pack("<H", value))  # Unsigned short (2 bytes)
                else:
                    ret.extend(struct.pack("<{:}B".format(size), value))  # Unsigned char array (n bytes)
            elif isinstance(value, str):
                ret.extend(struct.pack("<{:}s".format(size), value))  # Char array (n bytes)
            else:
                raise NotImplementedError("Pack of parameter '{:}' value of {:} not supported".format(name, type(value)))

            length_total += size

        # Update length
        ret[length_index] = struct.pack("<B", length_total)  # Unsigned char (1 byte)

        log.info("Packed {:} to <type 'bytearray'({:})>".format(self, " ".join(format(d, "02x") for d in ret)))

        return ret

    @staticmethod
    def unpack(data):
        """
        Unpacks from bytes.
        """

        cls = Packet.type_class_for(data).impl_class_for(data)

        if log.isEnabledFor(logging.DEBUG):
            log.debug("Unpacking <type 'bytearray'({:})> to {:}".format(" ".join(format(d, "02x") for d in data), cls))

        # Instantiate class
        obj = cls()

        # Unpack parameters
        offset = cls.OFFSET_DATA_LENGTH + 1
        for name, parameter in cls.all_parameters(sort_by="order").iteritems():

            sizes = parameter.actual_sizes(obj)
            # TODO HN: Support use multiple sizes?
            size = sizes[0]

            # Skip if size is zero
            if size == 0:
                log.info("Skipping unpack of parameter '{:}' because size is zero".format(name))

                continue

            # Unpack value
            if size == 1:
                value = struct.unpack_from("<B", data, offset)[0]  # Unsigned char (1 byte)
            elif size == 2:
                value = struct.unpack_from("<H", data, offset)[0]  # Unsigned short (2 bytes)
            else:
                value = struct.unpack_from("<{:}s".format(size), data, offset)[0]  # Char array (n bytes)

            # Set parameter value
            try:
                setattr(obj, name, value)
            except ValueError as ve:
                raise ValueError("Cannot unpack parameter '{:}' value {:}: {:}".format(name, repr(value), ve))

            offset += size

        log.info("Unpacked <type 'bytearray'({:})> to {:}".format(" ".join(format(d, "02x") for d in data), obj))

        return obj

    @classmethod
    def all_parameters(cls, sort_by):
        ret = OrderedDict()

        # TODO HN: Cache this result?

        # Retrieve recursively
        for base_cls in [c for c in cls.__bases__ if issubclass(c, Packet)]:
            ret.update(base_cls.all_parameters(sort_by))

        params = {k: v for k, v in cls.__dict__.iteritems() if isinstance(v, Parameter)}
        ret.update(sorted(params.iteritems(), key=lambda p: getattr(p[1], sort_by)))

        return ret

    @classmethod
    def type_class_for(cls, data):
        if not data:
            raise ValueError("No data")

        type = struct.unpack_from("<B", data, cls.OFFSET_TYPE)[0]

        ret = cached_inheritors(cls, lambda c: c.TYPE).get(type, None)
        if ret == None:
            raise ValueError("Unsupported packet type {:}".format(type))

        return ret


class CommandPacket(Packet):
    """
    """

    TYPE = 0x01

    OFFSET_OPCODE      = 0x01
    OFFSET_DATA_LENGTH = 0x03

    @classmethod
    def impl_class_for(cls, data):
        code = struct.unpack_from("<H", data, cls.OFFSET_OPCODE)[0]  # Unsigned short (2 bytes)

        cmd_cls = cached_inheritors(cls, lambda c: c.CODE).get(code, None)
        if cmd_cls == None:
            raise NotImplementedError("No command packet found by code {:}".format(code))

        return cmd_cls


class AsynchronousDataPacket(Packet):
    """
    """

    TYPE = 0x02

    @classmethod
    def impl_class_for(cls, data):
        raise NotImplementedError()


class SynchronousDataPacket(Packet):
    """
    """

    TYPE = 0x03

    @classmethod
    def impl_class_for(cls, data):
        raise NotImplementedError()


class EventPacket(Packet):
    """
    """

    TYPE = 0x04

    OFFSET_CODE        = 0x01
    OFFSET_DATA_LENGTH = 0x02

    @classmethod
    def impl_class_for(cls, data):
        code = struct.unpack_from("<B", data, cls.OFFSET_CODE)[0]  # Unsigned char (1 byte)

        evt_cls = cached_inheritors(cls, lambda c: c.CODE).get(code, None)
        if evt_cls == None:
            raise NotImplementedError("No event packet found by code {:}".format(code))

        # Check for subclasses
        if evt_cls.__subclasses__():

            if "Subcode" in evt_cls.__dict__:
                subcode = struct.unpack_from("<B" if evt_cls.__dict__["Subcode"].size == 1 else "<H", data, cls.OFFSET_DATA_LENGTH + 1)[0]

                # Find the subclass
                subevt_cls = cached_inheritors(evt_cls, lambda c: c.SUBCODE).get(subcode, None)
                if subevt_cls == None:
                    raise NotImplementedError("No event packet found by subcode {:} for event {:}".format(subcode, evt_cls))

                evt_cls = subevt_cls

            elif "Command_Opcode" in evt_cls.__dict__:
                cmd_code = struct.unpack_from("<H", data, cls.OFFSET_DATA_LENGTH + 2)[0]

                # Find the command class
                cmd_cls = cached_inheritors(CommandPacket, lambda c: c.CODE).get(cmd_code, None)
                if cmd_cls == None:
                    raise NotImplementedError("No command packet found by code {:} for event {:}".format(cmd_code, evt_cls))

                # Find the inner event class
                evt_cls = getattr(cmd_cls, evt_cls.__name__, None)
                if evt_cls == None:
                    raise NotImplementedError("No event packet found named '{:}' in command {:}".format(evt_cls.__name__, cmd_cls))

            else:
                raise NotImplementedError("Found {:} unsupported subclasses of {:}".format(len(evt_cls.__subclasses__()), evt_cls))

        return evt_cls


class LEMetaEventPacket(EventPacket):
    """
    """

    CODE = 0x3E

    Subcode = Parameter(order=1, size=1)


class VendorEventPacket(EventPacket):
    """
    """

    CODE = 0xFF

    Subcode = Parameter(order=1, size=2)
