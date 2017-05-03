# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import array

class ParamsConnect:

    def __init__(self):
        self.__dict__['id'] = 0

    def __getattr__(self, name):
        if name == 'id':
            return self.__dict__['id']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'id':
            self.__dict__['id'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_CONNECT_ID, self.__dict__['id'])
        mmsg.AddMessage(MSG_KEY_PARAMS_CONNECT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_CONNECT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['id'] = submsg.FindU32(MSG_KEY_PARAMS_CONNECT_ID)
        except:
            pass


class ParamsConfig:

    def __init__(self):
        self.__dict__['id'] = 0
        self.__dict__['hashModules'] = False

    def __getattr__(self, name):
        if name == 'id':
            return self.__dict__['id']
        if name == 'hashModules':
            return self.__dict__['hashModules']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'id':
            self.__dict__['id'] = value
        elif name == 'hashModules':
            self.__dict__['hashModules'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_CONFIG_ID, self.__dict__['id'])
        submsg.AddBool(MSG_KEY_PARAMS_CONFIG_HASH_MODULES, self.__dict__['hashModules'])
        mmsg.AddMessage(MSG_KEY_PARAMS_CONFIG, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_CONFIG, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        try:
            self.__dict__['id'] = submsg.FindU32(MSG_KEY_PARAMS_CONFIG_ID)
        except:
            pass

        try:
            self.__dict__['hashModules'] = submsg.FindBool(MSG_KEY_PARAMS_CONFIG_HASH_MODULES)
        except:
            pass


class ParamsModuleAdd:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['chunkOffset'] = 0
        self.__dict__['totalSize'] = 0
        self.__dict__['chunk'] = array.array('B')
        self.__dict__['moduleId'] = 0
        self.__dict__['moduleOrder'] = 0
        self.__dict__['moduleFlags'] = 0
        self.__dict__['moduleName'] = ''
        self.__dict__['processName'] = ''

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'chunkOffset':
            return self.__dict__['chunkOffset']
        if name == 'totalSize':
            return self.__dict__['totalSize']
        if name == 'chunk':
            return self.__dict__['chunk']
        if name == 'moduleId':
            return self.__dict__['moduleId']
        if name == 'moduleOrder':
            return self.__dict__['moduleOrder']
        if name == 'moduleFlags':
            return self.__dict__['moduleFlags']
        if name == 'moduleName':
            return self.__dict__['moduleName']
        if name == 'processName':
            return self.__dict__['processName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'chunkOffset':
            self.__dict__['chunkOffset'] = value
        elif name == 'totalSize':
            self.__dict__['totalSize'] = value
        elif name == 'chunk':
            self.__dict__['chunk'] = value
        elif name == 'moduleId':
            self.__dict__['moduleId'] = value
        elif name == 'moduleOrder':
            self.__dict__['moduleOrder'] = value
        elif name == 'moduleFlags':
            self.__dict__['moduleFlags'] = value
        elif name == 'moduleName':
            self.__dict__['moduleName'] = value
        elif name == 'processName':
            self.__dict__['processName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_MODULE_ADD_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_PARAMS_MODULE_ADD_CHUNK_OFFSET, self.__dict__['chunkOffset'])
        submsg.AddU32(MSG_KEY_PARAMS_MODULE_ADD_TOTAL_SIZE, self.__dict__['totalSize'])
        submsg.AddData(MSG_KEY_PARAMS_MODULE_ADD_CHUNK, self.__dict__['chunk'])
        submsg.AddU32(MSG_KEY_PARAMS_MODULE_ADD_MODULE_ID, self.__dict__['moduleId'])
        submsg.AddU32(MSG_KEY_PARAMS_MODULE_ADD_MODULE_ORDER, self.__dict__['moduleOrder'])
        submsg.AddU32(MSG_KEY_PARAMS_MODULE_ADD_MODULE_FLAGS, self.__dict__['moduleFlags'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_MODULE_ADD_MODULE_NAME, self.__dict__['moduleName'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_MODULE_ADD_PROCESS_NAME, self.__dict__['processName'])
        mmsg.AddMessage(MSG_KEY_PARAMS_MODULE_ADD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_MODULE_ADD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_PARAMS_MODULE_ADD_INSTANCE)
        self.__dict__['chunkOffset'] = submsg.FindU32(MSG_KEY_PARAMS_MODULE_ADD_CHUNK_OFFSET)
        self.__dict__['totalSize'] = submsg.FindU32(MSG_KEY_PARAMS_MODULE_ADD_TOTAL_SIZE)
        self.__dict__['chunk'] = submsg.FindData(MSG_KEY_PARAMS_MODULE_ADD_CHUNK)
        self.__dict__['moduleId'] = submsg.FindU32(MSG_KEY_PARAMS_MODULE_ADD_MODULE_ID)
        self.__dict__['moduleOrder'] = submsg.FindU32(MSG_KEY_PARAMS_MODULE_ADD_MODULE_ORDER)
        self.__dict__['moduleFlags'] = submsg.FindU32(MSG_KEY_PARAMS_MODULE_ADD_MODULE_FLAGS)
        self.__dict__['moduleName'] = submsg.FindString(MSG_KEY_PARAMS_MODULE_ADD_MODULE_NAME)
        self.__dict__['processName'] = submsg.FindString(MSG_KEY_PARAMS_MODULE_ADD_PROCESS_NAME)


class ParamsModuleDelete:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['moduleId'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'moduleId':
            return self.__dict__['moduleId']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'moduleId':
            self.__dict__['moduleId'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_MODULE_DELETE_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_PARAMS_MODULE_DELETE_MODULE_ID, self.__dict__['moduleId'])
        mmsg.AddMessage(MSG_KEY_PARAMS_MODULE_DELETE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_MODULE_DELETE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_PARAMS_MODULE_DELETE_INSTANCE)
        self.__dict__['moduleId'] = submsg.FindU32(MSG_KEY_PARAMS_MODULE_DELETE_MODULE_ID)


class ParamsModuleRead:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['moduleId'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'moduleId':
            return self.__dict__['moduleId']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'moduleId':
            self.__dict__['moduleId'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_MODULE_READ_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_PARAMS_MODULE_READ_MODULE_ID, self.__dict__['moduleId'])
        mmsg.AddMessage(MSG_KEY_PARAMS_MODULE_READ, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_MODULE_READ, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_PARAMS_MODULE_READ_INSTANCE)
        self.__dict__['moduleId'] = submsg.FindU32(MSG_KEY_PARAMS_MODULE_READ_MODULE_ID)


class ParamsModuleLoad:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['moduleId'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'moduleId':
            return self.__dict__['moduleId']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'moduleId':
            self.__dict__['moduleId'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_MODULE_LOAD_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_PARAMS_MODULE_LOAD_MODULE_ID, self.__dict__['moduleId'])
        mmsg.AddMessage(MSG_KEY_PARAMS_MODULE_LOAD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_MODULE_LOAD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_PARAMS_MODULE_LOAD_INSTANCE)
        self.__dict__['moduleId'] = submsg.FindU32(MSG_KEY_PARAMS_MODULE_LOAD_MODULE_ID)


class ParamsModuleFree:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['moduleHandle'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'moduleHandle':
            return self.__dict__['moduleHandle']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'moduleHandle':
            self.__dict__['moduleHandle'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_MODULE_FREE_INSTANCE, self.__dict__['instance'])
        submsg.AddU64(MSG_KEY_PARAMS_MODULE_FREE_MODULE_HANDLE, self.__dict__['moduleHandle'])
        mmsg.AddMessage(MSG_KEY_PARAMS_MODULE_FREE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_MODULE_FREE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_PARAMS_MODULE_FREE_INSTANCE)
        self.__dict__['moduleHandle'] = submsg.FindU64(MSG_KEY_PARAMS_MODULE_FREE_MODULE_HANDLE)


class ParamsDriverLoad:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['moduleId'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'moduleId':
            return self.__dict__['moduleId']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'moduleId':
            self.__dict__['moduleId'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_DRIVER_LOAD_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_PARAMS_DRIVER_LOAD_MODULE_ID, self.__dict__['moduleId'])
        mmsg.AddMessage(MSG_KEY_PARAMS_DRIVER_LOAD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_DRIVER_LOAD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_PARAMS_DRIVER_LOAD_INSTANCE)
        self.__dict__['moduleId'] = submsg.FindU32(MSG_KEY_PARAMS_DRIVER_LOAD_MODULE_ID)


class ParamsDriverUnload:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['moduleId'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'moduleId':
            return self.__dict__['moduleId']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'moduleId':
            self.__dict__['moduleId'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_DRIVER_UNLOAD_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_PARAMS_DRIVER_UNLOAD_MODULE_ID, self.__dict__['moduleId'])
        mmsg.AddMessage(MSG_KEY_PARAMS_DRIVER_UNLOAD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_DRIVER_UNLOAD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_PARAMS_DRIVER_UNLOAD_INSTANCE)
        self.__dict__['moduleId'] = submsg.FindU32(MSG_KEY_PARAMS_DRIVER_UNLOAD_MODULE_ID)


class ParamsProcessLoad:

    def __init__(self):
        self.__dict__['instance'] = 0
        self.__dict__['processId'] = 0

    def __getattr__(self, name):
        if name == 'instance':
            return self.__dict__['instance']
        if name == 'processId':
            return self.__dict__['processId']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'instance':
            self.__dict__['instance'] = value
        elif name == 'processId':
            self.__dict__['processId'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_PROCESS_LOAD_INSTANCE, self.__dict__['instance'])
        submsg.AddU32(MSG_KEY_PARAMS_PROCESS_LOAD_PROCESS_ID, self.__dict__['processId'])
        mmsg.AddMessage(MSG_KEY_PARAMS_PROCESS_LOAD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_PROCESS_LOAD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['instance'] = submsg.FindU32(MSG_KEY_PARAMS_PROCESS_LOAD_INSTANCE)
        self.__dict__['processId'] = submsg.FindU32(MSG_KEY_PARAMS_PROCESS_LOAD_PROCESS_ID)