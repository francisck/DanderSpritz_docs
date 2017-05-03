# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.IpAddr
import array

class Result:

    def __init__(self):
        self.__dict__['socketType'] = 0
        self.__dict__['port'] = 0
        self.__dict__['rspAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['response'] = array.array('B')

    def __getattr__(self, name):
        if name == 'socketType':
            return self.__dict__['socketType']
        if name == 'port':
            return self.__dict__['port']
        if name == 'rspAddr':
            return self.__dict__['rspAddr']
        if name == 'response':
            return self.__dict__['response']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'socketType':
            self.__dict__['socketType'] = value
        elif name == 'port':
            self.__dict__['port'] = value
        elif name == 'rspAddr':
            self.__dict__['rspAddr'] = value
        elif name == 'response':
            self.__dict__['response'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_SOCKETTYPE, self.__dict__['socketType'])
        submsg.AddU16(MSG_KEY_RESULT_PORT, self.__dict__['port'])
        submsg.AddIpAddr(MSG_KEY_RESULT_RESPONSE_ADDRESS, self.__dict__['rspAddr'])
        submsg.AddData(MSG_KEY_RESULT_RESPONSE, self.__dict__['response'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['socketType'] = submsg.FindU8(MSG_KEY_RESULT_SOCKETTYPE)
        self.__dict__['port'] = submsg.FindU16(MSG_KEY_RESULT_PORT)
        self.__dict__['rspAddr'] = submsg.FindIpAddr(MSG_KEY_RESULT_RESPONSE_ADDRESS)
        self.__dict__['response'] = submsg.FindData(MSG_KEY_RESULT_RESPONSE)