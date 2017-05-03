# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime

class Result:

    def __init__(self):
        self.__dict__['upTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['idleTime'] = mcl.object.MclTime.MclTime()

    def __getattr__(self, name):
        if name == 'upTime':
            return self.__dict__['upTime']
        if name == 'idleTime':
            return self.__dict__['idleTime']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'upTime':
            self.__dict__['upTime'] = value
        elif name == 'idleTime':
            self.__dict__['idleTime'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddTime(MSG_KEY_RESULT_UPTIME, self.__dict__['upTime'])
        submsg.AddTime(MSG_KEY_RESULT_IDLETIME, self.__dict__['idleTime'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['upTime'] = submsg.FindTime(MSG_KEY_RESULT_UPTIME)
        self.__dict__['idleTime'] = submsg.FindTime(MSG_KEY_RESULT_IDLETIME)