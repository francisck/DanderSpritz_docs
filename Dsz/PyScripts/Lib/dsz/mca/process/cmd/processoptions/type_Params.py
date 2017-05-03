# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_ACTION_QUERY = 1
PARAMS_ACTION_SET = 2

class Params:

    def __init__(self):
        self.__dict__['action'] = 0
        self.__dict__['elevate'] = False
        self.__dict__['processId'] = 0
        self.__dict__['setValue'] = 0

    def __getattr__(self, name):
        if name == 'action':
            return self.__dict__['action']
        if name == 'elevate':
            return self.__dict__['elevate']
        if name == 'processId':
            return self.__dict__['processId']
        if name == 'setValue':
            return self.__dict__['setValue']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'action':
            self.__dict__['action'] = value
        elif name == 'elevate':
            self.__dict__['elevate'] = value
        elif name == 'processId':
            self.__dict__['processId'] = value
        elif name == 'setValue':
            self.__dict__['setValue'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_ACTION, self.__dict__['action'])
        submsg.AddBool(MSG_KEY_PARAMS_ELEVATE, self.__dict__['elevate'])
        submsg.AddU32(MSG_KEY_PARAMS_PROCESS_ID, self.__dict__['processId'])
        submsg.AddU32(MSG_KEY_PARAMS_SET_VALUE, self.__dict__['setValue'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['action'] = submsg.FindU8(MSG_KEY_PARAMS_ACTION)
        self.__dict__['elevate'] = submsg.FindBool(MSG_KEY_PARAMS_ELEVATE)
        self.__dict__['processId'] = submsg.FindU32(MSG_KEY_PARAMS_PROCESS_ID)
        self.__dict__['setValue'] = submsg.FindU32(MSG_KEY_PARAMS_SET_VALUE)