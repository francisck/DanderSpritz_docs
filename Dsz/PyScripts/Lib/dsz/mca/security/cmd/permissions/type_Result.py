# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
RESULT_DACL_ACE = 1
RESULT_SACL_ACE = 2
RESULT_SD_FLAG_DACL_AUTO_INHERIT_REQ = 1
RESULT_SD_FLAG_DACL_AUTO_INHERITED = 2
RESULT_SD_FLAG_DACL_DEFAULTED = 4
RESULT_SD_FLAG_DACL_PRESENT = 8
RESULT_SD_FLAG_DACL_PROTECTED = 16
RESULT_SD_FLAG_GROUP_DEFAULTED = 32
RESULT_SD_FLAG_OWNER_DEFAULTED = 64
RESULT_SD_FLAG_RM_CONTROL_VALID = 128
RESULT_SD_FLAG_SACL_AUTO_INHERIT_REQ = 256
RESULT_SD_FLAG_SACL_AUTO_INHERITED = 512
RESULT_SD_FLAG_SACL_DEFAULTED = 1024
RESULT_SD_FLAG_SACL_PRESENT = 2048
RESULT_SD_FLAG_SACL_PROTECTED = 4096
RESULT_SD_FLAG_SELF_RELATIVE = 8192
WINDOWS_OS_DEFINE_SUCCESSFUL_ACCESS_ACE_FLAG = 64
WINDOWS_OS_DEFINE_FAILED_ACCESS_ACE_FLAG = 128
WINDOWS_OS_DEFINE_OBJECT_INHERIT_ACE = 1
WINDOWS_OS_DEFINE_CONTAINER_INHERIT_ACE = 2
WINDOWS_OS_DEFINE_NO_PROPAGATE_INHERIT_ACE = 4
WINDOWS_OS_DEFINE_INHERIT_ONLY_ACE = 8
WINDOWS_OS_DEFINE_INHERITED_ACE = 16
WINDOWS_OS_DEFINE_DELETE = 65536
WINDOWS_OS_DEFINE_READ_CONTROL = 131072
WINDOWS_OS_DEFINE_WRITE_DAC = 262144
WINDOWS_OS_DEFINE_WRITE_OWNER = 524288
WINDOWS_OS_DEFINE_SYNCHRONIZE = 1048576
WINDOWS_OS_DEFINE_GENERIC_READ = 2147483648L
WINDOWS_OS_DEFINE_GENERIC_WRITE = 1073741824
WINDOWS_OS_DEFINE_GENERIC_EXECUTE = 536870912
WINDOWS_OS_DEFINE_GENERIC_ALL = 268435456
WINDOWS_OS_DEFINE_FILE_READ_DATA = 1
WINDOWS_OS_DEFINE_FILE_WRITE_DATA = 2
WINDOWS_OS_DEFINE_FILE_APPEND_DATA = 4
WINDOWS_OS_DEFINE_FILE_READ_EA = 8
WINDOWS_OS_DEFINE_FILE_WRITE_EA = 16
WINDOWS_OS_DEFINE_FILE_EXECUTE = 32
WINDOWS_OS_DEFINE_FILE_DELETE_CHILD = 64
WINDOWS_OS_DEFINE_FILE_READ_ATTRIBUTES = 128
WINDOWS_OS_DEFINE_FILE_WRITE_ATTRIBUTES = 256
WINDOWS_OS_DEFINE_ACCESS_ALLOWED_ACE_TYPE = 0
WINDOWS_OS_DEFINE_ACCESS_DENIED_ACE_TYPE = 1
WINDOWS_OS_DEFINE_SYSTEM_AUDIT_ACE_TYPE = 2
WINDOWS_OS_DEFINE_SYSTEM_ALARM_ACE_TYPE = 3
WINDOWS_OS_DEFINE_ACCESS_ALLOWED_COMPOUND_ACE_TYPE = 4
WINDOWS_OS_DEFINE_ACCESS_ALLOWED_OBJECT_ACE_TYPE = 5
WINDOWS_OS_DEFINE_ACCESS_DENIED_OBJECT_ACE_TYPE = 6
WINDOWS_OS_DEFINE_SYSTEM_AUDIT_OBJECT_ACE_TYPE = 7
WINDOWS_OS_DEFINE_SYSTEM_ALARM_OBJECT_ACE_TYPE = 8
WINDOWS_OS_DEFINE_ACCESS_ALLOWED_CALLBACK_ACE_TYPE = 9
WINDOWS_OS_DEFINE_ACCESS_DENIED_CALLBACK_ACE_TYPE = 10
WINDOWS_OS_DEFINE_ACCESS_ALLOWED_CALLBACK_OBJECT_ACE_TYPE = 11
WINDOWS_OS_DEFINE_ACCESS_DENIED_CALLBACK_OBJECT_ACE_TYPE = 12
WINDOWS_OS_DEFINE_SYSTEM_AUDIT_CALLBACK_ACE_TYPE = 13
WINDOWS_OS_DEFINE_SYSTEM_ALARM_CALLBACK_ACE_TYPE = 14
WINDOWS_OS_DEFINE_SYSTEM_AUDIT_CALLBACK_OBJECT_ACE_TYPE = 15
WINDOWS_OS_DEFINE_SYSTEM_ALARM_CALLBACK_OBJECT_ACE_TYPE = 16
WINDOWS_OS_DEFINE_SYSTEM_MANDATORY_LABEL_ACE_TYPE = 17

