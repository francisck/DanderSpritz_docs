# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class Params:

    def __init__(self):
        self.__dict__['numLang'] = 1
        self.__dict__['path'] = ''
        self.__dict__['file'] = 'user.exe'

    def __getattr__(self, name):
        if name == 'numLang':
            return self.__dict__['numLang']
        if name == 'path':
            return self.__dict__['path']
        if name == 'file':
            return self.__dict__['file']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'numLang':
            self.__dict__['numLang'] = value
        elif name == 'path':
            self.__dict__['path'] = value
        elif name == 'file':
            self.__dict__['file'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_MAX_LANGUAGES, self.__dict__['numLang'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_PATH, self.__dict__['path'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_FILE, self.__dict__['file'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['numLang'] = submsg.FindU32(MSG_KEY_PARAMS_MAX_LANGUAGES)
        except:
            pass

        try:
            self.__dict__['path'] = submsg.FindString(MSG_KEY_PARAMS_PATH)
        except:
            pass

        try:
            self.__dict__['file'] = submsg.FindString(MSG_KEY_PARAMS_FILE)
        except:
            pass