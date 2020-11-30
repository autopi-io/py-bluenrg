# NOTE: This file is auto-generated, please do not modify

from ..packet import *
from .. import events


class HCI_DISCONNECT(CommandPacket):
    """
    The HCI_DISCONNECT is used to terminate an existing connection. The
    Connection_Handle command parameter indicates which connection is to be
    disconnected. The Reason command parameter indicates the reason for ending
    the connection. The remote Controller will receive the Reason command
    parameter in the HCI_DISCONNECTION_COMPLETE_EVENT event. All synchronous connections
    on a physical link should be disconnected before the ACL connection on the
    same physical connection is disconnected.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.1.6)
    It is important to leave an 100 ms blank window before sending any new command (including system hardware reset),
    since immediately after HCI_DISCONNECTION_COMPLETE_EVENT event, system could save important information in non volatile memory.
    """

    CODE = 0x0406

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Reason_Choices = {
        0x05: "Authentication Failure",
        0x13: "Remote User Terminated Connection",
        0x14: "Remote Device Terminated Connection due to Low Resources",
        0x15: "Remote Device Terminated Connection due to Power Off",
        0x1A: "Unsupported Remote Feature",
        0x3B: "Unacceptable Connection Parameters",
    }
    Reason = Parameter(order=2, size=1, choices=Reason_Choices)
    """
    The reason for ending the connection.
    """


class HCI_READ_REMOTE_VERSION_INFORMATION(CommandPacket):
    """
    This command will obtain the values for the version information for the remote
    device identified by the Connection_Handle parameter. The Connection_Handle
    must be a Connection_Handle for an ACL or LE connection.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.1.23)
    """

    CODE = 0x041D

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Specifies which Connection_Handle's version information to get.
    """


class HCI_SET_EVENT_MASK(CommandPacket):
    """
    The Set_Event_Mask command is used to control which events are generated
    by the HCI for the Host.
    
    If the bit in the Event_Mask is set to a one, then the
    event associated with that bit will be enabled. For an LE Controller, the LE
    Meta Event bit in the Event_Mask shall enable or disable all LE events in the
    LE Meta Event (see Section 7.7.65). The Host has to deal with each event that
    occurs. The event mask allows the Host to control how much it is interrupted.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.3.1)
    """

    CODE = 0x0C01

    Event_Mask_Choices = {
        0x0000000000000000: "No events specified",
        0x0000000000000001: "Inquiry Complete Event",
        0x0000000000000002: "Inquiry Result Event",
        0x0000000000000004: "Connection Complete Event",
        0x0000000000000008: "Connection Request Event",
        0x0000000000000010: "Disconnection Complete Event",
        0x0000000000000020: "Authentication Complete Event",
        0x0000000000000040: "Remote Name Request Complete Event",
        0x0000000000000080: "Encryption Change Event",
        0x0000000000000100: "Change Connection Link Key Complete Event",
        0x0000000000000200: "Master Link Key Complete Event",
        0x0000000000000400: "Read Remote Supported Features Complete Event",
        0x0000000000000800: "Read Remote Version Information Complete Event",
        0x0000000000001000: "QoS Setup Complete Event",
        0x0000000000008000: "Hardware Error Event",
        0x0000000000010000: "Flush Occurred Event",
        0x0000000000020000: "Role Change Event",
        0x0000000000080000: "Mode Change Event",
        0x0000000000100000: "Return Link Keys Event",
        0x0000000000200000: "PIN Code Request Event",
        0x0000000000400000: "Link Key Request Event",
        0x0000000000800000: "Link Key Notification Event",
        0x0000000001000000: "Loopback Command Event",
        0x0000000002000000: "Data Buffer Overflow Event",
        0x0000000004000000: "Max Slots Change Event",
        0x0000000008000000: "Read Clock Offset Complete Event",
        0x0000000010000000: "Connection Packet Type Changed Event",
        0x0000000020000000: "QoS Violation Event",
        0x0000000040000000: "Page Scan Mode Change Event",
        0x0000000080000000: "Page Scan Repetition Mode Change Event",
        0x0000000100000000: "Flow Specification Complete Event",
        0x0000000200000000: "Inquiry Result with RSSI Event",
        0x0000000400000000: "Read Remote Extended Features Complete Event",
        0x0000080000000000: "Synchronous Connection Complete Event",
        0x0000100000000000: "Synchronous Connection Changed Event",
        0x0000200000000000: "Sniff Subrating Event",
        0x0000400000000000: "Extended Inquiry Result Event",
        0x0000800000000000: "Encryption Key Refresh Complete Event",
        0x0001000000000000: "IO Capability Request Event",
        0x0002000000000000: "IO Capability Request Reply Event",
        0x0004000000000000: "User Confirmation Request Event",
        0x0008000000000000: "User Passkey Request Event",
        0x0010000000000000: "Remote OOB Data Request Event",
        0x0020000000000000: "Simple Pairing Complete Event",
        0x0080000000000000: "Link Supervision Timeout Changed Event",
        0x0100000000000000: "Enhanced Flush Complete Event",
        0x0400000000000000: "User Passkey Notification Event",
        0x0800000000000000: "Keypress Notification Event",
        0x1000000000000000: "Remote Host Supported Features Notification Event",
        0x2000000000000000: "LE Meta-Event",
    }
    Event_Mask = Parameter(order=1, size=8, choices=Event_Mask_Choices, multi_choice=True)
    """
    Event mask. Default: 0x00001FFFFFFFFFFF
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_RESET(CommandPacket):
    """
    The Reset command will reset the Link Layer on an LE
    Controller.
    
    The Reset command shall not affect the used HCI transport layer since the HCI transport
    layers may have reset mechanisms of their own. After the reset is completed,
    the current operational state will be lost, the Controller will enter standby mode
    and the Controller will automatically revert to the default values for the parameters
    for which default values are defined in the specification.
    Note: The Reset command will not necessarily perform a hardware reset. This
    is implementation defined. 
    The Host shall not send additional HCI commands before the Command Complete
    event related to the Reset command has been received.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.3.2)
    """

    CODE = 0x0C03

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_READ_TRANSMIT_POWER_LEVEL(CommandPacket):
    """
    This command reads the values for the Transmit_Power_Level parameter for
    the specified Connection_Handle. The Connection_Handle shall be a Connection_Handle
    for an ACL connection.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.3.35)
    """

    CODE = 0x0C2D

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Specifies which Connection_Handle's Transmit Power Level setting to read.
    """

    Type_Choices = {
        0x00: "Read Current Transmit Power Level.",
        0x01: "Read Maximum Transmit Power Level.",
    }
    Type = Parameter(order=2, size=1, choices=Type_Choices)
    """
    Current or maximum transmit power level.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Connection_Handle_Ranges = {
            (0x0000, 0x0EFF): "N/A",
        }
        Connection_Handle = Parameter(order=2, size=2, ranges=Connection_Handle_Ranges)
        """
        Connection handle that identifies the connection.
        """

        Transmit_Power_Level_Ranges = {
            (-30, 20): "N/A",
        }
        Transmit_Power_Level = Parameter(order=3, size=1, ranges=Transmit_Power_Level_Ranges)
        """
        Size: 1 Octet (signed integer)
        Units: dBm
        """


class HCI_READ_LOCAL_VERSION_INFORMATION(CommandPacket):
    """
    This command reads the values for the version information for the local Controller.
    The HCI Version information defines the version information of the HCI layer.
    The LMP/PAL Version information defines the version of the LMP or PAL. The
    Manufacturer_Name information indicates the manufacturer of the local device.
    The HCI Revision and LMP/PAL Subversion are implementation dependent.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.4.1)
    """

    CODE = 0x1001

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        HCI_Version = Parameter(order=2, size=1)
        """
        See Bluetooth Assigned Numbers (https://www.bluetooth.org/en-us/specification/assigned-numbers)
        """

        HCI_Revision = Parameter(order=3, size=2)
        """
        Revision of the Current HCI in the BR/EDR Controller.
        """

        LMP_PAL_Version = Parameter(order=4, size=1)
        """
        Version of the Current LMP or PAL in the Controller.
        See Bluetooth Assigned Numbers (https://www.bluetooth.org/en-us/specification/assigned-numbers)
        """

        Manufacturer_Name = Parameter(order=5, size=2)
        """
        Manufacturer Name of the BR/EDR Controller.
        See Bluetooth Assigned Numbers (https://www.bluetooth.org/en-us/specification/assigned-numbers)
        """

        LMP_PAL_Subversion = Parameter(order=6, size=2)
        """
        Subversion of the Current LMP or PAL in the Controller. This value is
        implementation dependent.
        """


