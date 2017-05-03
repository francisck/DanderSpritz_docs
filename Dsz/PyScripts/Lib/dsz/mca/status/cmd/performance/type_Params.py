# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class Params:

    def __init__(self):
        self.__dict__['initBuffer'] = 10240
        self.__dict__['objectNumber'] = 4294967295L
        self.__dict__['bare'] = False
        self.__dict__['target'] = ''
        self.__dict__['dataSet'] = ''

    def __getattr__(self, name):
        if name == 'initBuffer':
            return self.__dict__['initBuffer']
        if name == 'objectNumber':
            return self.__dict__['objectNumber']
        if name == 'bare':
            return self.__dict__['bare']
        if name == 'target':
            return self.__dict__['target']
        if name == 'dataSet':
            return self.__dict__['dataSet']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'initBuffer':
            self.__dict__['initBuffer'] = value
        elif name == 'objectNumber':
            self.__dict__['objectNumber'] = value
        elif name == 'bare':
            self.__dict__['bare'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        elif name == 'dataSet':
            self.__dict__['dataSet'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_INIT_BUFFER, self.__dict__['initBuffer'])
        submsg.AddU32(MSG_KEY_PARAMS_OBJECT_NUMBER, self.__dict__['objectNumber'])
        submsg.AddBool(MSG_KEY_PARAMS_BARE, self.__dict__['bare'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_TARGET, self.__dict__['target'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DATA_SET, self.__dict__['dataSet'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['initBuffer'] = submsg.FindU32(MSG_KEY_PARAMS_INIT_BUFFER)
        except:
            pass

        try:
            self.__dict__['objectNumber'] = submsg.FindU32(MSG_KEY_PARAMS_OBJECT_NUMBER)
        except:
            pass

        try:
            self.__dict__['bare'] = submsg.FindBool(MSG_KEY_PARAMS_BARE)
        except:
            pass

        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_TARGET)
        except:
            pass

        self.__dict__['dataSet'] = submsg.FindString(MSG_KEY_PARAMS_DATA_SET)