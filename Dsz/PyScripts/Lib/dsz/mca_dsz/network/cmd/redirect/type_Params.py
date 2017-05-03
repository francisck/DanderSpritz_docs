# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import mcl.object.IpAddr
PARAMS_STANDARD_FLAG_NOTIFY_CONNECT = 1

class ParamsCommon:

    def __init__(self):
        self.__dict__['cmdId'] = 0
        self.__dict__['statusAddress'] = 0

    def __getattr__(self, name):
        if name == 'cmdId':
            return self.__dict__['cmdId']
        if name == 'statusAddress':
            return self.__dict__['statusAddress']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'cmdId':
            self.__dict__['cmdId'] = value
        elif name == 'statusAddress':
            self.__dict__['statusAddress'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_COMMON_CMD_ID, self.__dict__['cmdId'])
        submsg.AddU32(MSG_KEY_PARAMS_COMMON_STATUS_ADDRESS, self.__dict__['statusAddress'])
        mmsg.AddMessage(MSG_KEY_PARAMS_COMMON, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_COMMON, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['cmdId'] = submsg.FindU32(MSG_KEY_PARAMS_COMMON_CMD_ID)
        self.__dict__['statusAddress'] = submsg.FindU32(MSG_KEY_PARAMS_COMMON_STATUS_ADDRESS)


class ParamsStandard:

    def __init__(self):
        self.__dict__['socketType'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['maxRecvSize'] = 0

    def __getattr__(self, name):
        if name == 'socketType':
            return self.__dict__['socketType']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'maxRecvSize':
            return self.__dict__['maxRecvSize']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'socketType':
            self.__dict__['socketType'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'maxRecvSize':
            self.__dict__['maxRecvSize'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_STANDARD_SOCKET_TYPE, self.__dict__['socketType'])
        submsg.AddU16(MSG_KEY_PARAMS_STANDARD_FLAGS, self.__dict__['flags'])
        submsg.AddU16(MSG_KEY_PARAMS_STANDARD_MAX_RECV_SIZE, self.__dict__['maxRecvSize'])
        mmsg.AddMessage(MSG_KEY_PARAMS_STANDARD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_STANDARD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['socketType'] = submsg.FindU8(MSG_KEY_PARAMS_STANDARD_SOCKET_TYPE)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_PARAMS_STANDARD_FLAGS)
        self.__dict__['maxRecvSize'] = submsg.FindU16(MSG_KEY_PARAMS_STANDARD_MAX_RECV_SIZE)


class ParamsListen:

    def __init__(self):
        self.__dict__['common'] = ParamsCommon()
        self.__dict__['standard'] = ParamsStandard()
        self.__dict__['connectAddress'] = 0
        self.__dict__['connectSocketType'] = 0
        self.__dict__['listenPort'] = 0
        self.__dict__['maxConnections'] = 0
        self.__dict__['targetDstPort'] = 0
        self.__dict__['targetSrcPort'] = 0
        self.__dict__['listenBindAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['targetAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['targetSrcAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['limitAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['limitMask'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['enablePortSharing'] = False
        self.__dict__['clientSrcPort'] = 0
        self.__dict__['clientSrcAddr'] = mcl.object.IpAddr.IpAddr()

    def __getattr__(self, name):
        if name == 'common':
            return self.__dict__['common']
        if name == 'standard':
            return self.__dict__['standard']
        if name == 'connectAddress':
            return self.__dict__['connectAddress']
        if name == 'connectSocketType':
            return self.__dict__['connectSocketType']
        if name == 'listenPort':
            return self.__dict__['listenPort']
        if name == 'maxConnections':
            return self.__dict__['maxConnections']
        if name == 'targetDstPort':
            return self.__dict__['targetDstPort']
        if name == 'targetSrcPort':
            return self.__dict__['targetSrcPort']
        if name == 'listenBindAddr':
            return self.__dict__['listenBindAddr']
        if name == 'targetAddr':
            return self.__dict__['targetAddr']
        if name == 'targetSrcAddr':
            return self.__dict__['targetSrcAddr']
        if name == 'limitAddr':
            return self.__dict__['limitAddr']
        if name == 'limitMask':
            return self.__dict__['limitMask']
        if name == 'enablePortSharing':
            return self.__dict__['enablePortSharing']
        if name == 'clientSrcPort':
            return self.__dict__['clientSrcPort']
        if name == 'clientSrcAddr':
            return self.__dict__['clientSrcAddr']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'common':
            self.__dict__['common'] = value
        elif name == 'standard':
            self.__dict__['standard'] = value
        elif name == 'connectAddress':
            self.__dict__['connectAddress'] = value
        elif name == 'connectSocketType':
            self.__dict__['connectSocketType'] = value
        elif name == 'listenPort':
            self.__dict__['listenPort'] = value
        elif name == 'maxConnections':
            self.__dict__['maxConnections'] = value
        elif name == 'targetDstPort':
            self.__dict__['targetDstPort'] = value
        elif name == 'targetSrcPort':
            self.__dict__['targetSrcPort'] = value
        elif name == 'listenBindAddr':
            self.__dict__['listenBindAddr'] = value
        elif name == 'targetAddr':
            self.__dict__['targetAddr'] = value
        elif name == 'targetSrcAddr':
            self.__dict__['targetSrcAddr'] = value
        elif name == 'limitAddr':
            self.__dict__['limitAddr'] = value
        elif name == 'limitMask':
            self.__dict__['limitMask'] = value
        elif name == 'enablePortSharing':
            self.__dict__['enablePortSharing'] = value
        elif name == 'clientSrcPort':
            self.__dict__['clientSrcPort'] = value
        elif name == 'clientSrcAddr':
            self.__dict__['clientSrcAddr'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg2 = MarshalMessage()
        self.__dict__['common'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_PARAMS_LISTEN_COMMON, submsg2)
        submsg2 = MarshalMessage()
        self.__dict__['standard'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_PARAMS_LISTEN_STANDARD, submsg2)
        submsg.AddU32(MSG_KEY_PARAMS_LISTEN_CONNECT_ADDRESS, self.__dict__['connectAddress'])
        submsg.AddU8(MSG_KEY_PARAMS_LISTEN_CONNECT_SOCKET_TYPE, self.__dict__['connectSocketType'])
        submsg.AddU16(MSG_KEY_PARAMS_LISTEN_LISTEN_PORT, self.__dict__['listenPort'])
        submsg.AddU16(MSG_KEY_PARAMS_LISTEN_MAX_CONNECTIONS, self.__dict__['maxConnections'])
        submsg.AddU16(MSG_KEY_PARAMS_LISTEN_TARGET_DST_PORT, self.__dict__['targetDstPort'])
        submsg.AddU16(MSG_KEY_PARAMS_LISTEN_TARGET_SRC_PORT, self.__dict__['targetSrcPort'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_LISTEN_LISTEN_BIND_ADDR, self.__dict__['listenBindAddr'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_LISTEN_TARGET_ADDR, self.__dict__['targetAddr'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_LISTEN_TARGET_SRC_ADDR, self.__dict__['targetSrcAddr'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_LISTEN_LIMIT_ADDR, self.__dict__['limitAddr'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_LISTEN_LIMIT_MASK, self.__dict__['limitMask'])
        submsg.AddBool(MSG_KEY_PARAMS_LISTEN_ENABLE_PORT_SHARING, self.__dict__['enablePortSharing'])
        submsg.AddU16(MSG_KEY_PARAMS_LISTEN_CLIENT_SRC_PORT, self.__dict__['clientSrcPort'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_LISTEN_CLIENT_SRC_ADDR, self.__dict__['clientSrcAddr'])
        mmsg.AddMessage(MSG_KEY_PARAMS_LISTEN, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_LISTEN, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        submsg2 = submsg.FindMessage(MSG_KEY_PARAMS_LISTEN_COMMON)
        self.__dict__['common'].Demarshal(submsg2)
        submsg2 = submsg.FindMessage(MSG_KEY_PARAMS_LISTEN_STANDARD)
        self.__dict__['standard'].Demarshal(submsg2)
        self.__dict__['connectAddress'] = submsg.FindU32(MSG_KEY_PARAMS_LISTEN_CONNECT_ADDRESS)
        self.__dict__['connectSocketType'] = submsg.FindU8(MSG_KEY_PARAMS_LISTEN_CONNECT_SOCKET_TYPE)
        self.__dict__['listenPort'] = submsg.FindU16(MSG_KEY_PARAMS_LISTEN_LISTEN_PORT)
        self.__dict__['maxConnections'] = submsg.FindU16(MSG_KEY_PARAMS_LISTEN_MAX_CONNECTIONS)
        self.__dict__['targetDstPort'] = submsg.FindU16(MSG_KEY_PARAMS_LISTEN_TARGET_DST_PORT)
        self.__dict__['targetSrcPort'] = submsg.FindU16(MSG_KEY_PARAMS_LISTEN_TARGET_SRC_PORT)
        self.__dict__['listenBindAddr'] = submsg.FindIpAddr(MSG_KEY_PARAMS_LISTEN_LISTEN_BIND_ADDR)
        self.__dict__['targetAddr'] = submsg.FindIpAddr(MSG_KEY_PARAMS_LISTEN_TARGET_ADDR)
        self.__dict__['targetSrcAddr'] = submsg.FindIpAddr(MSG_KEY_PARAMS_LISTEN_TARGET_SRC_ADDR)
        self.__dict__['limitAddr'] = submsg.FindIpAddr(MSG_KEY_PARAMS_LISTEN_LIMIT_ADDR)
        self.__dict__['limitMask'] = submsg.FindIpAddr(MSG_KEY_PARAMS_LISTEN_LIMIT_MASK)
        self.__dict__['enablePortSharing'] = submsg.FindBool(MSG_KEY_PARAMS_LISTEN_ENABLE_PORT_SHARING)
        self.__dict__['clientSrcPort'] = submsg.FindU16(MSG_KEY_PARAMS_LISTEN_CLIENT_SRC_PORT)
        self.__dict__['clientSrcAddr'] = submsg.FindIpAddr(MSG_KEY_PARAMS_LISTEN_CLIENT_SRC_ADDR)


class ParamsConnect:

    def __init__(self):
        self.__dict__['common'] = ParamsCommon()
        self.__dict__['standard'] = ParamsStandard()
        self.__dict__['socketIndex'] = 4294967295L
        self.__dict__['dstPort'] = 0
        self.__dict__['srcPort'] = 0
        self.__dict__['targetAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['targetSrcAddr'] = mcl.object.IpAddr.IpAddr()

    def __getattr__(self, name):
        if name == 'common':
            return self.__dict__['common']
        if name == 'standard':
            return self.__dict__['standard']
        if name == 'socketIndex':
            return self.__dict__['socketIndex']
        if name == 'dstPort':
            return self.__dict__['dstPort']
        if name == 'srcPort':
            return self.__dict__['srcPort']
        if name == 'targetAddr':
            return self.__dict__['targetAddr']
        if name == 'targetSrcAddr':
            return self.__dict__['targetSrcAddr']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'common':
            self.__dict__['common'] = value
        elif name == 'standard':
            self.__dict__['standard'] = value
        elif name == 'socketIndex':
            self.__dict__['socketIndex'] = value
        elif name == 'dstPort':
            self.__dict__['dstPort'] = value
        elif name == 'srcPort':
            self.__dict__['srcPort'] = value
        elif name == 'targetAddr':
            self.__dict__['targetAddr'] = value
        elif name == 'targetSrcAddr':
            self.__dict__['targetSrcAddr'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg2 = MarshalMessage()
        self.__dict__['common'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_PARAMS_CONNECT_COMMON, submsg2)
        submsg2 = MarshalMessage()
        self.__dict__['standard'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_PARAMS_CONNECT_STANDARD, submsg2)
        submsg.AddU32(MSG_KEY_PARAMS_CONNECT_SOCKET_INDEX, self.__dict__['socketIndex'])
        submsg.AddU16(MSG_KEY_PARAMS_CONNECT_DST_PORT, self.__dict__['dstPort'])
        submsg.AddU16(MSG_KEY_PARAMS_CONNECT_SRC_PORT, self.__dict__['srcPort'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_CONNECT_TARGET_ADDR, self.__dict__['targetAddr'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_CONNECT_TARGET_SRC_ADDR, self.__dict__['targetSrcAddr'])
        mmsg.AddMessage(MSG_KEY_PARAMS_CONNECT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_CONNECT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        submsg2 = submsg.FindMessage(MSG_KEY_PARAMS_CONNECT_COMMON)
        self.__dict__['common'].Demarshal(submsg2)
        submsg2 = submsg.FindMessage(MSG_KEY_PARAMS_CONNECT_STANDARD)
        self.__dict__['standard'].Demarshal(submsg2)
        self.__dict__['socketIndex'] = submsg.FindU32(MSG_KEY_PARAMS_CONNECT_SOCKET_INDEX)
        self.__dict__['dstPort'] = submsg.FindU16(MSG_KEY_PARAMS_CONNECT_DST_PORT)
        self.__dict__['srcPort'] = submsg.FindU16(MSG_KEY_PARAMS_CONNECT_SRC_PORT)
        self.__dict__['targetAddr'] = submsg.FindIpAddr(MSG_KEY_PARAMS_CONNECT_TARGET_ADDR)
        self.__dict__['targetSrcAddr'] = submsg.FindIpAddr(MSG_KEY_PARAMS_CONNECT_TARGET_SRC_ADDR)