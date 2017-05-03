# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import mcl.object.MclTime
PARAMS_FLAG_RECURSIVE = 1
PARAMS_FLAG_GET_VALUE = 2
PARAMS_FLAG_USE_WOW64_64 = 4
PARAMS_FLAG_USE_WOW64_32 = 8

class Params:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['hive'] = 0
        self.__dict__['chunksize'] = 65536
        self.__dict__['key'] = ''
        self.__dict__['value'] = ''
        self.__dict__['after'] = mcl.object.MclTime.MclTime()
        self.__dict__['before'] = mcl.object.MclTime.MclTime()
        self.__dict__['target'] = ''
        self.__dict__['provider'] = 0

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'hive':
            return self.__dict__['hive']
        if name == 'chunksize':
            return self.__dict__['chunksize']
        if name == 'key':
            return self.__dict__['key']
        if name == 'value':
            return self.__dict__['value']
        if name == 'after':
            return self.__dict__['after']
        if name == 'before':
            return self.__dict__['before']
        if name == 'target':
            return self.__dict__['target']
        if name == 'provider':
            return self.__dict__['provider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'hive':
            self.__dict__['hive'] = value
        elif name == 'chunksize':
            self.__dict__['chunksize'] = value
        elif name == 'key':
            self.__dict__['key'] = value
        elif name == 'value':
            self.__dict__['value'] = value
        elif name == 'after':
            self.__dict__['after'] = value
        elif name == 'before':
            self.__dict__['before'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        elif name == 'provider':
            self.__dict__['provider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_PARAMS_FLAGS, self.__dict__['flags'])
        submsg.AddU8(MSG_KEY_PARAMS_HIVE, self.__dict__['hive'])
        submsg.AddU32(MSG_KEY_PARAMS_CHUNKSIZE, self.__dict__['chunksize'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_KEY, self.__dict__['key'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_VALUE, self.__dict__['value'])
        submsg.AddTime(MSG_KEY_PARAMS_AFTER, self.__dict__['after'])
        submsg.AddTime(MSG_KEY_PARAMS_BEFORE, self.__dict__['before'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_TARGET, self.__dict__['target'])
        submsg.AddU32(MSG_KEY_PARAMS_PROVIDER, self.__dict__['provider'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_PARAMS_FLAGS)
        self.__dict__['hive'] = submsg.FindU8(MSG_KEY_PARAMS_HIVE)
        try:
            self.__dict__['chunksize'] = submsg.FindU32(MSG_KEY_PARAMS_CHUNKSIZE)
        except:
            pass

        self.__dict__['key'] = submsg.FindString(MSG_KEY_PARAMS_KEY)
        self.__dict__['value'] = submsg.FindString(MSG_KEY_PARAMS_VALUE)
        try:
            self.__dict__['after'] = submsg.FindTime(MSG_KEY_PARAMS_AFTER)
        except:
            pass

        try:
            self.__dict__['before'] = submsg.FindTime(MSG_KEY_PARAMS_BEFORE)
        except:
            pass

        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_TARGET)
        except:
            pass

        try:
            self.__dict__['provider'] = submsg.FindU32(MSG_KEY_PARAMS_PROVIDER)
        except:
            pass