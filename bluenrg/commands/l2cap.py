# NOTE: This file is auto-generated, please do not modify

from ..packet import *
from .. import events


class ACI_L2CAP_CONNECTION_PARAMETER_UPDATE_REQ(CommandPacket):
    """
    Send an L2CAP connection parameter update request from the slave to the master.
    An ACI_L2CAP_CONNECTION_UPDATE_RESP_EVENT event will be raised when the master will respond to the 
    request (accepts or rejects).
    """

    CODE = 0xFD81

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

    Slave_latency_Ranges = {
        (0x0000, 0x01F3): "N/A",
    }
    Slave_latency = Parameter(order=4, size=2, ranges=Slave_latency_Ranges)
    """
    Slave latency for the connection in number of connection events.
    """

    Timeout_Multiplier_Ranges = {
        (10, 3200): ("100 ms", "32000 ms"),
    }
    Timeout_Multiplier = Parameter(order=5, size=2, ranges=Timeout_Multiplier_Ranges)
    """
    Defines connection timeout parameter in the following manner: Timeout Multiplier * 10ms.
    """


class ACI_L2CAP_CONNECTION_PARAMETER_UPDATE_RESP(CommandPacket):
    """
    Accept or reject a connection update. This command should be sent in response
    to a ACI_L2CAP_CONNECTION_UPDATE_REQ_EVENT event from the controller. The accept parameter has to be
    set if the connection parameters given in the event are acceptable.
    """

    CODE = 0xFD82

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

    Slave_latency_Ranges = {
        (0x0000, 0x01F3): "N/A",
    }
    Slave_latency = Parameter(order=4, size=2, ranges=Slave_latency_Ranges)
    """
    Slave latency for the connection in number of connection events.
    """

    Timeout_Multiplier_Ranges = {
        (10, 3200): ("100 ms", "32000 ms"),
    }
    Timeout_Multiplier = Parameter(order=5, size=2, ranges=Timeout_Multiplier_Ranges)
    """
    Defines connection timeout parameter in the following manner: Timeout Multiplier * 10ms.
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

    Identifier = Parameter(order=8, size=1)
    """
    Identifier received in ACI_L2CAP_Connection_Update_Req event.
    """

    Accept_Choices = {
        0x00: "Reject",
        0x01: "Accept",
    }
    Accept = Parameter(order=9, size=1, choices=Accept_Choices)
    """
    Specify if connection update parameters are acceptable or not.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

