# NOTE: This file is auto-generated, please do not modify

from ..packet import *
from .. import events


class ACI_GAP_SET_NON_DISCOVERABLE(CommandPacket):
    """
    Put the device in non-discoverable mode. This command disables the LL advertising.
    """

    CODE = 0xFC81

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_SET_LIMITED_DISCOVERABLE(CommandPacket):
    """
    Put the device in limited discoverable mode (as defined in Bluetooth Specification v.4.1,
    Vol. 3, Part C, section 9.2.3). The device will be discoverable for maximum period of TGAP
    (lim_adv_timeout) = 180 seconds (from errata). The advertising can be disabled at any time
    by issuing ACI_GAP_SET_NON_DISCOVERABLE command.
    The Adv_Interval_Min and Adv_Interval_Max parameters are optional. If both are set to 0,
    the GAP will use default values for adv intervals for limited discoverable mode (250 ms
    and 500 ms respectively).
    To allow a fast connection, the host can set Local_Name, Service_Uuid_List,
    Slave_Conn_Interval_Min and Slave_Conn_Interval_Max. If provided, these data will be 
    inserted into the advertising packet payload as AD data. These parameters are optional
    in this command. These values can be set in advertised data using GAP_Update_Adv_Data
    command separately.
    The total size of data in advertising packet cannot exceed 31 bytes.
    With this command, the BLE Stack will also add automatically the following
    standard AD types:
    - AD Flags
    - Power Level
    When advertising timeout happens (i.e. limited discovery period has elapsed), controller generates
    ACI_GAP_LIMITED_DISCOVERABLE_EVENT event.
    """

    CODE = 0xFC82

    Advertising_Type_Choices = {
        0x00: "ADV_IND (Connectable undirected advertising)",
        0x01: "ADV_DIRECT_IND (Connectable directed advertising)",
        0x02: "ADV_SCAN_IND (Scannable undirected advertising)",
        0x03: "ADV_NONCONN_IND (Non connectable undirected advertising)",
    }
    Advertising_Type = Parameter(order=1, size=1, choices=Advertising_Type_Choices)
    """
    Advertising type. Advertising_Type type cannot be any of GAP_ADV_HIGH_DC_DIRECT_IND or GAP_ADV_HIGH_DC_DIRECT_IND.
    """

    Advertising_Interval_Min_Ranges = {
        (0x0020, 0x4000): ("20.000 ms", "10240.000 ms"),
    }
    Advertising_Interval_Min = Parameter(order=2, size=2, ranges=Advertising_Interval_Min_Ranges)
    """
    Minimum advertising interval for undirected and low duty cycle directed
        advertising.
        Time = N * 0.625 msec.
    """

    Advertising_Interval_Max_Ranges = {
        (0x0020, 0x4000): ("20.000 ms", "10240.000 ms"),
    }
    Advertising_Interval_Max = Parameter(order=3, size=2, ranges=Advertising_Interval_Max_Ranges)
    """
    Maximum advertising interval.
        Time = N * 0.625 msec.
    """

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address",
        0x03: "Non Resolvable Private Address",
    }
    Own_Address_Type = Parameter(order=4, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type:
        
        0x00: Public Device Address (it is allowed only if privacy is disabled)
        0x01: Random Device Address (it is allowed only if privacy is disabled)
        0x02: Resolvable Private Address (it is allowed only if privacy is enabled)
        0x03: Non Resolvable Private Address (it is allowed only if privacy is enabled)
    """

    Advertising_Filter_Policy = Parameter(order=5, size=1)
    """
    Advertising filter policy: not applicable (the value of Advertising_Filter_Policy parameter is not used inside the Stack)
    """

    Local_Name_Length = Parameter(order=6, size=1)
    """
    Length of the local_name field in octets.
        If length is set to 0x00, Local_Name parameter is not used.
    """

    Local_Name = Parameter(order=7, size=Local_Name_Length)
    """
    Local name of the device. First byte must be 0x08 for Shortened Local Name
        or 0x09 for Complete Local Name. No NULL character at the end.
    """

    Service_UUID_Length = Parameter(order=8, size=1)
    """
    Length of the Service Uuid List in octets.
        If there is no service to be advertised, set this field to 0x00.
    """

    Service_UUID_List = Parameter(order=9, size=Service_UUID_Length)
    """
    This is the list of the UUIDs as defined in Volume 3,
        Section 11 of GAP Specification. First byte is the AD Type.
        See also Supplement to the Bluetooth Core specification.
    """

    Slave_Conn_Interval_Min_Choices = {
        0x0000: "(NaN)",
        0xFFFF: "(NaN) No specific minimum",
    }
    Slave_Conn_Interval_Min_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Slave_Conn_Interval_Min = Parameter(order=10, size=2, choices=Slave_Conn_Interval_Min_Choices, ranges=Slave_Conn_Interval_Min_Ranges)
    """
    Minimum value for slave connection interval suggested by the Peripheral.
        If Slave_Conn_Interval_Min and Slave_Conn_Interval_Max are not 0x0000, Slave Connection Interval Range AD structure will be added in advertising data.
        Connection interval is defined in the following manner:
        connIntervalmin = Slave_Conn_Interval_Min x 1.25ms.
    """

    Slave_Conn_Interval_Max_Choices = {
        0x0000: "(NaN)",
        0xFFFF: "(NaN) No specific maximum",
    }
    Slave_Conn_Interval_Max_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Slave_Conn_Interval_Max = Parameter(order=11, size=2, choices=Slave_Conn_Interval_Max_Choices, ranges=Slave_Conn_Interval_Max_Ranges)
    """
    Slave connection interval maximum value suggested by Peripheral.
        If Slave_Conn_Interval_Min and Slave_Conn_Interval_Max are not 0x0000, Slave Connection Interval Range AD structure will be added in advertising data.
        Connection interval is defined in the following manner:
        connIntervalmax = Slave_Conn_Interval_Max x 1.25ms
    """


class ACI_GAP_SET_DISCOVERABLE(CommandPacket):
    """
    Put the device in general discoverable mode (as defined in Bluetooth Specification v.4.1,
    Vol. 3, Part C, section 9.2.4). The device will be discoverable until the host issues 
    the ACI_GAP_SET_NON_DISCOVERABLE command. The Adv_Interval_Min and Adv_Interval_Max
    parameters are optional. If both are set to 0, the GAP uses the default values for adv
    intervals for general discoverable mode.
    When using connectable undirected advertising events:
    - Adv_Interval_Min = 30 ms 
    - Adv_Interval_Max = 60 ms
    When using non-connectable advertising events or scannable undirected advertising events:
    - Adv_Interval_Min = 100 ms 
    - Adv_Interval_Max = 150 ms 
    Host can set the Local Name, a Service UUID list and the Slave Connection Interval Range.
    If provided, these data will be inserted into the advertising packet payload as AD data.
    These parameters are optional in this command. These values can be also set using
    aci_gap_update_adv_data() separately.
    The total size of data in advertising packet cannot exceed 31 bytes.
    With this command, the BLE Stack will also add automatically the following standard
    AD types:
    - AD Flags
    - TX Power Level
    """

    CODE = 0xFC83

    Advertising_Type_Choices = {
        0x00: "ADV_IND (Connectable undirected advertising)",
        0x01: "ADV_DIRECT_IND (Connectable directed advertising)",
        0x02: "ADV_SCAN_IND (Scannable undirected advertising)",
        0x03: "ADV_NONCONN_IND (Non connectable undirected advertising)",
    }
    Advertising_Type = Parameter(order=1, size=1, choices=Advertising_Type_Choices)
    """
    Advertising type. Advertising_Type type cannot be any of GAP_ADV_HIGH_DC_DIRECT_IND or GAP_ADV_HIGH_DC_DIRECT_IND.
    """

    Advertising_Interval_Min_Ranges = {
        (0x0020, 0x4000): ("20.000 ms", "10240.000 ms"),
    }
    Advertising_Interval_Min = Parameter(order=2, size=2, ranges=Advertising_Interval_Min_Ranges)
    """
    Minimum advertising interval for undirected and low duty cycle directed
        advertising.
        Time = N * 0.625 msec.
    """

    Advertising_Interval_Max_Ranges = {
        (0x0020, 0x4000): ("20.000 ms", "10240.000 ms"),
    }
    Advertising_Interval_Max = Parameter(order=3, size=2, ranges=Advertising_Interval_Max_Ranges)
    """
    Maximum advertising interval.
        Time = N * 0.625 msec.
    """

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address",
        0x03: "Non Resolvable Private Address",
    }
    Own_Address_Type = Parameter(order=4, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type:
        
        0x00: Public Device Address (it is allowed only if privacy is disabled)
        0x01: Random Device Address (it is allowed only if privacy is disabled)
        0x02: Resolvable Private Address (it is allowed only if privacy is enabled)
        0x03: Non Resolvable Private Address (it is allowed only if privacy is enabled)
    """

    Advertising_Filter_Policy = Parameter(order=5, size=1)
    """
    Advertising filter policy: not applicable (the value of Advertising_Filter_Policy parameter is not used inside the Stack)
    """

    Local_Name_Length = Parameter(order=6, size=1)
    """
    Length of the local_name field in octets.
        If length is set to 0x00, Local_Name parameter is not used.
    """

    Local_Name = Parameter(order=7, size=Local_Name_Length)
    """
    Local name of the device. First byte must be 0x08 for Shortened Local Name
        or 0x09 for Complete Local Name. No NULL character at the end.
    """

    Service_UUID_Length = Parameter(order=8, size=1)
    """
    Length of the Service Uuid List in octets.
        If there is no service to be advertised, set this field to 0x00.
    """

    Service_UUID_List = Parameter(order=9, size=Service_UUID_Length)
    """
    This is the list of the UUIDs as defined in Volume 3,
        Section 11 of GAP Specification. First byte is the AD Type.
        See also Supplement to the Bluetooth Core specification.
    """

    Slave_Conn_Interval_Min_Choices = {
        0x0000: "(NaN)",
        0xFFFF: "(NaN) No specific minimum",
    }
    Slave_Conn_Interval_Min_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Slave_Conn_Interval_Min = Parameter(order=10, size=2, choices=Slave_Conn_Interval_Min_Choices, ranges=Slave_Conn_Interval_Min_Ranges)
    """
    Minimum value for slave connection interval suggested by the Peripheral.
        If Slave_Conn_Interval_Min and Slave_Conn_Interval_Max are not 0x0000, Slave Connection Interval Range AD structure will be added in advertising data.
        Connection interval is defined in the following manner:
        connIntervalmin = Slave_Conn_Interval_Min x 1.25ms.
    """

    Slave_Conn_Interval_Max_Choices = {
        0x0000: "(NaN)",
        0xFFFF: "(NaN) No specific maximum",
    }
    Slave_Conn_Interval_Max_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Slave_Conn_Interval_Max = Parameter(order=11, size=2, choices=Slave_Conn_Interval_Max_Choices, ranges=Slave_Conn_Interval_Max_Ranges)
    """
    Slave connection interval maximum value suggested by Peripheral.
        If Slave_Conn_Interval_Min and Slave_Conn_Interval_Max are not 0x0000, Slave Connection Interval Range AD structure will be added in advertising data.
        Connection interval is defined in the following manner:
        connIntervalmax = Slave_Conn_Interval_Max x 1.25ms
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_SET_DIRECT_CONNECTABLE(CommandPacket):
    """
    Set the device in direct connectable mode (as defined in Bluetooth Specification v.4.1,
    Vol. 3, Part C, section 9.3.3). Device uses direct connectable mode to advertise using High Duty
    cycle advertisement events or Low Duty cycle advertisement events and the address as
    either what is specified in the Own Address Type parameter. The command specifies the type of the advertising used.
    If the privacy is enabled, the Type parameter in reconnection address is used for advertising, otherwise the address
    of the type specified in OwnAddrType is used.
    The device will be in directed connectable mode only for 1.28 seconds. If no connection
    is established within this duration, the device enters non discoverable mode and
    advertising will have to be again enabled explicitly.
    The controller generates a HCI_LE_CONNECTION_COMPLETE_EVENT event with the status set to
    0x3C (Directed Advertising Timeout) if the connection was not established and 0x00 if the
    connection was successfully established.
    If Host privacy (i.e. privacy 1.1) is enabled this command returns BLE_STATUS_INVALID_PARAMS.
    """

    CODE = 0xFC84

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address",
    }
    Own_Address_Type = Parameter(order=1, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type:
        
        0x00: Public Device Address (only if privacy is disabled)
        0x01: Random Device Address (only if privacy is disabled)
        0x02: Resolvable Private Address (only if privacy is enabled)
    """

    Directed_Advertising_Type_Choices = {
        0x01: "High Duty Cycle Directed Advertising",
        0x04: "Low Duty Cycle Directed Advertising",
    }
    Directed_Advertising_Type = Parameter(order=2, size=1, choices=Directed_Advertising_Type_Choices)
    """
    Type of directed advertising.
    """

    Direct_Address_Type_Choices = {
        0x00: "Public Device Address or Public Identity Address",
        0x01: "Random Device Address or Random (static) Identity Address",
    }
    Direct_Address_Type = Parameter(order=3, size=1, choices=Direct_Address_Type_Choices)
    """
    Peer Address type.
    """

    Direct_Address = Parameter(order=4, size=6)
    """
    Initiator Bluetooth address
    """

    Advertising_Interval_Min_Ranges = {
        (0x0020, 0x4000): ("20.000 ms", "10240.000 ms"),
    }
    Advertising_Interval_Min = Parameter(order=5, size=2, ranges=Advertising_Interval_Min_Ranges)
    """
    Minimum advertising interval for undirected and low duty cycle directed
        advertising.
        Time = N * 0.625 msec.
    """

    Advertising_Interval_Max_Ranges = {
        (0x0020, 0x4000): ("20.000 ms", "10240.000 ms"),
    }
    Advertising_Interval_Max = Parameter(order=6, size=2, ranges=Advertising_Interval_Max_Ranges)
    """
    Maximum advertising interval.
        Time = N * 0.625 msec.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_SET_IO_CAPABILITY(CommandPacket):
    """
    Set the IO capabilities of the device. This command has to be given only when the device is
    not in a connected state.
    """

    CODE = 0xFC85

    IO_Capability_Choices = {
        0x00: "IO_CAP_DISPLAY_ONLY",
        0x01: "IO_CAP_DISPLAY_YES_NO",
        0x02: "IO_CAP_KEYBOARD_ONLY",
        0x03: "IO_CAP_NO_INPUT_NO_OUTPUT",
        0x04: "IO_CAP_KEYBOARD_DISPLAY",
    }
    IO_Capability = Parameter(order=1, size=1, choices=IO_Capability_Choices)
    """
    IO capability of the device.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_SET_AUTHENTICATION_REQUIREMENT(CommandPacket):
    """
    Set the authentication requirements for the device. This command has to be
    given only when the device is not in a connected state.
    """

    CODE = 0xFC86

    Bonding_Mode_Choices = {
        0x00: "NO_BONDING",
        0x01: "BONDING",
    }
    Bonding_Mode = Parameter(order=1, size=1, choices=Bonding_Mode_Choices)
    """
    Bonding mode.
        Only if bonding is enabled (0x01), the bonding
        information is stored in flash
    """

    MITM_Mode_Choices = {
        0x00: "MITM_PROTECTION_NOT_REQUIRED",
        0x01: "MITM_PROTECTION_REQUIRED",
    }
    MITM_Mode = Parameter(order=2, size=1, choices=MITM_Mode_Choices)
    """
    MITM mode.
    """

    SC_Support_Choices = {
        0x00: "SC_IS_NOT_SUPPORTED",
        0x01: "SC_IS_SUPPORTED",
        0x02: "SC_IS_MANDATORY",
    }
    SC_Support = Parameter(order=3, size=1, choices=SC_Support_Choices)
    """
    LE Secure connections support.
        - 0x00: Secure Connections Pairing not supported
        - 0x01: Secure Connections Pairing supported but optional
        - 0x02: Secure Connections Pairing supported and mandatory (SC Only Mode)
    """

    KeyPress_Notification_Support_Choices = {
        0x00: "KEYPRESS_IS_NOT_SUPPORTED",
        0x01: "KEYPRESS_IS_SUPPORTED",
    }
    KeyPress_Notification_Support = Parameter(order=4, size=1, choices=KeyPress_Notification_Support_Choices)
    """
    Keypress notification support
    """

    Min_Encryption_Key_Size = Parameter(order=5, size=1)
    """
    Minimum encryption key size to be used during pairing
    """

    Max_Encryption_Key_Size = Parameter(order=6, size=1)
    """
    Maximum encryption key size to be used during pairing
    """

    Use_Fixed_Pin_Choices = {
        0x00: "USE_FIXED_PIN_FOR_PAIRING",
        0x01: "DONOT_USE_FIXED_PIN_FOR_PAIRING",
    }
    Use_Fixed_Pin = Parameter(order=7, size=1, choices=Use_Fixed_Pin_Choices)
    """
    Use or not fixed pin. If set to 0x00, then during the pairing process
        the application will not be requested for a pin (Fixed_Pin will be used).
        If set to 0x01, then during pairing process if a
        passkey is required the application will be
        notified
    """

    Fixed_Pin_Ranges = {
        (0, 999999): "N/A",
    }
    Fixed_Pin = Parameter(order=8, size=4, ranges=Fixed_Pin_Ranges)
    """
    Fixed pin to be used during pairing if MIMT protection is enabled.
        Any random value between 0 to 999999
    """

    Identity_Address_Type_Choices = {
        0x00: "Public Identity Address",
        0x01: "Random (static) Identity Address",
    }
    Identity_Address_Type = Parameter(order=9, size=1, choices=Identity_Address_Type_Choices)
    """
    Identity address type.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_SET_AUTHORIZATION_REQUIREMENT(CommandPacket):
    """
    Set the authorization requirements of the device. This command has to be given when connected
    to a device if authorization is required to access services which require authorization.
    """

    CODE = 0xFC87

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Authorization_Enable_Choices = {
        0x00: "AUTHORIZATION_NOT_REQUIRED",
        0x01: "AUTHORIZATION_REQUIRED",
    }
    Authorization_Enable = Parameter(order=2, size=1, choices=Authorization_Enable_Choices)
    """
    Enable the authorization in the device
        and when a remote device tries to read/write a characteristic with authorization
        requirements, the stack will send back an error response with
        "Insufficient authorization" error code. After pairing is complete a
        ACI_GAP_AUTHORIZATION_REQ_EVENT will be sent to the Host.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_PASS_KEY_RESP(CommandPacket):
    """
    This command should be send by the host in response to ACI_GAP_PASS_KEY_REQ_EVENT
    event. The command parameter contains the pass key which will be used during the pairing
    process.
    """

    CODE = 0xFC88

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Pass_Key_Ranges = {
        (0, 999999): "N/A",
    }
    Pass_Key = Parameter(order=2, size=4, ranges=Pass_Key_Ranges)
    """
    Pass key that will be used during the pairing process.
        Must be a six-digit decimal number.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_AUTHORIZATION_RESP(CommandPacket):
    """
    Authorize a device to access attributes. This command should be send by the host in
    response to ACI_GAP_AUTHORIZATION_REQ_EVENT event.
    """

    CODE = 0xFC89

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Authorize_Choices = {
        0x01: "Authorize",
        0x02: "Reject",
    }
    Authorize = Parameter(order=2, size=1, choices=Authorize_Choices)
    """
    Authorization response.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_INIT(CommandPacket):
    """
    Initialize the GAP layer. Register the GAP service with the GATT.
    All the standard GAP characteristics will also be added:
    - Device Name
    - Appearance
    - Peripheral Preferred Connection Parameters (peripheral role only)
    
    WARNING: A section of the Flash memory (pointed by stored_device_id_data_p) is used by this procedure. When this section is empty, data are written inside.
    This normally happens once during the lifetime of the device, when the command is executed for the first time (or every time it is called after that section has been erased).
    Do not power off the device while this function is writing into Flash memory.
    If the functions returns FLASH_WRITE_FAILED, it means that the flash area pointed by stored_device_id_data_p is corrupted (probably due to a power loss during the first call to aci_gap_init()). To fix the problem, that flash area has to be erased, so that the aci_gap_init() can reinitialize it correctly.
    """

    CODE = 0xFC8A

    Role_Choices = {
        0x01: "Peripheral",
        0x02: "Broadcaster",
        0x04: "Central",
        0x08: "Observer",
    }
    Role = Parameter(order=1, size=1, choices=Role_Choices, multi_choice=True)
    """
    Bitmap of allowed roles.
    """

    privacy_enabled_Choices = {
        0x00: "Privacy disabled",
        0x01: "Privacy host enabled",
        0x02: "Privacy controller enabled",
    }
    privacy_enabled = Parameter(order=2, size=1, choices=privacy_enabled_Choices)
    """
    Specify if privacy is enabled or not and which one .
    """

    device_name_char_len_Ranges = {
        (0, 248): "N/A",
    }
    device_name_char_len = Parameter(order=3, size=1, ranges=device_name_char_len_Ranges)
    """
    Length of the device name characteristic
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Service_Handle = Parameter(order=2, size=2)
        """
        Handle of the GAP service
        """

        Dev_Name_Char_Handle = Parameter(order=3, size=2)
        """
        Device Name Characteristic handle
        """

        Appearance_Char_Handle = Parameter(order=4, size=2)
        """
        Appearance Characteristic handle
        """


class ACI_GAP_SET_NON_CONNECTABLE(CommandPacket):
    """
    Put the device into non connectable mode. This mode does not support connection. The
    privacy setting done in the ACI_GAP_INIT command plays a role in deciding the valid 
    parameters for this command.
    Advertiser filter policy is internally set to 0x00
    """

    CODE = 0xFC8B

    Advertising_Event_Type_Choices = {
        0x02: "ADV_SCAN_IND (Scannable undirected advertising)",
        0x03: "ADV_NONCONN_IND (Non connectable undirected advertising)",
    }
    Advertising_Event_Type = Parameter(order=1, size=1, choices=Advertising_Event_Type_Choices)
    """
    Advertising type.
    """

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address",
        0x03: "Non Resolvable Private Address",
    }
    Own_Address_Type = Parameter(order=2, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type:
        
        0x00: Public Device Address (it is allowed only if privacy is disabled)
        0x01: Random Device Address (it is allowed only if privacy is disabled)
        0x02: Resolvable Private Address (it is allowed only if privacy is enabled)
        0x03: Non Resolvable Private Address (it is allowed only if privacy is enabled)
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_SET_UNDIRECTED_CONNECTABLE(CommandPacket):
    """
    Put the device into undirected connectable mode.
    If privacy is enabled in the device, a resolvable private address is generated and used as the 
    advertiser's address. If not, the address of the type specified in own_addr_type is used for
    advertising.
    """

    CODE = 0xFC8C

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

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address",
        0x03: "Non Resolvable Private Address",
    }
    Own_Address_Type = Parameter(order=3, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type:
        
        0x00: Public Device Address (it is allowed only if privacy is disabled)
        0x01: Random Device Address (it is allowed only if privacy is disabled)
        0x02: Resolvable Private Address (it is allowed only if controller privacy is enabled or if Host privacy (i.e. privacy 1.1) is enabled)
        0x03: Non Resolvable Private Address (it is allowed only if Host privacy (i.e. privacy 1.1) is enabled)
    """

    Adv_Filter_Policy_Choices = {
        0x00: "NO_WHITE_LIST_USE",
        0x03: "WHITE_LIST_FOR_ALL",
    }
    Adv_Filter_Policy = Parameter(order=4, size=1, choices=Adv_Filter_Policy_Choices)
    """
    Advertising filter policy.
        - 0x00: Allow Scan Request from Any, Allow Connect Request from Any
        - 0x03: Allow Scan Request from White List Only, Allow Connect Request from White List Only
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_SLAVE_SECURITY_REQ(CommandPacket):
    """
    Send a slave security request to the master.
    This command has to be issued to notify the master of the security requirements of the slave.
    The master may encrypt the link, initiate the pairing procedure, or reject the request.
    """

    CODE = 0xFC8D

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """


class ACI_GAP_UPDATE_ADV_DATA(CommandPacket):
    """
    This command can be used to update the advertising data for a particular AD type. If the AD
    type specified does not exist, then it is added to the advertising data. If the overall
    advertising data length is more than 31 octets after the update, then the command is
    rejected and the old data is retained.
    """

    CODE = 0xFC8E

    AdvDataLen = Parameter(order=1, size=1)
    """
    Length of AdvData in octets
    """

    AdvData = Parameter(order=2, size=AdvDataLen)
    """
    Advertising data used by the device while advertising.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_DELETE_AD_TYPE(CommandPacket):
    """
    This command can be used to delete the specified AD type from the advertisement data if
    present.
    """

    CODE = 0xFC8F

    ADType = Parameter(order=1, size=1)
    """
    One of the AD types like in Bluetooth specification (see volume 3, Part C, 11.1)
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_GET_SECURITY_LEVEL(CommandPacket):
    """
    This command can be used to get the current security settings of the device.
    """

    CODE = 0xFC90

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

        Security_Mode_Choices = {
            0x01: "Security Mode 1",
            0x02: "Security Mode 2",
        }
        Security_Mode = Parameter(order=2, size=1, choices=Security_Mode_Choices)
        """
        Security mode.
        """

        Security_Level_Choices = {
            0x01: "Security Level 1",
            0x02: "Security Level 2",
            0x03: "Security Level 3",
            0x04: "Security Level 4",
        }
        Security_Level = Parameter(order=3, size=1, choices=Security_Level_Choices)
        """
        Security Level.
        """


class ACI_GAP_SET_EVENT_MASK(CommandPacket):
    """
    It allows masking events from the GAP. The default configuration is all the events masked.
    """

    CODE = 0xFC91

    GAP_Evt_Mask_Choices = {
        0x0000: "No events",
        0x0001: "ACI_GAP_LIMITED_DISCOVERABLE_EVENT",
        0x0002: "ACI_GAP_PAIRING_COMPLETE_EVENT",
        0x0004: "ACI_GAP_PASS_KEY_REQ_EVENT",
        0x0008: "ACI_GAP_AUTHORIZATION_REQ_EVENT",
        0x0010: "ACI_GAP_SLAVE_SECURITY_INITIATED_EVENT",
        0x0020: "ACI_GAP_BOND_LOST_EVENT",
        0x0080: "ACI_GAP_PROC_COMPLETE_EVENT",
        0x0100: "ACI_L2CAP_CONNECTION_UPDATE_REQ_EVENT",
        0x0200: "ACI_L2CAP_CONNECTION_UPDATE_RESP_EVENT",
        0x0400: "ACI_L2CAP_PROC_TIMEOUT_EVENT",
        0x0800: "ACI_GAP_ADDR_NOT_RESOLVED_EVENT",
    }
    GAP_Evt_Mask = Parameter(order=1, size=2, choices=GAP_Evt_Mask_Choices, multi_choice=True)
    """
    GAP event mask. Default: 0xFFFF.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_CONFIGURE_WHITELIST(CommandPacket):
    """
    Add addresses of bonded devices into the controller's whitelist.
    The command will return an error if there are no devices in the database or if it was  
    unable to add the device into the whitelist.
    """

    CODE = 0xFC92

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_TERMINATE(CommandPacket):
    """
    Command the controller to terminate the connection.
    A HCI_DISCONNECTION_COMPLETE_EVENT event will be generated when the link is disconnected. It is important to leave an 100 ms blank window
    before sending any new command (including system hardware reset), since immediately after HCI_DISCONNECTION_COMPLETE_EVENT event,
    system could save important information in non volatile memory.
    """

    CODE = 0xFC93

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


class ACI_GAP_CLEAR_SECURITY_DB(CommandPacket):
    """
    Clear the security database. All the devices in the security database will be removed.
    """

    CODE = 0xFC94

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_ALLOW_REBOND(CommandPacket):
    """
    Allows the security manager to complete the pairing procedure and re-bond with the master.
    This command should be given by the application when it receives the
    ACI_GAP_BOND_LOST_EVENT if it wants the re-bonding to happen successfully. If this
    command is not given on receiving the event, the bonding procedure will timeout.
    """

    CODE = 0xFC95

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


class ACI_GAP_START_LIMITED_DISCOVERY_PROC(CommandPacket):
    """
    Start the limited discovery procedure. The controller is commanded to start active scanning.
    When this procedure is started, only the devices in limited discoverable mode are returned
    to the upper layers.
    The procedure is terminated when either the upper layers issue a command to terminate 
    the procedure by issuing the command ACI_GAP_TERMINATE_GAP_PROC with the procedure 
    code set to 0x01 or a timeout happens. When the procedure is terminated due to any of the 
    above  reasons, ACI_GAP_PROC_COMPLETE_EVENT event is returned with the procedure code
    set to 0x01.
    The device found when the procedure is ongoing is returned to the upper layers through the
    event HCI_LE_ADVERTISING_REPORT_EVENT.
    """

    CODE = 0xFC96

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

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address",
        0x03: "Non Resolvable Private Address",
    }
    Own_Address_Type = Parameter(order=3, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type:
        
        0x00: Public Device Address (it is allowed only if privacy is disabled)
        0x01: Random Device Address (it is allowed only if privacy is disabled)
        0x02: Resolvable Private Address (it is allowed only if privacy is enabled)
        0x03: Non Resolvable Private Address (it is allowed only if privacy is enabled)
    """

    Filter_Duplicates_Choices = {
        0x00: "Duplicate filtering disabled",
        0x01: "Duplicate filtering enabled",
    }
    Filter_Duplicates = Parameter(order=4, size=1, choices=Filter_Duplicates_Choices)
    """
    Enable/disable duplicate filtering.
    """


class ACI_GAP_START_GENERAL_DISCOVERY_PROC(CommandPacket):
    """
    Start the general discovery procedure. The controller is commanded to start active
    scanning. The procedure is terminated when  either the upper layers issue a command
    to terminate the procedure by issuing the command ACI_GAP_TERMINATE_GAP_PROC
    with the procedure code set to 0x02 or a timeout happens. When the procedure is
    terminated due to any of the above reasons, ACI_GAP_PROC_COMPLETE_EVENT event
    is returned with the procedure code set to 0x02. The device found when the procedure
    is ongoing is returned to HCI_LE_ADVERTISING_REPORT_EVENT.
    """

    CODE = 0xFC97

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

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address",
        0x03: "Non Resolvable Private Address",
    }
    Own_Address_Type = Parameter(order=3, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type:
        
        0x00: Public Device Address (it is allowed only if privacy is disabled)
        0x01: Random Device Address (it is allowed only if privacy is disabled)
        0x02: Resolvable Private Address (it is allowed only if privacy is enabled)
        0x03: Non Resolvable Private Address (it is allowed only if privacy is enabled)
    """

    Filter_Duplicates_Choices = {
        0x00: "Duplicate filtering disabled",
        0x01: "Duplicate filtering enabled",
    }
    Filter_Duplicates = Parameter(order=4, size=1, choices=Filter_Duplicates_Choices)
    """
    Enable/disable duplicate filtering.
    """


class ACI_GAP_START_NAME_DISCOVERY_PROC(CommandPacket):
    """
    Start the name discovery procedure. A LE_Create_Connection call will be made to the
    controller by GAP with the initiator filter policy set to "ignore whitelist and process
    connectable advertising packets only for the specified device". Once a connection is
    established, GATT procedure is started to read the device name characteristic. When the
    read is completed (successfully or unsuccessfully), a ACI_GAP_PROC_COMPLETE_EVENT
    event is given to the upper layer. The event also contains the name of the device if the
    device name was read successfully.
    """

    CODE = 0xFC98

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

    Peer_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
    }
    Peer_Address_Type = Parameter(order=3, size=1, choices=Peer_Address_Type_Choices)
    """
    Address type.
    """

    Peer_Address = Parameter(order=4, size=6)
    """
    Public Device Address, Random Device Address, Public Identity
        Address or Random (static) Identity Address of the advertising
        device.
    """

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address",
        0x03: "Non Resolvable Private Address",
    }
    Own_Address_Type = Parameter(order=5, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type:
        
        0x00: Public Device Address (it is allowed only if privacy is disabled)
        0x01: Random Device Address (it is allowed only if privacy is disabled)
        0x02: Resolvable Private Address (it is allowed only if privacy is enabled)
        0x03: Non Resolvable Private Address (it is allowed only if privacy is enabled)
    """

    Conn_Interval_Min_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Conn_Interval_Min = Parameter(order=6, size=2, ranges=Conn_Interval_Min_Ranges)
    """
    Minimum value for the connection event interval. This shall be less
        than or equal to Conn_Interval_Max.
        Time = N * 1.25 msec.
    """

    Conn_Interval_Max_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Conn_Interval_Max = Parameter(order=7, size=2, ranges=Conn_Interval_Max_Ranges)
    """
    Maximum value for the connection event interval. This shall be
        greater than or equal to Conn_Interval_Min.
        Time = N * 1.25 msec.
    """

    Conn_Latency_Ranges = {
        (0x0000, 0x01F3): "N/A",
    }
    Conn_Latency = Parameter(order=8, size=2, ranges=Conn_Latency_Ranges)
    """
    Slave latency for the connection in number of connection events.
    """

    Supervision_Timeout_Ranges = {
        (0x000A, 0x0C80): ("100 ms", "32000 ms"),
    }
    Supervision_Timeout = Parameter(order=9, size=2, ranges=Supervision_Timeout_Ranges)
    """
    Supervision timeout for the LE Link.
        It shall be a multiple of 10 ms and larger than (1 + connSlaveLatency) * connInterval * 2.
        Time = N * 10 msec.
    """

    Minimum_CE_Length = Parameter(order=10, size=2)
    """
    Information parameter about the minimum length of connection
        needed for this LE connection.
        Time = N * 0.625 msec.
    """

    Maximum_CE_Length = Parameter(order=11, size=2)
    """
    Information parameter about the maximum length of connection needed
        for this LE connection.
        Time = N * 0.625 msec.
    """


class ACI_GAP_START_AUTO_CONNECTION_ESTABLISH_PROC(CommandPacket):
    """
    Start the auto connection establishment procedure. The devices specified are added to the
    white list of the controller and a LE_Create_Connection call will be made to the controller by
    GAP with the initiator filter policy set to "use whitelist to determine which advertiser to
    connect to". When a command is issued to terminate the procedure by upper layer, a
    LE_Create_Connection_Cancel call will be made to the controller by GAP.
    The procedure is terminated when either a connection is successfully established with one of
    the specified devices in the white list or the procedure is explicitly terminated by issuing
    the command ACI_GAP_TERMINATE_GAP_PROC with the procedure code set to 0x08. A
    ACI_GAP_PROC_COMPLETE_EVENT event is returned with the procedure code set to 0x08.
    If controller privacy is enabled and the peer device (advertiser) is in the resolving list then
     the link layer will generate a RPA, if it is not then the RPA/NRPA generated by the Host will be used.
    """

    CODE = 0xFC99

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

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address",
        0x03: "Non Resolvable Private Address",
    }
    Own_Address_Type = Parameter(order=3, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type:
        
        0x00: Public Device Address (it is allowed only if privacy is disabled)
        0x01: Random Device Address (it is allowed only if privacy is disabled)
        0x02: Resolvable Private Address (it is allowed only if privacy is enabled)
        0x03: Non Resolvable Private Address (it is allowed only if privacy is enabled)
    """

    Conn_Interval_Min_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Conn_Interval_Min = Parameter(order=4, size=2, ranges=Conn_Interval_Min_Ranges)
    """
    Minimum value for the connection event interval. This shall be less
        than or equal to Conn_Interval_Max.
        Time = N * 1.25 msec.
    """

    Conn_Interval_Max_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Conn_Interval_Max = Parameter(order=5, size=2, ranges=Conn_Interval_Max_Ranges)
    """
    Maximum value for the connection event interval. This shall be
        greater than or equal to Conn_Interval_Min.
        Time = N * 1.25 msec.
    """

    Conn_Latency_Ranges = {
        (0x0000, 0x01F3): "N/A",
    }
    Conn_Latency = Parameter(order=6, size=2, ranges=Conn_Latency_Ranges)
    """
    Slave latency for the connection in number of connection events.
    """

    Supervision_Timeout_Ranges = {
        (0x000A, 0x0C80): ("100 ms", "32000 ms"),
    }
    Supervision_Timeout = Parameter(order=7, size=2, ranges=Supervision_Timeout_Ranges)
    """
    Supervision timeout for the LE Link.
        It shall be a multiple of 10 ms and larger than (1 + connSlaveLatency) * connInterval * 2.
        Time = N * 10 msec.
    """

    Minimum_CE_Length = Parameter(order=8, size=2)
    """
    Information parameter about the minimum length of connection
        needed for this LE connection.
        Time = N * 0.625 msec.
    """

    Maximum_CE_Length = Parameter(order=9, size=2)
    """
    Information parameter about the maximum length of connection needed
        for this LE connection.
        Time = N * 0.625 msec.
    """

    Num_of_Whitelist_Entries_Ranges = {
        (0x00, 0xFF): "N/A",
    }
    Num_of_Whitelist_Entries = Parameter(order=10, size=1, ranges=Num_of_Whitelist_Entries_Ranges)
    """
    Number of devices that have to be added to the whitelist.
    """

    Peer_Address_Type_N_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
    }
    Peer_Address_Type_N = Parameter(order=11, size=1, choices=Peer_Address_Type_N_Choices)
    """
    Address type.
    """

    Peer_Address_N = Parameter(order=12, size=6)
    """
    Public Device Address or Random Device Address of the device
        to be added to the white list.
    """


class ACI_GAP_START_GENERAL_CONNECTION_ESTABLISH_PROC(CommandPacket):
    """
    Start a general connection establishment procedure. The host enables scanning in the
    controller with the scanner filter policy set to "accept all advertising packets" and from the
    scanning results, all the devices are sent to the upper layer using the event
    LE_Advertising_Report. The upper layer then has to select one of the devices to which it
    wants to connect by issuing the command ACI_GAP_CREATE_CONNECTION. If privacy is
    enabled, then either a private resolvable address or a non resolvable address, based on the
    address type specified in the command is set as the scanner address but the gap create
    connection always uses a private resolvable address if the general connection
    establishment procedure is active.
    The procedure is terminated when a connection is established or the upper layer terminates
    the procedure by issuing the command ACI_GAP_TERMINATE_GAP_PROC with the procedure
    code set to 0x10. On completion of the procedure a ACI_GAP_PROC_COMPLETE_EVENT event
    is generated with the procedure code set to 0x10.
    If controller privacy is enabled and the peer device (advertiser) is in the resolving list then
    the link layer will generate a RPA, if it is not then the RPA/NRPA generated by the Host will be used.
    """

    CODE = 0xFC9A

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
        0x02: "Resolvable Private Address",
        0x03: "Non Resolvable Private Address",
    }
    Own_Address_Type = Parameter(order=4, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type:
        
        0x00: Public Device Address (it is allowed only if privacy is disabled)
        0x01: Random Device Address (it is allowed only if privacy is disabled)
        0x02: Resolvable Private Address (it is allowed only if privacy is enabled)
        0x03: Non Resolvable Private Address (it is allowed only if privacy is enabled)
    """

    Scanning_Filter_Policy_Choices = {
        0x00: "Accept all",
        0x01: "Ignore devices not in the White List",
        0x02: "Accept all (use resolving list)",
        0x03: "Ignore devices not in the White List (use resolving list)",
    }
    Scanning_Filter_Policy = Parameter(order=5, size=1, choices=Scanning_Filter_Policy_Choices)
    """
    Scanning filter policy:
        
        0x00 Accept all advertisement packets.Directed advertising packets which are not addressed for this device shall be ignored.
        0x01 Ignore advertisement packets from devices not in the White List Only.Directed advertising packets which are not addressed for this device shall be ignored.
        0x02 Accept all undirected advertisement packets (it is allowed only if controller privacy or host privacy is enabled).Directed advertisement packets where initiator address is a RPA and Directed advertisement packets addressed to this device shall be accepted.
        0x03 Accept all undirected advertisement packets from devices that are in the White List.Directed advertisement packets where initiator address is RPA and Directed advertisement packets addressed to this device shall be accepted.
        NOTE: if controller privacy is enabled Scanning_Filter_Policy can only assume values 0x00 or 0x02; if Host privacy is enabled Scanning_Filter_Policy can only assume value 0x00.
    """

    Filter_Duplicates_Choices = {
        0x00: "Duplicate filtering disabled",
        0x01: "Duplicate filtering enabled",
    }
    Filter_Duplicates = Parameter(order=6, size=1, choices=Filter_Duplicates_Choices)
    """
    Enable/disable duplicate filtering.
    """


class ACI_GAP_START_SELECTIVE_CONNECTION_ESTABLISH_PROC(CommandPacket):
    """
    Start a selective connection establishment procedure. The GAP adds the specified device
    addresses into white list and enables scanning in the controller with the scanner filter policy
    set to "accept packets only from devices in whitelist". All the devices found are sent to the
    upper layer by the event HCI_LE_ADVERTISING_REPORT_EVENT. The upper layer then has to select one of
    the devices to which it wants to connect by issuing the command ACI_GAP_CREATE_CONNECTION.
    On completion of the procedure a ACI_GAP_PROC_COMPLETE_EVENT event is generated with
    the procedure code set to 0x20. The procedure is terminated when a connection is established
    or the upper layer terminates the procedure by issuing the command
    ACI_GAP_TERMINATE_GAP_PROC with the procedure code set to 0x20.
    If controller privacy is enabled and the peer device (advertiser) is in the resolving list then
     the link layer will generate a RPA, if it is not then the RPA/NRPA generated by the Host will be used.
    """

    CODE = 0xFC9B

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
        0x02: "Resolvable Private Address",
        0x03: "Non Resolvable Private Address",
    }
    Own_Address_Type = Parameter(order=4, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type:
        
        0x00: Public Device Address (it is allowed only if privacy is disabled)
        0x01: Random Device Address (it is allowed only if privacy is disabled)
        0x02: Resolvable Private Address (it is allowed only if privacy is enabled)
        0x03: Non Resolvable Private Address (it is allowed only if privacy is enabled)
    """

    Scanning_Filter_Policy_Choices = {
        0x00: "Accept all",
        0x01: "Ignore devices not in the White List",
        0x02: "Accept all (use resolving list)",
        0x03: "Ignore devices not in the White List (use resolving list)",
    }
    Scanning_Filter_Policy = Parameter(order=5, size=1, choices=Scanning_Filter_Policy_Choices)
    """
    Scanning filter policy:
        
        0x00 Accept all advertisement packets.Directed advertising packets which are not addressed for this device shall be ignored.
        0x01 Ignore advertisement packets from devices not in the White List Only.Directed advertising packets which are not addressed for this device shall be ignored.
        0x02 Accept all undirected advertisement packets (it is allowed only if controller privacy or host privacy is enabled).Directed advertisement packets where initiator address is a RPA and Directed advertisement packets addressed to this device shall be accepted.
        0x03 Accept all undirected advertisement packets from devices that are in the White List.Directed advertisement packets where initiator address is RPA and Directed advertisement packets addressed to this device shall be accepted.
        NOTE: if controller privacy is enabled Scanning_Filter_Policy can only assume values 0x01 or 0x03; if Host privacy is enabled Scanning_Filter_Policy can only assume value 0x01.
    """

    Filter_Duplicates_Choices = {
        0x00: "Duplicate filtering disabled",
        0x01: "Duplicate filtering enabled",
    }
    Filter_Duplicates = Parameter(order=6, size=1, choices=Filter_Duplicates_Choices)
    """
    Enable/disable duplicate filtering.
    """

    Num_of_Whitelist_Entries_Ranges = {
        (0x00, 0xFF): "N/A",
    }
    Num_of_Whitelist_Entries = Parameter(order=7, size=1, ranges=Num_of_Whitelist_Entries_Ranges)
    """
    Number of devices that have to be added to the whitelist.
    """

    Peer_Address_Type_N_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
    }
    Peer_Address_Type_N = Parameter(order=8, size=1, choices=Peer_Address_Type_N_Choices)
    """
    Address type.
    """

    Peer_Address_N = Parameter(order=9, size=6)
    """
    Public Device Address or Random Device Address of the device
        to be added to the white list.
    """


class ACI_GAP_CREATE_CONNECTION(CommandPacket):
    """
    Start the direct connection establishment procedure. A LE_Create_Connection call will be
    made to the controller by GAP with the initiator filter policy set to "ignore whitelist and
    process connectable advertising packets only for the specified device". The procedure can
    be terminated explicitly by the upper layer by issuing the command
    ACI_GAP_TERMINATE_GAP_PROC. When a command is issued to terminate the
    procedure by upper layer, a HCI_LE_CREATE_CONNECTION_CANCEL call will be made to the
    controller by GAP.
    On termination of the procedure, a HCI_LE_CONNECTION_COMPLETE_EVENT event is returned. The  
    procedure can be explicitly terminated by the upper layer by issuing the command
    ACI_GAP_TERMINATE_GAP_PROC with the procedure_code set to 0x40.
    If controller privacy is enabled and the peer device (advertiser) is in the resolving list then
    the link layer will generate a RPA, if it is not then the RPA/NRPA generated by the Host will be used.
    """

    CODE = 0xFC9C

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

    Peer_Address_Type_Choices = {
        0x00: "Public Device Address or Public Identity Address",
        0x01: "Random Device Address or Random (static) Identity Address",
    }
    Peer_Address_Type = Parameter(order=3, size=1, choices=Peer_Address_Type_Choices)
    """
    Peer Address type.
    """

    Peer_Address = Parameter(order=4, size=6)
    """
    Public Device Address, Random Device Address, Public Identity
        Address or Random (static) Identity Address of the advertising
        device.
    """

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address",
        0x03: "Non Resolvable Private Address",
    }
    Own_Address_Type = Parameter(order=5, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type:
        
        0x00: Public Device Address (it is allowed only if privacy is disabled)
        0x01: Random Device Address (it is allowed only if privacy is disabled)
        0x02: Resolvable Private Address (it is allowed only if privacy is enabled)
        0x03: Non Resolvable Private Address (it is allowed only if privacy is enabled)
    """

    Conn_Interval_Min_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Conn_Interval_Min = Parameter(order=6, size=2, ranges=Conn_Interval_Min_Ranges)
    """
    Minimum value for the connection event interval. This shall be less
        than or equal to Conn_Interval_Max.
        Time = N * 1.25 msec.
    """

    Conn_Interval_Max_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Conn_Interval_Max = Parameter(order=7, size=2, ranges=Conn_Interval_Max_Ranges)
    """
    Maximum value for the connection event interval. This shall be
        greater than or equal to Conn_Interval_Min.
        Time = N * 1.25 msec.
    """

    Conn_Latency_Ranges = {
        (0x0000, 0x01F3): "N/A",
    }
    Conn_Latency = Parameter(order=8, size=2, ranges=Conn_Latency_Ranges)
    """
    Slave latency for the connection in number of connection events.
    """

    Supervision_Timeout_Ranges = {
        (0x000A, 0x0C80): ("100 ms", "32000 ms"),
    }
    Supervision_Timeout = Parameter(order=9, size=2, ranges=Supervision_Timeout_Ranges)
    """
    Supervision timeout for the LE Link.
        It shall be a multiple of 10 ms and larger than (1 + connSlaveLatency) * connInterval * 2.
        Time = N * 10 msec.
    """

    Minimum_CE_Length = Parameter(order=10, size=2)
    """
    Information parameter about the minimum length of connection
        needed for this LE connection.
        Time = N * 0.625 msec.
    """

    Maximum_CE_Length = Parameter(order=11, size=2)
    """
    Information parameter about the maximum length of connection needed
        for this LE connection.
        Time = N * 0.625 msec.
    """


class ACI_GAP_TERMINATE_GAP_PROC(CommandPacket):
    """
    Terminate the specified GATT procedure. An ACI_GAP_PROC_COMPLETE_EVENT event is
    returned with the procedure code set to the corresponding procedure.
    """

    CODE = 0xFC9D

    Procedure_Code_Choices = {
        0x00: "No events",
        0x01: "LIMITED_DISCOVERY_PROC",
        0x02: "GENERAL_DISCOVERY_PROC",
        0x04: "NAME_DISCOVERY_PROC",
        0x08: "AUTO_CONNECTION_ESTABLISHMENT_PROC",
        0x10: "GENERAL_CONNECTION_ESTABLISHMENT_PROC",
        0x20: "SELECTIVE_CONNECTION_ESTABLISHMENT_PROC",
        0x40: "DIRECT_CONNECTION_ESTABLISHMENT_PROC",
        0x80: "OBSERVATION_PROC",
    }
    Procedure_Code = Parameter(order=1, size=1, choices=Procedure_Code_Choices)
    """
    GAP procedure bitmap.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_START_CONNECTION_UPDATE(CommandPacket):
    """
    Start the connection update procedure (only when role is Master). A HCI_LE_CONNECTION_UPDATE is called.
    On completion of the procedure, an HCI_LE_CONNECTION_UPDATE_COMPLETE_EVENT event is returned to
    the upper layer.
    """

    CODE = 0xFC9E

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


class ACI_GAP_SEND_PAIRING_REQ(CommandPacket):
    """
    Send the SM pairing request to start a pairing process. The authentication requirements and
    IO capabilities should be set before issuing this command using the
    ACI_GAP_SET_IO_CAPABILITY and ACI_GAP_SET_AUTHENTICATION_REQUIREMENT commands.
    A ACI_GAP_PAIRING_COMPLETE_EVENT event is returned after the pairing process is completed.
    """

    CODE = 0xFC9F

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Force_Rebond_Choices = {
        0x00: "NO",
        0x01: "YES",
    }
    Force_Rebond = Parameter(order=2, size=1, choices=Force_Rebond_Choices)
    """
    If 1, Pairing request will be sent even if the device was previously bonded,
        otherwise pairing request is not sent.
    """


class ACI_GAP_RESOLVE_PRIVATE_ADDR(CommandPacket):
    """
    This command tries to resolve the address provided with the IRKs present in its database. If
    the address is resolved successfully with any one of the IRKs present in the database, it
    returns success and also the corresponding public/static random address stored with the
    IRK in the database.
    """

    CODE = 0xFCA0

    Address = Parameter(order=1, size=6)
    """
    Address to be resolved
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Actual_Address = Parameter(order=2, size=6)
        """
        The public or static random address of the peer device, distributed during pairing phase.
        """


class ACI_GAP_SET_BROADCAST_MODE(CommandPacket):
    """
    This command puts the device into broadcast mode. A privacy enabled device uses either a
    resolvable private address or a non-resolvable private address as specified in the
    Own_Addr_Type parameter of the command.
    """

    CODE = 0xFCA1

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
        0x02: "ADV_SCAN_IND (Scannable undirected advertising)",
        0x03: "ADV_NONCONN_IND (Non connectable undirected advertising)",
    }
    Advertising_Type = Parameter(order=3, size=1, choices=Advertising_Type_Choices)
    """
    Non connectable advertising type
    """

    Own_Address_Type_Choices = {
        0x00: "Public address",
        0x01: "Static random address",
        0x02: "Resolvable private address",
        0x03: "Non-resolvable private address",
    }
    Own_Address_Type = Parameter(order=4, size=1, choices=Own_Address_Type_Choices)
    """
    If Privacy is disabled, then the address can be public or static random.
        If Privacy is enabled, then the address can be a resolvable private address or a non-resolvable private address.
    """

    Adv_Data_Length = Parameter(order=5, size=1)
    """
    Length of the advertising data in the advertising packet.
    """

    Adv_Data = Parameter(order=6, size=Adv_Data_Length)
    """
    Advertising data used by the device while advertising.
    """

    Num_of_Whitelist_Entries_Ranges = {
        (0x00, 0xFF): "N/A",
    }
    Num_of_Whitelist_Entries = Parameter(order=7, size=1, ranges=Num_of_Whitelist_Entries_Ranges)
    """
    Number of devices that have to be added to the whitelist.
    """

    Peer_Address_Type_N_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
    }
    Peer_Address_Type_N = Parameter(order=8, size=1, choices=Peer_Address_Type_N_Choices)
    """
    Address type.
    """

    Peer_Address_N = Parameter(order=9, size=6)
    """
    Public Device Address or Random Device Address of the device
        to be added to the white list.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_START_OBSERVATION_PROC(CommandPacket):
    """
    Starts an Observation procedure, when the device is in Observer Role. The host enables
    scanning in the controller. The advertising reports are sent to the upper layer using standard
    LE Advertising Report Event. (See Bluetooth Core v4.1, Vol. 2, part E, Ch. 7.7.65.2, LE
    Advertising Report Event).
    If controller privacy is enabled and the peer device (advertiser) is in the resolving list then
    the link layer will generate a RPA, if it is not then the RPA/NRPA generated by the Host will be used.
    """

    CODE = 0xFCA2

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

    LE_Scan_Type_Choices = {
        0x00: "Passive Scanning",
        0x01: "Active scanning",
    }
    LE_Scan_Type = Parameter(order=3, size=1, choices=LE_Scan_Type_Choices)
    """
    Passive or active scanning. With active scanning SCAN_REQ packets are sent.
    """

    Own_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Resolvable Private Address",
        0x03: "Non Resolvable Private Address",
    }
    Own_Address_Type = Parameter(order=4, size=1, choices=Own_Address_Type_Choices)
    """
    Own address type:
        
        0x00: Public Device Address (it is allowed only if privacy is disabled)
        0x01: Random Device Address (it is allowed only if privacy is disabled)
        0x02: Resolvable Private Address (it is allowed only if privacy is enabled)
        0x03: Non Resolvable Private Address (it is allowed only if privacy is enabled)
    """

    Filter_Duplicates_Choices = {
        0x00: "Duplicate filtering disabled",
        0x01: "Duplicate filtering enabled",
    }
    Filter_Duplicates = Parameter(order=5, size=1, choices=Filter_Duplicates_Choices)
    """
    Enable/disable duplicate filtering.
    """

    Scanning_Filter_Policy_Choices = {
        0x00: "Accept all",
        0x01: "Ignore devices not in the White List",
        0x02: "Accept all (use resolving list)",
        0x03: "Ignore devices not in the White List (use resolving list)",
    }
    Scanning_Filter_Policy = Parameter(order=6, size=1, choices=Scanning_Filter_Policy_Choices)
    """
    Scanning filter policy:
        
        0x00 Accept all advertisement packets (it is allowed only if controller privacy is enabled).Directed advertising packets which are not addressed for this device shall be ignored.
        0x01 Ignore advertisement packets from devices not in the White List Only.Directed advertising packets which are not addressed for this device shall be ignored.
        0x02 Accept all undirected advertisement packets (it is allowed only if controller privacy or host privacy is enabled).Directed advertisement packets where initiator address is a RPA and Directed advertisement packets addressed to this device shall be accepted.
        0x03 Accept all undirected advertisement packets from devices that are in the White List.Directed advertisement packets where initiator address is RPA and Directed advertisement packets addressed to this device shall be accepted.
        NOTE: If Host privacy is enabled Scanning_Filter_Policy can only take values 0x00 or 0x01;
    """


class ACI_GAP_GET_BONDED_DEVICES(CommandPacket):
    """
    This command gets the list of the devices which are bonded. It returns the number of addresses and the corresponding address types and values. The maximum number of devices that can be returned is MAX_NUM_BONDED_DEVICES (12).
    """

    CODE = 0xFCA3

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Num_of_Addresses = Parameter(order=2, size=1)
        """
        The number of bonded devices
        """

        Address_Type_N_Choices = {
            0x00: "Public Device Address",
            0x01: "Random Device Address",
        }
        Address_Type_N = Parameter(order=3, size=1, choices=Address_Type_N_Choices)
        """
        Address type.
        """

        Address_N = Parameter(order=4, size=6)
        """
        Public Device Address or Random Device Address of the device
        to be added to the white list.
        """


class ACI_GAP_IS_DEVICE_BONDED(CommandPacket):
    """
    The command finds whether the device, whose address is specified in the command, is
    bonded. If the device is using a resolvable private address and it has been bonded, then the
    command will return BLE_STATUS_SUCCESS.
    """

    CODE = 0xFCA4

    Peer_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
    }
    Peer_Address_Type = Parameter(order=1, size=1, choices=Peer_Address_Type_Choices)
    """
    Address type.
    """

    Peer_Address = Parameter(order=2, size=6)
    """
    Address used by the peer device while advertising
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_NUMERIC_COMPARISON_VALUE_CONFIRM_YESNO(CommandPacket):
    """
    This command allows the User to validate/confirm or not the Numeric Comparison value showed through the ACI_GAP_Numeric_Comparison_Value_Event.
    """

    CODE = 0xFCA5

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Confirm_Yes_No_Choices = {
        0x00: "No",
        0x01: "YES",
    }
    Confirm_Yes_No = Parameter(order=2, size=1, choices=Confirm_Yes_No_Choices)
    """
    0 : The Numeric Values showed on both local and peer device are different!
        1 : The Numeric Values showed on both local and peer device are equal!
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_PASSKEY_INPUT(CommandPacket):
    """
    This command permits to signal to the Stack the input type detected during Passkey input.
    """

    CODE = 0xFCA6

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Input_Type_Choices = {
        0x00: "Passkey entry started",
        0x01: "Passkey digit entered",
        0x02: "Passkey digit erased",
        0x03: "Passkey cleared",
        0x04: "Passkey entry completed",
    }
    Input_Type = Parameter(order=2, size=1, choices=Input_Type_Choices)
    """
    Passkey input type detected
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_GET_OOB_DATA(CommandPacket):
    """
    This command is sent by the User to get (i.e. to extract from the Stack) the OOB data generated by the Stack itself.
    In a complete system (i.e. having an OOB channel fully handled) this command should be invoked by the OOB Channel manager to require the local OOB data
    (hence without user interaction) to be sent via OOB to the remote peer candidate device.
    The requested OOB data are returned in response to the incoming command. The OOB data are not generated on the fly, but they are already available in the Stack.
    """

    CODE = 0xFCA7

    OOB_Data_Type_Choices = {
        0x00: "SM_TK",
        0x01: "SM_RANDOM_VALUE",
        0x02: "SM_CONFIRM_VALUE",
    }
    OOB_Data_Type = Parameter(order=1, size=1, choices=OOB_Data_Type_Choices)
    """
    OOB Data type.
        - 0x00: Legacy Privacy (LP) v.4.1 TK (Temporary Key)
        - 0x01: Secure Connections (SC) v.4.2 Random value r used for generation of Confirm
        - 0x02: Secure Connections (SC) v.4.2 Confirm value C generated through AES-CMAC-128 based cryptographic function: C=f4(PKx, PKx, r, 0)
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Address_Type_Choices = {
            0x00: "Public Identity Address",
            0x01: "Random (static) Identity Address",
        }
        Address_Type = Parameter(order=2, size=1, choices=Address_Type_Choices)
        """
        Identity address type.
        """

        Address = Parameter(order=3, size=6)
        """
        Public or Random (static) address of this  device
        """

        OOB_Data_Type_Choices = {
            0x00: "SM_TK",
            0x01: "SM_RANDOM_VALUE",
            0x02: "SM_CONFIRM_VALUE",
        }
        OOB_Data_Type = Parameter(order=4, size=1, choices=OOB_Data_Type_Choices)
        """
        OOB Data type.
        - 0x00: Legacy Privacy (LP) v.4.1 TK (Temporary Key)
        - 0x01: Secure Connections (SC) v.4.2 Random value r used for generation of Confirm
        - 0x02: Secure Connections (SC) v.4.2 Confirm value C generated through AES-CMAC-128 based cryptographic function: C=f4(PKx, PKx, r, 0)
        """

        OOB_Data_Len = Parameter(order=5, size=1)
        """
        Length of OOB Data carried by next data field
        """

        OOB_Data = Parameter(order=6, size=16)
        """
        OOB Data to be exported via OOB.
        """


class ACI_GAP_SET_OOB_DATA(CommandPacket):
    """
    This command is sent (by the User) to input the OOB data arrived via OOB communication.
    It may be sent to set either the OOB Authentication data of the Local device, or the data received via OOB by the Remote peer candidate device.
    It can be used with OOB_Data_Len set to 0 to generate OOB authentication data for Secure Connections.
    In a complete system (i.e. having an OOB channel fully handled) this command should be invoked by the OOB Channel manager when receiving the OOB data (hence without user interaction).
    Since the BLE stack v 2.x implementation supports just one entry for the Remote peer candidate list containing the OOB data, at every command invocation the data existing in that entry are overwritten.
    """

    CODE = 0xFCA8

    Device_Type_Choices = {
        0x00: "Local device",
        0x01: "Remote device",
    }
    Device_Type = Parameter(order=1, size=1, choices=Device_Type_Choices)
    """
    OOB Device type:
        
        0x00: The Address information are ignored.
        - OOB_Data_Len= 0x00: this triggers the automatic regeneration of OOB Authentication data (for Secure Connections only; a ECDH-Public Key must).
        - OOB_Data_Len in [0..16]: the OOB_Data carried by the command will overwrite the current local Authentication OOB Data.
        0x01: The Address information is used to search the entry of the Remote peer candidate list containing the OOB data for that specific remote device; if no entry exists, the a new entry is used, if available (current implementation supports just 1 entry in this list).
        - OOB_Data_Len in [0..16]: the OOB_Data carried by the command overwrites (if present) the remote Authentication OOB Data.
    """

    Address_Type_Choices = {
        0x00: "Public Identity Address",
        0x01: "Random (static) Identity Address",
    }
    Address_Type = Parameter(order=2, size=1, choices=Address_Type_Choices)
    """
    Identity address type.
    """

    Address = Parameter(order=3, size=6)
    """
    Public or Random (static) address of the peer device
    """

    OOB_Data_Type_Choices = {
        0x00: "SM_TK",
        0x01: "SM_RANDOM_VALUE",
        0x02: "SM_CONFIRM_VALUE",
    }
    OOB_Data_Type = Parameter(order=4, size=1, choices=OOB_Data_Type_Choices)
    """
    OOB Data type.
        - 0x00: Legacy Privacy (LP) v.4.1 TK (Temporary Key)
        - 0x01: Secure Connections (SC) v.4.2 Random value r used for generation of Confirm
        - 0x02: Secure Connections (SC) v.4.2 Confirm value C generated through AES-CMAC-128 based cryptographic function: C=f4(PKx, PKx, r, 0)
    """

    OOB_Data_Len_Ranges = {
        (0x00, 0x10): "N/A",
    }
    OOB_Data_Len = Parameter(order=5, size=1, ranges=OOB_Data_Len_Ranges)
    """
    Length of OOB Data carried by next data field
    """

    OOB_Data = Parameter(order=6, size=16)
    """
    OOB Data to be exported via OOB.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_ADD_DEVICES_TO_RESOLVING_LIST(CommandPacket):
    """
    This  command is used to add one device to the list of address translations used to resolve Resolvable Private Addresses in the Controller.
    """

    CODE = 0xFCA9

    Num_of_Resolving_list_Entries = Parameter(order=1, size=1)
    """
    Number of devices that have to be added to the resolving list.
    """

    Peer_Identity_Address_Type_N_Choices = {
        0x00: "Public Identity Address",
        0x01: "Random (static) Identity Address",
    }
    Peer_Identity_Address_Type_N = Parameter(order=2, size=1, choices=Peer_Identity_Address_Type_N_Choices)
    """
    Identity address type.
    """

    Peer_Identity_Address_N = Parameter(order=3, size=6)
    """
    Public or Random (static) Identity address of the peer device
    """

    Clear_Resolving_List = Parameter(order=4, size=1)
    """
    Clear the resolving list before adding the devices.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GAP_REMOVE_BONDED_DEVICE(CommandPacket):
    """
    This command can be used to remove a specified device from the bonding table.
    """

    CODE = 0xFCAA

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

