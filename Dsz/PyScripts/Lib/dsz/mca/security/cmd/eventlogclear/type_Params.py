# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_FLAG_USE_CLASSIC_LOG = 1

class Params:

    def __init__(self):
        self.__dict__['log'] = ''
        self.__dict__['target'] = ''
        self.__dict__['flags'] = 0

    def __getattr__(self, name):
        if name == 'log':
            return self.__dict__['log']
        if name == 'target':
            return self.__dict__['target']
        if name == 'flags':
            return self.__dict__['flags']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'log':
            self.__dict__['log'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_LOG, self.__dict__['log'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_TARGET, self.__dict__['target'])
        submsg.AddU32(MSG_KEY_PARAMS_FLAGS, self.__dict__['flags'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['log'] = submsg.FindString(MSG_KEY_PARAMS_LOG)
        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_TARGET)
        except:
            pass

        try:
            self.__dict__['flags'] = submsg.FindU32(MSG_KEY_PARAMS_FLAGS)
        except:
            pass