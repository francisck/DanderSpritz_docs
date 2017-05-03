# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
MSG_KEY_RESULT_STATUS = 196608
MSG_KEY_RESULT_STATUS_TYPE = 196609
MSG_KEY_RESULT_STATUS_DATA = 196610
MSG_KEY_RESULT_CONNECT = 262144
MSG_KEY_RESULT_CONNECT_CONNECTION_TYPE = 262145
MSG_KEY_RESULT_CONNECT_BAUDRATE = 262148
MSG_KEY_RESULT_CONNECT_DATA_BITS = 262149
MSG_KEY_RESULT_CONNECT_PARITY = 262150
MSG_KEY_RESULT_CONNECT_STOP_BITS = 262151
MSG_KEY_RESULT_CONNECT_COMM_STATE = 262152
MSG_KEY_RESULT_CONNECT_INDEX = 262154

class StatusResult:

    def __init__(self):
        self.__dict__['statusType'] = 0
        self.__dict__['data'] = ''

    def __getattr__(self, name):
        if name == 'statusType':
            return self.__dict__['statusType']
        if name == 'data':
            return self.__dict__['data']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'statusType':
            self.__dict__['statusType'] = value
        elif name == 'data':
            self.__dict__['data'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_STATUS_TYPE, self.__dict__['statusType'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_STATUS_DATA, self.__dict__['data'])
        mmsg.AddMessage(MSG_KEY_RESULT_STATUS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_STATUS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['statusType'] = submsg.FindU8(MSG_KEY_RESULT_STATUS_TYPE)
        self.__dict__['data'] = submsg.FindString(MSG_KEY_RESULT_STATUS_DATA)


class ConnectResult:

    def __init__(self):
        self.__dict__['connectionType'] = 0
        self.__dict__['commStateRetrieved'] = False
        self.__dict__['baudrate'] = 0
        self.__dict__['dataBits'] = 0
        self.__dict__['parity'] = 0
        self.__dict__['stopBits'] = 0
        self.__dict__['index'] = 0

    def __getattr__(self, name):
        if name == 'connectionType':
            return self.__dict__['connectionType']
        if name == 'commStateRetrieved':
            return self.__dict__['commStateRetrieved']
        if name == 'baudrate':
            return self.__dict__['baudrate']
        if name == 'dataBits':
            return self.__dict__['dataBits']
        if name == 'parity':
            return self.__dict__['parity']
        if name == 'stopBits':
            return self.__dict__['stopBits']
        if name == 'index':
            return self.__dict__['index']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'connectionType':
            self.__dict__['connectionType'] = value
        elif name == 'commStateRetrieved':
            self.__dict__['commStateRetrieved'] = value
        elif name == 'baudrate':
            self.__dict__['baudrate'] = value
        elif name == 'dataBits':
            self.__dict__['dataBits'] = value
        elif name == 'parity':
            self.__dict__['parity'] = value
        elif name == 'stopBits':
            self.__dict__['stopBits'] = value
        elif name == 'index':
            self.__dict__['index'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_CONNECT_CONNECTION_TYPE, self.__dict__['connectionType'])
        submsg.AddBool(MSG_KEY_RESULT_CONNECT_COMM_STATE, self.__dict__['commStateRetrieved'])
        submsg.AddU32(MSG_KEY_RESULT_CONNECT_BAUDRATE, self.__dict__['baudrate'])
        submsg.AddU8(MSG_KEY_RESULT_CONNECT_DATA_BITS, self.__dict__['dataBits'])
        submsg.AddU8(MSG_KEY_RESULT_CONNECT_PARITY, self.__dict__['parity'])
        submsg.AddU8(MSG_KEY_RESULT_CONNECT_STOP_BITS, self.__dict__['stopBits'])
        submsg.AddU32(MSG_KEY_RESULT_CONNECT_INDEX, self.__dict__['index'])
        mmsg.AddMessage(MSG_KEY_RESULT_CONNECT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_CONNECT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['connectionType'] = submsg.FindU8(MSG_KEY_RESULT_CONNECT_CONNECTION_TYPE)
        self.__dict__['commStateRetrieved'] = submsg.FindBool(MSG_KEY_RESULT_CONNECT_COMM_STATE)
        self.__dict__['baudrate'] = submsg.FindU32(MSG_KEY_RESULT_CONNECT_BAUDRATE)
        self.__dict__['dataBits'] = submsg.FindU8(MSG_KEY_RESULT_CONNECT_DATA_BITS)
        self.__dict__['parity'] = submsg.FindU8(MSG_KEY_RESULT_CONNECT_PARITY)
        self.__dict__['stopBits'] = submsg.FindU8(MSG_KEY_RESULT_CONNECT_STOP_BITS)
        self.__dict__['index'] = submsg.FindU32(MSG_KEY_RESULT_CONNECT_INDEX)