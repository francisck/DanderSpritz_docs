# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import mcl.object.MclTime
PARAMS_QUERY_TYPE_ALL = 0
PARAMS_QUERY_TYPE_IP_ONLY = 1
PARAMS_QUERY_TYPE_TCP_ONLY = 2
PARAMS_QUERY_TYPE_UDP_ONLY = 3
PARAMS_QUERY_TYPE_PIPES_ONLY = 4

class Params:

    def __init__(self):
        self.__dict__['monitor'] = False
        self.__dict__['delay'] = mcl.object.MclTime.MclTime()
        self.__dict__['queryType'] = PARAMS_QUERY_TYPE_IP_ONLY
        self.__dict__['maximum'] = 1000

    def __getattr__(self, name):
        if name == 'monitor':
            return self.__dict__['monitor']
        if name == 'delay':
            return self.__dict__['delay']
        if name == 'queryType':
            return self.__dict__['queryType']
        if name == 'maximum':
            return self.__dict__['maximum']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'monitor':
            self.__dict__['monitor'] = value
        elif name == 'delay':
            self.__dict__['delay'] = value
        elif name == 'queryType':
            self.__dict__['queryType'] = value
        elif name == 'maximum':
            self.__dict__['maximum'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_PARAMS_MONITOR, self.__dict__['monitor'])
        submsg.AddTime(MSG_KEY_PARAMS_DELAY, self.__dict__['delay'])
        submsg.AddU8(MSG_KEY_PARAMS_QUERY_TYPE, self.__dict__['queryType'])
        submsg.AddU32(MSG_KEY_PARAMS_MAXIMUM, self.__dict__['maximum'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['monitor'] = submsg.FindBool(MSG_KEY_PARAMS_MONITOR)
        except:
            pass

        try:
            self.__dict__['delay'] = submsg.FindTime(MSG_KEY_PARAMS_DELAY)
        except:
            pass

        try:
            self.__dict__['queryType'] = submsg.FindU8(MSG_KEY_PARAMS_QUERY_TYPE)
        except:
            pass

        try:
            self.__dict__['maximum'] = submsg.FindU32(MSG_KEY_PARAMS_MAXIMUM)
        except:
            pass