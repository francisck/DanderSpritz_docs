# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_GROUP_TYPE_NONE = 0
PARAMS_GROUP_TYPE_LOCAL = 1
PARAMS_GROUP_TYPE_NETWORK = 2

class Params:

    def __init__(self):
        self.__dict__['groupType'] = PARAMS_GROUP_TYPE_NONE
        self.__dict__['target'] = ''
        self.__dict__['group'] = ''

    def __getattr__(self, name):
        if name == 'groupType':
            return self.__dict__['groupType']
        if name == 'target':
            return self.__dict__['target']
        if name == 'group':
            return self.__dict__['group']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'groupType':
            self.__dict__['groupType'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        elif name == 'group':
            self.__dict__['group'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_GROUP_TYPE, self.__dict__['groupType'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_TARGET, self.__dict__['target'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_GROUP, self.__dict__['group'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['groupType'] = submsg.FindU8(MSG_KEY_PARAMS_GROUP_TYPE)
        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_TARGET)
        except:
            pass

        try:
            self.__dict__['group'] = submsg.FindString(MSG_KEY_PARAMS_GROUP)
        except:
            pass