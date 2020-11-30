# NOTE: This file is auto-generated, please do not modify

from ..packet import *
from .. import events


class ACI_GATT_INIT(CommandPacket):
    """
    Initialize the GATT layer for server and client roles. 
    It adds also the GATT service with Service Changed Characteristic. 
    Until this command is issued the GATT channel will not process any commands even if the 
    connection is opened. This command has to be given before using any of the GAP features.
    """

    CODE = 0xFD01

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GATT_ADD_SERVICE(CommandPacket):
    """
    Add a service to GATT Server. When a service is created in the server, the host needs to
    reserve the handle ranges for this service using Max_Attribute_Records parameter. This
    parameter specifies the maximum number of attribute records that can be added to this
    service (including the service attribute, include attribute, characteristic attribute,
    characteristic value attribute and characteristic descriptor attribute). Handle of the created
    service is returned in command complete event. Service declaration is taken from the service pool. 
    The attributes for characteristics and descriptors are allocated from the attribute pool.
    """

    CODE = 0xFD02

    Service_UUID_Type_Choices = {
        0x01: "16-bit UUID",
        0x02: "128-bit UUID",
    }
    Service_UUID_Type = Parameter(order=1, size=1, choices=Service_UUID_Type_Choices)
    """
    UUID type.
    """

    Service_UUID = Parameter(order=2, size=(2, 16))
    """
    16-bit UUID or 128-bit UUID
    """

    Service_Type_Choices = {
        0x01: "Primary Service",
        0x02: "Secondary Service",
    }
    Service_Type = Parameter(order=3, size=1, choices=Service_Type_Choices)
    """
    Service type.
    """

    Max_Attribute_Records = Parameter(order=4, size=1)
    """
    Number of handles reserved for the service. If 0, no handles are served and when the next service is added to the GATT database, the first available handle is assigned to that service (this means that no more attributes can be assigned to the previously created service).
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Service_Handle = Parameter(order=2, size=2)
        """
        Handle of the Service.
        When this service is added, a handle is allocated by the server for this service.
        Server also allocates a range of handles for this service from serviceHandle to <serviceHandle + max_attr_records - 1>
        """


class ACI_GATT_INCLUDE_SERVICE(CommandPacket):
    """
    Include a service given by Include_Start_Handle and Include_End_Handle to another 
    service given by Service_Handle. Attribute server creates an INCLUDE definition 
    attribute and return the handle of this attribute in Included_handle.
    """

    CODE = 0xFD03

    Service_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Service_Handle = Parameter(order=1, size=2, ranges=Service_Handle_Ranges)
    """
    Handle of the Service to which another service has to be included.
    """

    Include_Start_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Include_Start_Handle = Parameter(order=2, size=2, ranges=Include_Start_Handle_Ranges)
    """
    Attribute Handle of the Service which has to be included in service
    """

    Include_End_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Include_End_Handle = Parameter(order=3, size=2, ranges=Include_End_Handle_Ranges)
    """
    End Handle of the Service which has to be included in service
    """

    Include_UUID_Type_Choices = {
        0x01: "16-bit UUID",
        0x02: "128-bit UUID",
    }
    Include_UUID_Type = Parameter(order=4, size=1, choices=Include_UUID_Type_Choices)
    """
    UUID type.
    """

    Include_UUID = Parameter(order=5, size=(2, 16))
    """
    16-bit UUID or 128-bit UUID
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Include_Handle = Parameter(order=2, size=2)
        """
        Handle of the include declaration
        """


