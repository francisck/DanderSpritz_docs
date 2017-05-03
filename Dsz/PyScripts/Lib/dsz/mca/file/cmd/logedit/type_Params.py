# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_FLAG_UNICODE = 1
PARAMS_FLAG_DOSRETURN = 2
PARAMS_FLAG_SHARE_READ = 4
PARAMS_FLAG_SHARE_WRITE = 8
PARAMS_FLAG_SHARE_DELETE = 16

class Params:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['file'] = ''
        self.__dict__['phrase'] = ''

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'file':
            return self.__dict__['file']
        if name == 'phrase':
            return self.__dict__['phrase']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'file':
            self.__dict__['file'] = value
        elif name == 'phrase':
            self.__dict__['phrase'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_FILE, self.__dict__['file'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_PHRASE, self.__dict__['phrase'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_PARAMS_FLAGS)
        self.__dict__['file'] = submsg.FindString(MSG_KEY_PARAMS_FILE)
        self.__dict__['phrase'] = submsg.FindString(MSG_KEY_PARAMS_PHRASE)