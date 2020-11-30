# NOTE: This file is auto-generated, please do not modify

from ..packet import *


class ACI_BLUE_INITIALIZED_EVENT(VendorEventPacket):
    """
    This event inform the application that the network coprocessor has been reset. If the reason code is a system crash,
    a following event ACI_BLUE_CRASH_INFO_EVENT will provide more information regarding the system crash details.
    """

    SUBCODE = 0x0001

    Reason_Code_Choices = {
        0x01: "Firmware started properly",
        0x02: "Updater mode entered with ACI command",
        0x03: "Updater mode entered due to bad Blue Flag",
        0x04: "Updater mode entered due to IRQ pin",
        0x05: "System reset due to watchdog",
        0x06: "System reset due to lockup",
        0x07: "System reset due to brownout reset",
        0x08: "System reset due to crash",
        0x09: "System reset due to ECC error",
    }
    Reason_Code = Parameter(order=1, size=1, choices=Reason_Code_Choices)
    """
    Reason code describing why device was reset and in which mode is operating (Updater or Normal mode)
    """


class ACI_BLUE_EVENTS_LOST_EVENT(VendorEventPacket):
    """
    This event is generated when an overflow occurs in the event queue read by the
    external microcontroller. This is normally caused when the external microcontroller does 
    not read pending events. The returned bitmap indicates which event has been lost. Please
     note that one bit set to 1 indicates one or more occurrences of the particular events.
    The event ACI_BLUE_EVENTS_LOST_EVENT cannot be lost and it will inserted in the
    event queue as soon as a position is freed in the event queue. This event should not happen under normal
    operating condition where external microcontroller promptly reads events signaled by IRQ pin.
    It is provided to detected unexpected behavior of the external microcontroller or to
    allow application to recover situations where critical events are lost.
    """

    SUBCODE = 0x0002

    Lost_Events_Choices = {
        0x0000000000000001: "HCI_DISCONNECTION_COMPLETE_EVENT",
        0x0000000000000002: "HCI_ENCRYPTION_CHANGE_EVENT",
        0x0000000000000004: "HCI_READ_REMOTE_VERSION_INFORMATION_COMPLETE_EVENT",
        0x0000000000000008: "HCI_COMMAND_COMPLETE_EVENT",
        0x0000000000000010: "HCI_COMMAND_STATUS_EVENT",
        0x0000000000000020: "HCI_HARDWARE_ERROR_EVENT",
        0x0000000000000040: "HCI_NUMBER_OF_COMPLETED_PACKETS_EVENT",
        0x0000000000000080: "HCI_ENCRYPTION_KEY_REFRESH_COMPLETE_EVENT",
        0x0000000000000100: "ACI_BLUE_INITIALIZED_EVENT",
        0x0000000000000200: "ACI_GAP_LIMITED_DISCOVERABLE_EVENT",
        0x0000000000000400: "ACI_GAP_PAIRING_COMPLETE_EVENT",
        0x0000000000000800: "ACI_GAP_PASS_KEY_REQ_EVENT",
        0x0000000000001000: "ACI_GAP_AUTHORIZATION_REQ_EVENT",
        0x0000000000002000: "ACI_GAP_SLAVE_SECURITY_INITIATED_EVENT",
        0x0000000000004000: "ACI_GAP_BOND_LOST_EVENT",
        0x0000000000008000: "ACI_GAP_PROC_COMPLETE_EVENT",
        0x0000000000010000: "ACI_GAP_ADDR_NOT_RESOLVED_EVENT",
        0x0000000000020000: "ACI_L2CAP_CONNECTION_UPDATE_RESP_EVENT",
        0x0000000000040000: "ACI_L2CAP_PROC_TIMEOUT_EVENT",
        0x0000000000080000: "ACI_L2CAP_CONNECTION_UPDATE_REQ_EVENT",
        0x0000000000100000: "ACI_GATT_ATTRIBUTE_MODIFIED_EVENT",
        0x0000000000200000: "ACI_GATT_PROC_TIMEOUT_EVENT",
        0x0000000000400000: "ACI_ATT_EXCHANGE_MTU_RESP_EVENT",
        0x0000000000800000: "ACI_ATT_FIND_INFO_RESP_EVENT",
        0x0000000001000000: "ACI_ATT_FIND_BY_TYPE_VALUE_RESP_EVENT",
        0x0000000002000000: "ACI_ATT_READ_BY_TYPE_RESP_EVENT",
        0x0000000004000000: "ACI_ATT_READ_RESP_EVENT",
        0x0000000008000000: "ACI_ATT_READ_BLOB_RESP_EVENT",
        0x0000000010000000: "ACI_ATT_READ_MULTIPLE_RESP_EVENT",
        0x0000000020000000: "ACI_ATT_READ_BY_GROUP_TYPE_RESP_EVENT",
        0x0000000040000000: "ACI_ATT_WRITE_RESP_EVENT",
        0x0000000080000000: "ACI_ATT_PREPARE_WRITE_RESP_EVENT",
        0x0000000100000000: "ACI_ATT_EXEC_WRITE_RESP_EVENT",
        0x0000000200000000: "ACI_GATT_INDICATION_EVENT",
        0x0000000400000000: "ACI_GATT_NOTIFICATION_EVENT",
        0x0000000800000000: "ACI_GATT_PROC_COMPLETE_EVENT",
        0x0000001000000000: "ACI_GATT_ERROR_RESP_EVENT",
        0x0000002000000000: "ACI_GATT_DISC_READ_CHAR_BY_UUID_RESP_EVENT",
        0x0000004000000000: "ACI_GATT_WRITE_PERMIT_REQ_EVENT",
        0x0000008000000000: "ACI_GATT_READ_PERMIT_REQ_EVENT",
        0x0000010000000000: "ACI_GATT_READ_MULTI_PERMIT_REQ_EVENT",
        0x0000020000000000: "ACI_GATT_TX_POOL_AVAILABLE_EVENT",
        0x0000040000000000: "ACI_GATT_SERVER_CONFIRMATION_EVENT",
        0x0000080000000000: "ACI_GATT_PREPARE_WRITE_PERMIT_REQ_EVENT",
        0x0000100000000000: "HCI_LE_CONNECTION_COMPLETE_EVENT",
        0x0000200000000000: "HCI_LE_ADVERTISING_REPORT_EVENT",
        0x0000400000000000: "HCI_LE_CONNECTION_UPDATE_COMPLETE_EVENT",
        0x0000800000000000: "HCI_LE_READ_REMOTE_USED_FEATURES_COMPLETE_EVENT",
        0x0001000000000000: "HCI_LE_LONG_TERM_KEY_REQUEST_EVENT",
        0x0002000000000000: "HCI_LE_DATA_LENGTH_CHANGE_EVENT",
        0x0004000000000000: "HCI_LE_READ_LOCAL_P256_PUBLIC_KEY_COMPLETE_EVENT",
        0x0008000000000000: "HCI_LE_GENERATE_DHKEY_COMPLETE_EVENT",
        0x0010000000000000: "HCI_LE_ENHANCED_CONNECTION_COMPLETE_EVENT",
        0x0020000000000000: "HCI_LE_DIRECT_ADVERTISING_REPORT_EVENT",
        0x0040000000000000: "ACI_GAP_NUMERIC_COMPARISON_VALUE_EVENT",
        0x0080000000000000: "ACI_GAP_KEYPRESS_NOTIFICATION_EVENT",
    }
    Lost_Events = Parameter(order=1, size=8, choices=Lost_Events_Choices, multi_choice=True)
    """
    Bitmap of lost events. Each bit indicates one or more occurrences of the specific event.
    """


