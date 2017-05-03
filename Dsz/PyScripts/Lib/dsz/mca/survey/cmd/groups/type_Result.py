# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
RESULT_GROUP_ATTRIBUTE_ENABLED = 4
RESULT_GROUP_ATTRIBUTE_ENABLED_BY_DEFAULT = 2
RESULT_GROUP_ATTRIBUTE_LOGON_ID = 3221225472L
RESULT_GROUP_ATTRIBUTE_MANDATORY = 1
RESULT_GROUP_ATTRIBUTE_OWNER = 8
RESULT_GROUP_ATTRIBUTE_RESOURCE = 536870912
RESULT_GROUP_ATTRIBUTE_USE_FOR_DENY_ONLY = 16

class Result:

    def __init__(self):
        self.__dict__['id'] = 0
        self.__dict__['attributes'] = 0
        self.__dict__['name'] = ''
        self.__dict__['comment'] = ''

    def __getattr__(self, name):
        if name == 'id':
            return self.__dict__['id']
        if name == 'attributes':
            return self.__dict__['attributes']
        if name == 'name':
            return self.__dict__['name']
        if name == 'comment':
            return self.__dict__['comment']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'id':
            self.__dict__['id'] = value
        elif name == 'attributes':
            self.__dict__['attributes'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'comment':
            self.__dict__['comment'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_ID, self.__dict__['id'])
        submsg.AddU32(MSG_KEY_RESULT_ATTRIBUTES, self.__dict__['attributes'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_COMMENT, self.__dict__['comment'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_ID)
        self.__dict__['attributes'] = submsg.FindU32(MSG_KEY_RESULT_ATTRIBUTES)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_NAME)
        self.__dict__['comment'] = submsg.FindString(MSG_KEY_RESULT_COMMENT)