class ACI_GATT_ADD_CHAR(CommandPacket):
    """
    Add a characteristic to a service.
    """

    CODE = 0xFD04

    Service_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Service_Handle = Parameter(order=1, size=2, ranges=Service_Handle_Ranges)
    """
    Handle of the Service to which the characteristic will be added.
    """

    Char_UUID_Type_Choices = {
        0x01: "16-bit UUID",
        0x02: "128-bit UUID",
    }
    Char_UUID_Type = Parameter(order=2, size=1, choices=Char_UUID_Type_Choices)
    """
    UUID type.
    """

    Char_UUID = Parameter(order=3, size=(2, 16))
    """
    16-bit UUID or 128-bit UUID
    """

    Char_Value_Length_Ranges = {
        (0, 512): "N/A",
    }
    Char_Value_Length = Parameter(order=4, size=2, ranges=Char_Value_Length_Ranges)
    """
    Maximum length of the characteristic value.
    """

    Char_Properties_Choices = {
        0x00: "CHAR_PROP_NONE",
        0x01: "CHAR_PROP_BROADCAST (Broadcast)",
        0x02: "CHAR_PROP_READ (Read)",
        0x04: "CHAR_PROP_WRITE_WITHOUT_RESP (Write w/o resp)",
        0x08: "CHAR_PROP_WRITE (Write)",
        0x10: "CHAR_PROP_NOTIFY (Notify)",
        0x20: "CHAR_PROP_INDICATE (Indicate)",
        0x40: "CHAR_PROP_SIGNED_WRITE (Authenticated Signed Writes)",
        0x80: "CHAR_PROP_EXT (Extended Properties)",
    }
    Char_Properties = Parameter(order=5, size=1, choices=Char_Properties_Choices, multi_choice=True)
    """
    Characteristic Properties (Volume 3, Part G, section 3.3.1.1 of Bluetooth Specification 4.1)
    """

    Security_Permissions_Choices = {
        0x00: "None",
        0x01: "AUTHEN_READ (Need authentication to read)",
        0x02: "AUTHOR_READ (Need authorization to read)",
        0x04: "ENCRY_READ (Need encryption to read)",
        0x08: "AUTHEN_WRITE (need authentication to write)",
        0x10: "AUTHOR_WRITE (need authorization to write)",
        0x20: "ENCRY_WRITE (need encryption to write)",
    }
    Security_Permissions = Parameter(order=6, size=1, choices=Security_Permissions_Choices, multi_choice=True)
    """
    Security permission flags.
    """

    GATT_Evt_Mask_Choices = {
        0x00: "GATT_DONT_NOTIFY_EVENTS",
        0x01: "GATT_NOTIFY_ATTRIBUTE_WRITE",
        0x02: "GATT_NOTIFY_WRITE_REQ_AND_WAIT_FOR_APPL_RESP",
        0x04: "GATT_NOTIFY_READ_REQ_AND_WAIT_FOR_APPL_RESP",
    }
    GATT_Evt_Mask = Parameter(order=7, size=1, choices=GATT_Evt_Mask_Choices, multi_choice=True)
    """
    GATT event mask.
    """

    Enc_Key_Size_Ranges = {
        (0x07, 0x10): "N/A",
    }
    Enc_Key_Size = Parameter(order=8, size=1, ranges=Enc_Key_Size_Ranges)
    """
    Minimum encryption key size required to read the characteristic.
    """

    Is_Variable_Choices = {
        0x00: "Fixed length",
        0x01: "Variable length",
    }
    Is_Variable = Parameter(order=9, size=1, choices=Is_Variable_Choices)
    """
    Specify if the characteristic value has a fixed length or
        a variable length.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Char_Handle = Parameter(order=2, size=2)
        """
        Handle of the Characteristic that has been added.
        It is the handle of the characteristic declaration.
        The attribute that holds the characteristic value is allocated at the next handle,
        followed by the Client Characteristic Configuration descriptor if the characteristic
        has CHAR_PROP_NOTIFY or CHAR_PROP_INDICATE properties.
        """


class ACI_GATT_ADD_CHAR_DESC(CommandPacket):
    """
    Add a characteristic descriptor to a service.
    """

    CODE = 0xFD05

    Service_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Service_Handle = Parameter(order=1, size=2, ranges=Service_Handle_Ranges)
    """
    Handle of service to which the characteristic belongs
    """

    Char_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Char_Handle = Parameter(order=2, size=2, ranges=Char_Handle_Ranges)
    """
    Handle of the characteristic to which description has to be added
    """

    Char_Desc_UUID_Type_Choices = {
        0x01: "16-bit UUID",
        0x02: "128-bit UUID",
    }
    Char_Desc_UUID_Type = Parameter(order=3, size=1, choices=Char_Desc_UUID_Type_Choices)
    """
    UUID type.
    """

    Char_Desc_UUID = Parameter(order=4, size=(2, 16))
    """
    16-bit UUID or 128-bit UUID
    """

    Char_Desc_Value_Max_Len_Ranges = {
        (0, 512): "N/A",
    }
    Char_Desc_Value_Max_Len = Parameter(order=5, size=1, ranges=Char_Desc_Value_Max_Len_Ranges)
    """
    The maximum length of the descriptor value
    """

    Char_Desc_Value_Length_Ranges = {
        (0, 512): "N/A",
    }
    Char_Desc_Value_Length = Parameter(order=6, size=1, ranges=Char_Desc_Value_Length_Ranges)
    """
    Current Length of the characteristic descriptor value
    """

    Char_Desc_Value = Parameter(order=7, size=Char_Desc_Value_Length)
    """
    Value of the characteristic description
    """

    Security_Permissions_Choices = {
        0x00: "None",
        0x01: "AUTHEN_READ (Need authentication to read)",
        0x02: "AUTHOR_READ (Need authorization to read)",
        0x04: "ENCRY_READ (Need encryption to read)",
        0x08: "AUTHEN_WRITE (need authentication to write)",
        0x10: "AUTHOR_WRITE (need authorization to write)",
        0x20: "ENCRY_WRITE (need encryption to write)",
    }
    Security_Permissions = Parameter(order=8, size=1, choices=Security_Permissions_Choices, multi_choice=True)
    """
    Security permission flags.
    """

    Access_Permissions_Choices = {
        0x00: "None",
        0x01: "READ",
        0x02: "WRITE",
        0x04: "WRITE_WO_RESP",
        0x08: "SIGNED_WRITE",
    }
    Access_Permissions = Parameter(order=9, size=1, choices=Access_Permissions_Choices, multi_choice=True)
    """
    Access permission
    """

    GATT_Evt_Mask_Choices = {
        0x00: "GATT_DONT_NOTIFY_EVENTS",
        0x01: "GATT_NOTIFY_ATTRIBUTE_WRITE",
        0x02: "GATT_NOTIFY_WRITE_REQ_AND_WAIT_FOR_APPL_RESP",
        0x04: "GATT_NOTIFY_READ_REQ_AND_WAIT_FOR_APPL_RESP",
    }
    GATT_Evt_Mask = Parameter(order=10, size=1, choices=GATT_Evt_Mask_Choices, multi_choice=True)
    """
    GATT event mask.
    """

    Enc_Key_Size_Ranges = {
        (0x07, 0x10): "N/A",
    }
    Enc_Key_Size = Parameter(order=11, size=1, ranges=Enc_Key_Size_Ranges)
    """
    Minimum encryption key size required to read the characteristic.
    """

    Is_Variable_Choices = {
        0x00: "Fixed length",
        0x01: "Variable length",
    }
    Is_Variable = Parameter(order=12, size=1, choices=Is_Variable_Choices)
    """
    Specify if the characteristic value has a fixed length or
        a variable length.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Char_Desc_Handle_Ranges = {
            (0x0001, 0xFFFF): "N/A",
        }
        Char_Desc_Handle = Parameter(order=2, size=2, ranges=Char_Desc_Handle_Ranges)
        """
        Handle of the characteristic descriptor
        """


