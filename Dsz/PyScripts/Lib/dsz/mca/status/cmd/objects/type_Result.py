# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
RESULT_FLAG_DIR_START = 1

class Result:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['status'] = 0
        self.__dict__['name'] = ''
        self.__dict__['type'] = ''

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'status':
            return self.__dict__['status']
        if name == 'name':
            return self.__dict__['name']
        if name == 'type':
            return self.__dict__['type']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'status':
            self.__dict__['status'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_FLAGS, self.__dict__['flags'])
        submsg.AddU32(MSG_KEY_RESULT_STATUS, self.__dict__['status'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TYPE, self.__dict__['type'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_FLAGS)
        self.__dict__['status'] = submsg.FindU32(MSG_KEY_RESULT_STATUS)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_NAME)
        self.__dict__['type'] = submsg.FindString(MSG_KEY_RESULT_TYPE)