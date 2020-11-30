# NOTE: This file is auto-generated, please do not modify

from ..packet import *
from .. import events


class APP_GATT_GET_TERMINAL_HANDLES(CommandPacket):
    """
    N/A
    """

    CODE = 0xFE05

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Service_Handle = Parameter(order=1, size=2)
        """
        N/A
        """

        Auth_Char_Handle = Parameter(order=2, size=2)
        """
        N/A
        """

        Command_Char_Handle = Parameter(order=3, size=2)
        """
        N/A
        """

        Result_Char_Handle = Parameter(order=4, size=2)
        """
        N/A
        """