class ACI_GATT_UPDATE_CHAR_VALUE(CommandPacket):
    """
    Update a characteristic value in a service. 
    If notifications (or indications) are enabled on that characteristic, 
    a notification (or indication) will be sent to the client after sending 
    this command to the BlueNRG. The command is queued into the BlueNRG command queue. 
    If the buffer is full, because previous commands could not be still processed,
    the function will return BLE_STATUS_INSUFFICIENT_RESOURCES. This will happen 
    if notifications (or indications) are enabled and the application calls 
    ACI_GATT_UPDATE_CHAR_VALUE at an higher rate than what is allowed by the link. 
    Throughput on BLE link depends on connection interval and connection length 
    parameters (decided by the master, see aci_l2cap_connection_parameter_update_request() 
    for more info on how to suggest new connection parameters from a slave). If the 
    application does not want to lose notifications because BlueNRG buffer becomes full, 
    it has to retry again till the function returns BLE_STATUS_SUCCESS or any other error code.
    DEPRECATED API (still supported but not recommended)
    """

    CODE = 0xFD06

    Service_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Service_Handle = Parameter(order=1, size=2, ranges=Service_Handle_Ranges)
    """
    Handle of service to which the characteristic belongs
    """

    Char_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Char_Handle = Parameter(order=2, size=2, ranges=Char_Handle_Ranges)
    """
    Handle of the characteristic
    """

    Val_Offset_Ranges = {
        (0, 511): "N/A",
    }
    Val_Offset = Parameter(order=3, size=1, ranges=Val_Offset_Ranges)
    """
    The offset from which the attribute value has to be updated.
        If this is set to 0 and the attribute value is of variable length, then the length of the attribute will be set to the Char_Value_Length.
        If the Val_Offset is set to a value greater than 0, then the length of the attribute will be set to the maximum length as
        specified for the attribute while adding the characteristic.
    """

    Char_Value_Length = Parameter(order=4, size=1)
    """
    Length of the characteristic value in octets
    """

    Char_Value = Parameter(order=5, size=Char_Value_Length)
    """
    Characteristic value
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GATT_DEL_CHAR(CommandPacket):
    """
    Delete the specified characteristic from the service.
    """

    CODE = 0xFD07

    Serv_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Serv_Handle = Parameter(order=1, size=2, ranges=Serv_Handle_Ranges)
    """
    Handle of service to which the characteristic belongs
    """

    Char_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Char_Handle = Parameter(order=2, size=2, ranges=Char_Handle_Ranges)
    """
    Handle of the characteristic which has to be deleted
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GATT_DEL_SERVICE(CommandPacket):
    """
    Delete the specified service from the GATT server database.
    """

    CODE = 0xFD08

    Serv_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Serv_Handle = Parameter(order=1, size=2, ranges=Serv_Handle_Ranges)
    """
    Handle of the service to be deleted
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GATT_DEL_INCLUDE_SERVICE(CommandPacket):
    """
    Delete the Include definition from the service.
    """

    CODE = 0xFD09

    Serv_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Serv_Handle = Parameter(order=1, size=2, ranges=Serv_Handle_Ranges)
    """
    Handle of the service to which the include service belongs
    """

    Include_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Include_Handle = Parameter(order=2, size=2, ranges=Include_Handle_Ranges)
    """
    Handle of the included service which has to be deleted
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GATT_SET_EVENT_MASK(CommandPacket):
    """
    Mask events from the GATT. The default configuration is all the events masked.
    """

    CODE = 0xFD0A

    GATT_Evt_Mask_Choices = {
        0x00000001: "ACI_GATT_ATTRIBUTE_MODIFIED_EVENT",
        0x00000002: "ACI_GATT_PROC_TIMEOUT_EVENT",
        0x00000004: "ACI_ATT_EXCHANGE_MTU_RESP_EVENT",
        0x00000008: "ACI_ATT_FIND_INFO_RESP_EVENT",
        0x00000010: "ACI_ATT_FIND_BY_TYPE_VALUE_RESP_EVENT",
        0x00000020: "ACI_ATT_READ_BY_TYPE_RESP_EVENT",
        0x00000040: "ACI_ATT_READ_RESP_EVENT",
        0x00000080: "ACI_ATT_READ_BLOB_RESP_EVENT",
        0x00000100: "ACI_ATT_READ_MULTIPLE_RESP_EVENT",
        0x00000200: "ACI_ATT_READ_BY_GROUP_TYPE_RESP_EVENT",
        0x00000800: "ACI_ATT_PREPARE_WRITE_RESP_EVENT",
        0x00001000: "ACI_ATT_EXEC_WRITE_RESP_EVENT",
        0x00002000: "ACI_GATT_INDICATION_EVENT",
        0x00004000: "ACI_GATT_NOTIFICATION_EVENT",
        0x00008000: "ACI_GATT_ERROR_RESP_EVENT",
        0x00010000: "ACI_GATT_PROC_COMPLETE_EVENT",
        0x00020000: "ACI_GATT_DISC_READ_CHAR_BY_UUID_RESP_EVENT",
        0x00040000: "ACI_GATT_TX_POOL_AVAILABLE_EVENT",
    }
    GATT_Evt_Mask = Parameter(order=1, size=4, choices=GATT_Evt_Mask_Choices)
    """
    GATT/ATT event mask.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GATT_EXCHANGE_CONFIG(CommandPacket):
    """
    Perform an ATT MTU exchange procedure.
    When the ATT MTU exchange procedure is completed, a ACI_ATT_EXCHANGE_MTU_RESP_EVENT
    event is generated. A ACI_GATT_PROC_COMPLETE_EVENT event is also generated
    to indicate the end of the procedure.
    """

    CODE = 0xFD0B

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """


class ACI_ATT_FIND_INFO_REQ(CommandPacket):
    """
    Send a Find Information Request.
    This command is used to obtain the mapping of attribute handles with their associated
    types. The responses of the procedure are given through the 
    ACI_ATT_FIND_INFO_RESP_EVENT event. The end of the procedure is indicated by
    a ACI_GATT_PROC_COMPLETE_EVENT event.
    """

    CODE = 0xFD0C

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Start_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Start_Handle = Parameter(order=2, size=2, ranges=Start_Handle_Ranges)
    """
    First requested handle number
    """

    End_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    End_Handle = Parameter(order=3, size=2, ranges=End_Handle_Ranges)
    """
    Last requested handle number
    """


