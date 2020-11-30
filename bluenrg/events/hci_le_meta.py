# NOTE: This file is auto-generated, please do not modify

from ..packet import *


class HCI_LE_CONNECTION_COMPLETE_EVENT(LEMetaEventPacket):
    """
    The LE Connection Complete event indicates to both of the Hosts forming the
    connection that a new connection has been created. Upon the creation of the
    connection a Connection_Handle shall be assigned by the Controller, and
    passed to the Host in this event. If the connection establishment fails this event
    shall be provided to the Host that had issued the LE_Create_Connection command.
    This event indicates to the Host which issued a LE_Create_Connection
    command and received a Command Status event if the connection
    establishment failed or was successful.
    The Master_Clock_Accuracy parameter is only valid for a slave. On a master,
    this parameter shall be set to 0x00.
    """

    SUBCODE = 0x01

    Status = Parameter(order=1, size=1)
    """
    For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
    """

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=2, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle to be used to identify the connection with the peer device.
    """

    Role_Choices = {
        0x00: "Master",
        0x01: "Slave",
    }
    Role = Parameter(order=3, size=1, choices=Role_Choices)
    """
    Role of the local device in the connection.
    """

    Peer_Address_Type_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
    }
    Peer_Address_Type = Parameter(order=4, size=1, choices=Peer_Address_Type_Choices)
    """
    The address type of the peer device.
    """

    Peer_Address = Parameter(order=5, size=6)
    """
    Public Device Address or Random Device Address of the peer
        device
    """

    Conn_Interval_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Conn_Interval = Parameter(order=6, size=2, ranges=Conn_Interval_Ranges)
    """
    Connection interval used on this connection.
        Time = N * 1.25 msec
    """

    Conn_Latency_Ranges = {
        (0x0000, 0x01F3): "N/A",
    }
    Conn_Latency = Parameter(order=7, size=2, ranges=Conn_Latency_Ranges)
    """
    Slave latency for the connection in number of connection events.
    """

    Supervision_Timeout_Ranges = {
        (0x000A, 0x0C80): ("100 ms", "32000 ms"),
    }
    Supervision_Timeout = Parameter(order=8, size=2, ranges=Supervision_Timeout_Ranges)
    """
    Supervision timeout for the LE Link.
        It shall be a multiple of 10 ms and larger than (1 + connSlaveLatency) * connInterval * 2.
        Time = N * 10 msec.
    """

    Master_Clock_Accuracy_Choices = {
        0x00: "500 ppm",
        0x01: "250 ppm",
        0x02: "150 ppm",
        0x03: "100 ppm",
        0x04: "75 ppm",
        0x05: "50 ppm",
        0x06: "30 ppm",
        0x07: "20 ppm",
    }
    Master_Clock_Accuracy = Parameter(order=9, size=1, choices=Master_Clock_Accuracy_Choices)
    """
    Master clock accuracy. Only valid for a slave.
    """


class HCI_LE_ADVERTISING_REPORT_EVENT(LEMetaEventPacket):
    """
    The LE Advertising Report event indicates that a Bluetooth device or multiple
    Bluetooth devices have responded to an active scan or received some information
    during a passive scan. The Controller may queue these advertising reports
    and send information from multiple devices in one LE Advertising Report event.
    """

    SUBCODE = 0x02

    Num_Reports_Choices = {
        0x01: "N/A",
    }
    Num_Reports = Parameter(order=1, size=1, choices=Num_Reports_Choices)
    """
    Number of responses in this event.
    """

    Event_Type_N_Choices = {
        0x00: "ADV_IND",
        0x01: "ADV_DIRECT_IND",
        0x02: "ADV_SCAN_IND",
        0x03: "ADV_NONCONN_IND",
        0x04: "SCAN_RSP",
    }
    Event_Type_N = Parameter(order=2, size=1, choices=Event_Type_N_Choices)
    """
    Type of advertising report event:
        ADV_IND: Connectable undirected advertising',
        ADV_DIRECT_IND: Connectable directed advertising,
        ADV_SCAN_IND: Scannable undirected advertising,
        ADV_NONCONN_IND: Non connectable undirected advertising,
        SCAN_RSP: Scan response.
    """

    Address_Type_N_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Public Identity Address",
        0x03: "Random (Static) Identity Address",
    }
    Address_Type_N = Parameter(order=3, size=1, choices=Address_Type_N_Choices)
    """
    0x00 Public Device Address
        0x01 Random Device Address
        0x02 Public Identity Address (Corresponds to Resolved Private Address)
        0x03 Random (Static) Identity Address (Corresponds to Resolved Private Address)
    """

    Address_N = Parameter(order=4, size=6)
    """
    Public Device Address, Random Device Address, Public Identity
        Address or Random (static) Identity Address of the advertising
        device.
    """

    Length_Data_N_Ranges = {
        (0, 31): "N/A",
    }
    Length_Data_N = Parameter(order=5, size=1, ranges=Length_Data_N_Ranges)
    """
    Length of the Data[i] field for each device which responded.
    """

    Data_N = Parameter(order=6, size=Length_Data_N)
    """
    Length_Data[i] octets of advertising or scan response data formatted
        as defined in [Vol 3] Part C, Section 8.
    """

    RSSI_N_Choices = {
        127: "RSSI not available",
    }
    RSSI_N_Ranges = {
        (-127, 20): "N/A",
    }
    RSSI_N = Parameter(order=7, size=1, choices=RSSI_N_Choices, ranges=RSSI_N_Ranges)
    """
    N Size: 1 Octet (signed integer)
        Units: dBm
    """


class HCI_LE_CONNECTION_UPDATE_COMPLETE_EVENT(LEMetaEventPacket):
    """
    The LE Connection Update Complete event is used to indicate that the Controller
    process to update the connection has completed.
    On a slave, if no connection parameters are updated, then this event shall not be issued.
    On a master, this event shall be issued if the Connection_Update command was sent.
    """

    SUBCODE = 0x03

    Status = Parameter(order=1, size=1)
    """
    For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
    """

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=2, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle to be used to identify the connection with the peer device.
    """

    Conn_Interval_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Conn_Interval = Parameter(order=3, size=2, ranges=Conn_Interval_Ranges)
    """
    Connection interval used on this connection.
        Time = N * 1.25 msec
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


class HCI_LE_READ_REMOTE_USED_FEATURES_COMPLETE_EVENT(LEMetaEventPacket):
    """
    The LE Read Remote Used Features Complete event is used to indicate the
    completion of the process of the Controller obtaining the used features of the
    remote Bluetooth device specified by the Connection_Handle event parameter.
    """

    SUBCODE = 0x04

    Status = Parameter(order=1, size=1)
    """
    For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
    """

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=2, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle to be used to identify the connection with the peer device.
    """

    LE_Features = Parameter(order=3, size=8)
    """
    Bit Mask List of used LE features. For details see LE Link Layer specification.
    """