class HCI_READ_LOCAL_SUPPORTED_COMMANDS(CommandPacket):
    """
    This command reads the list of HCI commands supported for the local Controller.
    This command shall return the Supported_Commands configuration parameter.
    It is implied that if a command is listed as supported, the feature underlying
    that command is also supported.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.4.2)
    """

    CODE = 0x1002

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Supported_Commands = Parameter(order=2, size=64)
        """
        Bit mask for each HCI Command. If a bit is 1, the Controller supports the
        corresponding command and the features required for the command.
        Unsupported or undefined commands shall be set to 0.
        """


class HCI_READ_LOCAL_SUPPORTED_FEATURES(CommandPacket):
    """
    This command requests a list of the supported features for the local 
    Controller. This command will return a list of the LMP features. For details see
    Part C, Link Manager Protocol Specification on page 227.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.4.3)
    """

    CODE = 0x1003

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        LMP_Features = Parameter(order=2, size=8)
        """
        Bit Mask List of LMP features.
        """


class HCI_READ_BD_ADDR(CommandPacket):
    """
    On an LE Controller, this command shall read the Public Device Address as
    defined in [Vol 6] Part B, Section 1.3, Device Address. If this Controller does
    not have a Public Device Address, the value 0x000000000000 shall be
    returned.
    On an LE Controller, the public address shall be the same as the
    BD_ADDR.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.4.6)
    """

    CODE = 0x1009

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        BD_ADDR = Parameter(order=2, size=6)
        """
        BD_ADDR ( Bluetooth Device Address) of the Device.
        """


class HCI_READ_RSSI(CommandPacket):
    """
    This command reads the Received Signal Strength Indication (RSSI) value from
    a Controller.
    For an LE transport, a Connection_Handle is used as the Handle command
    parameter and return parameter. The meaning of the RSSI metric is an absolute
    receiver signal strength value in dBm to +/- 6 dB accuracy. If the RSSI cannot
    be read, the RSSI metric shall be set to 127.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.5.4)
    """

    CODE = 0x1405

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Connection_Handle_Ranges = {
            (0x0000, 0x0EFF): "N/A",
        }
        Connection_Handle = Parameter(order=2, size=2, ranges=Connection_Handle_Ranges)
        """
        Connection handle that identifies the connection.
        """

        RSSI_Choices = {
            127: "RSSI not available",
        }
        RSSI_Ranges = {
            (-127, 20): "N/A",
        }
        RSSI = Parameter(order=3, size=1, choices=RSSI_Choices, ranges=RSSI_Ranges)
        """
        N Size: 1 Octet (signed integer)
        Units: dBm
        """


