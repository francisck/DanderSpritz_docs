# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class Result:

    def __init__(self):
        self.__dict__['hUser'] = 0
        self.__dict__['user'] = ''
        self.__dict__['domain'] = ''

    def __getattr__(self, name):
        if name == 'hUser':
            return self.__dict__['hUser']
        if name == 'user':
            return self.__dict__['user']
        if name == 'domain':
            return self.__dict__['domain']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'hUser':
            self.__dict__['hUser'] = value
        elif name == 'user':
            self.__dict__['user'] = value
        elif name == 'domain':
            self.__dict__['domain'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_HUSER, self.__dict__['hUser'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER, self.__dict__['user'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DOMAIN, self.__dict__['domain'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['hUser'] = submsg.FindU64(MSG_KEY_RESULT_HUSER)
        self.__dict__['user'] = submsg.FindString(MSG_KEY_RESULT_USER)
        self.__dict__['domain'] = submsg.FindString(MSG_KEY_RESULT_DOMAIN)