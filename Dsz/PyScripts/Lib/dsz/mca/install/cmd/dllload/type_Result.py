# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class ResultLoad:

    def __init__(self):
        self.__dict__['loadAddress'] = 0

    def __getattr__(self, name):
        if name == 'loadAddress':
            return self.__dict__['loadAddress']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'loadAddress':
            self.__dict__['loadAddress'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_LOAD_LOAD_ADDRESS, self.__dict__['loadAddress'])
        mmsg.AddMessage(MSG_KEY_RESULT_LOAD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_LOAD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['loadAddress'] = submsg.FindU64(MSG_KEY_RESULT_LOAD_LOAD_ADDRESS)


class ResultUnload:

    def __init__(self):
        self.__dict__['unloaded'] = False

    def __getattr__(self, name):
        if name == 'unloaded':
            return self.__dict__['unloaded']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'unloaded':
            self.__dict__['unloaded'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_UNLOAD_UNLOADED, self.__dict__['unloaded'])
        mmsg.AddMessage(MSG_KEY_RESULT_UNLOAD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_UNLOAD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['unloaded'] = submsg.FindBool(MSG_KEY_RESULT_UNLOAD_UNLOADED)


class ResultInjected:

    def __init__(self):
        self.__dict__['pid'] = 0
        self.__dict__['loadAddress'] = 0
        self.__dict__['unloaded'] = False

    def __getattr__(self, name):
        if name == 'pid':
            return self.__dict__['pid']
        if name == 'loadAddress':
            return self.__dict__['loadAddress']
        if name == 'unloaded':
            return self.__dict__['unloaded']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'pid':
            self.__dict__['pid'] = value
        elif name == 'loadAddress':
            self.__dict__['loadAddress'] = value
        elif name == 'unloaded':
            self.__dict__['unloaded'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_INJECTED_PROCESS_ID, self.__dict__['pid'])
        submsg.AddU64(MSG_KEY_RESULT_INJECTED_LOAD_ADDRESS, self.__dict__['loadAddress'])
        submsg.AddBool(MSG_KEY_RESULT_INJECTED_UNLOADED, self.__dict__['unloaded'])
        mmsg.AddMessage(MSG_KEY_RESULT_INJECTED, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_INJECTED, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['pid'] = submsg.FindU32(MSG_KEY_RESULT_INJECTED_PROCESS_ID)
        self.__dict__['loadAddress'] = submsg.FindU64(MSG_KEY_RESULT_INJECTED_LOAD_ADDRESS)
        self.__dict__['unloaded'] = submsg.FindBool(MSG_KEY_RESULT_INJECTED_UNLOADED)