class HCI_LE_SET_EVENT_MASK(CommandPacket):
    """
    The LE_Set_Event_Mask command is used to control which LE events are
    generated by the HCI for the Host. If the bit in the LE_Event_Mask is set to a
    one, then the event associated with that bit will be enabled. The Host has to
    deal with each event that is generated by an LE Controller. The event mask
    allows the Host to control which events will interrupt it.
    For LE events to be generated, the LE Meta-Event bit in the Event_Mask shall
    also be set. If that bit is not set, then LE events shall not be generated, regardless
    of how the LE_Event_Mask is set.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.1)
    """

    CODE = 0x2001

    LE_Event_Mask_Choices = {
        0x0000000000000000: "No LE events specified",
        0x0000000000000001: "LE Connection Complete Event",
        0x0000000000000002: "LE Advertising Report Event",
        0x0000000000000004: "LE Connection Update Complete Event",
        0x0000000000000008: "LE Read Remote Used Features Complete Event",
        0x0000000000000010: "LE Long Term Key Request Event",
        0x0000000000000020: "LE Remote Connection Parameter Request Event",
        0x0000000000000040: "LE Data Length Change Event",
        0x0000000000000080: "LE Read Local P-256 Public Key Complete Event",
        0x0000000000000100: "LE Generate DHKey Complete Event",
        0x0000000000000200: "LE Enhanced Connection Complete Event",
        0x0000000000000400: "LE Direct Advertising Report Event",
    }
    LE_Event_Mask = Parameter(order=1, size=8, choices=LE_Event_Mask_Choices, multi_choice=True)
    """
    LE event mask. Default: 0x000000000000001F.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_READ_BUFFER_SIZE(CommandPacket):
    """
    The LE_Read_Buffer_Size command is used to read the maximum size of the
    data portion of HCI LE ACL Data Packets sent from the Host to the Controller.
    The Host will segment the data transmitted to the Controller according to these
    values, so that the HCI Data Packets will contain data with up to this size. The
    LE_Read_Buffer_Size command also returns the total number of HCI LE ACL
    Data Packets that can be stored in the data buffers of the Controller. The
    LE_Read_Buffer_Size command must be issued by the Host before it sends
    any data to an LE Controller (see Section 4.1.1).
    If the Controller returns a length value of zero, the Host shall use the
    Read_Buffer_Size command to determine the size of the data buffers
    Note: Both the Read_Buffer_Size and LE_Read_Buffer_Size commands may
    return buffer length and number of packets parameter values that are nonzero.
    The HC_LE_ACL_Data_Packet_Length return parameter shall be used to
    determine the size of the L2CAP PDU segments contained in ACL Data
    Packets, which are transferred from the Host to the Controller to be broken up
    into packets by the Link Layer. Both the Host and the Controller shall support
    command and event packets, where the data portion (excluding header)
    contained in the packets is 255 octets in size. The
    HC_Total_Num_LE_ACL_Data_Packets return parameter contains the total
    number of HCI ACL Data Packets that can be stored in the data buffers of the
    Controller. The Host determines how the buffers are to be divided between
    different Connection Handles.
    Note: The HC_LE_ACL_Data_Packet_Length return parameter does not
    include the length of the HCI Data Packet header.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.2)
    """

    CODE = 0x2002

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        HC_LE_ACL_Data_Packet_Length = Parameter(order=2, size=2)
        """
        0x0000 No dedicated LE Buffer - use Read_Buffer_Size command.
        0x0001 - 0xFFFF Maximum length (in octets) of the data portion of each HCI ACL Data
        Packet that the Controller is able to accept.
        """

        HC_Total_Num_LE_ACL_Data_Packets = Parameter(order=3, size=1)
        """
        0x00 No dedicated LE Buffer - use Read_Buffer_Size command.
        0x01 - 0xFF Total number of HCI ACL Data Packets that can be stored in the data
        buffers of the Controller.
        """


class HCI_LE_READ_LOCAL_SUPPORTED_FEATURES(CommandPacket):
    """
    This command requests the list of the supported LE features for the Controller.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.3)
    """

    CODE = 0x2003

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        LE_Features = Parameter(order=2, size=8)
        """
        Bit Mask List of LE features. See Core v4.1, Vol. 6, Part B, Section 4.6.
        """


class HCI_LE_SET_RANDOM_ADDRESS(CommandPacket):
    """
    The LE_Set_Random_Address command is used by the Host to set the LE
    Random Device Address in the Controller (see [Vol 6] Part B, Section 1.3).
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.4)
    """

    CODE = 0x2005

    Random_Address = Parameter(order=1, size=6)
    """
    Random Device Address.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_SET_ADVERTISING_PARAMETERS(CommandPacket):
    """
    The LE_Set_Advertising_Parameters command is used by the Host to set the
    advertising parameters.
    The Advertising_Interval_Min shall be less than or equal to the
    Advertising_Interval_Max. The Advertising_Interval_Min and
    Advertising_Interval_Max should not be the same value to enable the
    Controller to determine the best advertising interval given other activities.
    For high duty cycle directed advertising, i.e. when Advertising_Type is 0x01
    (ADV_DIRECT_IND, high duty cycle), the Advertising_Interval_Min and
    Advertising_Interval_Max parameters are not used and shall be ignored.
    The Advertising_Type is used to determine the packet type that is used for
    advertising when advertising is enabled.
    Own_Address_Type parameter indicates the type of address being used in the
    advertising packets.
    If Own_Address_Type equals 0x02 or 0x03, the Peer_Address parameter
    contains the peer's Identity Address and the Peer_Address_Type parameter
    contains the Peer's Identity Type (i.e. 0x00 or 0x01). These parameters are
    used to locate the corresponding local IRK in the resolving list; this IRK is used
    to generate the own address used in the advertisement.
    If directed advertising is performed, i.e. when Advertising_Type is set to 0x01
    (ADV_DIRECT_IND, high duty cycle) or 0x04 (ADV_DIRECT_IND, low duty
    cycle mode), then the Peer_Address_Type and Peer_Address shall be valid.
    If Own_Address_Type equals 0x02 or 0x03, the Controller generates the
    peer's Resolvable Private Address using the peer's IRK corresponding to the
    peer's Identity Address contained in the Peer_Address parameter and peer's
    Identity Address Type (i.e. 0x00 or 0x01) contained in the Peer_Address_Type
    parameter.
    The Advertising_Channel_Map is a bit field that indicates the advertising
    channels that shall be used when transmitting advertising packets. At least one
    channel bit shall be set in the Advertising_Channel_Map parameter.
    The Advertising_Filter_Policy parameter shall be ignored when directed
    advertising is enabled.
    The Host shall not issue this command when advertising is enabled in the
    Controller; if it is the Command Disallowed error code shall be used.
    If the advertising interval range provided by the Host (Advertising_Interval_Min,
    Advertising_Interval_Max) is outside the advertising interval range supported
    by the Controller, then the Controller shall return the Unsupported Feature or
    Parameter Value (0x11) error code.
    """

    CODE = 0x2006

    Advertising_Interval_Min_Ranges = {
        (0x0020, 0x4000): ("20.000 ms", "10240.000 ms"),
    }
    Advertising_Interval_Min = Parameter(order=1, size=2, ranges=Advertising_Interval_Min_Ranges)
    """
    Minimum advertising interval for undirected and low duty cycle directed
        advertising.
        Time = N * 0.625 msec.
    """

    Advertising_Interval_Max_Ranges = {
        (0x0020, 0x4000): ("20.000 ms", "10240.000 ms"),
    }
    Advertising_Interval_Max = Parameter(order=2, size=2, ranges=Advertising_Interval_Max_Ranges)
    """
    Maximum advertising interval.
        Time = N * 0.625 msec.
    """

    Advertising_Type_Choices = {
        0x00: "ADV_IND (Connectable undirected advertising)",
        0x01: "ADV_DIRECT_IND, high duty cycle (Connectable high duty cycle directed advertising)",
        0x02: "ADV_SCAN_IND (Scannable undirected advertising)",
        0x03: "ADV_NONCONN_IND (Non connectable undirected advertising)",
        0x04: "ADV_DIRECT_IND, low duty cycle (Connectable low duty cycle directed advertising)",
    }
    Advertising_Type = Parameter(order=3, size=1, choices=Advertising_Type_Choices)
    """
    Advertising type.
    """

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address or Public Address",
        0x03: "Resolvable Private Address or Random Address",
    }
    Own_Address_Type = Parameter(order=4, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type.
        
        0x00: Public Device Address
        0x01 Random Device Address
        
        0x02: Controller generates Resolvable Private Address based on the local
        IRK from resolving list. If resolving list contains no matching entry,
        use public address.
        
        
        
        0x03: Controller generates Resolvable Private Address based on the local
        IRK from resolving list. If resolving list contains no matching entry,
        use random address from LE_Set_Random_Address.
    """

    Peer_Address_Type_Choices = {
        0x00: "Public Device Address or Public Identity Address",
        0x01: "Random Device Address or Random (static) Identity Address",
    }
    Peer_Address_Type = Parameter(order=5, size=1, choices=Peer_Address_Type_Choices)
    """
    Peer Address type.
    """

    Peer_Address = Parameter(order=6, size=6)
    """
    Public Device Address, Random Device Address, Public Identity
        Address or Random (static) Identity Address of the device to be connected.
    """

    Advertising_Channel_Map_Choices = {
        0x01: "ch 37",
        0x02: "ch 38",
        0x04: "ch 39",
    }
    Advertising_Channel_Map = Parameter(order=7, size=1, choices=Advertising_Channel_Map_Choices, multi_choice=True)
    """
    Advertising channel map.
        Default: 00000111b (all channels enabled).
    """

    Advertising_Filter_Policy_Choices = {
        0x00: "Allow Scan Request from Any, Allow Connect Request from Any",
        0x01: "Allow Scan Request from White List Only, Allow Connect Request from Any",
        0x02: "Allow Scan Request from Any, Allow Connect Request from White List Only",
        0x03: "Allow Scan Request from White List Only, Allow Connect Request from White List Only",
    }
    Advertising_Filter_Policy = Parameter(order=8, size=1, choices=Advertising_Filter_Policy_Choices)
    """
    Advertising filter policy.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_READ_ADVERTISING_CHANNEL_TX_POWER(CommandPacket):
    """
    The LE_Read_Advertising_Channel_Tx_Power command is used by the Host
    to read the transmit power level used for LE advertising channel packets.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.6)
    """

    CODE = 0x2007

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Transmit_Power_Level_Ranges = {
            (-20, 10): "N/A",
        }
        Transmit_Power_Level = Parameter(order=2, size=1, ranges=Transmit_Power_Level_Ranges)
        """
        Size: 1 Octet (signed integer)
        Units: dBm
        Accuracy: +/- 4 dBm
        """


class HCI_LE_SET_ADVERTISING_DATA(CommandPacket):
    """
    The LE_Set_Advertising_Data command is used to set the data used in advertising
    packets that have a data field.
    Only the significant part of the Advertising_Data is transmitted in the advertising
    packets, as defined in [Vol 3] Part C, Section 11.,
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.7)
    """

    CODE = 0x2008

    Advertising_Data_Length_Ranges = {
        (0, 31): "N/A",
    }
    Advertising_Data_Length = Parameter(order=1, size=1, ranges=Advertising_Data_Length_Ranges)
    """
    The number of significant octets in the following data field
    """

    Advertising_Data = Parameter(order=2, size=31)
    """
    31 octets of data formatted as defined in [Vol 3] Part
        C, Section 11.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_SET_SCAN_RESPONSE_DATA(CommandPacket):
    """
    This command is used to provide data used in Scanning Packets that have a
    data field.
    Only the significant part of the Scan_Response_Data is transmitted in the
    Scanning Packets, as defined in [Vol 3] Part C, Section 11.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.8)
    """

    CODE = 0x2009

    Scan_Response_Data_Length_Ranges = {
        (0, 31): "N/A",
    }
    Scan_Response_Data_Length = Parameter(order=1, size=1, ranges=Scan_Response_Data_Length_Ranges)
    """
    The number of significant octets in the following data field
    """

    Scan_Response_Data = Parameter(order=2, size=31)
    """
    31 octets of data formatted as defined in [Vol 3] Part
        C, Section 11.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_SET_ADVERTISE_ENABLE(CommandPacket):
    """
    The LE_Set_Advertise_Enable command is used to request the Controller to
    start or stop advertising. The Controller manages the timing of advertisements
    as per the advertising parameters given in the LE_Set_Advertising_Parameters
    command.
    The Controller shall continue advertising until the Host issues an LE_Set_Advertise_Enable
    command with Advertising_Enable set to 0x00 (Advertising is
    disabled) or until a connection is created or until the Advertising is timed out
    due to high duty cycle Directed Advertising. In these cases, advertising is then
    disabled.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.9)
    """

    CODE = 0x200A

    Advertising_Enable_Choices = {
        0x00: "Disable",
        0x01: "Enable",
    }
    Advertising_Enable = Parameter(order=1, size=1, choices=Advertising_Enable_Choices)
    """
    Enable/disable advertise. Default is 0 (disabled).
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_SET_SCAN_PARAMETERS(CommandPacket):
    """
    The LE_Set_Scan_Parameters command is used to set the scan parameters.
    The LE_Scan_Type parameter controls the type of scan to perform.
    The LE_Scan_Interval and LE_Scan_Window parameters are recommendations
    from the Host on how long (LE_Scan_Window) and how frequently
    (LE_Scan_Interval) the Controller should scan (See [Vol 6] Part B, Section
    4.5.3). The LE_Scan_Window parameter shall always be set to a value smaller
    or equal to the value set for the LE_Scan_Interval parameter. If they are set to
    the same value scanning should be run continuously.
    The Own_Address_Type parameter determines the address used (Public or
    Random Device Address) when performing active scan.
    The Host shall not issue this command when scanning is enabled in the Controller;
    if it is the Command Disallowed error code shall be used.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.10)
    """

    CODE = 0x200B

    LE_Scan_Type_Choices = {
        0x00: "Passive Scanning",
        0x01: "Active scanning",
    }
    LE_Scan_Type = Parameter(order=1, size=1, choices=LE_Scan_Type_Choices)
    """
    Passive or active scanning. With active scanning SCAN_REQ packets are sent.
    """

    LE_Scan_Interval_Ranges = {
        (0x0004, 0x4000): ("2.500 ms", "10240.000 ms"),
    }
    LE_Scan_Interval = Parameter(order=2, size=2, ranges=LE_Scan_Interval_Ranges)
    """
    This is defined as the time interval from when the Controller started its last LE scan until it begins the subsequent LE scan.
        Time = N * 0.625 msec.
    """

    LE_Scan_Window_Ranges = {
        (0x0004, 0x4000): ("2.500 ms", "10240.000 ms"),
    }
    LE_Scan_Window = Parameter(order=3, size=2, ranges=LE_Scan_Window_Ranges)
    """
    The duration of the LE scan. LE_Scan_Window shall be less than or equal to LE_Scan_Interval.
        Time = N * 0.625 msec.
    """

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address or Public Address",
        0x03: "Resolvable Private Address or Random Address",
    }
    Own_Address_Type = Parameter(order=4, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type.
        
        0x00: Public Device Address
        0x01 Random Device Address
        
        0x02: Controller generates Resolvable Private Address based on the local
        IRK from resolving list. If resolving list contains no matching entry,
        use public address.
        
        
        
        0x03: Controller generates Resolvable Private Address based on the local
        IRK from resolving list. If resolving list contains no matching entry,
        use random address from LE_Set_Random_Address.
    """

    Scanning_Filter_Policy_Choices = {
        0x00: "Accept all",
        0x01: "Ignore devices not in the White List",
        0x02: "Accept all (use resolving list)",
        0x03: "Ignore devices not in the White List (use resolving list)",
    }
    Scanning_Filter_Policy = Parameter(order=5, size=1, choices=Scanning_Filter_Policy_Choices)
    """
    0x00 Accept all advertisement packets.
        Directed advertising packets which are not addressed for this device
        shall be ignored.
        0x01 Ignore advertisement packets from devices not in the White List Only.
        Directed advertising packets which are not addressed for this device
        shall be ignored
        0x02 Accept all undirected advertisement packets.
        Directed advertisement packets where initiator address is a RPA and
        Directed advertisement packets addressed to this device shall be accepted.
        0x03 Accept all undirected advertisement packets from devices that are in
        the White List.Directed advertisement packets where initiator address is RPA and Directed advertisement packets addressed to this device shall be accepted.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_SET_SCAN_ENABLE(CommandPacket):
    """
    The LE_Set_Scan_Enable command is used to start scanning. Scanning is
    used to discover advertising devices nearby.
    The Filter_Duplicates parameter controls whether the Link Layer shall filter
    duplicate advertising reports to the Host, or if the Link Layer should generate
    advertising reports for each packet received.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.11)
    """

    CODE = 0x200C

    LE_Scan_Enable_Choices = {
        0x00: "Scanning disabled",
        0x01: "Scanning enabled",
    }
    LE_Scan_Enable = Parameter(order=1, size=1, choices=LE_Scan_Enable_Choices)
    """
    Enable/disable scan. Default is 0 (disabled).
    """

    Filter_Duplicates_Choices = {
        0x00: "Duplicate filtering disabled",
        0x01: "Duplicate filtering enabled",
    }
    Filter_Duplicates = Parameter(order=2, size=1, choices=Filter_Duplicates_Choices)
    """
    Enable/disable duplicate filtering.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_CREATE_CONNECTION(CommandPacket):
    """
    The LE_Create_Connection command is used to create a Link Layer connection
    to a connectable advertiser.
    The LE_Scan_Interval and LE_Scan_Window parameters are recommendations
    from the Host on how long (LE_Scan_Window) and how frequently
    (LE_Scan_Interval) the Controller should scan. The LE_Scan_Window parameter
    shall be set to a value smaller or equal to the value set for the LE_Scan_Interval
    parameter. If both are set to the same value, scanning should run
    continuously.
    The Initiator_Filter_Policy is used to determine whether the White List is used.
    If the White List is not used, the Peer_Address_Type and the Peer_Address
    parameters specify the address type and address of the advertising device to
    connect to.
    The Link Layer shall set the address in the CONNECT_REQ packets to either
    the Public Device Address or the Random Device Addressed based on the
    Own_Address_Type parameter.
    The Conn_Interval_Min and Conn_Interval_Max parameters define the minimum
    and maximum allowed connection interval. The Conn_Interval_Min
    parameter shall not be greater than the Conn_Interval_Max parameter.
    The Conn_Latency parameter defines the maximum allowed connection
    latency (see [Vol 6] Part B, Section 4.5.1).
    The Supervision_Timeout parameter defines the link supervision timeout for
    the connection. The Supervision_Timeout in milliseconds shall be larger than
    (1 + Conn_Latency) * Conn_Interval_Max * 2, where Conn_Interval_Max is
    given in milliseconds. (See [Vol 6] Part B, Section 4.5.2).
    The Minimum_CE_Length and Maximum_CE_Length parameters are informative
    parameters providing the Controller with the expected minimum and maximum
    length of the connection events. The Minimum_CE_Length parameter
    shall be less than or equal to the Maximum_CE_Length parameter.
    The Host shall not issue this command when another LE_Create_Connection
    is pending in the Controller; if this does occur the Controller shall return the
    Command Disallowed error code shall be used.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.12)
    """

    CODE = 0x200D

    LE_Scan_Interval_Ranges = {
        (0x0004, 0x4000): ("2.500 ms", "10240.000 ms"),
    }
    LE_Scan_Interval = Parameter(order=1, size=2, ranges=LE_Scan_Interval_Ranges)
    """
    This is defined as the time interval from when the Controller started its last LE scan until it begins the subsequent LE scan.
        Time = N * 0.625 msec.
    """

    LE_Scan_Window_Ranges = {
        (0x0004, 0x4000): ("2.500 ms", "10240.000 ms"),
    }
    LE_Scan_Window = Parameter(order=2, size=2, ranges=LE_Scan_Window_Ranges)
    """
    The duration of the LE scan. LE_Scan_Window shall be less than or equal to LE_Scan_Interval.
        Time = N * 0.625 msec.
    """

    Initiator_Filter_Policy_Choices = {
        0x00: "White list not used",
        0x01: "White list used",
    }
    Initiator_Filter_Policy = Parameter(order=3, size=1, choices=Initiator_Filter_Policy_Choices)
    """
    0x00 White list is not used to determine which advertiser to connect to.
        Peer_Address_Type and Peer_Address shall be used.
        0x01 White list is used to determine which advertiser to connect to.
        Peer_Address_Type and Peer_Address shall be ignored.
    """

    Peer_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Public Identity Address",
        0x03: "Random (Static) Identity Address",
    }
    Peer_Address_Type = Parameter(order=4, size=1, choices=Peer_Address_Type_Choices)
    """
    0x00 Public Device Address
        0x01 Random Device Address
        0x02 Public Identity Address (Corresponds to Resolved Private Address)
        0x03 Random (Static) Identity Address (Corresponds to Resolved Private Address)
    """

    Peer_Address = Parameter(order=5, size=6)
    """
    Public Device Address, Random Device Address, Public Identity
        Address or Random (static) Identity Address of the advertising
        device.
    """

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address or Public Address",
        0x03: "Resolvable Private Address or Random Address",
    }
    Own_Address_Type = Parameter(order=6, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type.
        
        0x00: Public Device Address
        0x01 Random Device Address
        
        0x02: Controller generates Resolvable Private Address based on the local
        IRK from resolving list. If resolving list contains no matching entry,
        use public address.
        
        
        
        0x03: Controller generates Resolvable Private Address based on the local
        IRK from resolving list. If resolving list contains no matching entry,
        use random address from LE_Set_Random_Address.
    """

    Conn_Interval_Min_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Conn_Interval_Min = Parameter(order=7, size=2, ranges=Conn_Interval_Min_Ranges)
    """
    Minimum value for the connection event interval. This shall be less
        than or equal to Conn_Interval_Max.
        Time = N * 1.25 msec.
    """

    Conn_Interval_Max_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Conn_Interval_Max = Parameter(order=8, size=2, ranges=Conn_Interval_Max_Ranges)
    """
    Maximum value for the connection event interval. This shall be
        greater than or equal to Conn_Interval_Min.
        Time = N * 1.25 msec.
    """

    Conn_Latency_Ranges = {
        (0x0000, 0x01F3): "N/A",
    }
    Conn_Latency = Parameter(order=9, size=2, ranges=Conn_Latency_Ranges)
    """
    Slave latency for the connection in number of connection events.
    """

    Supervision_Timeout_Ranges = {
        (0x000A, 0x0C80): ("100 ms", "32000 ms"),
    }
    Supervision_Timeout = Parameter(order=10, size=2, ranges=Supervision_Timeout_Ranges)
    """
    Supervision timeout for the LE Link.
        It shall be a multiple of 10 ms and larger than (1 + connSlaveLatency) * connInterval * 2.
        Time = N * 10 msec.
    """

    Minimum_CE_Length = Parameter(order=11, size=2)
    """
    Information parameter about the minimum length of connection
        needed for this LE connection.
        Time = N * 0.625 msec.
    """

    Maximum_CE_Length = Parameter(order=12, size=2)
    """
    Information parameter about the maximum length of connection needed
        for this LE connection.
        Time = N * 0.625 msec.
    """


class HCI_LE_CREATE_CONNECTION_CANCEL(CommandPacket):
    """
    The LE_Create_Connection_Cancel command is used to cancel the LE_Create_Connection
    command. This command shall only be issued after the
    LE_Create_Connection command has been issued, a Command Status event
    has been received for the LE Create Connection command and before the LE
    Connection Complete event.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.13)
    """

    CODE = 0x200E

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_READ_WHITE_LIST_SIZE(CommandPacket):
    """
    The LE_Read_White_List_Size command is used to read the total number of
    white list entries that can be stored in the Controller.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.14)
    """

    CODE = 0x200F

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        White_List_Size = Parameter(order=2, size=1)
        """
        Total number of white list entries that can be stored in the Controller.
        """


class HCI_LE_CLEAR_WHITE_LIST(CommandPacket):
    """
    The LE_Clear_White_List command is used to clear the white list stored in the
    Controller.
    This command can be used at any time except when:
    - the advertising filter policy uses the white list and advertising is enabled.
    - the scanning filter policy uses the white list and scanning is enabled.
    - the initiator filter policy uses the white list and an LE_Create_Connection
    command is outstanding.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.15)
    """

    CODE = 0x2010

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_ADD_DEVICE_TO_WHITE_LIST(CommandPacket):
    """
    The LE_Add_Device_To_White_List command is used to add a single device
    to the white list stored in the Controller.
    This command can be used at any time except when:
    - the advertising filter policy uses the white list and advertising is enabled.
    - the scanning filter policy uses the white list and scanning is enabled.
    - the initiator filter policy uses the white list and a create connection command
    is outstanding.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.16)
    """

    CODE = 0x2011

    Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
    }
    Address_Type = Parameter(order=1, size=1, choices=Address_Type_Choices)
    """
    Address type.
    """

    Address = Parameter(order=2, size=6)
    """
    Public Device Address or Random Device Address of the device
        to be added to the white list.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_REMOVE_DEVICE_FROM_WHITE_LIST(CommandPacket):
    """
    The LE_Remove_Device_From_White_List command is used to remove a single
    device from the white list stored in the Controller.
    This command can be used at any time except when:
    - the advertising filter policy uses the white list and advertising is enabled.
    - the scanning filter policy uses the white list and scanning is enabled.
    - the initiator filter policy uses the white list and a create connection command
    is outstanding.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.17)
    """

    CODE = 0x2012

    Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
    }
    Address_Type = Parameter(order=1, size=1, choices=Address_Type_Choices)
    """
    Address type.
    """

    Address = Parameter(order=2, size=6)
    """
    Public Device Address or Random Device Address of the device
        to be removed from the white list.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_CONNECTION_UPDATE(CommandPacket):
    """
    The LE_Connection_Update command is used to change the Link Layer connection
    parameters of a connection. This command is supported only on master side.
    The Conn_Interval_Min and Conn_Interval_Max parameters are used to define
    the minimum and maximum allowed connection interval. The Conn_Interval_Min
    parameter shall not be greater than the Conn_Interval_Max parameter.
    The Conn_Latency parameter shall define the maximum allowed connection
    latency.
    The Supervision_Timeout parameter shall define the link supervision timeout
    for the LE link. The Supervision_Timeout in milliseconds shall be larger than (1
    + Conn_Latency) * Conn_Interval_Max * 2, where Conn_Interval_Max is given
    in milliseconds.
    The Minimum_CE_Length and Maximum_CE_Length are information parameters
    providing the Controller with a hint about the expected minimum and maximum
    length of the connection events. The Minimum_CE_Length shall be less
    than or equal to the Maximum_CE_Length.
    The actual parameter values selected by the Link Layer may be different from
    the parameter values provided by the Host through this command.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.18)
    """

    CODE = 0x2013

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Conn_Interval_Min_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Conn_Interval_Min = Parameter(order=2, size=2, ranges=Conn_Interval_Min_Ranges)
    """
    Minimum value for the connection event interval. This shall be less
        than or equal to Conn_Interval_Max.
        Time = N * 1.25 msec.
    """

    Conn_Interval_Max_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Conn_Interval_Max = Parameter(order=3, size=2, ranges=Conn_Interval_Max_Ranges)
    """
    Maximum value for the connection event interval. This shall be
        greater than or equal to Conn_Interval_Min.
        Time = N * 1.25 msec.
    """

    Conn_Latency_Ranges = {
        (0x0000, 0x01F3): "N/A",
    }
    Conn_Latency = Parameter(order=4, size=2, ranges=Conn_Latency_Ranges)
    """
    Slave latency for the connection in number of connection events.
    """

    Supervision_Timeout_Ranges = {
        (0x000A, 0x0C80): ("100 ms", "32000 ms"),
    }
    Supervision_Timeout = Parameter(order=5, size=2, ranges=Supervision_Timeout_Ranges)
    """
    Supervision timeout for the LE Link.
        It shall be a multiple of 10 ms and larger than (1 + connSlaveLatency) * connInterval * 2.
        Time = N * 10 msec.
    """

    Minimum_CE_Length = Parameter(order=6, size=2)
    """
    Information parameter about the minimum length of connection
        needed for this LE connection.
        Time = N * 0.625 msec.
    """

    Maximum_CE_Length = Parameter(order=7, size=2)
    """
    Information parameter about the maximum length of connection needed
        for this LE connection.
        Time = N * 0.625 msec.
    """


class HCI_LE_SET_HOST_CHANNEL_CLASSIFICATION(CommandPacket):
    """
    The LE_Set_Host_Channel_Classification command allows the Host to specify
    a channel classification for data channels based on its "local information". This
    classification persists until overwritten with a subsequent LE_Set_Host_Channel_Classification
    command or until the Controller is reset using the Reset
    command (see [Vol 6] Part B, Section 4.5.8.1).
    If this command is used, the Host should send it within 10 seconds of knowing
    that the channel classification has changed. The interval between two successive
    commands sent shall be at least one second.
    This command shall only be used when the local device supports the Master
    role.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.19)
    """

    CODE = 0x2014

    LE_Channel_Map_Ranges = {
        (0x0000000000, 0x1FFFFFFFFF): "N/A",
    }
    LE_Channel_Map = Parameter(order=1, size=5, ranges=LE_Channel_Map_Ranges)
    """
    This parameter contains 37 1-bit fields.
        The nth such field (in the range 0 to 36) contains the value for the
        link layer channel index n.
        Channel n is bad = 0.
        Channel n is unknown = 1.
        The most significant bits are reserved and shall be set to 0.
        At least one channel shall be marked as unknown.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_READ_CHANNEL_MAP(CommandPacket):
    """
    The LE_Read_Channel_Map command returns the current Channel_Map for
    the specified Connection_Handle. The returned value indicates the state of the
    Channel_Map specified by the last transmitted or received Channel_Map (in a
    CONNECT_REQ or LL_CHANNEL_MAP_REQ message) for the specified
    Connection_Handle, regardless of whether the Master has received an
    acknowledgement.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.20)
    """

    CODE = 0x2015

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Connection_Handle_Ranges = {
            (0x0000, 0x0EFF): "N/A",
        }
        Connection_Handle = Parameter(order=2, size=2, ranges=Connection_Handle_Ranges)
        """
        Connection handle that identifies the connection.
        """

        LE_Channel_Map = Parameter(order=3, size=5)
        """
        This parameter contains 37 1-bit fields.
        The nth such field (in the range 0 to 36) contains the value for the
        link layer channel index n.
        Channel n is unused = 0.
        Channel n is used = 1.
        The most significant bits are reserved and shall be set to 0.
        """


