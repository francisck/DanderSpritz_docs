# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class Params:

    def __init__(self):
        self.__dict__['user'] = ''
        self.__dict__['memoryProvider'] = 0
        self.__dict__['threadProvider'] = 0

    def __getattr__(self, name):
        if name == 'user':
            return self.__dict__['user']
        if name == 'memoryProvider':
            return self.__dict__['memoryProvider']
        if name == 'threadProvider':
            return self.__dict__['threadProvider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'user':
            self.__dict__['user'] = value
        elif name == 'memoryProvider':
            self.__dict__['memoryProvider'] = value
        elif name == 'threadProvider':
            self.__dict__['threadProvider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_USER, self.__dict__['user'])
        submsg.AddU32(MSG_KEY_PARAMS_MEMORY_PROVIDER, self.__dict__['memoryProvider'])
        submsg.AddU32(MSG_KEY_PARAMS_THREAD_PROVIDER, self.__dict__['threadProvider'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['user'] = submsg.FindString(MSG_KEY_PARAMS_USER)
        try:
            self.__dict__['memoryProvider'] = submsg.FindU32(MSG_KEY_PARAMS_MEMORY_PROVIDER)
        except:
            pass

        try:
            self.__dict__['threadProvider'] = submsg.FindU32(MSG_KEY_PARAMS_THREAD_PROVIDER)
        except:
            pass