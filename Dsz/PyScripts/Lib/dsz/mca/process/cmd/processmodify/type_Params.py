# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_TYPE_CHANGE_GROUP = 1
PARAMS_TYPE_CHANGE_PRIVILEGE = 2
PARAMS_TYPE_ADD_PRIVILEGE = 3
PARAMS_TYPE_DELETE_PRIVILEGE = 4

class Params:

    def __init__(self):
        self.__dict__['type'] = 0
        self.__dict__['pid'] = 0
        self.__dict__['newAttributes'] = 0
        self.__dict__['changeAttributes'] = False
        self.__dict__['origValue'] = ''
        self.__dict__['newValue'] = ''

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'pid':
            return self.__dict__['pid']
        if name == 'newAttributes':
            return self.__dict__['newAttributes']
        if name == 'changeAttributes':
            return self.__dict__['changeAttributes']
        if name == 'origValue':
            return self.__dict__['origValue']
        if name == 'newValue':
            return self.__dict__['newValue']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'pid':
            self.__dict__['pid'] = value
        elif name == 'newAttributes':
            self.__dict__['newAttributes'] = value
        elif name == 'changeAttributes':
            self.__dict__['changeAttributes'] = value
        elif name == 'origValue':
            self.__dict__['origValue'] = value
        elif name == 'newValue':
            self.__dict__['newValue'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_PARAMS_PROCESS_ID, self.__dict__['pid'])
        submsg.AddU32(MSG_KEY_PARAMS_NEW_ATTRIBUTES, self.__dict__['newAttributes'])
        submsg.AddBool(MSG_KEY_PARAMS_CHANGE_ATTRIBUTES, self.__dict__['changeAttributes'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_ORIGINAL_VALUE, self.__dict__['origValue'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_NEW_VALUE, self.__dict__['newValue'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_PARAMS_TYPE)
        self.__dict__['pid'] = submsg.FindU32(MSG_KEY_PARAMS_PROCESS_ID)
        try:
            self.__dict__['newAttributes'] = submsg.FindU32(MSG_KEY_PARAMS_NEW_ATTRIBUTES)
        except:
            pass

        try:
            self.__dict__['changeAttributes'] = submsg.FindBool(MSG_KEY_PARAMS_CHANGE_ATTRIBUTES)
        except:
            pass

        self.__dict__['origValue'] = submsg.FindString(MSG_KEY_PARAMS_ORIGINAL_VALUE)
        self.__dict__['newValue'] = submsg.FindString(MSG_KEY_PARAMS_NEW_VALUE)