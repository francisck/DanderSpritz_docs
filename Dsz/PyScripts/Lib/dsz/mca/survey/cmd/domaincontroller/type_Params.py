# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class Params:

    def __init__(self):
        self.__dict__['primary'] = False
        self.__dict__['domain'] = ''

    def __getattr__(self, name):
        if name == 'primary':
            return self.__dict__['primary']
        if name == 'domain':
            return self.__dict__['domain']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'primary':
            self.__dict__['primary'] = value
        elif name == 'domain':
            self.__dict__['domain'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_PARAMS_PRIMARY, self.__dict__['primary'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DOMAIN, self.__dict__['domain'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['primary'] = submsg.FindBool(MSG_KEY_PARAMS_PRIMARY)
        try:
            self.__dict__['domain'] = submsg.FindString(MSG_KEY_PARAMS_DOMAIN)
        except:
            pass