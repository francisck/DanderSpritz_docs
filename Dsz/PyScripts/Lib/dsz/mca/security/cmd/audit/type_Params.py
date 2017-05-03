# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class ParamsModify:

    def __init__(self):
        self.__dict__['type'] = 0
        self.__dict__['force'] = False
        self.__dict__['provider'] = 0

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'force':
            return self.__dict__['force']
        if name == 'provider':
            return self.__dict__['provider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'force':
            self.__dict__['force'] = value
        elif name == 'provider':
            self.__dict__['provider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_MODIFY_TYPE, self.__dict__['type'])
        submsg.AddBool(MSG_KEY_PARAMS_MODIFY_FORCE, self.__dict__['force'])
        submsg.AddU32(MSG_KEY_PARAMS_MODIFY_PROVIDER, self.__dict__['provider'])
        mmsg.AddMessage(MSG_KEY_PARAMS_MODIFY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_MODIFY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_PARAMS_MODIFY_TYPE)
        self.__dict__['force'] = submsg.FindBool(MSG_KEY_PARAMS_MODIFY_FORCE)
        try:
            self.__dict__['provider'] = submsg.FindU32(MSG_KEY_PARAMS_MODIFY_PROVIDER)
        except:
            pass