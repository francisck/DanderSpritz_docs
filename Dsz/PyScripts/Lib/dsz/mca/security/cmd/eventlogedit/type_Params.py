# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_MEM_PROVIDER_NONE = 4294967295L
PARAMS_MEM_PROVIDER_ANY = 0
PARAMS_MEM_PROVIDER_STANDARD = 1
PARAMS_MEM_PROVIDER_DRNI = 2
PARAMS_INJECT_PROVIDER_NONE = 4294967295L
PARAMS_INJECT_PROVIDER_ANY = 0
PARAMS_INJECT_PROVIDER_STANDARD = 1
PARAMS_INJECT_PROVIDER_DRNI = 2

class Params:

    def __init__(self):
        self.__dict__['recnum'] = 0
        self.__dict__['logname'] = ''
        self.__dict__['searchlen'] = 0
        self.__dict__['memoryProvider'] = PARAMS_MEM_PROVIDER_ANY
        self.__dict__['injectProvider'] = PARAMS_INJECT_PROVIDER_ANY

    def __getattr__(self, name):
        if name == 'recnum':
            return self.__dict__['recnum']
        if name == 'logname':
            return self.__dict__['logname']
        if name == 'searchlen':
            return self.__dict__['searchlen']
        if name == 'memoryProvider':
            return self.__dict__['memoryProvider']
        if name == 'injectProvider':
            return self.__dict__['injectProvider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'recnum':
            self.__dict__['recnum'] = value
        elif name == 'logname':
            self.__dict__['logname'] = value
        elif name == 'searchlen':
            self.__dict__['searchlen'] = value
        elif name == 'memoryProvider':
            self.__dict__['memoryProvider'] = value
        elif name == 'injectProvider':
            self.__dict__['injectProvider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_PARAMS_RECORDNUMBER, self.__dict__['recnum'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_LOGNAME, self.__dict__['logname'])
        submsg.AddU32(MSG_KEY_PARAMS_SEARCHLENGTH, self.__dict__['searchlen'])
        submsg.AddU32(MSG_KEY_PARAMS_PROVIDER_MEMORY, self.__dict__['memoryProvider'])
        submsg.AddU32(MSG_KEY_PARAMS_PROVIDER_INJECT, self.__dict__['injectProvider'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['recnum'] = submsg.FindU64(MSG_KEY_PARAMS_RECORDNUMBER)
        self.__dict__['logname'] = submsg.FindString(MSG_KEY_PARAMS_LOGNAME)
        self.__dict__['searchlen'] = submsg.FindU32(MSG_KEY_PARAMS_SEARCHLENGTH)
        self.__dict__['memoryProvider'] = submsg.FindU32(MSG_KEY_PARAMS_PROVIDER_MEMORY)
        self.__dict__['injectProvider'] = submsg.FindU32(MSG_KEY_PARAMS_PROVIDER_INJECT)