class HCI_LE_READ_REMOTE_USED_FEATURES(CommandPacket):
    """
    This command requests a list of the used LE features from the remote device.
    This command shall return a list of the used LE features. For details see [Vol 6]
    Part B, Section 4.6.
    This command may be issued on both the master and slave.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.21)
    """

    CODE = 0x2016

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """


class HCI_LE_ENCRYPT(CommandPacket):
    """
    The LE_Encrypt command is used to request the Controller to encrypt the
    Plaintext_Data in the command using the Key given in the command and
    returns the Encrypted_Data to the Host. The AES-128 bit block cypher is
    defined in NIST Publication FIPS-197 (http://csrc.nist.gov/publications/fips/
    fips197/fips-197.pdf).
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.22)
    """

    CODE = 0x2017

    Key = Parameter(order=1, size=16)
    """
    128 bit key for the encryption of the data given in the command.
    """

    Plaintext_Data = Parameter(order=2, size=16)
    """
    128 bit data block that is requested to be encrypted.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Encrypted_Data = Parameter(order=2, size=16)
        """
        128 bit encrypted data block.
        """


class HCI_LE_RAND(CommandPacket):
    """
    The LE_Rand command is used to request the Controller to generate 8 octets
    of random data to be sent to the Host. The Random_Number shall be generated
    according to [Vol 2] Part H, Section 2 if the LE Feature (LL Encryption) is
    supported.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.23)
    """

    CODE = 0x2018

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Random_Number = Parameter(order=2, size=8)
        """
        Random Number
        """