class HCI_LE_LONG_TERM_KEY_REQUEST_EVENT(LEMetaEventPacket):
    """
    The LE Long Term Key Request event indicates that the master device is
    attempting to encrypt or re-encrypt the link and is requesting the Long Term
    Key from the Host. (See [Vol 6] Part B, Section 5.1.3).
    """

    SUBCODE = 0x05

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle to be used to identify the connection with the peer device.
    """

    Random_Number = Parameter(order=2, size=8)
    """
    64-bit random number
    """

    Encrypted_Diversifier = Parameter(order=3, size=2)
    """
    16-bit encrypted diversifier
    """


class HCI_LE_DATA_LENGTH_CHANGE_EVENT(LEMetaEventPacket):
    """
    The LE Data Length Change event notifies the Host of a change to either the maximum Payload length or the maximum transmission time of Data Channel PDUs in either direction. The values reported are the maximum that will actually be used on the connection following the change.
    """

    SUBCODE = 0x07

    Connection_Handle = Parameter(order=1, size=2)
    """
    Connection_Handle to be used to identify a connection.
    """

    MaxTxOctets = Parameter(order=2, size=2)
    """
    The maximum number of payload octets in a Link Layer Data Channel PDU that the local Controller will send on this connection (connEffectiveMaxTxOctets defined in [Vol 6] Part B, Section 4.5.10).
        Range 0x001B-0x00FB (0x0000 - 0x001A and 0x00FC - 0xFFFF Reserved for future use)
    """

    MaxTxTime = Parameter(order=3, size=2)
    """
    The maximum time that the local Controller will take to send a Link Layer Data Channel PDU on this connection (connEffectiveMaxTx-Time defined in [Vol 6] Part B, Section 4.5.10).
        Range 0x0148-0x0848 (0x0000 - 0x0127 and 0x0849 - 0xFFFF
        Reserved for future use)
    """

    MaxRxOctets = Parameter(order=4, size=2)
    """
    The maximum number of payload octets in a Link Layer Data Channel PDU that the local controller expects to receive on this connection (connEfectiveMaxRxOctets defined in [Vol 6] Part B, Section 4.5.10).
        Range 0x001B-0x00FB (0x0000 - 0x001A and 0x00FC - 0xFFFF Reserved for future use)
    """

    MaxRxTime = Parameter(order=5, size=2)
    """
    The maximum time that the local Controller expects to take to receive a Link Layer Data Channel PDU on this connection (connEffectiveMax-RxTime defined in [Vol 6] Part B, Section 4.5.10).
        Range 0x0148-0x0848 (0x0000 - 0x0127 and 0x0849 - 0xFFFF Reserved for future use)
    """


class HCI_LE_READ_LOCAL_P256_PUBLIC_KEY_COMPLETE_EVENT(LEMetaEventPacket):
    """
    This event is generated when local P-256 key generation is complete.
    """

    SUBCODE = 0x08

    Status = Parameter(order=1, size=1)
    """
    For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
    """

    Local_P256_Public_Key = Parameter(order=2, size=64)
    """
    Local P-256 public key.
    """


class HCI_LE_GENERATE_DHKEY_COMPLETE_EVENT(LEMetaEventPacket):
    """
    This event indicates that LE Diffie Hellman key generation has been completed
    by the Controller.
    """

    SUBCODE = 0x09

    Status = Parameter(order=1, size=1)
    """
    For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
    """

    DHKey = Parameter(order=2, size=32)
    """
    Diffie Hellman Key
    """


class HCI_LE_ENHANCED_CONNECTION_COMPLETE_EVENT(LEMetaEventPacket):
    """
    The LE Enhanced Connection Complete event indicates to both of the Hosts
    forming the connection that a new connection has been created. Upon the
    creation of the connection a Connection_Handle shall be assigned by the
    Controller, and passed to the Host in this event. If the connection establishment
    fails, this event shall be provided to the Host that had issued the
    LE_Create_Connection command.
    If this event is unmasked and LE Connection Complete event is unmasked,
    only the LE Enhanced Connection Complete event is sent when a new
    connection has been completed.
    This event indicates to the Host that issued a LE_Create_Connection
    command and received a Command Status event if the connection
    establishment failed or was successful.
    The Master_Clock_Accuracy parameter is only valid for a slave. On a master,
    this parameter shall be set to 0x00.
    """

    SUBCODE = 0x0A

    Status = Parameter(order=1, size=1)
    """
    For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
    """

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=2, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle to be used to identify the connection with the peer device.
    """

    Role_Choices = {
        0x00: "Master",
        0x01: "Slave",
    }
    Role = Parameter(order=3, size=1, choices=Role_Choices)
    """
    Role of the local device in the connection.
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
        Address or Random (static) Identity Address of the device to be connected.
    """

    Local_Resolvable_Private_Address = Parameter(order=6, size=6)
    """
    Resolvable Private Address being used by the local device for this connection.
        This is only valid when the Own_Address_Type is set to 0x02 or 0x03. For other Own_Address_Type values,
        the Controller shall return all zeros.
    """

    Peer_Resolvable_Private_Address = Parameter(order=7, size=6)
    """
    Resolvable Private Address being used by the peer device for this connection.
        This is only valid for Peer_Address_Type 0x02 and 0x03. For
        other Peer_Address_Type values, the Controller shall return all zeros.
    """

    Conn_Interval_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Conn_Interval = Parameter(order=8, size=2, ranges=Conn_Interval_Ranges)
    """
    Connection interval used on this connection.
        Time = N * 1.25 msec
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

    Master_Clock_Accuracy_Choices = {
        0x00: "500 ppm",
        0x01: "250 ppm",
        0x02: "150 ppm",
        0x03: "100 ppm",
        0x04: "75 ppm",
        0x05: "50 ppm",
        0x06: "30 ppm",
        0x07: "20 ppm",
    }
    Master_Clock_Accuracy = Parameter(order=11, size=1, choices=Master_Clock_Accuracy_Choices)
    """
    Master clock accuracy. Only valid for a slave.
    """


class HCI_LE_DIRECT_ADVERTISING_REPORT_EVENT(LEMetaEventPacket):
    """
    The LE Direct Advertising Report event indicates that directed advertisements
    have been received where the advertiser is using a resolvable private address
    for the InitA field in the ADV_DIRECT_IND PDU and the
    Scanning_Filter_Policy is equal to 0x02 or 0x03, see HCI_LE_Set_Scan_Parameters.
    Direct_Address_Type and Direct_Addres is the address the directed
    advertisements are being directed to. Address_Type and Address is the
    address of the advertiser sending the directed advertisements.
    """

    SUBCODE = 0x0B

    Num_Reports_Choices = {
        0x01: "N/A",
    }
    Num_Reports = Parameter(order=1, size=1, choices=Num_Reports_Choices)
    """
    Number of responses in this event.
    """

    Event_Type_N_Choices = {
        0x01: "Connectable directed advertising (ADV_DIRECT_IND)",
    }
    Event_Type_N = Parameter(order=2, size=1, choices=Event_Type_N_Choices)
    """
    Advertising type
    """

    Address_Type_N_Choices = {
        0x00: "Public Device Address",
        0x01: "Random Device Address",
        0x02: "Public Identity Address",
        0x03: "Random (Static) Identity Address",
    }
    Address_Type_N = Parameter(order=3, size=1, choices=Address_Type_N_Choices)
    """
    0x00 Public Device Address
        0x01 Random Device Address
        0x02 Public Identity Address (Corresponds to Resolved Private Address)
        0x03 Random (Static) Identity Address (Corresponds to Resolved Private Address)
    """

    Address_N = Parameter(order=4, size=6)
    """
    Public Device Address, Random Device Address, Public Identity
        Address or Random (static) Identity Address of the advertising device.
    """

    Direct_Address_Type_N_Choices = {
        0x01: "Random Device Address",
    }
    Direct_Address_Type_N = Parameter(order=5, size=1, choices=Direct_Address_Type_N_Choices)
    """
    0x01 Random Device Address
    """

    Direct_Address_N = Parameter(order=6, size=6)
    """
    Random Device Address
    """

    RSSI_N_Choices = {
        127: "RSSI not available",
    }
    RSSI_N_Ranges = {
        (-127, 20): "N/A",
    }
    RSSI_N = Parameter(order=7, size=1, choices=RSSI_N_Choices, ranges=RSSI_N_Ranges)
    """
    N Size: 1 Octet (signed integer)
        Units: dBm
    """

