# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_FLAG_NO_SIGNATURE = 1
PARAMS_FLAG_NO_VERSION = 2

class Params:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['name'] = ''
        self.__dict__['params'] = ''
        self.__dict__['provider'] = 0

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'name':
            return self.__dict__['name']
        if name == 'params':
            return self.__dict__['params']
        if name == 'provider':
            return self.__dict__['provider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'params':
            self.__dict__['params'] = value
        elif name == 'provider':
            self.__dict__['provider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_PARAMS, self.__dict__['params'])
        submsg.AddU32(MSG_KEY_PARAMS_PROVIDER, self.__dict__['provider'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_PARAMS_FLAGS)
        try:
            self.__dict__['name'] = submsg.FindString(MSG_KEY_PARAMS_NAME)
        except:
            pass

        try:
            self.__dict__['params'] = submsg.FindString(MSG_KEY_PARAMS_PARAMS)
        except:
            pass

        try:
            self.__dict__['provider'] = submsg.FindU32(MSG_KEY_PARAMS_PROVIDER)
        except:
            pass