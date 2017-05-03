# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *

class InstallParams:

    def __init__(self):
        self.__dict__['procname'] = ''
        self.__dict__['remotelibname'] = ''

    def __getattr__(self, name):
        if name == 'procname':
            return self.__dict__['procname']
        if name == 'remotelibname':
            return self.__dict__['remotelibname']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'procname':
            self.__dict__['procname'] = value
        elif name == 'remotelibname':
            self.__dict__['remotelibname'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_PROCESS_NAME, self.__dict__['procname'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_REMOTE_LIBRARY_NAME, self.__dict__['remotelibname'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['procname'] = submsg.FindString(MSG_KEY_PARAMS_PROCESS_NAME)
        self.__dict__['remotelibname'] = submsg.FindString(MSG_KEY_PARAMS_REMOTE_LIBRARY_NAME)


class UninstallParams:

    def __init__(self):
        self.__dict__['procname'] = ''
        self.__dict__['remotelibname'] = ''

    def __getattr__(self, name):
        if name == 'procname':
            return self.__dict__['procname']
        if name == 'remotelibname':
            return self.__dict__['remotelibname']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'procname':
            self.__dict__['procname'] = value
        elif name == 'remotelibname':
            self.__dict__['remotelibname'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_UNINSTALL_PROCESS_NAME, self.__dict__['procname'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_UNINSTALL_LIBRARY_NAME, self.__dict__['remotelibname'])
        mmsg.AddMessage(MSG_KEY_PARAMS_UNINSTALL, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_UNINSTALL, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['procname'] = submsg.FindString(MSG_KEY_PARAMS_UNINSTALL_PROCESS_NAME)
        self.__dict__['remotelibname'] = submsg.FindString(MSG_KEY_PARAMS_UNINSTALL_LIBRARY_NAME)