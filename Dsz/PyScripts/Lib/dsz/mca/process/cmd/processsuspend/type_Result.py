# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
MCL_RESULT_ACTION_SUSPENDED = 0
MCL_RESULT_ACTION_RESUMED = 1

class Result:

    def __init__(self):
        self.__dict__['resultType'] = 0

    def __getattr__(self, name):
        if name == 'resultType':
            return self.__dict__['resultType']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'resultType':
            self.__dict__['resultType'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_RESULT_TYPE, self.__dict__['resultType'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['resultType'] = submsg.FindU8(MSG_KEY_RESULT_RESULT_TYPE)