# NOTE: This file is auto-generated, please do not modify

from ..packet import *
from .. import events


class HCI_LE_RECEIVER_TEST(CommandPacket):
    """
    This command is used to start a test where the DUT receives test reference
    packets at a fixed interval. The tester generates the test reference packets.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.28)
    """

    CODE = 0x201D

    RX_Frequency_Ranges = {
        (0x00, 0x27): "N = (F - 2402) / 2.Frequency Range : 2402 MHz to 2480 MHz",
    }
    RX_Frequency = Parameter(order=1, size=1, ranges=RX_Frequency_Ranges)
    """
    N/A
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_TRANSMITTER_TEST(CommandPacket):
    """
    This command is used to start a test where the DUT generates test reference
    packets at a fixed interval. The Controller shall transmit at maximum power.
    An LE Controller supporting the LE_Transmitter_Test command shall support
    Packet_Payload values 0x00, 0x01 and 0x02. An LE Controller may support
    other values of Packet_Payload.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.29)
    """

    CODE = 0x201E

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

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class HCI_LE_TEST_END(CommandPacket):
    """
    This command is used to stop any test which is in progress. The Number_Of_Packets
    for a transmitter test shall be reported as 0x0000. The Number_Of_Packets
    is an unsigned number and contains the number of received
    packets.
    (See Bluetooth Specification v.4.1, Vol. 2, Part E, 7.8.30)
    """

    CODE = 0x201F

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Number_Of_Packets = Parameter(order=2, size=2)
        """
        Number of packets received.
        """

