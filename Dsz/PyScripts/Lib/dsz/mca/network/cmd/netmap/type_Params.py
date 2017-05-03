# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_FLAG_GET_OS_INFO = 1
PARAMS_FLAG_GET_TIME = 2

class Params:

    def __init__(self):
        self.__dict__['scope'] = NETMAP_SCOPE_ALL
        self.__dict__['flags'] = 0

    def __getattr__(self, name):
        if name == 'scope':
            return self.__dict__['scope']
        if name == 'flags':
            return self.__dict__['flags']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'scope':
            self.__dict__['scope'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_SCOPE, self.__dict__['scope'])
        submsg.AddU32(MSG_KEY_PARAMS_FLAGS, self.__dict__['flags'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['scope'] = submsg.FindU8(MSG_KEY_PARAMS_SCOPE)
        except:
            pass

        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_PARAMS_FLAGS)