class ACI_ATT_FIND_BY_TYPE_VALUE_REQ(CommandPacket):
    """
    Send a Find By Type Value Request
    The Find By Type Value Request is used to obtain the handles of attributes that
    have a given 16-bit UUID attribute type and a given attribute value.
    The responses of the procedure are given through the ACI_ATT_FIND_BY_TYPE_VALUE_RESP_EVENT event.
    The end of the procedure is indicated by a ACI_GATT_PROC_COMPLETE_EVENT event.
    """

    CODE = 0xFD0D

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Start_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Start_Handle = Parameter(order=2, size=2, ranges=Start_Handle_Ranges)
    """
    First requested handle number
    """

    End_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    End_Handle = Parameter(order=3, size=2, ranges=End_Handle_Ranges)
    """
    Last requested handle number
    """

    UUID = Parameter(order=4, size=2)
    """
    2 octet UUID to find (little-endian)
    """

    Attribute_Val_Length = Parameter(order=5, size=1)
    """
    Length of attribute value (maximum value is ATT_MTU - 7).
    """

    Attribute_Val = Parameter(order=6, size=Attribute_Val_Length)
    """
    Attribute value to find
    """


class ACI_ATT_READ_BY_TYPE_REQ(CommandPacket):
    """
    Send a Read By Type Request.
    The Read By Type Request is used to obtain the values of attributes where the attribute
    type is known but the handle is not known.
    The responses of the procedure are given through the ACI_ATT_READ_BY_TYPE_RESP_EVENT event.
    The end of the procedure is indicated by a ACI_GATT_PROC_COMPLETE_EVENT event.
    """

    CODE = 0xFD0E

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Start_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Start_Handle = Parameter(order=2, size=2, ranges=Start_Handle_Ranges)
    """
    First requested handle number
    """

    End_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    End_Handle = Parameter(order=3, size=2, ranges=End_Handle_Ranges)
    """
    Last requested handle number
    """

    UUID_Type_Choices = {
        0x01: "16-bit UUID",
        0x02: "128-bit UUID",
    }
    UUID_Type = Parameter(order=4, size=1, choices=UUID_Type_Choices)
    """
    UUID type.
    """

    UUID = Parameter(order=5, size=(2, 16))
    """
    16-bit UUID or 128-bit UUID
    """


class ACI_ATT_READ_BY_GROUP_TYPE_REQ(CommandPacket):
    """
    Send a Read By Group Type Request. 
    The Read By Group Type Request is used to obtain the values of grouping attributes where
    the attribute type is known but the handle is not known. Grouping attributes are defined 
    at GATT layer. The grouping attribute types are: "Primary Service", "Secondary Service" 
    and "Characteristic". 
    The responses of the procedure are given through the ACI_ATT_READ_BY_GROUP_TYPE_RESP_EVENT event. 
    The end of the procedure is indicated by a ACI_GATT_PROC_COMPLETE_EVENT.
    """

    CODE = 0xFD0F

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Start_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Start_Handle = Parameter(order=2, size=2, ranges=Start_Handle_Ranges)
    """
    First requested handle number
    """

    End_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    End_Handle = Parameter(order=3, size=2, ranges=End_Handle_Ranges)
    """
    Last requested handle number
    """

    UUID_Type_Choices = {
        0x01: "16-bit UUID",
        0x02: "128-bit UUID",
    }
    UUID_Type = Parameter(order=4, size=1, choices=UUID_Type_Choices)
    """
    UUID type.
    """

    UUID = Parameter(order=5, size=(2, 16))
    """
    16-bit UUID or 128-bit UUID
    """


class ACI_ATT_PREPARE_WRITE_REQ(CommandPacket):
    """
    Send a Prepare Write Request.
    The Prepare Write Request is used to request the server to prepare to write the value of an attribute. 
    The responses of the procedure are given through the ACI_ATT_PREPARE_WRITE_RESP_EVENT event. 
    The end of the procedure is indicated by a ACI_GATT_PROC_COMPLETE_EVENT.
    """

    CODE = 0xFD10

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

    Val_Offset_Ranges = {
        (0, 511): "N/A",
    }
    Val_Offset = Parameter(order=3, size=2, ranges=Val_Offset_Ranges)
    """
    The offset of the first octet to be written
    """

    Attribute_Val_Length = Parameter(order=4, size=1)
    """
    Length of attribute value (maximum value is ATT_MTU - 5).
    """

    Attribute_Val = Parameter(order=5, size=Attribute_Val_Length)
    """
    The value of the attribute to be written
    """


class ACI_ATT_EXECUTE_WRITE_REQ(CommandPacket):
    """
    Send an Execute Write Request.
    The Execute Write Request is used to request the server to write or cancel the write 
    of all the prepared values currently held in the prepare queue from this client. 
    The result of the procedure is given through the ACI_ATT_EXEC_WRITE_RESP_EVENT event. 
    The end of the procedure is indicated by a ACI_GATT_PROC_COMPLETE_EVENT event.
    """

    CODE = 0xFD11

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Execute_Choices = {
        0x00: "Cancel all prepared writes",
        0x01: "Immediately write all pending prepared values",
    }
    Execute = Parameter(order=2, size=1, choices=Execute_Choices)
    """
    Execute or cancel writes.
    """


