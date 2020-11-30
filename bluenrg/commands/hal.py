# NOTE: This file is auto-generated, please do not modify

from ..packet import *
from .. import events


class ACI_HAL_GET_FW_BUILD_NUMBER(CommandPacket):
    """
    This command returns the build number associated with the firmware version currently running
    """

    CODE = 0xFC00

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Build_Number = Parameter(order=2, size=2)
        """
        Build number of the firmware.
        """


class ACI_HAL_GET_FIRMWARE_DETAILS(CommandPacket):
    """
    This commands return information regarding the version of the network coprocessor firmware and BTLE stack library associated. The information returned includes values that can be
    retrieved with existing commands see HCI_READ_LOCAL_VERSION_INFORMATION and ACI_HAL_GET_FW_BUILD_NUMBER. The aim is to have a single command that returns all version information details
    for a network coprocessor application (also known as DTM application)
    """

    CODE = 0xFC01

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        DTM_version_major = Parameter(order=2, size=1)
        """
        Major version number of the DTM application part
        """

        DTM_version_minor = Parameter(order=3, size=1)
        """
        Minor version number of the DTM application part
        """

        DTM_version_patch = Parameter(order=4, size=1)
        """
        Patch version number of the DTM application part
        """

        DTM_variant_Choices = {
            0x01: "UART",
            0x02: "SPI",
        }
        DTM_variant = Parameter(order=5, size=1, choices=DTM_variant_Choices)
        """
        Transport layer mode (numbers not defined reserved for future use)
        """

        DTM_Build_Number = Parameter(order=6, size=2)
        """
        Build number for DTM application part
        """

        BTLE_Stack_version_major = Parameter(order=7, size=1)
        """
        Major version number of BTLE stack
        """

        BTLE_Stack_version_minor = Parameter(order=8, size=1)
        """
        Minor version number of BTLE stack
        """

        BTLE_Stack_version_patch = Parameter(order=9, size=1)
        """
        Patch version number of BTLE stack
        """

        BTLE_Stack_development_Choices = {
            0x00: "Official release",
            0x01: "Internal development release",
        }
        BTLE_Stack_development = Parameter(order=10, size=1, choices=BTLE_Stack_development_Choices)
        """
        Specific variant build
        """

        BTLE_Stack_variant_Choices = {
            0x0001: "CONTROLLER_PRIVACY_ENABLED",
            0x0002: "SECURE_CONNECTIONS_ENABLED",
            0x0004: "CONTROLLER_MASTER_ENABLED",
            0x0008: "CONTROLLER_DATA_LENGTH_EXTENSION_ENABLED",
            0x0010: "LINK LAYER ONLY",
        }
        BTLE_Stack_variant = Parameter(order=11, size=2, choices=BTLE_Stack_variant_Choices, multi_choice=True)
        """
        Bitmask of BLE stack v2.1 or later variants (modular configurations options and link layer only)
        """

        BTLE_Stack_Build_Number = Parameter(order=12, size=2)
        """
        Build number for BTLE stack
        """


