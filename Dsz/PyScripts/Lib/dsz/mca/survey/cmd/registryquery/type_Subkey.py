# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Subkey.py
from types import *
import mcl.object.MclTime

class Subkey:

    def __init__(self):
        self.__dict__['lastUpdate'] = mcl.object.MclTime.MclTime()
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'lastUpdate':
            return self.__dict__['lastUpdate']
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'lastUpdate':
            self.__dict__['lastUpdate'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddTime(MSG_KEY_RESULT_SUBKEY_LAST_UPDATE, self.__dict__['lastUpdate'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_SUBKEY_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_RESULT_SUBKEY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_SUBKEY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['lastUpdate'] = submsg.FindTime(MSG_KEY_RESULT_SUBKEY_LAST_UPDATE)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_SUBKEY_NAME)