class ACI_GATT_DISC_ALL_PRIMARY_SERVICES(CommandPacket):
    """
    Start the GATT client procedure to discover all primary services on the server.
    The responses of the procedure are given through the ACI_ATT_READ_BY_GROUP_TYPE_RESP_EVENT event.
    """

    CODE = 0xFD12

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """


class ACI_GATT_DISC_PRIMARY_SERVICE_BY_UUID(CommandPacket):
    """
    Start the procedure to discover the primary services of the specified UUID on the server.
    The responses of the procedure are given through the ACI_ATT_FIND_BY_TYPE_VALUE_RESP_EVENT event.
    The end of the procedure is indicated by a ACI_GATT_PROC_COMPLETE_EVENT event.
    """

    CODE = 0xFD13

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    UUID_Type_Choices = {
        0x01: "16-bit UUID",
        0x02: "128-bit UUID",
    }
    UUID_Type = Parameter(order=2, size=1, choices=UUID_Type_Choices)
    """
    UUID type.
    """

    UUID = Parameter(order=3, size=(2, 16))
    """
    16-bit UUID or 128-bit UUID
    """


class ACI_GATT_FIND_INCLUDED_SERVICES(CommandPacket):
    """
    Start the procedure to find all included services.
    The responses of the procedure are given through the ACI_ATT_READ_BY_TYPE_RESP_EVENT event.
    The end of the procedure is indicated by a ACI_GATT_PROC_COMPLETE_EVENT event.
    """

    CODE = 0xFD14

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Start_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Start_Handle = Parameter(order=2, size=2, ranges=Start_Handle_Ranges)
    """
    Start attribute handle of the service
    """

    End_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    End_Handle = Parameter(order=3, size=2, ranges=End_Handle_Ranges)
    """
    End attribute handle of the service
    """


class ACI_GATT_DISC_ALL_CHAR_OF_SERVICE(CommandPacket):
    """
    Start the procedure to discover all the characteristics of a given service.
    When the procedure is completed, a ACI_GATT_PROC_COMPLETE_EVENT event is generated.
    Before procedure completion the response packets are given through
    ACI_ATT_READ_BY_TYPE_RESP_EVENT event.
    """

    CODE = 0xFD15

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Start_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Start_Handle = Parameter(order=2, size=2, ranges=Start_Handle_Ranges)
    """
    Start attribute handle of the service
    """

    End_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    End_Handle = Parameter(order=3, size=2, ranges=End_Handle_Ranges)
    """
    End attribute handle of the service
    """


class ACI_GATT_DISC_CHAR_BY_UUID(CommandPacket):
    """
    Start the procedure to discover all the characteristics specified by a UUID.
    When the procedure is completed, a ACI_GATT_PROC_COMPLETE_EVENT event is generated.
    Before procedure completion the response packets are given through
    ACI_GATT_DISC_READ_CHAR_BY_UUID_RESP_EVENT event.
    """

    CODE = 0xFD16

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Start_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Start_Handle = Parameter(order=2, size=2, ranges=Start_Handle_Ranges)
    """
    Start attribute handle of the service
    """

    End_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    End_Handle = Parameter(order=3, size=2, ranges=End_Handle_Ranges)
    """
    End attribute handle of the service
    """

    UUID_Type_Choices = {
        0x01: "16-bit UUID",
        0x02: "128-bit UUID",
    }
    UUID_Type = Parameter(order=4, size=1, choices=UUID_Type_Choices)
    """
    UUID type.
    """

    UUID = Parameter(order=5, size=(2, 16))
    """
    16-bit UUID or 128-bit UUID
    """


class ACI_GATT_DISC_ALL_CHAR_DESC(CommandPacket):
    """
    Start the procedure to discover all characteristic descriptors on the server.
    When the procedure is completed, a ACI_GATT_PROC_COMPLETE_EVENT event is generated.
    Before procedure completion the response packets are given through
    ACI_ATT_FIND_INFO_RESP_EVENT event.
    """

    CODE = 0xFD17

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Char_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Char_Handle = Parameter(order=2, size=2, ranges=Char_Handle_Ranges)
    """
    Handle of the characteristic value
    """

    End_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    End_Handle = Parameter(order=3, size=2, ranges=End_Handle_Ranges)
    """
    End handle of the characteristic
    """


class ACI_GATT_READ_CHAR_VALUE(CommandPacket):
    """
    Start the procedure to read the attribute value.
    When the procedure is completed, a ACI_GATT_PROC_COMPLETE_EVENT event is generated.
    Before procedure completion the response packet is given through ACI_ATT_READ_RESP_EVENT event.
    """

    CODE = 0xFD18

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
    Handle of the attribute to be read
    """


class ACI_GATT_READ_USING_CHAR_UUID(CommandPacket):
    """
    Start the procedure to read all the characteristics specified by the UUID.
    When the procedure is completed, a ACI_GATT_PROC_COMPLETE_EVENT event is generated.
    Before procedure completion the response packets are given through
    ACI_GATT_DISC_READ_CHAR_BY_UUID_RESP_EVENT event.
    """

    CODE = 0xFD19

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Start_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Start_Handle = Parameter(order=2, size=2, ranges=Start_Handle_Ranges)
    """
    Starting handle of the range to be searched
    """

    End_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    End_Handle = Parameter(order=3, size=2, ranges=End_Handle_Ranges)
    """
    End handle of the range to be searched
    """

    UUID_Type_Choices = {
        0x01: "16-bit UUID",
        0x02: "128-bit UUID",
    }
    UUID_Type = Parameter(order=4, size=1, choices=UUID_Type_Choices)
    """
    UUID type.
    """

    UUID = Parameter(order=5, size=(2, 16))
    """
    16-bit UUID or 128-bit UUID
    """


