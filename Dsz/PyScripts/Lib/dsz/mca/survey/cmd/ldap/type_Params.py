# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import array
PARAMS_MAX_SEARCH_ATTRIBUTES = 30

class Params:

    def __init__(self):
        self.__dict__['port'] = 389
        self.__dict__['scope'] = 0
        self.__dict__['chunkSize'] = 65536
        self.__dict__['hostName'] = ''
        self.__dict__['filter'] = 'objectClass=*'
        self.__dict__['attributes'] = list()
        i = 0
        while i < PARAMS_MAX_SEARCH_ATTRIBUTES:
            self.__dict__['attributes'].append('')
            i = i + 1

    def __getattr__(self, name):
        if name == 'port':
            return self.__dict__['port']
        if name == 'scope':
            return self.__dict__['scope']
        if name == 'chunkSize':
            return self.__dict__['chunkSize']
        if name == 'hostName':
            return self.__dict__['hostName']
        if name == 'filter':
            return self.__dict__['filter']
        if name == 'attributes':
            return self.__dict__['attributes']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'port':
            self.__dict__['port'] = value
        elif name == 'scope':
            self.__dict__['scope'] = value
        elif name == 'chunkSize':
            self.__dict__['chunkSize'] = value
        elif name == 'hostName':
            self.__dict__['hostName'] = value
        elif name == 'filter':
            self.__dict__['filter'] = value
        elif name == 'attributes':
            self.__dict__['attributes'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_PARAMS_PORT, self.__dict__['port'])
        submsg.AddU16(MSG_KEY_PARAMS_SCOPE, self.__dict__['scope'])
        submsg.AddU32(MSG_KEY_PARAMS_CHUNK_SIZE, self.__dict__['chunkSize'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_HOST_NAME, self.__dict__['hostName'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_FILTER, self.__dict__['filter'])
        i = 0
        while i < PARAMS_MAX_SEARCH_ATTRIBUTES:
            submsg.AddStringUtf8(MSG_KEY_PARAMS_ATTRIBUTES, self.__dict__['attributes'][i])
            i = i + 1

        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['port'] = submsg.FindU16(MSG_KEY_PARAMS_PORT)
        except:
            pass

        try:
            self.__dict__['scope'] = submsg.FindU16(MSG_KEY_PARAMS_SCOPE)
        except:
            pass

        try:
            self.__dict__['chunkSize'] = submsg.FindU32(MSG_KEY_PARAMS_CHUNK_SIZE)
        except:
            pass

        self.__dict__['hostName'] = submsg.FindString(MSG_KEY_PARAMS_HOST_NAME)
        try:
            self.__dict__['filter'] = submsg.FindString(MSG_KEY_PARAMS_FILTER)
        except:
            pass

        try:
            i = 0
            while i < PARAMS_MAX_SEARCH_ATTRIBUTES:
                self.__dict__['attributes'][i] = submsg.FindString(MSG_KEY_PARAMS_ATTRIBUTES)
                i = i + 1

        except:
            pass