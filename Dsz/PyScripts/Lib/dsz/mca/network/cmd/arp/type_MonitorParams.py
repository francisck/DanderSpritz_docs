# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_MonitorParams.py
from types import *
import mcl.object.MclTime

class MonitorParams:

    def __init__(self):
        self.__dict__['delay'] = mcl.object.MclTime.MclTime()
        self.__dict__['entries'] = 100
        self.__dict__['sendInterval'] = 0

    def __getattr__(self, name):
        if name == 'delay':
            return self.__dict__['delay']
        if name == 'entries':
            return self.__dict__['entries']
        if name == 'sendInterval':
            return self.__dict__['sendInterval']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'delay':
            self.__dict__['delay'] = value
        elif name == 'entries':
            self.__dict__['entries'] = value
        elif name == 'sendInterval':
            self.__dict__['sendInterval'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddTime(MSG_KEY_PARAMS_MONITOR_DELAY, self.__dict__['delay'])
        submsg.AddU32(MSG_KEY_PARAMS_MONITOR_ENTRIES, self.__dict__['entries'])
        submsg.AddU8(MSG_KEY_PARAMS_MONITOR_SEND_INTERVAL, self.__dict__['sendInterval'])
        mmsg.AddMessage(MSG_KEY_PARAMS_MONITOR, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_MONITOR, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['delay'] = submsg.FindTime(MSG_KEY_PARAMS_MONITOR_DELAY)
        try:
            self.__dict__['entries'] = submsg.FindU32(MSG_KEY_PARAMS_MONITOR_ENTRIES)
        except:
            pass

        self.__dict__['sendInterval'] = submsg.FindU8(MSG_KEY_PARAMS_MONITOR_SEND_INTERVAL)