class ResultQueryInfo:

    def __init__(self):
        self.__dict__['type'] = 0
        self.__dict__['objectType'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['object'] = ''
        self.__dict__['account'] = ''
        self.__dict__['group'] = ''
        self.__dict__['acctDomain'] = ''
        self.__dict__['groupDomain'] = ''
        self.__dict__['permString'] = ''

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'objectType':
            return self.__dict__['objectType']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'object':
            return self.__dict__['object']
        if name == 'account':
            return self.__dict__['account']
        if name == 'group':
            return self.__dict__['group']
        if name == 'acctDomain':
            return self.__dict__['acctDomain']
        if name == 'groupDomain':
            return self.__dict__['groupDomain']
        if name == 'permString':
            return self.__dict__['permString']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'objectType':
            self.__dict__['objectType'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'object':
            self.__dict__['object'] = value
        elif name == 'account':
            self.__dict__['account'] = value
        elif name == 'group':
            self.__dict__['group'] = value
        elif name == 'acctDomain':
            self.__dict__['acctDomain'] = value
        elif name == 'groupDomain':
            self.__dict__['groupDomain'] = value
        elif name == 'permString':
            self.__dict__['permString'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_QUERY_INFO_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_RESULT_QUERY_INFO_OBJECT_TYPE, self.__dict__['objectType'])
        submsg.AddU32(MSG_KEY_RESULT_QUERY_INFO_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_QUERY_INFO_OBJECT, self.__dict__['object'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_QUERY_INFO_ACCOUNT, self.__dict__['account'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_QUERY_INFO_GROUP, self.__dict__['group'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_QUERY_INFO_ACCOUNT_DOMAIN, self.__dict__['acctDomain'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_QUERY_INFO_GROUP_DOMAIN, self.__dict__['groupDomain'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_QUERY_INFO_PERMISSIONS_STRING, self.__dict__['permString'])
        mmsg.AddMessage(MSG_KEY_RESULT_QUERY_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_QUERY_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_QUERY_INFO_TYPE)
        self.__dict__['objectType'] = submsg.FindU32(MSG_KEY_RESULT_QUERY_INFO_OBJECT_TYPE)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_QUERY_INFO_FLAGS)
        self.__dict__['object'] = submsg.FindString(MSG_KEY_RESULT_QUERY_INFO_OBJECT)
        self.__dict__['account'] = submsg.FindString(MSG_KEY_RESULT_QUERY_INFO_ACCOUNT)
        self.__dict__['group'] = submsg.FindString(MSG_KEY_RESULT_QUERY_INFO_GROUP)
        self.__dict__['acctDomain'] = submsg.FindString(MSG_KEY_RESULT_QUERY_INFO_ACCOUNT_DOMAIN)
        self.__dict__['groupDomain'] = submsg.FindString(MSG_KEY_RESULT_QUERY_INFO_GROUP_DOMAIN)
        self.__dict__['permString'] = submsg.FindString(MSG_KEY_RESULT_QUERY_INFO_PERMISSIONS_STRING)


class ResultAce:

    def __init__(self):
        self.__dict__['aceType'] = 0
        self.__dict__['type'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['accessMask'] = 0
        self.__dict__['user'] = ''
        self.__dict__['domain'] = ''

    def __getattr__(self, name):
        if name == 'aceType':
            return self.__dict__['aceType']
        if name == 'type':
            return self.__dict__['type']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'accessMask':
            return self.__dict__['accessMask']
        if name == 'user':
            return self.__dict__['user']
        if name == 'domain':
            return self.__dict__['domain']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'aceType':
            self.__dict__['aceType'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'accessMask':
            self.__dict__['accessMask'] = value
        elif name == 'user':
            self.__dict__['user'] = value
        elif name == 'domain':
            self.__dict__['domain'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_ACE_ACE_TYPE, self.__dict__['aceType'])
        submsg.AddU8(MSG_KEY_RESULT_ACE_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_RESULT_ACE_FLAGS, self.__dict__['flags'])
        submsg.AddU32(MSG_KEY_RESULT_ACE_ACCESS_MASK, self.__dict__['accessMask'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_ACE_USER, self.__dict__['user'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_ACE_DOMAIN, self.__dict__['domain'])
        mmsg.AddMessage(MSG_KEY_RESULT_ACE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_ACE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['aceType'] = submsg.FindU8(MSG_KEY_RESULT_ACE_ACE_TYPE)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_ACE_TYPE)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_ACE_FLAGS)
        self.__dict__['accessMask'] = submsg.FindU32(MSG_KEY_RESULT_ACE_ACCESS_MASK)
        self.__dict__['user'] = submsg.FindString(MSG_KEY_RESULT_ACE_USER)
        self.__dict__['domain'] = submsg.FindString(MSG_KEY_RESULT_ACE_DOMAIN)


class ResultModify:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['accessMask'] = 0

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'accessMask':
            return self.__dict__['accessMask']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'accessMask':
            self.__dict__['accessMask'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_MODIFY_FLAGS, self.__dict__['flags'])
        submsg.AddU32(MSG_KEY_RESULT_MODIFY_ACCESS_MASK, self.__dict__['accessMask'])
        mmsg.AddMessage(MSG_KEY_RESULT_MODIFY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MODIFY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_MODIFY_FLAGS)
        self.__dict__['accessMask'] = submsg.FindU32(MSG_KEY_RESULT_MODIFY_ACCESS_MASK)