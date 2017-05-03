# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import array
RESULT_HASH_TYPE_MD5 = 1
RESULT_HASH_TYPE_SHA1 = 2
RESULT_HASH_TYPE_SHA256 = 3
RESULT_HASH_TYPE_SHA512 = 4
RESULT_TOKEN_TYPE_INVALID = 0
RESULT_TOKEN_TYPE_USER = 1
RESULT_TOKEN_TYPE_GROUP = 2
RESULT_TOKEN_TYPE_DOMAIN = 3
RESULT_TOKEN_TYPE_ALIAS = 4
RESULT_TOKEN_TYPE_WELLKNOWN_GROUP = 5
RESULT_TOKEN_TYPE_DELETED_ACCOUNT = 6
RESULT_TOKEN_TYPE_UNKNOWN = 7
RESULT_TOKEN_TYPE_COMPUTER = 8
RESULT_PRIV_ATTRIBUTE_ENABLED_BY_DEFAULT = 1
RESULT_PRIV_ATTRIBUTE_ENABLED = 2
RESULT_PRIV_ATTRIBUTE_REMOVED = 4
RESULT_PRIV_ATTRIBUTE_USED_FOR_ACCESS = 8
RESULT_TOKEN_ATTRIBUTE_MANDATORY = 1
RESULT_TOKEN_ATTRIBUTE_ENABLED_BY_DEFAULT = 2
RESULT_TOKEN_ATTRIBUTE_ENABLED = 4
RESULT_TOKEN_ATTRIBUTE_OWNER = 8
RESULT_TOKEN_ATTRIBUTE_USE_FOR_DENY_ONLY = 16
RESULT_TOKEN_ATTRIBUTE_LOGON_ID = 32
RESULT_TOKEN_ATTRIBUTE_RESOURCE = 64