class ACI_BLUE_CRASH_INFO_EVENT(VendorEventPacket):
    """
    This event is given to the application after the ACI_BLUE_INITIALIZED_EVENT
    when a system crash is detected. This events returns system crash information for debugging purposes. 
    Information reported are useful to understand the root cause of the crash.
    """

    SUBCODE = 0x0003

    Crash_Type_Choices = {
        0x00: "Assert failed",
        0x01: "NMI fault",
        0x02: "Hard fault",
    }
    Crash_Type = Parameter(order=1, size=1, choices=Crash_Type_Choices)
    """
    Crash type
    """

    SP = Parameter(order=2, size=4)
    """
    Stack pointer
    """

    R0 = Parameter(order=3, size=4)
    """
    Register R0
    """

    R1 = Parameter(order=4, size=4)
    """
    Register R1
    """

    R2 = Parameter(order=5, size=4)
    """
    Register R2
    """

    R3 = Parameter(order=6, size=4)
    """
    Register R3
    """

    R12 = Parameter(order=7, size=4)
    """
    Register R12
    """

    LR = Parameter(order=8, size=4)
    """
    Link register
    """

    PC = Parameter(order=9, size=4)
    """
    Program counter where crash occurred
    """

    xPSR = Parameter(order=10, size=4)
    """
    xPSR register
    """

    Debug_Data_Length = Parameter(order=11, size=1)
    """
    Length of Debug_Data field
    """

    Debug_Data = Parameter(order=12, size=Debug_Data_Length)
    """
    Debug data
    """