class ACI_GATT_READ_LONG_CHAR_VALUE(CommandPacket):
    """
    Start the procedure to read a long characteristic value.
    the procedure is completed, a ACI_GATT_PROC_COMPLETE_EVENT event is generated.
    Before procedure completion the response packets are given through ACI_ATT_READ_BLOB_RESP_EVENT event.
    """

    CODE = 0xFD1A

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
    Handle of the attribute to be read
    """

    Val_Offset_Ranges = {
        (0, 511): "N/A",
    }
    Val_Offset = Parameter(order=3, size=2, ranges=Val_Offset_Ranges)
    """
    Offset from which the value needs to be read
    """


class ACI_GATT_READ_MULTIPLE_CHAR_VALUE(CommandPacket):
    """
    Start a procedure to read multiple characteristic values from a server.
    This sub-procedure is used to read multiple Characteristic Values from a server when the
    client knows the Characteristic Value Handles.
    When the procedure is completed, a ACI_GATT_PROC_COMPLETE_EVENT event is generated.
    Before procedure completion the response packets are given through
    ACI_ATT_READ_MULTIPLE_RESP_EVENT event.
    """

    CODE = 0xFD1B

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Number_of_Handles_Ranges = {
        (0x02, 0xFF): "N/A",
    }
    Number_of_Handles = Parameter(order=2, size=1, ranges=Number_of_Handles_Ranges)
    """
    The number of handles for which the value has to be read. From 2 to (ATT_MTU-1)/2
    """

    Handle_N_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Handle_N = Parameter(order=3, size=2, ranges=Handle_N_Ranges)
    """
    The handles for which the attribute value has to be read
    """


class ACI_GATT_WRITE_CHAR_VALUE(CommandPacket):
    """
    Start the procedure to write a long characteristic value.
    When the procedure is completed, a ACI_GATT_PROC_COMPLETE_EVENT event is generated.
    During the procedure, ACI_ATT_PREPARE_WRITE_RESP_EVENT and ACI_ATT_EXEC_WRITE_RESP_EVENT
    events are raised.
    """

    CODE = 0xFD1C

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

    Attribute_Val_Length = Parameter(order=3, size=1)
    """
    Length of the value to be written
    """

    Attribute_Val = Parameter(order=4, size=Attribute_Val_Length)
    """
    Value to be written
    """


class ACI_GATT_WRITE_LONG_CHAR_VALUE(CommandPacket):
    """
    Start the procedure to write a long characteristic value.
    When the procedure is completed, a ACI_GATT_PROC_COMPLETE_EVENT event is generated.
    During the procedure, ACI_ATT_PREPARE_WRITE_RESP_EVENT and ACI_ATT_EXEC_WRITE_RESP_EVENT
    events are raised.
    """

    CODE = 0xFD1D

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

    Val_Offset_Ranges = {
        (0, 511): "N/A",
    }
    Val_Offset = Parameter(order=3, size=2, ranges=Val_Offset_Ranges)
    """
    Offset at which the attribute has to be written
    """

    Attribute_Val_Length = Parameter(order=4, size=1)
    """
    Length of the value to be written
    """

    Attribute_Val = Parameter(order=5, size=Attribute_Val_Length)
    """
    Value to be written
    """


class ACI_GATT_WRITE_CHAR_RELIABLE(CommandPacket):
    """
    Start the procedure to write a characteristic reliably.
    When the procedure is completed, a  ACI_GATT_PROC_COMPLETE_EVENT event is generated.
    During the procedure, ACI_ATT_PREPARE_WRITE_RESP_EVENT and ACI_ATT_EXEC_WRITE_RESP_EVENT
    events are raised.
    """

    CODE = 0xFD1E

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

    Val_Offset_Ranges = {
        (0, 511): "N/A",
    }
    Val_Offset = Parameter(order=3, size=2, ranges=Val_Offset_Ranges)
    """
    Offset at which the attribute has to be written
    """

    Attribute_Val_Length = Parameter(order=4, size=1)
    """
    Length of the value to be written
    """

    Attribute_Val = Parameter(order=5, size=Attribute_Val_Length)
    """
    Value to be written
    """


class ACI_GATT_WRITE_LONG_CHAR_DESC(CommandPacket):
    """
    Start the procedure to write a long characteristic descriptor.
    When the procedure is completed, a ACI_GATT_PROC_COMPLETE_EVENT event is generated.
    During the procedure, ACI_ATT_PREPARE_WRITE_RESP_EVENT and ACI_ATT_EXEC_WRITE_RESP_EVENT
    events are raised.
    """

    CODE = 0xFD1F

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

    Val_Offset_Ranges = {
        (0, 511): "N/A",
    }
    Val_Offset = Parameter(order=3, size=2, ranges=Val_Offset_Ranges)
    """
    Offset at which the attribute has to be written
    """

    Attribute_Val_Length = Parameter(order=4, size=1)
    """
    Length of the value to be written
    """

    Attribute_Val = Parameter(order=5, size=Attribute_Val_Length)
    """
    Value to be written
    """


class ACI_GATT_READ_LONG_CHAR_DESC(CommandPacket):
    """
    Start the procedure to read a long characteristic value.
    When the procedure is completed, a ACI_GATT_PROC_COMPLETE_EVENT event is
    generated. Before procedure completion the response packets are given through
    ACI_ATT_READ_BLOB_RESP_EVENT event.
    """

    CODE = 0xFD20

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
    Handle of the characteristic descriptor
    """

    Val_Offset_Ranges = {
        (0, 511): "N/A",
    }
    Val_Offset = Parameter(order=3, size=2, ranges=Val_Offset_Ranges)
    """
    Offset from which the value needs to be read
    """


class ACI_GATT_WRITE_CHAR_DESC(CommandPacket):
    """
    Start the procedure to write a characteristic descriptor.
    When the procedure is completed, a ACI_GATT_PROC_COMPLETE_EVENT event is generated.
    """

    CODE = 0xFD21

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

    Attribute_Val_Length = Parameter(order=3, size=1)
    """
    Length of the value to be written
    """

    Attribute_Val = Parameter(order=4, size=Attribute_Val_Length)
    """
    Value to be written
    """


