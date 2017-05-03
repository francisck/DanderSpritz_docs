# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_TYPE_USER = 0
PARAMS_TYPE_GROUP = 1

class Params:

    def __init__(self):
        self.__dict__['type'] = PARAMS_TYPE_USER
        self.__dict__['id'] = 0
        self.__dict__['local'] = False
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'id':
            return self.__dict__['id']
        if name == 'local':
            return self.__dict__['local']
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'id':
            self.__dict__['id'] = value
        elif name == 'local':
            self.__dict__['local'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_PARAMS_ID, self.__dict__['id'])
        submsg.AddBool(MSG_KEY_PARAMS_LOCAL, self.__dict__['local'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_PARAMS_TYPE)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_PARAMS_ID)
        self.__dict__['local'] = submsg.FindBool(MSG_KEY_PARAMS_LOCAL)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_PARAMS_NAME)