class HCI_LE_START_ENCRYPTION(CommandPacket):
    """
    The LE_Start_Encryption command is used to authenticate the given encryption
    key associated with the remote device specified by the connection handle,
    and once authenticated will encrypt the connection. The parameters are as
    defined in [Vol 3] Part H, Section 2.4.4.
    If the connection is already encrypted then the Controller shall pause connection
    encryption before attempting to authenticate the given encryption key, and
    then re-encrypt the connection. While encryption is paused no user data shall
    be transmitted.
    On an authentication failure, the connection shall be automatically disconnected
    by the Link Layer. If this command succeeds, then the connection shall
    be encrypted.
    This command shall only be used when the local device's role is Master.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.24)
    """

    CODE = 0x2019

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Random_Number = Parameter(order=2, size=8)
    """
    64 bit random number.
    """

    Encrypted_Diversifier = Parameter(order=3, size=2)
    """
    16 bit encrypted diversifier.
    """

    Long_Term_Key = Parameter(order=4, size=16)
    """
    128 bit long term key.
    """


class HCI_LE_LONG_TERM_KEY_REQUEST_REPLY(CommandPacket):
    """
    The LE_Long_Term_Key_Request_Reply command is used to reply to an LE
    Long Term Key Request event from the Controller, and specifies the
    Long_Term_Key parameter that shall be used for this Connection_Handle. The
    Long_Term_Key is used as defined in [Vol 6] Part B, Section 5.1.3.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.25)
    """

    CODE = 0x201A

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Long_Term_Key = Parameter(order=2, size=16)
    """
    128 bit long term key.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Connection_Handle_Ranges = {
            (0x0000, 0x0EFF): "N/A",
        }
        Connection_Handle = Parameter(order=2, size=2, ranges=Connection_Handle_Ranges)
        """
        Connection handle that identifies the connection.
        """


class HCI_LE_LONG_TERM_KEY_REQUESTED_NEGATIVE_REPLY(CommandPacket):
    """
    The LE_Long_Term_Key_Request_Negative_Reply command is used to reply
    to an LE Long Term Key Request event from the Controller if the Host cannot
    provide a Long Term Key for this Connection_Handle.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.26)
    """

    CODE = 0x201B

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Connection_Handle_Ranges = {
            (0x0000, 0x0EFF): "N/A",
        }
        Connection_Handle = Parameter(order=2, size=2, ranges=Connection_Handle_Ranges)
        """
        Connection handle that identifies the connection.
        """


class HCI_LE_READ_SUPPORTED_STATES(CommandPacket):
    """
    The LE_Read_Supported_States command reads the states and state combinations
    that the link layer supports. See [Vol 6] Part B, Section 1.1.1.
    LE_States is an 8-octet bit field. If a bit is set to 1 then this state or state combination
    is supported by the Controller. Multiple bits in LE_States may be set to 1
    to indicate support for multiple state and state combinations.
    All the Advertising type with the Initiate State combinations shall be set only if
    the corresponding Advertising types and Master Role combination are set.
    All the Scanning types and the Initiate State combinations shall be set only if
    the corresponding Scanning types and Master Role combination are set.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.27)
    """

    CODE = 0x201C

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        LE_States = Parameter(order=2, size=8)
        """
        State or state combination is supported by the Controller.
        See Core v4.1, Vol.2, part E, Ch. 7.8.27.
        """


class HCI_LE_SET_DATA_LENGTH(CommandPacket):
    """
    The LE_Set_Data_Length command allows the Host to suggest maximum transmission packet size and maximum packet transmission time (connMaxTxOctets and connMaxTxTime - see [Vol 6] Part B, Section 4.5.10) to be used for a given connection. The Controller may use smaller or larger values based on local information.
    """

    CODE = 0x2022

    Connection_Handle = Parameter(order=1, size=2)
    """
    Connection_Handle to be used to identify a connection.
    """

    TxOctets_Ranges = {
        (0x001B, 0x00FB): "N/A",
    }
    TxOctets = Parameter(order=2, size=2, ranges=TxOctets_Ranges)
    """
    Preferred maximum number of payload octets that the local Controller should include in a single Link Layer Data Channel PDU.
        Range 0x001B-0x00FB (0x0000 - 0x001A and 0x00FC - 0xFFFF) Reserved for future use). Default: 27 bytes.
    """

    TxTime_Ranges = {
        (0x0148, 0x0848): "N/A",
    }
    TxTime = Parameter(order=3, size=2, ranges=TxTime_Ranges)
    """
    Preferred maximum number of microseconds that the local Controller should use to transmit a single Link Layer Data Channel PDU.
        Range 0x0148-0x0848 (0x0000 - 0x0147 and 0x0849 - 0xFFFF Reserved for future use). Default: 328 bytes.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Connection_Handle = Parameter(order=2, size=2)
        """
        Connection_Handle to be used to identify a connection.
        """


