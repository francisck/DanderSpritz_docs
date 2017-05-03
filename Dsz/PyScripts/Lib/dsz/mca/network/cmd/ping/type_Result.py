# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime
import mcl.object.IpAddr
import array
REPLY_TYPE_UNKNOWN = 0
REPLY_TYPE_REPLY = 1
REPLY_TYPE_DEST_UNREACH = 2

class Result:

    def __init__(self):
        self.__dict__['type'] = REPLY_TYPE_UNKNOWN
        self.__dict__['ttl'] = 0
        self.__dict__['time'] = mcl.object.MclTime.MclTime()
        self.__dict__['fromAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['toAddr'] = mcl.object.IpAddr.IpAddr()
        self.__dict__['rawData'] = array.array('B')

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'ttl':
            return self.__dict__['ttl']
        if name == 'time':
            return self.__dict__['time']
        if name == 'fromAddr':
            return self.__dict__['fromAddr']
        if name == 'toAddr':
            return self.__dict__['toAddr']
        if name == 'rawData':
            return self.__dict__['rawData']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'ttl':
            self.__dict__['ttl'] = value
        elif name == 'time':
            self.__dict__['time'] = value
        elif name == 'fromAddr':
            self.__dict__['fromAddr'] = value
        elif name == 'toAddr':
            self.__dict__['toAddr'] = value
        elif name == 'rawData':
            self.__dict__['rawData'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_TYPE, self.__dict__['type'])
        submsg.AddU8(MSG_KEY_RESULT_TTL, self.__dict__['ttl'])
        submsg.AddTime(MSG_KEY_RESULT_TIME, self.__dict__['time'])
        submsg.AddIpAddr(MSG_KEY_RESULT_FROM_ADDRESS, self.__dict__['fromAddr'])
        submsg.AddIpAddr(MSG_KEY_RESULT_TO_ADDRESS, self.__dict__['toAddr'])
        submsg.AddData(MSG_KEY_RESULT_RAW_DATA, self.__dict__['rawData'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_TYPE)
        self.__dict__['ttl'] = submsg.FindU8(MSG_KEY_RESULT_TTL)
        self.__dict__['time'] = submsg.FindTime(MSG_KEY_RESULT_TIME)
        self.__dict__['fromAddr'] = submsg.FindIpAddr(MSG_KEY_RESULT_FROM_ADDRESS)
        self.__dict__['toAddr'] = submsg.FindIpAddr(MSG_KEY_RESULT_TO_ADDRESS)
        self.__dict__['rawData'] = submsg.FindData(MSG_KEY_RESULT_RAW_DATA)