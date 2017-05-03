# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_SET_FLAG_PERMANENT = 1
PARAMS_SET_FLAG_GRANT = 2
PARAMS_SET_FLAG_SET = 4
PARAMS_SET_FLAG_DENY = 8
PARAMS_SET_FLAG_REVOKE = 16

class QueryParams:

    def __init__(self):
        self.__dict__['type'] = 0
        self.__dict__['objectType'] = 0
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'objectType':
            return self.__dict__['objectType']
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'objectType':
            self.__dict__['objectType'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_QUERY_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_PARAMS_QUERY_OBJECT_TYPE, self.__dict__['objectType'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_QUERY_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_PARAMS_QUERY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_QUERY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_PARAMS_QUERY_TYPE)
        self.__dict__['objectType'] = submsg.FindU32(MSG_KEY_PARAMS_QUERY_OBJECT_TYPE)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_PARAMS_QUERY_NAME)


class ModifyParams:

    def __init__(self):
        self.__dict__['type'] = 0
        self.__dict__['objectType'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['accessMask'] = 0
        self.__dict__['name'] = ''
        self.__dict__['sid'] = ''

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'objectType':
            return self.__dict__['objectType']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'accessMask':
            return self.__dict__['accessMask']
        if name == 'name':
            return self.__dict__['name']
        if name == 'sid':
            return self.__dict__['sid']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'objectType':
            self.__dict__['objectType'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'accessMask':
            self.__dict__['accessMask'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'sid':
            self.__dict__['sid'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_MODIFY_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_PARAMS_MODIFY_OBJECT_TYPE, self.__dict__['objectType'])
        submsg.AddU32(MSG_KEY_PARAMS_MODIFY_FLAGS, self.__dict__['flags'])
        submsg.AddU32(MSG_KEY_PARAMS_MODIFY_ACCESS_MASK, self.__dict__['accessMask'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_MODIFY_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_MODIFY_SID, self.__dict__['sid'])
        mmsg.AddMessage(MSG_KEY_PARAMS_MODIFY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_MODIFY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_PARAMS_MODIFY_TYPE)
        self.__dict__['objectType'] = submsg.FindU32(MSG_KEY_PARAMS_MODIFY_OBJECT_TYPE)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_PARAMS_MODIFY_FLAGS)
        self.__dict__['accessMask'] = submsg.FindU32(MSG_KEY_PARAMS_MODIFY_ACCESS_MASK)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_PARAMS_MODIFY_NAME)
        self.__dict__['sid'] = submsg.FindString(MSG_KEY_PARAMS_MODIFY_SID)