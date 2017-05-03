# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import mcl.object.MclTime
import mcl.object.IpAddr
import array

class Params:

    def __init__(self):
        self.__dict__['socketType'] = 0
        self.__dict__['wait'] = mcl.object.MclTime.MclTime()
        self.__dict__['broadcast'] = False
        self.__dict__['dstPort'] = 0
        self.__dict__['srcPort'] = 0
        self.__dict__['targetAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['data'] = array.array('B')

    def __getattr__(self, name):
        if name == 'socketType':
            return self.__dict__['socketType']
        if name == 'wait':
            return self.__dict__['wait']
        if name == 'broadcast':
            return self.__dict__['broadcast']
        if name == 'dstPort':
            return self.__dict__['dstPort']
        if name == 'srcPort':
            return self.__dict__['srcPort']
        if name == 'targetAddr':
            return self.__dict__['targetAddr']
        if name == 'data':
            return self.__dict__['data']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'socketType':
            self.__dict__['socketType'] = value
        elif name == 'wait':
            self.__dict__['wait'] = value
        elif name == 'broadcast':
            self.__dict__['broadcast'] = value
        elif name == 'dstPort':
            self.__dict__['dstPort'] = value
        elif name == 'srcPort':
            self.__dict__['srcPort'] = value
        elif name == 'targetAddr':
            self.__dict__['targetAddr'] = value
        elif name == 'data':
            self.__dict__['data'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_SOCKETTYPE, self.__dict__['socketType'])
        submsg.AddTime(MSG_KEY_PARAMS_WAIT, self.__dict__['wait'])
        submsg.AddBool(MSG_KEY_PARAMS_BROADCAST, self.__dict__['broadcast'])
        submsg.AddU16(MSG_KEY_PARAMS_DST_PORT, self.__dict__['dstPort'])
        submsg.AddU16(MSG_KEY_PARAMS_SRC_PORT, self.__dict__['srcPort'])
        submsg.AddIpAddr(MSG_KEY_PARAMS_TARGET_ADDRESS, self.__dict__['targetAddr'])
        submsg.AddData(MSG_KEY_PARAMS_DATA, self.__dict__['data'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['socketType'] = submsg.FindU8(MSG_KEY_PARAMS_SOCKETTYPE)
        self.__dict__['wait'] = submsg.FindTime(MSG_KEY_PARAMS_WAIT)
        self.__dict__['broadcast'] = submsg.FindBool(MSG_KEY_PARAMS_BROADCAST)
        self.__dict__['dstPort'] = submsg.FindU16(MSG_KEY_PARAMS_DST_PORT)
        self.__dict__['srcPort'] = submsg.FindU16(MSG_KEY_PARAMS_SRC_PORT)
        self.__dict__['targetAddr'] = submsg.FindIpAddr(MSG_KEY_PARAMS_TARGET_ADDRESS)
        self.__dict__['data'] = submsg.FindData(MSG_KEY_PARAMS_DATA)