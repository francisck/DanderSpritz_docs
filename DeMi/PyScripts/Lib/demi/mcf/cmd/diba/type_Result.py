# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import array
RESULT_PERSISTENCE_TYPE_SOTI = 1
RESULT_PERSISTENCE_TYPE_LAUNCHER = 2
RESULT_PERSISTENCE_TYPE_JUVI = 3

class ResultPersistence:

    def __init__(self):
        self.__dict__['type'] = 0
        self.__dict__['compatible'] = False
        self.__dict__['reason'] = 0

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'compatible':
            return self.__dict__['compatible']
        if name == 'reason':
            return self.__dict__['reason']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'compatible':
            self.__dict__['compatible'] = value
        elif name == 'reason':
            self.__dict__['reason'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_PERSISTENCE_TYPE, self.__dict__['type'])
        submsg.AddBool(MSG_KEY_RESULT_PERSISTENCE_COMPATIBLE, self.__dict__['compatible'])
        submsg.AddU32(MSG_KEY_RESULT_PERSISTENCE_REASON, self.__dict__['reason'])
        mmsg.AddMessage(MSG_KEY_RESULT_PERSISTENCE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_PERSISTENCE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_PERSISTENCE_TYPE)
        self.__dict__['compatible'] = submsg.FindBool(MSG_KEY_RESULT_PERSISTENCE_COMPATIBLE)
        self.__dict__['reason'] = submsg.FindU32(MSG_KEY_RESULT_PERSISTENCE_REASON)


class ResultInstall:

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
        submsg.AddU32(MSG_KEY_RESULT_INSTALL_INSTANCE, self.__dict__['instance'])
        mmsg.AddMessage(MSG_KEY_RESULT_INSTALL, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_INSTALL, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_RESULT_INSTALL_INSTANCE)


class ResultUninstall:

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
        submsg.AddU32(MSG_KEY_RESULT_UNINSTALL_INSTANCE, self.__dict__['instance'])
        mmsg.AddMessage(MSG_KEY_RESULT_UNINSTALL, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_UNINSTALL, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_RESULT_UNINSTALL_INSTANCE)


class ResultUpgrade:

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
        submsg.AddU32(MSG_KEY_RESULT_UPGRADE_INSTANCE, self.__dict__['instance'])
        mmsg.AddMessage(MSG_KEY_RESULT_UPGRADE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_UPGRADE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_RESULT_UPGRADE_INSTANCE)


class ResultModule:

    def __init__(self):
        self.__dict__['size'] = 0
        self.__dict__['order'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['id'] = 0
        self.__dict__['moduleName'] = ''
        self.__dict__['processName'] = ''
        self.__dict__['hash'] = array.array('B')
        self.__dict__['actionStatus'] = 0

    def __getattr__(self, name):
        if name == 'size':
            return self.__dict__['size']
        if name == 'order':
            return self.__dict__['order']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'id':
            return self.__dict__['id']
        if name == 'moduleName':
            return self.__dict__['moduleName']
        if name == 'processName':
            return self.__dict__['processName']
        if name == 'hash':
            return self.__dict__['hash']
        if name == 'actionStatus':
            return self.__dict__['actionStatus']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'size':
            self.__dict__['size'] = value
        elif name == 'order':
            self.__dict__['order'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'id':
            self.__dict__['id'] = value
        elif name == 'moduleName':
            self.__dict__['moduleName'] = value
        elif name == 'processName':
            self.__dict__['processName'] = value
        elif name == 'hash':
            self.__dict__['hash'] = value
        elif name == 'actionStatus':
            self.__dict__['actionStatus'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_MODULE_SIZE, self.__dict__['size'])
        submsg.AddU32(MSG_KEY_RESULT_MODULE_ORDER, self.__dict__['order'])
        submsg.AddU32(MSG_KEY_RESULT_MODULE_FLAGS, self.__dict__['flags'])
        submsg.AddU32(MSG_KEY_RESULT_MODULE_ID, self.__dict__['id'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_MODULE_MODULE_NAME, self.__dict__['moduleName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_MODULE_PROCESS_NAME, self.__dict__['processName'])
        submsg.AddData(MSG_KEY_RESULT_MODULE_HASH, self.__dict__['hash'])
        submsg.AddU32(MSG_KEY_RESULT_MODULE_ACTION_STATUS, self.__dict__['actionStatus'])
        mmsg.AddMessage(MSG_KEY_RESULT_MODULE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MODULE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['size'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_SIZE)
        self.__dict__['order'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_ORDER)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_FLAGS)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_ID)
        self.__dict__['moduleName'] = submsg.FindString(MSG_KEY_RESULT_MODULE_MODULE_NAME)
        self.__dict__['processName'] = submsg.FindString(MSG_KEY_RESULT_MODULE_PROCESS_NAME)
        try:
            self.__dict__['hash'] = submsg.FindData(MSG_KEY_RESULT_MODULE_HASH)
        except:
            pass

        self.__dict__['actionStatus'] = submsg.FindU32(MSG_KEY_RESULT_MODULE_ACTION_STATUS)