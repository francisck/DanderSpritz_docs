# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime
import array
RESULT_CACHE_DATATYPE_UNKNOWN = 0

class ResultCache:

    def __init__(self):
        self.__dict__['ttl'] = mcl.object.MclTime.MclTime()
        self.__dict__['dataType'] = RESULT_CACHE_DATATYPE_UNKNOWN
        self.__dict__['data'] = ''
        self.__dict__['name'] = ''
        self.__dict__['entryName'] = ''

    def __getattr__(self, name):
        if name == 'ttl':
            return self.__dict__['ttl']
        if name == 'dataType':
            return self.__dict__['dataType']
        if name == 'data':
            return self.__dict__['data']
        if name == 'name':
            return self.__dict__['name']
        if name == 'entryName':
            return self.__dict__['entryName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'ttl':
            self.__dict__['ttl'] = value
        elif name == 'dataType':
            self.__dict__['dataType'] = value
        elif name == 'data':
            self.__dict__['data'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'entryName':
            self.__dict__['entryName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddTime(MSG_KEY_RESULT_CACHE_TTL, self.__dict__['ttl'])
        submsg.AddU32(MSG_KEY_RESULT_CACHE_DATA_TYPE, self.__dict__['dataType'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_CACHE_DATA, self.__dict__['data'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_CACHE_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_CACHE_ENTRY_NAME, self.__dict__['entryName'])
        mmsg.AddMessage(MSG_KEY_RESULT_CACHE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_CACHE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['ttl'] = submsg.FindTime(MSG_KEY_RESULT_CACHE_TTL)
        self.__dict__['dataType'] = submsg.FindU32(MSG_KEY_RESULT_CACHE_DATA_TYPE)
        self.__dict__['data'] = submsg.FindString(MSG_KEY_RESULT_CACHE_DATA)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_CACHE_NAME)
        self.__dict__['entryName'] = submsg.FindString(MSG_KEY_RESULT_CACHE_ENTRY_NAME)


class ResultDns:

    def __init__(self):
        self.__dict__['rawData'] = array.array('B')

    def __getattr__(self, name):
        if name == 'rawData':
            return self.__dict__['rawData']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'rawData':
            self.__dict__['rawData'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddData(MSG_KEY_RESULT_DNS_RAW_DATA, self.__dict__['rawData'])
        mmsg.AddMessage(MSG_KEY_RESULT_DNS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_DNS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['rawData'] = submsg.FindData(MSG_KEY_RESULT_DNS_RAW_DATA)