class ACI_GATT_READ_CHAR_DESC(CommandPacket):
    """
    Start the procedure to read the descriptor specified.
    When the procedure is completed, a ACI_GATT_PROC_COMPLETE_EVENT event is generated.
    Before procedure completion the response packet is given through ACI_ATT_READ_RESP_EVENT event.
    """

    CODE = 0xFD22

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
    Handle of the descriptor to be read
    """


class ACI_GATT_WRITE_WITHOUT_RESP(CommandPacket):
    """
    Start the procedure to write a characteristic value without waiting for any response from the
    server. No events are generated after this command is executed.
    """

    CODE = 0xFD23

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

    Attribute_Val_Length = Parameter(order=3, size=1)
    """
    Length of the value to be written (maximum value is ATT_MTU - 3)
    """

    Attribute_Val = Parameter(order=4, size=Attribute_Val_Length)
    """
    Value to be written
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GATT_SIGNED_WRITE_WITHOUT_RESP(CommandPacket):
    """
    Start a signed write without response from the server.
    The procedure is used to write a characteristic value with an authentication signature without waiting
    for any response from the server. It cannot be used when the link is encrypted.
    """

    CODE = 0xFD24

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

    Attribute_Val_Length = Parameter(order=3, size=1)
    """
    Length of the value to be written (up to ATT_MTU - 13)
    """

    Attribute_Val = Parameter(order=4, size=Attribute_Val_Length)
    """
    Value to be written
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GATT_CONFIRM_INDICATION(CommandPacket):
    """
    Allow application to confirm indication. This command has to be sent when the application
    receives the event ACI_GATT_INDICATION_EVENT.
    """

    CODE = 0xFD25

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


class ACI_GATT_WRITE_RESP(CommandPacket):
    """
    Allow or reject a write request from a client.
    This command has to be sent by the application when it receives the
    ACI_GATT_WRITE_PERMIT_REQ_EVENT. If the write can be allowed, then the status and error
    code has to be set to 0. If the write cannot be allowed, then the status has to be set to 1 and
    the error code has to be set to the error code that has to be passed to the client.
    """

    CODE = 0xFD26

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
    Handle of the attribute that was passed in the event EVT_BLUE_GATT_WRITE_PERMIT_REQ
    """

    Write_status_Choices = {
        0x00: "The value can be written to the attribute specified by attr_handle",
        0x01: "The value cannot be written to the attribute specified by the attr_handle",
    }
    Write_status = Parameter(order=3, size=1, choices=Write_status_Choices)
    """
    If the value can be written or not.
    """

    Error_Code_Ranges = {
        (0x80, 0x9F): "Application Error",
        (0xE0, 0xFF): "Profile Error",
    }
    Error_Code = Parameter(order=4, size=1, ranges=Error_Code_Ranges)
    """
    The error code that has to be passed to the client in case the write has to be rejected
    """

    Attribute_Val_Length = Parameter(order=5, size=1)
    """
    Length of the value to be written as passed in the event EVT_BLUE_GATT_WRITE_PERMIT_REQ
    """

    Attribute_Val = Parameter(order=6, size=Attribute_Val_Length)
    """
    Value as passed in the event EVT_BLUE_GATT_WRITE_PERMIT_REQ
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GATT_ALLOW_READ(CommandPacket):
    """
    Allow the GATT server to send a response to a read request from a client.
    The application has to send this command when it receives the
    ACI_GATT_READ_PERMIT_REQ_EVENT or ACI_GATT_READ_MULTI_PERMIT_REQ_EVENT. This
    command indicates to the stack that the response can be sent to the client. So if the
    application wishes to update any of the attributes before they are read by the client, it has to
    update the characteristic values using the ACI_GATT_UPDATE_CHAR_VALUE and then give
    this command. The application should perform the required operations within 30 seconds.
    Otherwise the GATT procedure will be timeout.
    """

    CODE = 0xFD27

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


class ACI_GATT_SET_SECURITY_PERMISSION(CommandPacket):
    """
    This command sets the security permission for the attribute handle specified. Currently the
    setting of security permission is allowed only for client configuration descriptor.
    """

    CODE = 0xFD28

    Serv_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Serv_Handle = Parameter(order=1, size=2, ranges=Serv_Handle_Ranges)
    """
    Handle of the service which contains the attribute whose security permission has to be modified
    """

    Attr_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Attr_Handle = Parameter(order=2, size=2, ranges=Attr_Handle_Ranges)
    """
    Handle of the attribute whose security permission has to be modified
    """

    Security_Permissions_Choices = {
        0x00: "None",
        0x01: "AUTHEN_READ (Need authentication to read)",
        0x02: "AUTHOR_READ (Need authorization to read)",
        0x04: "ENCRY_READ (Need encryption to read)",
        0x08: "AUTHEN_WRITE (need authentication to write)",
        0x10: "AUTHOR_WRITE (need authorization to write)",
        0x20: "ENCRY_WRITE (need encryption to write)",
    }
    Security_Permissions = Parameter(order=3, size=1, choices=Security_Permissions_Choices, multi_choice=True)
    """
    Security permission flags.
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GATT_SET_DESC_VALUE(CommandPacket):
    """
    This command sets the value of the descriptor specified by charDescHandle.
    """

    CODE = 0xFD29

    Serv_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Serv_Handle = Parameter(order=1, size=2, ranges=Serv_Handle_Ranges)
    """
    Handle of the service which contains the characteristic descriptor
    """

    Char_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Char_Handle = Parameter(order=2, size=2, ranges=Char_Handle_Ranges)
    """
    Handle of the characteristic which contains the descriptor
    """

    Char_Desc_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Char_Desc_Handle = Parameter(order=3, size=2, ranges=Char_Desc_Handle_Ranges)
    """
    Handle of the descriptor whose value has to be set
    """

    Val_Offset_Ranges = {
        (0, 511): "N/A",
    }
    Val_Offset = Parameter(order=4, size=2, ranges=Val_Offset_Ranges)
    """
    Offset from which the descriptor value has to be updated
    """

    Char_Desc_Value_Length = Parameter(order=5, size=1)
    """
    Length of the descriptor value.
    """

    Char_Desc_Value = Parameter(order=6, size=Char_Desc_Value_Length)
    """
    Descriptor value
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GATT_READ_HANDLE_VALUE(CommandPacket):
    """
    Reads the value of the attribute handle specified from the local GATT database.
    """

    CODE = 0xFD2A

    Attr_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Attr_Handle = Parameter(order=1, size=2, ranges=Attr_Handle_Ranges)
    """
    Handle of the attribute to read
    """

    Offset_Ranges = {
        (0, 511): "N/A",
    }
    Offset = Parameter(order=2, size=2, ranges=Offset_Ranges)
    """
    Offset from which the value needs to be read
    """

    Value_Length_Requested_Ranges = {
        (0, 512): "N/A",
    }
    Value_Length_Requested = Parameter(order=3, size=2, ranges=Value_Length_Requested_Ranges)
    """
    Maximum number of octets to be returned as attribute value
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

        Length = Parameter(order=2, size=2)
        """
        Length of the attribute value
        """

        Value_Length = Parameter(order=3, size=2)
        """
        Length in octets of the Value parameter
        """

        Value = Parameter(order=4, size=Value_Length)
        """
        Attribute value
        """


