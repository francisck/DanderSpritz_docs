# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class ResultList:

    def __init__(self):
        self.__dict__['id'] = 0
        self.__dict__['name'] = ''
        self.__dict__['user'] = ''

    def __getattr__(self, name):
        if name == 'id':
            return self.__dict__['id']
        if name == 'name':
            return self.__dict__['name']
        if name == 'user':
            return self.__dict__['user']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'id':
            self.__dict__['id'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'user':
            self.__dict__['user'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_LIST_PROCESS_ID, self.__dict__['id'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_LIST_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_LIST_USER, self.__dict__['user'])
        mmsg.AddMessage(MSG_KEY_RESULT_LIST, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_LIST, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_LIST_PROCESS_ID)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_LIST_NAME)
        self.__dict__['user'] = submsg.FindString(MSG_KEY_RESULT_LIST_USER)


class ResultSteal:

    def __init__(self):
        self.__dict__['hUser'] = 0
        self.__dict__['id'] = 0

    def __getattr__(self, name):
        if name == 'hUser':
            return self.__dict__['hUser']
        if name == 'id':
            return self.__dict__['id']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'hUser':
            self.__dict__['hUser'] = value
        elif name == 'id':
            self.__dict__['id'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_STEAL_HUSER, self.__dict__['hUser'])
        submsg.AddU32(MSG_KEY_RESULT_STEAL_ID, self.__dict__['id'])
        mmsg.AddMessage(MSG_KEY_RESULT_STEAL, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_STEAL, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['hUser'] = submsg.FindU64(MSG_KEY_RESULT_STEAL_HUSER)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_STEAL_ID)