# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class Params:

    def __init__(self):
        self.__dict__['action'] = 0
        self.__dict__['hive'] = 0
        self.__dict__['key'] = ''
        self.__dict__['file'] = ''
        self.__dict__['permanent'] = False
        self.__dict__['target'] = ''
        self.__dict__['provider'] = 0

    def __getattr__(self, name):
        if name == 'action':
            return self.__dict__['action']
        if name == 'hive':
            return self.__dict__['hive']
        if name == 'key':
            return self.__dict__['key']
        if name == 'file':
            return self.__dict__['file']
        if name == 'permanent':
            return self.__dict__['permanent']
        if name == 'target':
            return self.__dict__['target']
        if name == 'provider':
            return self.__dict__['provider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'action':
            self.__dict__['action'] = value
        elif name == 'hive':
            self.__dict__['hive'] = value
        elif name == 'key':
            self.__dict__['key'] = value
        elif name == 'file':
            self.__dict__['file'] = value
        elif name == 'permanent':
            self.__dict__['permanent'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        elif name == 'provider':
            self.__dict__['provider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_ACTION, self.__dict__['action'])
        submsg.AddU8(MSG_KEY_PARAMS_HIVE, self.__dict__['hive'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_KEY, self.__dict__['key'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_FILE, self.__dict__['file'])
        submsg.AddBool(MSG_KEY_PARAMS_PERMANENT, self.__dict__['permanent'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_TARGET, self.__dict__['target'])
        submsg.AddU32(MSG_KEY_PARAMS_PROVIDER, self.__dict__['provider'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['action'] = submsg.FindU8(MSG_KEY_PARAMS_ACTION)
        self.__dict__['hive'] = submsg.FindU8(MSG_KEY_PARAMS_HIVE)
        self.__dict__['key'] = submsg.FindString(MSG_KEY_PARAMS_KEY)
        self.__dict__['file'] = submsg.FindString(MSG_KEY_PARAMS_FILE)
        self.__dict__['permanent'] = submsg.FindBool(MSG_KEY_PARAMS_PERMANENT)
        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_TARGET)
        except:
            pass

        try:
            self.__dict__['provider'] = submsg.FindU32(MSG_KEY_PARAMS_PROVIDER)
        except:
            pass