class ProcessResult:

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
        submsg.AddU32(MSG_KEY_RESULT_PROCESS_ID, self.__dict__['id'])
        mmsg.AddMessage(MSG_KEY_RESULT_PROCESS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_PROCESS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['id'] = submsg.FindU32(MSG_KEY_RESULT_PROCESS_ID)


class TokenResult:

    def __init__(self):
        self.__dict__['name'] = ''
        self.__dict__['type'] = RESULT_TOKEN_TYPE_INVALID
        self.__dict__['attributes'] = 0

    def __getattr__(self, name):
        if name == 'name':
            return self.__dict__['name']
        if name == 'type':
            return self.__dict__['type']
        if name == 'attributes':
            return self.__dict__['attributes']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'name':
            self.__dict__['name'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        elif name == 'attributes':
            self.__dict__['attributes'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TOKEN_NAME, self.__dict__['name'])
        submsg.AddU8(MSG_KEY_RESULT_TOKEN_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_RESULT_TOKEN_ATTRIBUTES, self.__dict__['attributes'])
        mmsg.AddMessage(MSG_KEY_RESULT_TOKEN, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TOKEN, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_TOKEN_NAME)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_TOKEN_TYPE)
        self.__dict__['attributes'] = submsg.FindU32(MSG_KEY_RESULT_TOKEN_ATTRIBUTES)


class ProcessBasicInfoResult:

    def __init__(self):
        self.__dict__['user'] = TokenResult()
        self.__dict__['owner'] = TokenResult()
        self.__dict__['group'] = TokenResult()

    def __getattr__(self, name):
        if name == 'user':
            return self.__dict__['user']
        if name == 'owner':
            return self.__dict__['owner']
        if name == 'group':
            return self.__dict__['group']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'user':
            self.__dict__['user'] = value
        elif name == 'owner':
            self.__dict__['owner'] = value
        elif name == 'group':
            self.__dict__['group'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg2 = MarshalMessage()
        self.__dict__['user'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_RESULT_PROCESS_BASIC_INFO_USER, submsg2)
        submsg2 = MarshalMessage()
        self.__dict__['owner'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_RESULT_PROCESS_BASIC_INFO_OWNER, submsg2)
        submsg2 = MarshalMessage()
        self.__dict__['group'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_RESULT_PROCESS_BASIC_INFO_GROUP, submsg2)
        mmsg.AddMessage(MSG_KEY_RESULT_PROCESS_BASIC_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_PROCESS_BASIC_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        submsg2 = submsg.FindMessage(MSG_KEY_RESULT_PROCESS_BASIC_INFO_USER)
        self.__dict__['user'].Demarshal(submsg2)
        submsg2 = submsg.FindMessage(MSG_KEY_RESULT_PROCESS_BASIC_INFO_OWNER)
        self.__dict__['owner'].Demarshal(submsg2)
        submsg2 = submsg.FindMessage(MSG_KEY_RESULT_PROCESS_BASIC_INFO_GROUP)
        self.__dict__['group'].Demarshal(submsg2)


class PrivilegeResult:

    def __init__(self):
        self.__dict__['attributes'] = 0
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'attributes':
            return self.__dict__['attributes']
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'attributes':
            self.__dict__['attributes'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_PRIVILEGE_ATTRIBUTES, self.__dict__['attributes'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_PRIVILEGE_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_RESULT_PRIVILEGE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_PRIVILEGE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['attributes'] = submsg.FindU32(MSG_KEY_RESULT_PRIVILEGE_ATTRIBUTES)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_PRIVILEGE_NAME)


class ModuleResult:

    def __init__(self):
        self.__dict__['baseAddress'] = 0
        self.__dict__['entryPoint'] = 0
        self.__dict__['imageSize'] = 0
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'baseAddress':
            return self.__dict__['baseAddress']
        if name == 'entryPoint':
            return self.__dict__['entryPoint']
        if name == 'imageSize':
            return self.__dict__['imageSize']
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'baseAddress':
            self.__dict__['baseAddress'] = value
        elif name == 'entryPoint':
            self.__dict__['entryPoint'] = value
        elif name == 'imageSize':
            self.__dict__['imageSize'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_MODULE_INFO_BASE_ADDRESS, self.__dict__['baseAddress'])
        submsg.AddU64(MSG_KEY_RESULT_MODULE_INFO_ENTRY_POINT, self.__dict__['entryPoint'])
        submsg.AddU64(MSG_KEY_RESULT_MODULE_INFO_IMAGE_SIZE, self.__dict__['imageSize'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_MODULE_INFO_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_RESULT_MODULE_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MODULE_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['baseAddress'] = submsg.FindU64(MSG_KEY_RESULT_MODULE_INFO_BASE_ADDRESS)
        self.__dict__['entryPoint'] = submsg.FindU64(MSG_KEY_RESULT_MODULE_INFO_ENTRY_POINT)
        self.__dict__['imageSize'] = submsg.FindU64(MSG_KEY_RESULT_MODULE_INFO_IMAGE_SIZE)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_MODULE_INFO_NAME)


class HashResult:

    def __init__(self):
        self.__dict__['hashType'] = 0
        self.__dict__['hash'] = array.array('B')

    def __getattr__(self, name):
        if name == 'hashType':
            return self.__dict__['hashType']
        if name == 'hash':
            return self.__dict__['hash']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'hashType':
            self.__dict__['hashType'] = value
        elif name == 'hash':
            self.__dict__['hash'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_MODULE_HASH_TYPE, self.__dict__['hashType'])
        submsg.AddData(MSG_KEY_RESULT_MODULE_HASH_VALUE, self.__dict__['hash'])
        mmsg.AddMessage(MSG_KEY_RESULT_MODULE_HASH, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MODULE_HASH, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['hashType'] = submsg.FindU8(MSG_KEY_RESULT_MODULE_HASH_TYPE)
        self.__dict__['hash'] = submsg.FindData(MSG_KEY_RESULT_MODULE_HASH_VALUE)