# NOTE: This file is auto-generated, please do not modify

from ..packet import *


class HCI_DISCONNECTION_COMPLETE_EVENT(EventPacket):
    """
    The Disconnection Complete event occurs when a connection is terminated.
    The status parameter indicates if the disconnection was successful or not. The
    reason parameter indicates the reason for the disconnection if the disconnection
    was successful. If the disconnection was not successful, the value of the
    reason parameter can be ignored by the Host. For example, this can be the
    case if the Host has issued the Disconnect command and there was a parameter
    error, or the command was not presently allowed, or a Connection_Handle
    that didn't correspond to a connection was given.
    """

    CODE = 0x05

    Status = Parameter(order=1, size=1)
    """
    For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
    """

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=2, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection_Handle which was disconnected.
    """

    Reason = Parameter(order=3, size=1)
    """
    Reason for disconnection. See Error Codes.
    """


class HCI_ENCRYPTION_CHANGE_EVENT(EventPacket):
    """
    The Encryption Change event is used to indicate that the change of the encryption
    mode has been completed. The Connection_Handle will be a Connection_Handle
    for an ACL connection. The Encryption_Enabled event parameter
    specifies the new Encryption_Enabled parameter for the Connection_Handle
    specified by the Connection_Handle event parameter. This event will occur on
    both devices to notify the Hosts when Encryption has changed for the specified
    Connection_Handle between two devices. Note: This event shall not be generated
    if encryption is paused or resumed; during a role switch, for example.
    The meaning of the Encryption_Enabled parameter depends on whether the
    Host has indicated support for Secure Connections in the Secure_Connections_Host_Support
    parameter. When Secure_Connections_Host_Support is
    'disabled' or the Connection_Handle refers to an LE link, the Controller shall
    only use Encryption_Enabled values 0x00 (OFF) and 0x01 (ON).
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.7.8)
    """

    CODE = 0x08

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

    Encryption_Enabled_Choices = {
        0x00: "Link Level Encryption OFF",
        0x01: "Link Level Encryption is ON with AES-CCM",
    }
    Encryption_Enabled = Parameter(order=3, size=1, choices=Encryption_Enabled_Choices)
    """
    Link Level Encryption.
    """


class HCI_READ_REMOTE_VERSION_INFORMATION_COMPLETE_EVENT(EventPacket):
    """
    The Read Remote Version Information Complete event is used to indicate the
    completion of the process obtaining the version information of the remote Controller
    specified by the Connection_Handle event parameter. The Connection_Handle
    shall be for an ACL connection.
    The Version event parameter defines the specification version of the LE Controller.
    The Manufacturer_Name event parameter indicates the manufacturer
    of the remote Controller. The Subversion event parameter is controlled
    by the manufacturer and is implementation dependent. The Subversion
    event parameter defines the various revisions that each version of the Bluetooth
    hardware will go through as design processes change and errors are
    fixed. This allows the software to determine what Bluetooth hardware is being
    used and, if necessary, to work around various bugs in the hardware.
    When the Connection_Handle is associated with an LE-U logical link, the Version
    event parameter shall be Link Layer VersNr parameter, the Manufacturer_Name
    event parameter shall be the CompId parameter, and the Subversion
    event parameter shall be the SubVersNr parameter.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.7.12)
    """

    CODE = 0x0C

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

    Version = Parameter(order=3, size=1)
    """
    Version of the Current LMP in the remote Controller
    """

    Manufacturer_Name = Parameter(order=4, size=2)
    """
    Manufacturer Name of the remote Controller
    """

    Subversion = Parameter(order=5, size=2)
    """
    Subversion of the LMP in the remote Controller
    """


class HCI_HARDWARE_ERROR_EVENT(EventPacket):
    """
    The Hardware Error event is used to indicate some implementation specific type of hardware failure for the controller. This event is used to notify the Host that a hardware failure has occurred in the Controller.
    """

    CODE = 0x10

    Hardware_Code_Choices = {
        0x01: "Radio state error",
        0x02: "Timer overrun error",
        0x03: "Internal queue overflow error",
    }
    Hardware_Code = Parameter(order=1, size=1, choices=Hardware_Code_Choices)
    """
    Hardware Error Event code.
        Error code 0x01 and 0x02 are errors generally caused by hardware issue on the PCB; another possible cause is a slow crystal startup.
        In the latter case, the HS_STARTUP_TIME in the device configuration needs to be tuned.
        Error code 0x03 indicates an internal error of the protocol stack.
        After this event is recommended to force device reset.
    """


class HCI_NUMBER_OF_COMPLETED_PACKETS_EVENT(EventPacket):
    """
    'The Number Of Completed Packets event is used by the Controller to indicate
    to the Host how many HCI Data Packets have been completed (transmitted or
    flushed) for each Connection_Handle since the previous Number Of Completed
    Packets event was sent to the Host. This means that the corresponding
    buffer space has been freed in the Controller. Based on this information, and
    the HC_Total_Num_ACL_Data_Packets and HC_Total_Num_Synchronous_-
    Data_Packets return parameter of the Read_Buffer_Size command, the Host
    can determine for which Connection_Handles the following HCI Data Packets
    should be sent to the Controller. The Number Of Completed Packets event
    must not be sent before the corresponding Connection Complete event. While
    the Controller has HCI data packets in its buffer, it must keep sending the Number
    Of Completed Packets event to the Host at least periodically, until it finally
    reports that all the pending ACL Data Packets have been transmitted or
    flushed.
    """

    CODE = 0x13

    Number_of_Handles = Parameter(order=1, size=1)
    """
    The number of Connection_Handles and Num_HCI_Data_Packets parameters pairs contained in this event
    """

    Connection_Handle_N = Parameter(order=2, size=2)
    """
    Connection handle
    """

    HC_Num_Of_Completed_Packets_N = Parameter(order=3, size=2)
    """
    The number of HCI Data Packets that have been completed (transmitted
        or flushed) for the associated Connection_Handle since the previous time
        the event was returned.
    """


class HCI_DATA_BUFFER_OVERFLOW_EVENT(EventPacket):
    """
    'This event is used to indicate that the Controller's data buffers have been overflowed.
    This can occur if the Host has sent more packets than allowed. The
    Link_Type parameter is used to indicate that the overflow was caused by ACL data.
    """

    CODE = 0x1A

    Link_Type_Choices = {
        0x01: "ACL Buffer Overflow",
    }
    Link_Type = Parameter(order=1, size=1, choices=Link_Type_Choices)
    """
    On which type of channel overflow has occurred.
    """


class HCI_ENCRYPTION_KEY_REFRESH_COMPLETE_EVENT(EventPacket):
    """
    'The Encryption Key Refresh Complete event is used to indicate to the Host
    that the encryption key was refreshed on the given Connection_Handle any
    time encryption is paused and then resumed.
    If the Encryption Key Refresh Complete event was generated due to an
    encryption pause and resume operation embedded within a change connection
    link key procedure, the Encryption Key Refresh Complete event shall be sent
    prior to the Change Connection Link Key Complete event.
    If the Encryption Key Refresh Complete event was generated due to an
    encryption pause and resume operation embedded within a role switch procedure,
    the Encryption Key Refresh Complete event shall be sent prior to the
    Role Change event.
    """

    CODE = 0x30

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


class HCI_COMMAND_COMPLETE_EVENT(EventPacket):
    """
    'The Command Complete event is used by the Controller for most commands
    to transmit return status of a command and the other event parameters that are
    specified for the issued HCI command.
    The Num_HCI_Command_Packets event parameter allows the Controller to
    indicate the number of HCI command packets the Host can send to the Controller.
    If the Controller requires the Host to stop sending commands, the
    Num_HCI_Command_Packets event parameter will be set to zero. To indicate
    to the Host that the Controller is ready to receive HCI command packets, the
    Controller generates a Command Complete event with the Command_Opcode
    0x0000, and the Num_HCI_Command_Packets event parameter is set to 1 or
    more. See each command for the parameters that are returned
    by this event.
    """

    CODE = 0x0E

    Num_HCI_Command_Packets = Parameter(order=1, size=1)
    """
    The Number of HCI command packets which are allowed to be sent to the
        Controller from the Host.
    """

    Command_Opcode = Parameter(order=2, size=2)
    """
    Opcode of the command which caused this event.
    """


class HCI_COMMAND_STATUS_EVENT(EventPacket):
    """
    'The Command Status event is used to indicate that the command described by
    the Command_Opcode parameter has been received, and that the Controller
    is currently performing the task for this command. This event is needed to provide
    mechanisms for asynchronous operation, which makes it possible to prevent
    the Host from waiting for a command to finish. If the command cannot
    begin to execute (a parameter error may have occurred, or the command may
    currently not be allowed), the Status event parameter will contain the corresponding
    error code, and no complete event will follow since the command was
    not started. The Num_HCI_Command_Packets event parameter allows the
    Controller to indicate the number of HCI command packets the Host can send
    to the Controller. If the Controller requires the Host to stop sending commands,
    the Num_HCI_Command_Packets event parameter will be set to zero. To indicate
    to the Host that the Controller is ready to receive HCI command packets,
    the Controller generates a Command Status event with Status 0x00 and Command_Opcode
    0x0000, and the Num_HCI_Command_Packets event parameter
    is set to 1 or more.
    """

    CODE = 0x0F

    Status = Parameter(order=1, size=1)
    """
    For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
    """

    Num_HCI_Command_Packets = Parameter(order=2, size=1)
    """
    The Number of HCI command packets which are allowed to be sent to the
        Controller from the Host.
    """

    Command_Opcode = Parameter(order=3, size=2)
    """
    Opcode of the command which caused this event.
    """