class ACI_HAL_WRITE_CONFIG_DATA(CommandPacket):
    """
    This command writes a value to a low level configure data structure. It is useful to setup
    directly some low level parameters for the system in the runtime.NOTE: This command shall not be called if a command different than Stack Init, HCI_RESET, ACI_HAL_WRITE_CONFIG_DATA or ACI_HAL_READ_CONFIG_DATA has already been called.
    """

    CODE = 0xFC0C

    Offset_Choices = {
        0x00: "CONFIG_DATA_PUBADDR_OFFSET",
        0x08: "CONFIG_DATA_ER_OFFSET",
        0x18: "CONFIG_DATA_IR_OFFSET",
        0x2C: "LL_WITHOUT_HOST",
        0x2E: "CONFIG_DATA_STATIC_RANDOM_ADDRESS",
        0xD0: "CONFIG_DATA_DEBUG_KEY",
        0xD1: "CONFIG_DATA_DLE",
    }
    Offset = Parameter(order=1, size=1, choices=Offset_Choices)
    """
    Offset of the element in the configuration data structure
        which has to be written. The valid offsets are:
        
        0x00: Bluetooth public address, Value length to be written: 6 bytes
        0x08: Encryption root key used to derive LTK and CSRK, Value length to be written: 16 bytes
        0x18: Identity root key used to derive LTK and CSRK, Value length to be written: 16 bytes
        0x2C: Link layer without host (for certification purposes), Value length to be written: 1 byte
        0x2E: If set, the stack uses this address as the static random address instead of the one stored in NVM.
        0xD0: Use debug key for Secure connection: 1 byte
        
        0xD1: Set the maximum allowed parameter values for Data Length Extension: 8 bytes, 2 bytes for each of the following parameters:
        supportedMaxTxOctets, supportedMaxTxTime, supportedMaxRxOctets, supportedMaxRxTime, in little-endian order.
        (default 251,2120,251,2120).
    """

    Length = Parameter(order=2, size=1)
    """
    Length of data to be written
    """

    Value = Parameter(order=3, size=Length)
    """
    Data to be written
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_HAL_READ_CONFIG_DATA(CommandPacket):
    """
    This command requests the value in the low level configure data structure.
    The number of read bytes changes for different Offset.
    """

    CODE = 0xFC0D

    Offset_Choices = {
        0x00: "CONFIG_DATA_PUBADDR_OFFSET",
        0x08: "CONFIG_DATA_ER_OFFSET",
        0x18: "CONFIG_DATA_IR_OFFSET",
        0x2C: "LL_WITHOUT_HOST",
        0x2E: "CONFIG_DATA_STATIC_RANDOM_ADDRESS",
        0x80: "CONFIG_DATA_STORED_STATIC_RANDOM_ADDRESS",
    }
    Offset = Parameter(order=1, size=1, choices=Offset_Choices)
    """
    Offset of the element in the configuration data structure
        which has to be read. The valid offsets are:
        
        0x00: Bluetooth public address, Value length returned: 6 bytes
        0x08: Encryption root key used to derive LTK and CSRK, Value length returned: 16 bytes
        0x18: Identity root key used to derive LTK and CSRK, Value length returned: 16 bytes
        0x2C: Link layer without host (for certification purposes), Value length returned: 1 byte
        0x2E: The static random address overwritten by application (used instead of the one stored in NVM).
        0x80: The static random address stored in NVM. Value length returned: 6 bytes (read-only)
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Data_Length = Parameter(order=2, size=1)
        """
        Length of Data in octets
        """

        Data = Parameter(order=3, size=Data_Length)
        """
        Data field associated with Offset parameter
        """


