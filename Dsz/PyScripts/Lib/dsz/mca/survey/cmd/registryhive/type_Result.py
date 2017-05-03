# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class ResultHive:

    def __init__(self):
        self.__dict__['hive'] = 0
        self.__dict__['key'] = ''
        self.__dict__['file'] = ''
        self.__dict__['action'] = 0
        self.__dict__['permanent'] = False

    def __getattr__(self, name):
        if name == 'hive':
            return self.__dict__['hive']
        if name == 'key':
            return self.__dict__['key']
        if name == 'file':
            return self.__dict__['file']
        if name == 'action':
            return self.__dict__['action']
        if name == 'permanent':
            return self.__dict__['permanent']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'hive':
            self.__dict__['hive'] = value
        elif name == 'key':
            self.__dict__['key'] = value
        elif name == 'file':
            self.__dict__['file'] = value
        elif name == 'action':
            self.__dict__['action'] = value
        elif name == 'permanent':
            self.__dict__['permanent'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_HIVE, self.__dict__['hive'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_HIVE_KEY, self.__dict__['key'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_HIVE_FILE, self.__dict__['file'])
        submsg.AddU8(MSG_KEY_RESULT_HIVE_ACTION, self.__dict__['action'])
        submsg.AddBool(MSG_KEY_RESULT_HIVE_PERMANENT, self.__dict__['permanent'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['hive'] = submsg.FindU8(MSG_KEY_RESULT_HIVE)
        self.__dict__['key'] = submsg.FindString(MSG_KEY_RESULT_HIVE_KEY)
        self.__dict__['file'] = submsg.FindString(MSG_KEY_RESULT_HIVE_FILE)
        self.__dict__['action'] = submsg.FindU8(MSG_KEY_RESULT_HIVE_ACTION)
        self.__dict__['permanent'] = submsg.FindBool(MSG_KEY_RESULT_HIVE_PERMANENT)