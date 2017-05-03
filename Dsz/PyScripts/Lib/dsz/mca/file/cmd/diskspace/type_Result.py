# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class Result:

    def __init__(self):
        self.__dict__['available'] = 0
        self.__dict__['total'] = 0
        self.__dict__['free'] = 0
        self.__dict__['disk'] = ''

    def __getattr__(self, name):
        if name == 'available':
            return self.__dict__['available']
        if name == 'total':
            return self.__dict__['total']
        if name == 'free':
            return self.__dict__['free']
        if name == 'disk':
            return self.__dict__['disk']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'available':
            self.__dict__['available'] = value
        elif name == 'total':
            self.__dict__['total'] = value
        elif name == 'free':
            self.__dict__['free'] = value
        elif name == 'disk':
            self.__dict__['disk'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_AVAILABLE, self.__dict__['available'])
        submsg.AddU64(MSG_KEY_RESULT_TOTAL, self.__dict__['total'])
        submsg.AddU64(MSG_KEY_RESULT_FREE, self.__dict__['free'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DISK, self.__dict__['disk'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['available'] = submsg.FindU64(MSG_KEY_RESULT_AVAILABLE)
        self.__dict__['total'] = submsg.FindU64(MSG_KEY_RESULT_TOTAL)
        self.__dict__['free'] = submsg.FindU64(MSG_KEY_RESULT_FREE)
        self.__dict__['disk'] = submsg.FindString(MSG_KEY_RESULT_DISK)