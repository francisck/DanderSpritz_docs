# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.IpAddr
RESULT_DATA_TYPE_INITIAL = 1
RESULT_DATA_TYPE_ADDED = 2
RESULT_DATA_TYPE_REMOVED = 3
RESULT_DATA_TYPE_LIST = 4
RESULT_IP_PROTOCOL_UNKNOWN = 0
RESULT_IP_PROTOCOL_TCP = 1
RESULT_IP_PROTOCOL_UDP = 2
RESULT_IP_PROTOCOL_RAW = 3
RESULT_IP_STATE_UNKNOWN = 0
RESULT_IP_STATE_ESTABLISHED = 1
RESULT_IP_STATE_SYN_SENT = 2
RESULT_IP_STATE_SYN_RECV = 3
RESULT_IP_STATE_FIN_WAIT_1 = 4
RESULT_IP_STATE_FIN_WAIT_2 = 5
RESULT_IP_STATE_TIME_WAIT = 6
RESULT_IP_STATE_CLOSED = 7
RESULT_IP_STATE_CLOSE_WAIT = 8
RESULT_IP_STATE_LAST_ACK = 9
RESULT_IP_STATE_LISTEN = 10
RESULT_IP_STATE_CLOSING = 11

class Result:

    def __init__(self):
        self.__dict__['dataType'] = 0

    def __getattr__(self, name):
        if name == 'dataType':
            return self.__dict__['dataType']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'dataType':
            self.__dict__['dataType'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_INFO_DATA_TYPE, self.__dict__['dataType'])
        mmsg.AddMessage(MSG_KEY_RESULT_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['dataType'] = submsg.FindU8(MSG_KEY_RESULT_INFO_DATA_TYPE)


class ResultIp:

    def __init__(self):
        self.__dict__['protocol'] = RESULT_IP_PROTOCOL_UNKNOWN
        self.__dict__['localIp'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['localPort'] = 0
        self.__dict__['remoteIp'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['remotePort'] = 0
        self.__dict__['state'] = 0
        self.__dict__['valid'] = True
        self.__dict__['hasRemoteIp'] = False
        self.__dict__['pid'] = 0

    def __getattr__(self, name):
        if name == 'protocol':
            return self.__dict__['protocol']
        if name == 'localIp':
            return self.__dict__['localIp']
        if name == 'localPort':
            return self.__dict__['localPort']
        if name == 'remoteIp':
            return self.__dict__['remoteIp']
        if name == 'remotePort':
            return self.__dict__['remotePort']
        if name == 'state':
            return self.__dict__['state']
        if name == 'valid':
            return self.__dict__['valid']
        if name == 'hasRemoteIp':
            return self.__dict__['hasRemoteIp']
        if name == 'pid':
            return self.__dict__['pid']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'protocol':
            self.__dict__['protocol'] = value
        elif name == 'localIp':
            self.__dict__['localIp'] = value
        elif name == 'localPort':
            self.__dict__['localPort'] = value
        elif name == 'remoteIp':
            self.__dict__['remoteIp'] = value
        elif name == 'remotePort':
            self.__dict__['remotePort'] = value
        elif name == 'state':
            self.__dict__['state'] = value
        elif name == 'valid':
            self.__dict__['valid'] = value
        elif name == 'hasRemoteIp':
            self.__dict__['hasRemoteIp'] = value
        elif name == 'pid':
            self.__dict__['pid'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_IP_PROTOCOL, self.__dict__['protocol'])
        submsg.AddIpAddr(MSG_KEY_RESULT_IP_LOCAL_IP, self.__dict__['localIp'])
        submsg.AddU16(MSG_KEY_RESULT_IP_LOCAL_PORT, self.__dict__['localPort'])
        submsg.AddIpAddr(MSG_KEY_RESULT_IP_REMOTE_IP, self.__dict__['remoteIp'])
        submsg.AddU16(MSG_KEY_RESULT_IP_REMOTE_PORT, self.__dict__['remotePort'])
        submsg.AddU8(MSG_KEY_RESULT_IP_STATE, self.__dict__['state'])
        submsg.AddBool(MSG_KEY_RESULT_IP_VALID, self.__dict__['valid'])
        submsg.AddBool(MSG_KEY_RESULT_IP_HAS_REMOTE_IP, self.__dict__['hasRemoteIp'])
        submsg.AddU32(MSG_KEY_RESULT_IP_PROCESS_ID, self.__dict__['pid'])
        mmsg.AddMessage(MSG_KEY_RESULT_IP, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_IP, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['protocol'] = submsg.FindU8(MSG_KEY_RESULT_IP_PROTOCOL)
        self.__dict__['localIp'] = submsg.FindIpAddr(MSG_KEY_RESULT_IP_LOCAL_IP)
        self.__dict__['localPort'] = submsg.FindU16(MSG_KEY_RESULT_IP_LOCAL_PORT)
        self.__dict__['remoteIp'] = submsg.FindIpAddr(MSG_KEY_RESULT_IP_REMOTE_IP)
        self.__dict__['remotePort'] = submsg.FindU16(MSG_KEY_RESULT_IP_REMOTE_PORT)
        self.__dict__['state'] = submsg.FindU8(MSG_KEY_RESULT_IP_STATE)
        self.__dict__['valid'] = submsg.FindBool(MSG_KEY_RESULT_IP_VALID)
        self.__dict__['hasRemoteIp'] = submsg.FindBool(MSG_KEY_RESULT_IP_HAS_REMOTE_IP)
        self.__dict__['pid'] = submsg.FindU32(MSG_KEY_RESULT_IP_PROCESS_ID)


class ResultNamedPipe:

    def __init__(self):
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_NAMEDPIPE_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_RESULT_NAMEDPIPE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_NAMEDPIPE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_NAMEDPIPE_NAME)


class ResultMailSlot:

    def __init__(self):
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_MAILSLOT_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_RESULT_MAILSLOT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MAILSLOT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_MAILSLOT_NAME)