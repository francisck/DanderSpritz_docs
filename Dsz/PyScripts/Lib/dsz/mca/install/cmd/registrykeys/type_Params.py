# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import array
PARAMS_HIVE_USERS = 1
PARAMS_HIVE_LOCAL_MACHINE = 2
PARAMS_HIVE_CURRENT_USER = 3
PARAMS_HIVE_CURRENT_CONFIG = 4
PARAMS_HIVE_CLASSES_ROOT = 5
PARAMS_TYPE_REG_NONE = 0
PARAMS_TYPE_REG_SZ = 1
PARAMS_TYPE_REG_EXPAND_SZ = 2
PARAMS_TYPE_REG_BINARY = 3
PARAMS_TYPE_REG_DWORD = 4
PARAMS_TYPE_REG_DWORD_LITTLE_ENDIAN = 4
PARAMS_TYPE_REG_DWORD_BIG_ENDIAN = 5
PARAMS_TYPE_REG_LINK = 6
PARAMS_TYPE_REG_MULTI_SZ = 7
PARAMS_TYPE_REG_RESOURCE_LIST = 8
PARAMS_TYPE_REG_FULL_RESOURCE_DESCRIPTOR = 9
PARAMS_TYPE_REG_RESOURCE_REQUIREMENTS_LIST = 10
PARAMS_ADD_FLAG_USE_WOW64_64 = 1
PARAMS_ADD_FLAG_USE_WOW64_32 = 2
PARAMS_ADD_FLAG_VOLATILE = 4
PARAMS_DELETE_FLAG_USE_WOW64_64 = 1
PARAMS_DELETE_FLAG_USE_WOW64_32 = 2

class ParamsAdd:

    def __init__(self):
        self.__dict__['hive'] = 0
        self.__dict__['type'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['key'] = ''
        self.__dict__['value'] = ''
        self.__dict__['target'] = ''
        self.__dict__['data'] = array.array('B')
        self.__dict__['provider'] = 0

    def __getattr__(self, name):
        if name == 'hive':
            return self.__dict__['hive']
        if name == 'type':
            return self.__dict__['type']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'key':
            return self.__dict__['key']
        if name == 'value':
            return self.__dict__['value']
        if name == 'target':
            return self.__dict__['target']
        if name == 'data':
            return self.__dict__['data']
        if name == 'provider':
            return self.__dict__['provider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'hive':
            self.__dict__['hive'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'key':
            self.__dict__['key'] = value
        elif name == 'value':
            self.__dict__['value'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        elif name == 'data':
            self.__dict__['data'] = value
        elif name == 'provider':
            self.__dict__['provider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_ADD_HIVE, self.__dict__['hive'])
        submsg.AddU32(MSG_KEY_PARAMS_ADD_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_PARAMS_ADD_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_ADD_KEY, self.__dict__['key'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_ADD_VALUE, self.__dict__['value'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_ADD_TARGET, self.__dict__['target'])
        submsg.AddData(MSG_KEY_PARAMS_ADD_DATA, self.__dict__['data'])
        submsg.AddU32(MSG_KEY_PARAMS_ADD_PROVIDER, self.__dict__['provider'])
        mmsg.AddMessage(MSG_KEY_PARAMS_ADD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_ADD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['hive'] = submsg.FindU8(MSG_KEY_PARAMS_ADD_HIVE)
        self.__dict__['type'] = submsg.FindU32(MSG_KEY_PARAMS_ADD_TYPE)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_PARAMS_ADD_FLAGS)
        self.__dict__['key'] = submsg.FindString(MSG_KEY_PARAMS_ADD_KEY)
        self.__dict__['value'] = submsg.FindString(MSG_KEY_PARAMS_ADD_VALUE)
        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_ADD_TARGET)
        except:
            pass

        self.__dict__['data'] = submsg.FindData(MSG_KEY_PARAMS_ADD_DATA)
        try:
            self.__dict__['provider'] = submsg.FindU32(MSG_KEY_PARAMS_ADD_PROVIDER)
        except:
            pass


class ParamsDelete:

    def __init__(self):
        self.__dict__['deleteValue'] = False
        self.__dict__['hive'] = 0
        self.__dict__['recursive'] = False
        self.__dict__['flags'] = 0
        self.__dict__['key'] = ''
        self.__dict__['value'] = ''
        self.__dict__['target'] = ''
        self.__dict__['provider'] = 0

    def __getattr__(self, name):
        if name == 'deleteValue':
            return self.__dict__['deleteValue']
        if name == 'hive':
            return self.__dict__['hive']
        if name == 'recursive':
            return self.__dict__['recursive']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'key':
            return self.__dict__['key']
        if name == 'value':
            return self.__dict__['value']
        if name == 'target':
            return self.__dict__['target']
        if name == 'provider':
            return self.__dict__['provider']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'deleteValue':
            self.__dict__['deleteValue'] = value
        elif name == 'hive':
            self.__dict__['hive'] = value
        elif name == 'recursive':
            self.__dict__['recursive'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'key':
            self.__dict__['key'] = value
        elif name == 'value':
            self.__dict__['value'] = value
        elif name == 'target':
            self.__dict__['target'] = value
        elif name == 'provider':
            self.__dict__['provider'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_PARAMS_DELETE_VALUE_DELETE, self.__dict__['deleteValue'])
        submsg.AddU8(MSG_KEY_PARAMS_DELETE_HIVE, self.__dict__['hive'])
        submsg.AddBool(MSG_KEY_PARAMS_DELETE_RECURSIVE, self.__dict__['recursive'])
        submsg.AddU32(MSG_KEY_PARAMS_DELETE_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DELETE_KEY, self.__dict__['key'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DELETE_VALUE, self.__dict__['value'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DELETE_TARGET, self.__dict__['target'])
        submsg.AddU32(MSG_KEY_PARAMS_DELETE_PROVIDER, self.__dict__['provider'])
        mmsg.AddMessage(MSG_KEY_PARAMS_DELETE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_DELETE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['deleteValue'] = submsg.FindBool(MSG_KEY_PARAMS_DELETE_VALUE_DELETE)
        self.__dict__['hive'] = submsg.FindU8(MSG_KEY_PARAMS_DELETE_HIVE)
        self.__dict__['recursive'] = submsg.FindBool(MSG_KEY_PARAMS_DELETE_RECURSIVE)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_PARAMS_DELETE_FLAGS)
        self.__dict__['key'] = submsg.FindString(MSG_KEY_PARAMS_DELETE_KEY)
        self.__dict__['value'] = submsg.FindString(MSG_KEY_PARAMS_DELETE_VALUE)
        try:
            self.__dict__['target'] = submsg.FindString(MSG_KEY_PARAMS_DELETE_TARGET)
        except:
            pass

        try:
            self.__dict__['provider'] = submsg.FindU32(MSG_KEY_PARAMS_DELETE_PROVIDER)
        except:
            pass