# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class ProcessParams:

    def __init__(self):
        self.__dict__['processId'] = 0
        self.__dict__['unhide'] = False
        self.__dict__['metaData'] = ''

    def __getattr__(self, name):
        if name == 'processId':
            return self.__dict__['processId']
        if name == 'unhide':
            return self.__dict__['unhide']
        if name == 'metaData':
            return self.__dict__['metaData']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'processId':
            self.__dict__['processId'] = value
        elif name == 'unhide':
            self.__dict__['unhide'] = value
        elif name == 'metaData':
            self.__dict__['metaData'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_PROCESS_ID, self.__dict__['processId'])
        submsg.AddBool(MSG_KEY_PARAMS_UNHIDE, self.__dict__['unhide'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_METADATA, self.__dict__['metaData'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['processId'] = submsg.FindU32(MSG_KEY_PARAMS_PROCESS_ID)
        self.__dict__['unhide'] = submsg.FindBool(MSG_KEY_PARAMS_UNHIDE)
        self.__dict__['metaData'] = submsg.FindString(MSG_KEY_PARAMS_METADATA)