# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_LOGIN_TYPE_BATCH = 1
PARAMS_LOGIN_TYPE_INTERACTIVE = 2
PARAMS_LOGIN_TYPE_NETWORK = 3
PARAMS_LOGIN_TYPE_SERVICE = 4
PARAMS_LOGIN_TYPE_CLEARTEXT = 5
PARAMS_LOGIN_TYPE_NEW_CREDS = 6

class Params:

    def __init__(self):
        self.__dict__['loginType'] = 0
        self.__dict__['user'] = ''
        self.__dict__['password'] = ''
        self.__dict__['domain'] = ''

    def __getattr__(self, name):
        if name == 'loginType':
            return self.__dict__['loginType']
        if name == 'user':
            return self.__dict__['user']
        if name == 'password':
            return self.__dict__['password']
        if name == 'domain':
            return self.__dict__['domain']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'loginType':
            self.__dict__['loginType'] = value
        elif name == 'user':
            self.__dict__['user'] = value
        elif name == 'password':
            self.__dict__['password'] = value
        elif name == 'domain':
            self.__dict__['domain'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_LOGIN_TYPE, self.__dict__['loginType'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_USER, self.__dict__['user'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_PASSWORD, self.__dict__['password'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DOMAIN, self.__dict__['domain'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['loginType'] = submsg.FindU8(MSG_KEY_PARAMS_LOGIN_TYPE)
        self.__dict__['user'] = submsg.FindString(MSG_KEY_PARAMS_USER)
        self.__dict__['password'] = submsg.FindString(MSG_KEY_PARAMS_PASSWORD)
        self.__dict__['domain'] = submsg.FindString(MSG_KEY_PARAMS_DOMAIN)