class HCI_LE_READ_SUGGESTED_DEFAULT_DATA_LENGTH(CommandPacket):
    """
    The LE_Read_Suggested_Default_Data_Length command allows the Host to read the Host preferred values for the Controller maximum transmitted number of payload octets and maximum packet transmission time to be used for new connections (connInitialMaxTxOctets and connInitialMaxTxTime - see ([Vol 6] Part B, Section 4.5.10).
    """

    CODE = 0x2023

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        SuggestedMaxTxOctets = Parameter(order=2, size=2)
        """
        The Host suggested value for the Controller maximum transmitted number of payload octets to be used for new connections - connInitialMaxTxOctets.
        Range 0x001B-0x00FB (0x0000 - 0x001A and 0x00FC - 0xFFFF Reserved for future use)
        Default: 0x001B
        """

        SuggestedMaxTxTime = Parameter(order=3, size=2)
        """
        The Host suggested value for the Controller maximum packet transmission time to be used for new connections - connInitialMaxTx-Time.
        Range 0x0148-0x0848 (0x0000 - 0x0147 and 0x0849 - 0xFFFF Reserved for future use)
        Default: 0x0148
        """


class HCI_LE_WRITE_SUGGESTED_DEFAULT_DATA_LENGTH(CommandPacket):
    """
    The LE_Write_Suggested_Default_Data_Length command allows the Host to specify its preferred values for the Controller maximum transmission number of payload octets and maximum packet transmission time to be used for new connections (connInitialMaxTxOctets and connInitialMaxTxTime - see [Vol 6] Part B, Section 4.5.10). The Controller may use smaller or larger values based on local information.
    """

    CODE = 0x2024

    SuggestedMaxTxOctets_Ranges = {
        (0x001B, 0x00FB): "N/A",
    }
    SuggestedMaxTxOctets = Parameter(order=1, size=2, ranges=SuggestedMaxTxOctets_Ranges)
    """
    The Host suggested value for the Controller maximum transmitted number of payload octets to be used for new connections - connInitialMaxTxOctets.
        Range 0x001B-0x00FB (0x0000 - 0x001A and 0x00FC - 0xFFFF Reserved for future use)
    """

    SuggestedMaxTxTime_Ranges = {
        (0x0148, 0x0848): "N/A",
    }
    SuggestedMaxTxTime = Parameter(order=2, size=2, ranges=SuggestedMaxTxTime_Ranges)
    """
    The Host suggested value for the Controller maximum packet transmission time to be used for new connections - connInitialMaxTx-Time.
        Range 0x0148-0x0848 (0x0000 - 0x0147 and 0x0849 - 0xFFFF Reserved for future use)
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_READ_LOCAL_P256_PUBLIC_KEY(CommandPacket):
    """
    The LE_Read_Local_P-256_Public_Key command is used to return the local
    P-256 public key from the Controller. The Controller shall generate a new P-256 public/private key pair upon receipt of this command.
    (See Bluetooth Specification v.4.2, Vol. 2, Part E, 7.8.36)
    """

    CODE = 0x2025


class HCI_LE_GENERATE_DHKEY(CommandPacket):
    """
    The LE_Generate_DHKey command is used to initiate generation of a Diffie-
    Hellman key in the Controller for use over the LE transport. This command
    takes the remote P-256 public key as input. The Diffie-Hellman key generation
    uses the private key generated by LE_Read_Local_P256_Public_Key command.
    (See Bluetooth Specification v.4.2, Vol. 2, Part E, 7.8.37)
    """

    CODE = 0x2026

    Remote_P256_Public_Key = Parameter(order=1, size=64)
    """
    The remote P-256 public key:
        X, Y format
        Octets 31-0: X co-ordinate
        Octets 63-32: Y co-ordinate
        Little Endian Format
    """


class HCI_LE_ADD_DEVICE_TO_RESOLVING_LIST(CommandPacket):
    """
    The LE_Add_Device_To_Resolving_List command is used to add one device
    to the list of address translations used to resolve Resolvable Private Addresses
    in the Controller.
    This command cannot be used when address translation is enabled in the
    Controller and:
    - Advertising is enabled
    - Scanning is enabled
    - Create connection command is outstanding
    This command can be used at any time when address translation is disabled in
    the Controller.
    When a Controller cannot add a device to the resolving list because the list is
    full, it shall respond with error code 0x07 (Memory Capacity Exceeded).
    (See Bluetooth Specification v.4.2, Vol. 2, Part E, 7.8.38)
    """

    CODE = 0x2027

    Peer_Identity_Address_Type_Choices = {
        0x00: "Public Identity Address",
        0x01: "Random (static) Identity Address",
    }
    Peer_Identity_Address_Type = Parameter(order=1, size=1, choices=Peer_Identity_Address_Type_Choices)
    """
    Identity address type.
    """

    Peer_Identity_Address = Parameter(order=2, size=6)
    """
    Public or Random (static) Identity address of the peer device
    """

    Peer_IRK = Parameter(order=3, size=16)
    """
    IRK of the peer device
    """

    Local_IRK = Parameter(order=4, size=16)
    """
    IRK of the local device
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_REMOVE_DEVICE_FROM_RESOLVING_LIST(CommandPacket):
    """
    The LE_Remove_Device_From_Resolving_List command is used to remove
    one device from the list of address translations used to resolve Resolvable
    Private Addresses in the controller.
    This command cannot be used when address translation is enabled in the
    Controller and:
    - Advertising is enabled
    - Scanning is enabled
    - Create connection command is outstanding
    This command can be used at any time when address translation is disabled in
    the Controller.
    When a Controller cannot remove a device from the resolving list because it is
    not found, it shall respond with error code 0x02 (Unknown Connection
    Identifier).
    (See Bluetooth Specification v.4.2, Vol. 2, Part E, 7.8.39)
    """

    CODE = 0x2028

    Peer_Identity_Address_Type_Choices = {
        0x00: "Public Identity Address",
        0x01: "Random (static) Identity Address",
    }
    Peer_Identity_Address_Type = Parameter(order=1, size=1, choices=Peer_Identity_Address_Type_Choices)
    """
    Identity address type.
    """

    Peer_Identity_Address = Parameter(order=2, size=6)
    """
    Public or Random (static) Identity address of the peer device
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_CLEAR_RESOLVING_LIST(CommandPacket):
    """
    The LE_Clear_Resolving_List command is used to remove all devices from the
    list of address translations used to resolve Resolvable Private Addresses in the
    Controller.
    This command cannot be used when address translation is enabled in the
    Controller and:
    - Advertising is enabled
    - Scanning is enabled
    - Create connection command is outstanding
    This command can be used at any time when address translation is disabled in
    the Controller.
    (See Bluetooth Specification v.4.2, Vol. 2, Part E, 7.8.40)
    """

    CODE = 0x2029

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_READ_RESOLVING_LIST_SIZE(CommandPacket):
    """
    The LE_Read_Resolving_List_Size command is used to read the total number
    of address translation entries in the resolving list that can be stored in the
    Controller.
    (See Bluetooth Specification v.4.2, Vol. 2, Part E, 7.8.41)
    """

    CODE = 0x202A

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Resolving_List_Size = Parameter(order=2, size=1)
        """
        Number of address translation entries in the resolving list
        """


class HCI_LE_READ_PEER_RESOLVABLE_ADDRESS(CommandPacket):
    """
    The LE_Read_Peer_Resolvable_Address command is used to get the current
    peer Resolvable Private Address being used for the corresponding peer Public
    and Random (static) Identity Address. The peer's resolvable address being
    used may change after the command is called.
    This command can be used at any time.
    When a Controller cannot find a Resolvable Private Address associated with
    the Peer Identity Address, it shall respond with error code 0x02 (Unknown
    Connection Identifier).
    (See Bluetooth Specification v.4.2, Vol. 2, Part E, 7.8.42)
    """

    CODE = 0x202B

    Peer_Identity_Address_Type_Choices = {
        0x00: "Public Identity Address",
        0x01: "Random (static) Identity Address",
    }
    Peer_Identity_Address_Type = Parameter(order=1, size=1, choices=Peer_Identity_Address_Type_Choices)
    """
    Identity address type.
    """

    Peer_Identity_Address = Parameter(order=2, size=6)
    """
    Public or Random (static) Identity address of the peer device
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Peer_Resolvable_Address = Parameter(order=2, size=6)
        """
        Resolvable Private Address being used by the peer device
        """