class ACI_HAL_END_OF_RADIO_ACTIVITY_EVENT(VendorEventPacket):
    """
    This event is generated when the device completes a radio activity and provide information when a new radio activity will be performed.
    Information provided includes type of radio activity and absolute time in system ticks when a new radio activity is schedule, if any. Application can use this information to schedule user activities synchronous to selected radio activities. A command ACI_HAL_SET_RADIO_ACTIVITY_MASK is provided to enable radio activity events of user interests, by default no events are enabled.
    User should take into account that enabling radio events in application with intense radio activity could lead to a fairly high rate of events generated.
    Application use cases includes synchronizing notification with connection interval, switching  antenna at the end of advertising or performing flash erase operation while radio is idle.
    """

    SUBCODE = 0x0004

    Last_State_Choices = {
        0x00: "Idle",
        0x01: "Advertising",
        0x02: "Connection event slave",
        0x03: "Scanning",
        0x04: "Connection request",
        0x05: "Connection event master",
        0x06: "TX test mode",
        0x07: "RX test mode",
    }
    Last_State = Parameter(order=1, size=1, choices=Last_State_Choices)
    """
    Completed radio events
    """

    Next_State_Choices = {
        0x00: "Idle",
        0x01: "Advertising",
        0x02: "Connection event slave",
        0x03: "Scanning",
        0x04: "Connection request",
        0x05: "Connection event master",
        0x06: "TX test mode",
        0x07: "RX test mode",
    }
    Next_State = Parameter(order=2, size=1, choices=Next_State_Choices)
    """
    Incoming radio events
    """

    Next_State_SysTime = Parameter(order=3, size=4)
    """
    32bit absolute current time expressed in internal time units.
    """


class ACI_HAL_SCAN_REQ_REPORT_EVENT(VendorEventPacket):
    """
    This event is reported to the application after a scan request is received and a scan reponse
    is scheduled to be transmitted.
    """

    SUBCODE = 0x0005

    RSSI_Choices = {
        127: "RSSI not available",
    }
    RSSI_Ranges = {
        (-127, 20): "N/A",
    }
    RSSI = Parameter(order=1, size=1, choices=RSSI_Choices, ranges=RSSI_Ranges)
    """
    N Size: 1 Octet (signed integer)
        Units: dBm
    """

    Peer_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Public Identity Address",
        0x03: "Random (Static) Identity Address",
    }
    Peer_Address_Type = Parameter(order=2, size=1, choices=Peer_Address_Type_Choices)
    """
    0x00 Public Device Address
        0x01 Random Device Address
        0x02 Public Identity Address (Corresponds to Resolved Private Address)
        0x03 Random (Static) Identity Address (Corresponds to Resolved Private Address)
    """

    Peer_Address = Parameter(order=3, size=6)
    """
    Public Device Address or Random Device Address of the peer device
    """


class ACI_HAL_FW_ERROR_EVENT(VendorEventPacket):
    """
    This event is generated to report firmware error informations.
    After this event with error type equal to either 0x01, 0x02 or 0x3, it is recommended to disconnect the link (handle is reported in Data field).
    """

    SUBCODE = 0x0006

    FW_Error_Type_Choices = {
        0x01: "HAL_FW_L2CAP_RECOMBINATION_ERROR",
        0x02: "HAL_FW_GATT_UNEXPECTED_RESPONSE_ERROR",
        0x03: "HAL_FW_GATT_SEQUENTIAL_PROTOCOL_ERROR",
        0x04: "HAL_FW_BONDING_DB_FULL_PAIRING_ERROR",
        0x05: "HAL_FW_BONDING_DB_FULL_GATTSERVICE_ERROR",
    }
    FW_Error_Type = Parameter(order=1, size=1, choices=FW_Error_Type_Choices)
    """
    Errore code identifying the type of error that has occurred.
    """

    Data_Length = Parameter(order=2, size=1)
    """
    Length of Data in octets
    """

    Data = Parameter(order=3, size=Data_Length)
    """
    If FW_Error_Type is 0x01, 0x02 or 0x03, this parameter contains the connection handle where the abnormal condition has occurred.
    """

