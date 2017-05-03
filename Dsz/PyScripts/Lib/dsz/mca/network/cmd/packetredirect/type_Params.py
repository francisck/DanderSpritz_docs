# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import array
PARAMS_SEND_TYPE_DRIVER = 0
PARAMS_SEND_TYPE_RAW = 1

class Params:

    def __init__(self):
        self.__dict__['sendType'] = 0
        self.__dict__['data'] = array.array('B')
        self.__dict__['extraInfo'] = ''

    def __getattr__(self, name):
        if name == 'sendType':
            return self.__dict__['sendType']
        if name == 'data':
            return self.__dict__['data']
        if name == 'extraInfo':
            return self.__dict__['extraInfo']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'sendType':
            self.__dict__['sendType'] = value
        elif name == 'data':
            self.__dict__['data'] = value
        elif name == 'extraInfo':
            self.__dict__['extraInfo'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_SEND_TYPE, self.__dict__['sendType'])
        submsg.AddData(MSG_KEY_PARAMS_DATA, self.__dict__['data'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_EXTRA_INFO, self.__dict__['extraInfo'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['sendType'] = submsg.FindU8(MSG_KEY_PARAMS_SEND_TYPE)
        self.__dict__['data'] = submsg.FindData(MSG_KEY_PARAMS_DATA)
        self.__dict__['extraInfo'] = submsg.FindString(MSG_KEY_PARAMS_EXTRA_INFO)