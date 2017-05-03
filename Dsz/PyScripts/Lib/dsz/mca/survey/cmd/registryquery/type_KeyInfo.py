# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_KeyInfo.py
from types import *
import mcl.object.MclTime
KEY_FLAG_ACCESS_DENIED = 1

class KeyInfo:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['hive'] = 0
        self.__dict__['lastUpdate'] = mcl.object.MclTime.MclTime()
        self.__dict__['classValue'] = ''
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'hive':
            return self.__dict__['hive']
        if name == 'lastUpdate':
            return self.__dict__['lastUpdate']
        if name == 'classValue':
            return self.__dict__['classValue']
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'hive':
            self.__dict__['hive'] = value
        elif name == 'lastUpdate':
            self.__dict__['lastUpdate'] = value
        elif name == 'classValue':
            self.__dict__['classValue'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_RESULT_KEYINFO_FLAGS, self.__dict__['flags'])
        submsg.AddU8(MSG_KEY_RESULT_KEYINFO_HIVE, self.__dict__['hive'])
        submsg.AddTime(MSG_KEY_RESULT_KEYINFO_LAST_UPDATE, self.__dict__['lastUpdate'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_KEYINFO_CLASS_VALUE, self.__dict__['classValue'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_KEYINFO_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_RESULT_KEYINFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_KEYINFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_RESULT_KEYINFO_FLAGS)
        self.__dict__['hive'] = submsg.FindU8(MSG_KEY_RESULT_KEYINFO_HIVE)
        self.__dict__['lastUpdate'] = submsg.FindTime(MSG_KEY_RESULT_KEYINFO_LAST_UPDATE)
        self.__dict__['classValue'] = submsg.FindString(MSG_KEY_RESULT_KEYINFO_CLASS_VALUE)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_KEYINFO_NAME)