class ACI_GATT_UPDATE_CHAR_VALUE_EXT(CommandPacket):
    """
    This command is a more flexible version of ACI_GATT_UPDATE_CHAR_VALUE
                          to support update of long attribute up to 512 bytes and indicate selectively the generation of Indication/Notification.
    """

    CODE = 0xFD2C

    Conn_Handle_To_Notify = Parameter(order=1, size=2)
    """
    Connection handle to notify. Notify all subscribed clients if equal to 0x0000: DEPRECATED feature (still supported but not recommended).
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

    Update_Type_Choices = {
        0x00: "GATT_LOCAL_UPDATE",
        0x01: "GATT_NOTIFICATION",
        0x02: "GATT_INDICATION",
        0x04: "GATT_DISABLE_RETRANSMISSIONS",
    }
    Update_Type = Parameter(order=4, size=1, choices=Update_Type_Choices, multi_choice=True)
    """
    Allow Notification or Indication generation, if enabled in the client characteristic configuration descriptor.
        If bit 3 is set, standard BLE Link Layer retransmission mechanism for notifications PDUs si disabled: PDUs will be transmitted only once, even if they have not been acknowledged.
    """

    Char_Length_Ranges = {
        (0, 512): "N/A",
    }
    Char_Length = Parameter(order=5, size=2, ranges=Char_Length_Ranges)
    """
    Total length of the characteristic value.
        In case of a variable size characteristic, this field specifies the new length of the characteristic value after the update; in case of fixed length characteristic this field is ignored.
    """

    Value_Offset_Ranges = {
        (0, 511): "N/A",
    }
    Value_Offset = Parameter(order=6, size=2, ranges=Value_Offset_Ranges)
    """
    The offset from which the attribute value has to be updated.
    """

    Value_Length = Parameter(order=7, size=1)
    """
    Length of the Value parameter in octets
    """

    Value = Parameter(order=8, size=Value_Length)
    """
    Updated characteristic value
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GATT_DENY_READ(CommandPacket):
    """
    Deny the GATT server to send a response to a read request from a client.
    The application may send this command when it receives the ACI_GATT_READ_PERMIT_REQ_EVENT or  ACI_GATT_READ_MULTI_PERMIT_REQ_EVENT.
    This command indicates to the stack that the client is not allowed to read the requested characteristic due to e.g. application restrictions.
    The Error code shall be either 0x08 (Insufficient Authorization) or a value in the range 0x80-0x9F (Application Error).
    The application should issue the ACI_GATT_DENY_READ  or ACI_GATT_ALLOW_READ command within 30 seconds from the reception of
    the ACI_GATT_READ_PERMIT_REQ_EVENT or  ACI_GATT_READ_MULTI_PERMIT_REQ_EVENT events otherwise the GATT procedure will issue a timeout.
    """

    CODE = 0xFD2D

    Connection_Handle_Ranges = {
        (0x0000, 0x0EFF): "N/A",
    }
    Connection_Handle = Parameter(order=1, size=2, ranges=Connection_Handle_Ranges)
    """
    Connection handle that identifies the connection.
    """

    Error_Code_Choices = {
        0x08: "Insufficient Authorization",
    }
    Error_Code_Ranges = {
        (0x80, 0x9F): "Application Error",
    }
    Error_Code = Parameter(order=2, size=1, choices=Error_Code_Choices, ranges=Error_Code_Ranges)
    """
    Error code for the command
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """


class ACI_GATT_SET_ACCESS_PERMISSION(CommandPacket):
    """
    This command sets the access permission for the attribute handle specified.
    """

    CODE = 0xFD2E

    Serv_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Serv_Handle = Parameter(order=1, size=2, ranges=Serv_Handle_Ranges)
    """
    Handle of the service which contains the attribute whose access permission has to be modified
    """

    Attr_Handle_Ranges = {
        (0x0001, 0xFFFF): "N/A",
    }
    Attr_Handle = Parameter(order=2, size=2, ranges=Attr_Handle_Ranges)
    """
    Handle of the attribute whose security permission has to be modified
    """

    Access_Permissions_Choices = {
        0x00: "None",
        0x01: "READ",
        0x02: "WRITE",
        0x04: "WRITE_NO_RESP",
        0x08: "SIGNED_WRITE",
    }
    Access_Permissions = Parameter(order=3, size=1, choices=Access_Permissions_Choices)
    """
    Access permission
    """

    class HCI_COMMAND_COMPLETE_EVENT(events.HCI_COMMAND_COMPLETE_EVENT):

        Status = Parameter(order=1, size=1)
        """
        For standard error codes see Bluetooth specification, Vol. 2, part D. For proprietary error code refer to Error codes section
        """