class ACI_HAL_SET_TX_POWER_LEVEL(CommandPacket):
    """
    This command sets the TX power level of the device. By controlling the
    EN_HIGH_POWER and the PA_LEVEL, the combination of the 2 determines the output
    power level (dBm). 
    When the system starts up or reboots, the default TX power level will be used, which is the
    maximum value of 8 dBm. Once this command is given, the output power will be changed
    instantly, regardless if there is Bluetooth communication going on or not. For example, for
    debugging purpose, the device can be set to advertise all the time. And use this
    command to observe the signal strength changing.
    The system will keep the last received TX power level from the command, i.e. the 2nd
    command overwrites the previous TX power level. The new TX power level remains until
    another Set TX Power command, or the system reboots.
    """

    CODE = 0xFC0F

    En_High_Power_Choices = {
        0x00: "Normal Power",
        0x01: "High Power",
    }
    En_High_Power = Parameter(order=1, size=1, choices=En_High_Power_Choices)
    """
    Enable High Power mode.
        High power mode should be enabled only to reach the maximum output power.
    """

    PA_Level_Choices = {
        0: "-14 dBm (High Power)",
        1: "-11 dBm (High Power)",
        2: "-8 dBm (High Power)",
        3: "-5 dBm (High Power)",
        4: "-2 dBm (High Power)",
        5: "2 dBm (High Power)",
        6: "4 dBm (High Power)",
        7: "8 dBm (High Power)",
    }
    PA_Level = Parameter(order=2, size=1, choices=PA_Level_Choices)
    """
    Power amplifier output level. Output power is indicative and it depends on the PCB layout and associated components
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_HAL_LE_TX_TEST_PACKET_NUMBER(CommandPacket):
    """
    This command returns the number of packets sent in Direct Test Mode.
    When the Direct TX test is started, a 32-bit counter is used to count how many packets have been transmitted. 
    This command can be used to check how many packets have been sent during the Direct TX test.
    The counter starts from 0 and counts upwards. The counter can wrap and start from 0 again. 
    The counter is not cleared until the next Direct TX test starts.
    """

    CODE = 0xFC14

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Number_Of_Packets = Parameter(order=2, size=4)
        """
        Number of packets sent during the last Direct TX test.
        """


class ACI_HAL_TONE_START(CommandPacket):
    """
    This command starts a carrier frequency, i.e. a tone, on a specific channel. The frequency
    sine wave at the specific channel may be used for debugging purpose only. The channel ID
    is a parameter from 0x00 to 0x27 for the 40 BLE channels, e.g. 0x00 for 2.402 GHz, 0x01
    for 2.404 GHz etc.
    This command should not be used when normal Bluetooth activities are ongoing.
    The tone should be stopped by ACI_HAL_TONE_STOP command.
    """

    CODE = 0xFC15

    RF_Channel_Ranges = {
        (0x00, 0x27): "N/A",
    }
    RF_Channel = Parameter(order=1, size=1, ranges=RF_Channel_Ranges)
    """
    BLE Channel ID, from 0x00 to 0x27 meaning (2.402 + 2*0xXX) GHz.
    """

    Offset_Choices = {
        0x00: "0 kHz offset",
        0x01: "+250 kHz offset",
        0x02: "-250 kHz offset",
    }
    Offset = Parameter(order=2, size=1, choices=Offset_Choices)
    """
    Specify if the tone must be emitted with an offset from the channel center frequency.  If 0, the tone is emitted at the channel center frequency.
        If 1 or 2, the device will continuously emit the tone at the center frequency plus or minus 250 kHz respectively.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_HAL_TONE_STOP(CommandPacket):
    """
    This command is used to stop the previously started ACI_HAL_TONE_START command.
    """

    CODE = 0xFC16

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_HAL_GET_LINK_STATUS(CommandPacket):
    """
    This command returns the status of the 8 Bluetooth low energy links managed by the device
    """

    CODE = 0xFC17

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Link_Status = Parameter(order=2, size=8)
        """
        Array of link status (8 links). Each link status is 1 byte.
        """

        Link_Connection_Handle = Parameter(order=3, size=16)
        """
        Array of connection handles (2 bytes) for 8 links.
        """


class ACI_HAL_SET_RADIO_ACTIVITY_MASK(CommandPacket):
    """
    This command set the bitmask associated to ACI_HAL_END_OF_RADIO_ACTIVITY_EVENT. 
    Only the radio activities enabled in the mask will be reported to application by ACI_HAL_END_OF_RADIO_ACTIVITY_EVENT
    """

    CODE = 0xFC18

    Radio_Activity_Mask_Choices = {
        0x0001: "Idle",
        0x0002: "Advertising",
        0x0004: "Connection event slave",
        0x0008: "Scanning",
        0x0010: "Connection request",
        0x0020: "Connection event master",
        0x0040: "TX test mode",
        0x0080: "RX test mode",
    }
    Radio_Activity_Mask = Parameter(order=1, size=2, choices=Radio_Activity_Mask_Choices, multi_choice=True)
    """
    Bitmask of radio events
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_HAL_GET_ANCHOR_PERIOD(CommandPacket):
    """
    This command returns information about the Anchor Period to help application in selecting 
                          slot timings when operating in multi-link scenarios.
    """

    CODE = 0xFC19

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Anchor_Period = Parameter(order=2, size=4)
        """
        Current anchor period.
        T = N * 0.625 ms.
        """

        Max_Free_Slot = Parameter(order=3, size=4)
        """
        Maximum available time that can be allocated for a new slot.
        T = N * 0.625 ms.
        """


class ACI_HAL_SET_EVENT_MASK(CommandPacket):
    """
    N/A
    """

    CODE = 0xFC1A

    Event_Mask_Choices = {
        0x00000000: "No events specified (Default)",
        0x00000001: "ACI_HAL_SCAN_REQ_REPORT_EVENT",
    }
    Event_Mask = Parameter(order=1, size=4, choices=Event_Mask_Choices, multi_choice=True)
    """
    Mask to enable/disable generation of HAL events
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_HAL_UPDATER_START(CommandPacket):
    """
    This command is only implemented together with the normal application. The updater does
    not support this command. If this command is called, the system reboots and enters updater
    mode.
    """

    CODE = 0xFC20

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_HAL_TRANSMITTER_TEST_PACKETS(CommandPacket):
    """
    This command is equivalent to the corresponding Bluetooth Low Energy standard command HCI_LE_TRANSMITTER_TEST, the only difference is that user can specify the number of packets to be transmitted. The HCI_COMMAND_COMPLETE_EVENT is generated when the number of packets have been sent.
    """

    CODE = 0xFC2B

    TX_Frequency_Ranges = {
        (0x00, 0x27): "N/A",
    }
    TX_Frequency = Parameter(order=1, size=1, ranges=TX_Frequency_Ranges)
    """
    N = (F - 2402) / 2
        Frequency Range : 2402 MHz to 2480 MHz
    """

    Length_Of_Test_Data_Ranges = {
        (0x00, 0xFF): "N/A",
    }
    Length_Of_Test_Data = Parameter(order=2, size=1, ranges=Length_Of_Test_Data_Ranges)
    """
    Length in bytes of payload data in each packet.
        
        Supported ranges:
        
        (0x00,0x25): BlueNRG-1 and BlueNRG-2 with BLE stack version < 2.1
        (0x00,0xFF): BlueNRG-2 with BLE stack version >= 2.1 and extended packet length.
    """

    Packet_Payload_Choices = {
        0x00: "Pseudo-Random bit sequence 9",
        0x01: "Pattern of alternating bits '11110000'",
        0x02: "Pattern of alternating bits '10101010'",
        0x03: "Pseudo-Random bit sequence 15",
        0x04: "Pattern of All '1' bits",
        0x05: "Pattern of All '0' bits",
        0x06: "Pattern of alternating bits '00001111'",
        0x07: "Pattern of alternating bits '0101'",
    }
    Packet_Payload = Parameter(order=3, size=1, choices=Packet_Payload_Choices)
    """
    Type of packet payload.
    """

    Number_Of_Packets = Parameter(order=4, size=2)
    """
    Number of packets to be sent
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        Error code returned by the command
        """


