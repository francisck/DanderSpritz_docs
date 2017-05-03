# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_PERSISTENCE_TYPE_DEFAULT = 0
PARAMS_PERSISTENCE_TYPE_SOTI = 1
PARAMS_PERSISTENCE_TYPE_LAUNCHER = 2
PARAMS_PERSISTENCE_TYPE_JUVI = 3
PARAMS_UPGRADE_MODULEACTION_COPY_MEMORY = 0
PARAMS_UPGRADE_MODULEACTION_COPY_NONE = 1

class ParamsInstall:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['persistence'] = PARAMS_PERSISTENCE_TYPE_DEFAULT

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'persistence':
            return self.__dict__['persistence']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'persistence':
            self.__dict__['persistence'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_INSTALL_INSTANCE, self.__dict__['instance'])
        submsg.AddU8(MSG_KEY_PARAMS_INSTALL_PERSISTENCE, self.__dict__['persistence'])
        mmsg.AddMessage(MSG_KEY_PARAMS_INSTALL, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_INSTALL, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_PARAMS_INSTALL_INSTANCE)
        try:
            self.__dict__['persistence'] = submsg.FindU8(MSG_KEY_PARAMS_INSTALL_PERSISTENCE)
        except:
            pass


class ParamsUninstall:

    def __init__(self):
        self.__dict__['instance'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_UNINSTALL_INSTANCE, self.__dict__['instance'])
        mmsg.AddMessage(MSG_KEY_PARAMS_UNINSTALL, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_UNINSTALL, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_PARAMS_UNINSTALL_INSTANCE)


class ParamsUpgrade:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['persistence'] = PARAMS_PERSISTENCE_TYPE_DEFAULT
        self.__dict__['moduleAction'] = PARAMS_UPGRADE_MODULEACTION_COPY_MEMORY

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'persistence':
            return self.__dict__['persistence']
        if name == 'moduleAction':
            return self.__dict__['moduleAction']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'persistence':
            self.__dict__['persistence'] = value
        elif name == 'moduleAction':
            self.__dict__['moduleAction'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_UPGRADE_INSTANCE, self.__dict__['instance'])
        submsg.AddU8(MSG_KEY_PARAMS_UPGRADE_PERSISTENCE, self.__dict__['persistence'])
        submsg.AddU8(MSG_KEY_PARAMS_UPGRADE_MODULEACTION, self.__dict__['moduleAction'])
        mmsg.AddMessage(MSG_KEY_PARAMS_UPGRADE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_UPGRADE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_PARAMS_UPGRADE_INSTANCE)
        try:
            self.__dict__['persistence'] = submsg.FindU8(MSG_KEY_PARAMS_UPGRADE_PERSISTENCE)
        except:
            pass

        try:
            self.__dict__['moduleAction'] = submsg.FindU8(MSG_KEY_PARAMS_UPGRADE_MODULEACTION)
        except:
            pass