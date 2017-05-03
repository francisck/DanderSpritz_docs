# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
RESULT_TYPE_PROCESS_HIDE = 0
RESULT_TYPE_PROCESS_UNHIDE = 1

class Result:

    def __init__(self):
        self.__dict__['type'] = 0
        self.__dict__['item'] = ''
        self.__dict__['metaData'] = ''

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'item':
            return self.__dict__['item']
        if name == 'metaData':
            return self.__dict__['metaData']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'item':
            self.__dict__['item'] = value
        elif name == 'metaData':
            self.__dict__['metaData'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_TYPE, self.__dict__['type'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_ITEM, self.__dict__['item'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_METADATA, self.__dict__['metaData'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_TYPE)
        self.__dict__['item'] = submsg.FindString(MSG_KEY_RESULT_ITEM)
        self.__dict__['metaData'] = submsg.FindString(MSG_KEY_RESULT_METADATA)