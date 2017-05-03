# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Command.py
from types import *

class CommandConnect:

    def __init__(self):
        self.__dict__['common'] = ParamsCommon()
        self.__dict__['cmdId'] = 0
        self.__dict__['requestSocketIndex'] = 4294967295L
        self.__dict__['remoteSocketIndex'] = 4294967295L
        self.__dict__['errorModule'] = 0
        self.__dict__['errorOs'] = 0

    def __getattr__(self, name):
        if name == 'common':
            return self.__dict__['common']
        if name == 'cmdId':
            return self.__dict__['cmdId']
        if name == 'requestSocketIndex':
            return self.__dict__['requestSocketIndex']
        if name == 'remoteSocketIndex':
            return self.__dict__['remoteSocketIndex']
        if name == 'errorModule':
            return self.__dict__['errorModule']
        if name == 'errorOs':
            return self.__dict__['errorOs']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'common':
            self.__dict__['common'] = value
        elif name == 'cmdId':
            self.__dict__['cmdId'] = value
        elif name == 'requestSocketIndex':
            self.__dict__['requestSocketIndex'] = value
        elif name == 'remoteSocketIndex':
            self.__dict__['remoteSocketIndex'] = value
        elif name == 'errorModule':
            self.__dict__['errorModule'] = value
        elif name == 'errorOs':
            self.__dict__['errorOs'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg2 = MarshalMessage()
        self.__dict__['common'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_COMMAND_CONNECT_COMMON, submsg2)
        submsg.AddU32(MSG_KEY_COMMAND_CONNECT_CMD_ID, self.__dict__['cmdId'])
        submsg.AddU32(MSG_KEY_COMMAND_CONNECT_REQUEST_SOCKET_INDEX, self.__dict__['requestSocketIndex'])
        submsg.AddU32(MSG_KEY_COMMAND_CONNECT_REMOTE_SOCKET_INDEX, self.__dict__['remoteSocketIndex'])
        submsg.AddU32(MSG_KEY_COMMAND_CONNECT_ERROR_MODULE, self.__dict__['errorModule'])
        submsg.AddU32(MSG_KEY_COMMAND_CONNECT_ERROR_OS, self.__dict__['errorOs'])
        mmsg.AddMessage(MSG_KEY_COMMAND_CONNECT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_COMMAND_CONNECT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        submsg2 = submsg.FindMessage(MSG_KEY_COMMAND_CONNECT_COMMON)
        self.__dict__['common'].Demarshal(submsg2)
        self.__dict__['cmdId'] = submsg.FindU32(MSG_KEY_COMMAND_CONNECT_CMD_ID)
        self.__dict__['requestSocketIndex'] = submsg.FindU32(MSG_KEY_COMMAND_CONNECT_REQUEST_SOCKET_INDEX)
        self.__dict__['remoteSocketIndex'] = submsg.FindU32(MSG_KEY_COMMAND_CONNECT_REMOTE_SOCKET_INDEX)
        self.__dict__['errorModule'] = submsg.FindU32(MSG_KEY_COMMAND_CONNECT_ERROR_MODULE)
        self.__dict__['errorOs'] = submsg.FindU32(MSG_KEY_COMMAND_CONNECT_ERROR_OS)


class CommandStopAll:

    def __init__(self):
        self.__dict__['common'] = ParamsCommon()

    def __getattr__(self, name):
        if name == 'common':
            return self.__dict__['common']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'common':
            self.__dict__['common'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg2 = MarshalMessage()
        self.__dict__['common'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_COMMAND_STOP_ALL_COMMON, submsg2)
        mmsg.AddMessage(MSG_KEY_COMMAND_STOP_ALL, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_COMMAND_STOP_ALL, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        submsg2 = submsg.FindMessage(MSG_KEY_COMMAND_STOP_ALL_COMMON)
        self.__dict__['common'].Demarshal(submsg2)