class HCI_LE_READ_LOCAL_RESOLVABLE_ADDRESS(CommandPacket):
    """
    The LE_Read_Local_Resolvable_Address command is used to get the current
    local Resolvable Private Address being used for the corresponding peer
    Identity Address. The local's resolvable address being used may change after
    the command is called.
    This command can be used at any time.
    When a Controller cannot find a Resolvable Private Address associated with
    the Peer Identity Address, it shall respond with error code 0x02 (Unknown
    Connection Identifier).
    (See Bluetooth Specification v.4.2, Vol. 2, Part E, 7.8.43)
    """

    CODE = 0x202C

    Peer_Identity_Address_Type_Choices = {
        0x00: "Public Identity Address",
        0x01: "Random (static) Identity Address",
    }
    Peer_Identity_Address_Type = Parameter(order=1, size=1, choices=Peer_Identity_Address_Type_Choices)
    """
    Identity address type.
    """

    Peer_Identity_Address = Parameter(order=2, size=6)
    """
    Public or Random (static) Identity address of the peer device
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Local_Resolvable_Address = Parameter(order=2, size=6)
        """
        Resolvable Private Address being used by the local device
        """


class HCI_LE_SET_ADDRESS_RESOLUTION_ENABLE(CommandPacket):
    """
    The LE_Set_Address_Resolution_Enable command is used to enable
    resolution of Resolvable Private Addresses in the Controller. This causes the
    Controller to use the resolving list whenever the Controller receives a local or
    peer Resolvable Private Address.
    This command can be used at any time except when:
    - Advertising is enabled
    - Scanning is enabled
    - Create connection command is outstanding
    (See Bluetooth Specification v.4.2, Vol. 2, Part E, 7.8.44)
    """

    CODE = 0x202D

    Address_Resolution_Enable_Choices = {
        0x00: "Address Resolution in controller disabled (default)",
        0x01: "Address Resolution in controller enabled",
    }
    Address_Resolution_Enable = Parameter(order=1, size=1, choices=Address_Resolution_Enable_Choices)
    """
    Enable/disable address resolution in the controller.
        0x00: Address Resolution in controller disabled (default),
        0x01: Address Resolution in controller enabled
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_SET_RESOLVABLE_PRIVATE_ADDRESS_TIMEOUT(CommandPacket):
    """
    The LE_Set_Resolvable_Private_Address_Timeout command set the length of
    time the controller uses a Resolvable Private Address before a new resolvable
    private address is generated and starts being used.
    This timeout applies to all addresses generated by the controller.
    (See Bluetooth Specification v.4.2, Vol. 2, Part E, 7.8.45)
    """

    CODE = 0x202E

    RPA_Timeout_Ranges = {
        (0x0001, 0xA1B8): "N/A",
    }
    RPA_Timeout = Parameter(order=1, size=2, ranges=RPA_Timeout_Ranges)
    """
    RPA_Timeout measured in seconds.
        Range for N: 0x0001 - 0xA1B8 (1 sec - approximately 11.5 hours)
        Default: N= 0x0384 (900 secs or 15 minutes)
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_READ_MAXIMUM_DATA_LENGTH(CommandPacket):
    """
    The LE_Read_Maximum_Data_Length command allows the Host to read the Controller  maximum supported payload octets and packet duration times for transmission and reception (supportedMaxTxOctets and supportedMaxTxTime, supportedMaxRxOctets, and supportedMaxRxTime, see [Vol 6] Part B, Section 4.5.10).
    """

    CODE = 0x202F

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        supportedMaxTxOctets = Parameter(order=2, size=2)
        """
        Maximum number of payload octets that the local Controller supports for transmission of a single Link Layer Data Channel PDU.
        Range 0x001B-0x00FB (0x0000 - 0x001A and 0x00FC - 0xFFFF Reserved for future use)
        """

        supportedMaxTxTime = Parameter(order=3, size=2)
        """
        Maximum time, in microseconds, that the local Controller supports for transmission of a single Link Layer Data Channel PDU.
        Range 0x0148-0x0848 (0x0000 - 0x0147 and 0x0849 - 0xFFFF Reserved for future use)
        """

        supportedMaxRxOctets = Parameter(order=4, size=2)
        """
        Maximum number of payload octets that the local Controller supports for reception of a single Link Layer Data Channel PDU.
        Range 0x001B-0x00FB (0x0000 - 0x001A and 0x00FC - 0xFFFF Reserved for future use)
        """

        supportedMaxRxTime = Parameter(order=5, size=2)
        """
        Maximum time, in microseconds, that the local Controller supports for reception of a single Link Layer Data Channel PDU.
        Range 0x0148-0x0848 (0x0000 - 0x0147 and 0x0849 - 0xFFFF Reserved for future use)
        """


class HCI_LE_SET_PRIVACY_MODE(CommandPacket):
    """
    The HCI_LE_Set_Privacy_Mode command is used to allow the Host to specify
    the privacy mode to be used for a given entry on the resolving list. The effect of
    this setting is specified in [Vol 6] Part B, Section 4.7.
    When an entry on the resolving list is removed, the mode associated with that
    entry shall also be removed.
    This command cannot be used when address translation is enabled in the
    Controller and:
    Advertising is enabled
    Scanning is enabled
    Create connection command is outstanding
    This command can be used at any time when address translation is disabled in
    the Controller.
    If the device is not on the resolving list, the Controller shall return the error
    code Unknown Connection Identifier (0x02).
    """

    CODE = 0x204E

    Peer_Identity_Address_Type_Choices = {
        0x00: "Public Identity Address",
        0x01: "Random (static) Identity Address",
    }
    Peer_Identity_Address_Type = Parameter(order=1, size=1, choices=Peer_Identity_Address_Type_Choices)
    """
    Peer Address type
    """

    Peer_Identity_Address = Parameter(order=2, size=6)
    """
    Public Identity Address or Random (static) Identity Address of the
        advertiser
    """

    Privacy_Mode_Choices = {
        0x00: "Network Privacy Mode",
        0x01: "Device Privacy Mode",
    }
    Privacy_Mode = Parameter(order=3, size=1, choices=Privacy_Mode_Choices)
    """
    0x00 Use Network Privacy Mode for this peer device (default)
        0x01 Use Device Privacy Mode for this peer device
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

