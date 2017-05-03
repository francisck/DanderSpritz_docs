# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Status.py
from types import *
import mcl.object.IpAddr
STATUS_CONNECTION_TYPE_LISTENING = 1
STATUS_CONNECTION_TYPE_NEW = 2
STATUS_CONNECTION_TYPE_REJECTED = 3
STATUS_CONNECTION_TYPE_CLOSED = 4

class StatusError:

    def __init__(self):
        self.__dict__['errorModule'] = 0
        self.__dict__['errorOs'] = 0

    def __getattr__(self, name):
        if name == 'errorModule':
            return self.__dict__['errorModule']
        if name == 'errorOs':
            return self.__dict__['errorOs']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'errorModule':
            self.__dict__['errorModule'] = value
        elif name == 'errorOs':
            self.__dict__['errorOs'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_STATUS_ERROR_ERROR_MODULE, self.__dict__['errorModule'])
        submsg.AddU32(MSG_KEY_STATUS_ERROR_ERROR_OS, self.__dict__['errorOs'])
        mmsg.AddMessage(MSG_KEY_STATUS_ERROR, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_STATUS_ERROR, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['errorModule'] = submsg.FindU32(MSG_KEY_STATUS_ERROR_ERROR_MODULE)
        self.__dict__['errorOs'] = submsg.FindU32(MSG_KEY_STATUS_ERROR_ERROR_OS)


class StatusConnection:

    def __init__(self):
        self.__dict__['type'] = 0
        self.__dict__['socketType'] = 0
        self.__dict__['localAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['localPort'] = 0
        self.__dict__['remoteAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['remotePort'] = 0
        self.__dict__['socketError'] = 0

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'socketType':
            return self.__dict__['socketType']
        if name == 'localAddr':
            return self.__dict__['localAddr']
        if name == 'localPort':
            return self.__dict__['localPort']
        if name == 'remoteAddr':
            return self.__dict__['remoteAddr']
        if name == 'remotePort':
            return self.__dict__['remotePort']
        if name == 'socketError':
            return self.__dict__['socketError']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'socketType':
            self.__dict__['socketType'] = value
        elif name == 'localAddr':
            self.__dict__['localAddr'] = value
        elif name == 'localPort':
            self.__dict__['localPort'] = value
        elif name == 'remoteAddr':
            self.__dict__['remoteAddr'] = value
        elif name == 'remotePort':
            self.__dict__['remotePort'] = value
        elif name == 'socketError':
            self.__dict__['socketError'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_STATUS_CONNECTION_TYPE, self.__dict__['type'])
        submsg.AddU8(MSG_KEY_STATUS_CONNECTION_SOCKET_TYPE, self.__dict__['socketType'])
        submsg.AddIpAddr(MSG_KEY_STATUS_CONNECTION_LOCAL_ADDR, self.__dict__['localAddr'])
        submsg.AddU16(MSG_KEY_STATUS_CONNECTION_LOCAL_PORT, self.__dict__['localPort'])
        submsg.AddIpAddr(MSG_KEY_STATUS_CONNECTION_REMOTE_ADDR, self.__dict__['remoteAddr'])
        submsg.AddU16(MSG_KEY_STATUS_CONNECTION_REMOTE_PORT, self.__dict__['remotePort'])
        submsg.AddU32(MSG_KEY_STATUS_CONNECTION_SOCKET_ERROR, self.__dict__['socketError'])
        mmsg.AddMessage(MSG_KEY_STATUS_CONNECTION, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_STATUS_CONNECTION, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_STATUS_CONNECTION_TYPE)
        self.__dict__['socketType'] = submsg.FindU8(MSG_KEY_STATUS_CONNECTION_SOCKET_TYPE)
        self.__dict__['localAddr'] = submsg.FindIpAddr(MSG_KEY_STATUS_CONNECTION_LOCAL_ADDR)
        self.__dict__['localPort'] = submsg.FindU16(MSG_KEY_STATUS_CONNECTION_LOCAL_PORT)
        self.__dict__['remoteAddr'] = submsg.FindIpAddr(MSG_KEY_STATUS_CONNECTION_REMOTE_ADDR)
        self.__dict__['remotePort'] = submsg.FindU16(MSG_KEY_STATUS_CONNECTION_REMOTE_PORT)
        self.__dict__['socketError'] = submsg.FindU32(MSG_KEY_STATUS_CONNECTION_SOCKET_ERROR)