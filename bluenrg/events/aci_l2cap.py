# NOTE: This file is auto-generated, please do not modify

from ..packet import *


class ACI_L2CAP_CONNECTION_UPDATE_RESP_EVENT(VendorEventPacket):
    """
    This event is generated when the master responds to the connection update request packet
    with a connection update response packet.
    """

    SUBCODE = 0x0800

    Connection_Handle = Parameter(order=1, size=2)
    """
    Connection handle referring to the COS Channel where the Disconnection has been received.
    """

    Result = Parameter(order=2, size=2)
    """
    N/A
    """


class ACI_L2CAP_PROC_TIMEOUT_EVENT(VendorEventPacket):
    """
    This event is generated when the master does not respond to the connection update
    request packet with a connection update response packet or a command reject packet
    within 30 seconds.
    """

    SUBCODE = 0x0801

    Connection_Handle = Parameter(order=1, size=2)
    """
    Handle of the connection related to this
        L2CAP procedure.
    """

    Data_Length = Parameter(order=2, size=1)
    """
    Length of following data
    """

    Data = Parameter(order=3, size=Data_Length)
    """
    N/A
    """


class ACI_L2CAP_CONNECTION_UPDATE_REQ_EVENT(VendorEventPacket):
    """
    The event is given by the L2CAP layer when a connection update request is received from
    the slave. The upper layer which receives this event has to respond by sending a
    ACI_L2CAP_CONNECTION_PARAMETER_UPDATE_RESP command.
    """

    SUBCODE = 0x0802

    Connection_Handle = Parameter(order=1, size=2)
    """
    Handle of the connection related to this
        L2CAP procedure.
    """

    Identifier = Parameter(order=2, size=1)
    """
    This is the identifier which associate the request to the
        response.
    """

    L2CAP_Length = Parameter(order=3, size=2)
    """
    Length of the L2CAP connection update request.
    """

    Interval_Min_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Interval_Min = Parameter(order=4, size=2, ranges=Interval_Min_Ranges)
    """
    Minimum value for the connection event interval. This shall be less
        than or equal to Conn_Interval_Max.
        Time = N * 1.25 msec.
    """

    Interval_Max_Ranges = {
        (0x0006, 0x0C80): ("7.50 ms", "4000.00 ms"),
    }
    Interval_Max = Parameter(order=5, size=2, ranges=Interval_Max_Ranges)
    """
    Maximum value for the connection event interval. This shall be
        greater than or equal to Conn_Interval_Min.
        Time = N * 1.25 msec.
    """

    Slave_Latency_Ranges = {
        (0x0000, 0x01F3): "N/A",
    }
    Slave_Latency = Parameter(order=6, size=2, ranges=Slave_Latency_Ranges)
    """
    Slave latency for the connection in number of connection events.
    """

    Timeout_Multiplier_Ranges = {
        (10, 3200): ("100 ms", "32000 ms"),
    }
    Timeout_Multiplier = Parameter(order=7, size=2, ranges=Timeout_Multiplier_Ranges)
    """
    Defines connection timeout parameter in the following manner: Timeout Multiplier * 10ms.
    """


class ACI_L2CAP_COMMAND_REJECT_EVENT(VendorEventPacket):
    """
    This event is generated when the master responds to the connection update request packet
    with a command reject packet.
    """

    SUBCODE = 0x080A

    Connection_Handle = Parameter(order=1, size=2)
    """
    Connection handle referring to the COS Channel where the Disconnection has been received.
    """

    Identifier = Parameter(order=2, size=1)
    """
    This is the identifier which associate the request to the
        response.
    """

    Reason = Parameter(order=3, size=2)
    """
    Reason
    """

    Data_Length = Parameter(order=4, size=1)
    """
    Length of following data
    """

    Data = Parameter(order=5, size=Data_Length)
    """
    Data field associated with Reason
    """

