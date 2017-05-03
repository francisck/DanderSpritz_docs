# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
MSG_KEY_CONNECT_PARAMS = 65536
MSG_KEY_CONNECT_PARAMS_CONNECTION_TYPE = 65537
MSG_KEY_CONNECT_PARAMS_PORT = 65538
MSG_KEY_CONNECT_PARAMS_HANDLE = 65539
MSG_KEY_CONNECT_PARAMS_BAUDRATE = 65540
MSG_KEY_CONNECT_PARAMS_DATA_BITS = 65541
MSG_KEY_CONNECT_PARAMS_PARITY = 65542
MSG_KEY_CONNECT_PARAMS_STOP_BITS = 65543
MSG_KEY_CONNECT_PARAMS_TIMEOUT = 65544
MSG_KEY_WRITE_PARAMS = 131072
MSG_KEY_WRITE_PARAMS_DATA = 131073
MSG_KEY_WRITE_PARAMS_INDEX = 131074

class ConnectParams:

    def __init__(self):
        self.__dict__['connectionType'] = 0
        self.__dict__['port'] = ''
        self.__dict__['handle'] = 0
        self.__dict__['baudrate'] = 0
        self.__dict__['dataBits'] = 0
        self.__dict__['parity'] = 0
        self.__dict__['stopBits'] = 0
        self.__dict__['timeout'] = 0

    def __getattr__(self, name):
        if name == 'connectionType':
            return self.__dict__['connectionType']
        if name == 'port':
            return self.__dict__['port']
        if name == 'handle':
            return self.__dict__['handle']
        if name == 'baudrate':
            return self.__dict__['baudrate']
        if name == 'dataBits':
            return self.__dict__['dataBits']
        if name == 'parity':
            return self.__dict__['parity']
        if name == 'stopBits':
            return self.__dict__['stopBits']
        if name == 'timeout':
            return self.__dict__['timeout']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'connectionType':
            self.__dict__['connectionType'] = value
        elif name == 'port':
            self.__dict__['port'] = value
        elif name == 'handle':
            self.__dict__['handle'] = value
        elif name == 'baudrate':
            self.__dict__['baudrate'] = value
        elif name == 'dataBits':
            self.__dict__['dataBits'] = value
        elif name == 'parity':
            self.__dict__['parity'] = value
        elif name == 'stopBits':
            self.__dict__['stopBits'] = value
        elif name == 'timeout':
            self.__dict__['timeout'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_CONNECT_PARAMS_CONNECTION_TYPE, self.__dict__['connectionType'])
        submsg.AddStringUtf8(MSG_KEY_CONNECT_PARAMS_PORT, self.__dict__['port'])
        submsg.AddU32(MSG_KEY_CONNECT_PARAMS_HANDLE, self.__dict__['handle'])
        submsg.AddU32(MSG_KEY_CONNECT_PARAMS_BAUDRATE, self.__dict__['baudrate'])
        submsg.AddU8(MSG_KEY_CONNECT_PARAMS_DATA_BITS, self.__dict__['dataBits'])
        submsg.AddU8(MSG_KEY_CONNECT_PARAMS_PARITY, self.__dict__['parity'])
        submsg.AddU8(MSG_KEY_CONNECT_PARAMS_STOP_BITS, self.__dict__['stopBits'])
        submsg.AddU16(MSG_KEY_CONNECT_PARAMS_TIMEOUT, self.__dict__['timeout'])
        mmsg.AddMessage(MSG_KEY_CONNECT_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_CONNECT_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['connectionType'] = submsg.FindU8(MSG_KEY_CONNECT_PARAMS_CONNECTION_TYPE)
        self.__dict__['port'] = submsg.FindString(MSG_KEY_CONNECT_PARAMS_PORT)
        self.__dict__['handle'] = submsg.FindU32(MSG_KEY_CONNECT_PARAMS_HANDLE)
        self.__dict__['baudrate'] = submsg.FindU32(MSG_KEY_CONNECT_PARAMS_BAUDRATE)
        self.__dict__['dataBits'] = submsg.FindU8(MSG_KEY_CONNECT_PARAMS_DATA_BITS)
        self.__dict__['parity'] = submsg.FindU8(MSG_KEY_CONNECT_PARAMS_PARITY)
        self.__dict__['stopBits'] = submsg.FindU8(MSG_KEY_CONNECT_PARAMS_STOP_BITS)
        self.__dict__['timeout'] = submsg.FindU16(MSG_KEY_CONNECT_PARAMS_TIMEOUT)


class WriteParams:

    def __init__(self):
        self.__dict__['data'] = ''
        self.__dict__['index'] = 0

    def __getattr__(self, name):
        if name == 'data':
            return self.__dict__['data']
        if name == 'index':
            return self.__dict__['index']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'data':
            self.__dict__['data'] = value
        elif name == 'index':
            self.__dict__['index'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_WRITE_PARAMS_DATA, self.__dict__['data'])
        submsg.AddU32(MSG_KEY_WRITE_PARAMS_INDEX, self.__dict__['index'])
        mmsg.AddMessage(MSG_KEY_WRITE_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_WRITE_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['data'] = submsg.FindString(MSG_KEY_WRITE_PARAMS_DATA)
        self.__dict__['index'] = submsg.FindU32(MSG_KEY_WRITE_PARAMS_INDEX)