class ACI_TEST_TX_NOTIFICATION_START(CommandPacket):
    """
    N/A
    """

    CODE = 0xFE00

    Connection_Handle = Parameter(order=1, size=2)
    """
    Connection handle to notify.
    """

    Service_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Service_Handle = Parameter(order=2, size=2, ranges=Service_Handle_Ranges)
    """
    Handle of service to which the characteristic belongs
    """

    Char_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Char_Handle = Parameter(order=3, size=2, ranges=Char_Handle_Ranges)
    """
    Handle of the characteristic
    """

    Value_Length = Parameter(order=4, size=2)
    """
    Length of the characteristic to be notified. Only ATT_MTU - 3 bytes are sent with notifications.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_TEST_TX_WRITE_COMMAND_START(CommandPacket):
    """
    N/A
    """

    CODE = 0xFE01

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Attr_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Attr_Handle = Parameter(order=2, size=2, ranges=Attr_Handle_Ranges)
    """
    Handle of the attribute to be written
    """

    Value_Length = Parameter(order=3, size=2)
    """
    Length of the characteristic to be written with write commands. Only ATT_MTU - 3 bytes are written.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_TEST_RX_START(CommandPacket):
    """
    N/A
    """

    CODE = 0xFE02

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Attr_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Attr_Handle = Parameter(order=2, size=2, ranges=Attr_Handle_Ranges)
    """
    Handle of the attribute to be written
    """

    Notifications_WriteCmds_Choices = {
        0x00: "Notifications",
        0x01: "Write Commands",
    }
    Notifications_WriteCmds = Parameter(order=3, size=1, choices=Notifications_WriteCmds_Choices)
    """
    N/A
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_TEST_STOP(CommandPacket):
    """
    N/A
    """

    CODE = 0xFE03

    TX_RX_Choices = {
        0x00: "TX",
        0x01: "RX",
    }
    TX_RX = Parameter(order=1, size=1, choices=TX_RX_Choices)
    """
    N/A
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_TEST_REPORT(CommandPacket):
    """
    N/A
    """

    CODE = 0xFE04

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        TX_Packets = Parameter(order=2, size=4)
        """
        N/A
        """

        RX_Packets = Parameter(order=3, size=4)
        """
        N/A
        """

        RX_Data_Length = Parameter(order=4, size=2)
        """
        N/A
        """

        RX_Sequence_Errors = Parameter(order=5, size=4)
        """
        N/A
        """

