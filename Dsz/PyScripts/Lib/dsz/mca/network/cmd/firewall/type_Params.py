# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_DIRECTION_IN = 0
PARAMS_DIRECTION_OUT = 1

class Params:

    def __init__(self):
        self.__dict__['portNum'] = 0
        self.__dict__['protocol'] = 0
        self.__dict__['cleanup'] = True
        self.__dict__['direction'] = 0
        self.__dict__['name'] = ''
        self.__dict__['group'] = ''
        self.__dict__['provider'] = 0

    def __getattr__(self, name):
        if name == 'portNum':
            return self.__dict__['portNum']
        if name == 'protocol':
            return self.__dict__['protocol']
        if name == 'cleanup':
            return self.__dict__['cleanup']
        if name == 'direction':
            return self.__dict__['direction']
        if name == 'name':
            return self.__dict__['name']
        if name == 'group':
            return self.__dict__['group']
        if name == 'provider':
            return self.__dict__['provider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'portNum':
            self.__dict__['portNum'] = value
        elif name == 'protocol':
            self.__dict__['protocol'] = value
        elif name == 'cleanup':
            self.__dict__['cleanup'] = value
        elif name == 'direction':
            self.__dict__['direction'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'group':
            self.__dict__['group'] = value
        elif name == 'provider':
            self.__dict__['provider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_PARAMS_PORT, self.__dict__['portNum'])
        submsg.AddU8(MSG_KEY_PARAMS_PROTOCOL, self.__dict__['protocol'])
        submsg.AddBool(MSG_KEY_PARAMS_CLEANUP, self.__dict__['cleanup'])
        submsg.AddU8(MSG_KEY_PARAMS_DIRECTION, self.__dict__['direction'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_GROUP, self.__dict__['group'])
        submsg.AddU32(MSG_KEY_PARAMS_PROVIDER, self.__dict__['provider'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['portNum'] = submsg.FindU16(MSG_KEY_PARAMS_PORT)
        self.__dict__['protocol'] = submsg.FindU8(MSG_KEY_PARAMS_PROTOCOL)
        self.__dict__['cleanup'] = submsg.FindBool(MSG_KEY_PARAMS_CLEANUP)
        self.__dict__['direction'] = submsg.FindU8(MSG_KEY_PARAMS_DIRECTION)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_PARAMS_NAME)
        self.__dict__['group'] = submsg.FindString(MSG_KEY_PARAMS_GROUP)
        try:
            self.__dict__['provider'] = submsg.FindU32(MSG_KEY_PARAMS_PROVIDER)
        except:
            pass