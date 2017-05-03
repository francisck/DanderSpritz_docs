# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
RESULT_LIST_TYPE_UNKNOWN = 0
RESULT_LIST_TYPE_WILDCARD = 1
RESULT_LIST_TYPE_DISK_DEVICE = 2
RESULT_LIST_TYPE_SPOOL_DEVICE = 3
RESULT_LIST_TYPE_IPC = 4
RESULT_LIST_STATUS_UNKNOWN = 0
RESULT_LIST_STATUS_OK = 1
RESULT_LIST_STATUS_PAUSED = 2
RESULT_LIST_STATUS_DISCONNECTED = 3
RESULT_LIST_STATUS_NETWORK_ERROR = 4
RESULT_LIST_STATUS_CONNECTING = 5
RESULT_LIST_STATUS_RECONNECTING = 6
RESULT_QUERY_TYPE_UNKNOWN = 0
RESULT_QUERY_TYPE_ANY = 1
RESULT_QUERY_TYPE_DISK = 2
RESULT_QUERY_TYPE_PRINT = 3
RESULT_QUERY_TYPE_DEVICE = 4
RESULT_QUERY_TYPE_IPC = 5

class ResultMap:

    def __init__(self):
        self.__dict__['resourcePath'] = ''
        self.__dict__['resourceName'] = ''

    def __getattr__(self, name):
        if name == 'resourcePath':
            return self.__dict__['resourcePath']
        if name == 'resourceName':
            return self.__dict__['resourceName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'resourcePath':
            self.__dict__['resourcePath'] = value
        elif name == 'resourceName':
            self.__dict__['resourceName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_MAP_RESOURCE_PATH, self.__dict__['resourcePath'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_MAP_RESOURCE_NAME, self.__dict__['resourceName'])
        mmsg.AddMessage(MSG_KEY_RESULT_MAP, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_MAP, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['resourcePath'] = submsg.FindString(MSG_KEY_RESULT_MAP_RESOURCE_PATH)
        self.__dict__['resourceName'] = submsg.FindString(MSG_KEY_RESULT_MAP_RESOURCE_NAME)


class ResultList:

    def __init__(self):
        self.__dict__['local'] = ''
        self.__dict__['remote'] = ''
        self.__dict__['password'] = ''
        self.__dict__['status'] = 0
        self.__dict__['type'] = 0
        self.__dict__['referenceCount'] = 0
        self.__dict__['useCount'] = 0
        self.__dict__['username'] = ''
        self.__dict__['domainName'] = ''

    def __getattr__(self, name):
        if name == 'local':
            return self.__dict__['local']
        if name == 'remote':
            return self.__dict__['remote']
        if name == 'password':
            return self.__dict__['password']
        if name == 'status':
            return self.__dict__['status']
        if name == 'type':
            return self.__dict__['type']
        if name == 'referenceCount':
            return self.__dict__['referenceCount']
        if name == 'useCount':
            return self.__dict__['useCount']
        if name == 'username':
            return self.__dict__['username']
        if name == 'domainName':
            return self.__dict__['domainName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'local':
            self.__dict__['local'] = value
        elif name == 'remote':
            self.__dict__['remote'] = value
        elif name == 'password':
            self.__dict__['password'] = value
        elif name == 'status':
            self.__dict__['status'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        elif name == 'referenceCount':
            self.__dict__['referenceCount'] = value
        elif name == 'useCount':
            self.__dict__['useCount'] = value
        elif name == 'username':
            self.__dict__['username'] = value
        elif name == 'domainName':
            self.__dict__['domainName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_LIST_LOCAL, self.__dict__['local'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_LIST_REMOTE, self.__dict__['remote'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_LIST_PASSWORD, self.__dict__['password'])
        submsg.AddU8(MSG_KEY_RESULT_LIST_STATUS, self.__dict__['status'])
        submsg.AddU8(MSG_KEY_RESULT_LIST_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_RESULT_LIST_REFERENCE_COUNT, self.__dict__['referenceCount'])
        submsg.AddU32(MSG_KEY_RESULT_LIST_USE_COUNT, self.__dict__['useCount'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_LIST_USERNAME, self.__dict__['username'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_LIST_DOMAIN, self.__dict__['domainName'])
        mmsg.AddMessage(MSG_KEY_RESULT_LIST, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_LIST, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['local'] = submsg.FindString(MSG_KEY_RESULT_LIST_LOCAL)
        self.__dict__['remote'] = submsg.FindString(MSG_KEY_RESULT_LIST_REMOTE)
        self.__dict__['password'] = submsg.FindString(MSG_KEY_RESULT_LIST_PASSWORD)
        self.__dict__['status'] = submsg.FindU8(MSG_KEY_RESULT_LIST_STATUS)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_LIST_TYPE)
        self.__dict__['referenceCount'] = submsg.FindU32(MSG_KEY_RESULT_LIST_REFERENCE_COUNT)
        self.__dict__['useCount'] = submsg.FindU32(MSG_KEY_RESULT_LIST_USE_COUNT)
        self.__dict__['username'] = submsg.FindString(MSG_KEY_RESULT_LIST_USERNAME)
        self.__dict__['domainName'] = submsg.FindString(MSG_KEY_RESULT_LIST_DOMAIN)


class ResultQuery:

    def __init__(self):
        self.__dict__['name'] = ''
        self.__dict__['path'] = ''
        self.__dict__['hasPath'] = False
        self.__dict__['type'] = RESULT_QUERY_TYPE_UNKNOWN
        self.__dict__['admin'] = False
        self.__dict__['caption'] = ''
        self.__dict__['description'] = ''

    def __getattr__(self, name):
        if name == 'name':
            return self.__dict__['name']
        if name == 'path':
            return self.__dict__['path']
        if name == 'hasPath':
            return self.__dict__['hasPath']
        if name == 'type':
            return self.__dict__['type']
        if name == 'admin':
            return self.__dict__['admin']
        if name == 'caption':
            return self.__dict__['caption']
        if name == 'description':
            return self.__dict__['description']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'name':
            self.__dict__['name'] = value
        elif name == 'path':
            self.__dict__['path'] = value
        elif name == 'hasPath':
            self.__dict__['hasPath'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        elif name == 'admin':
            self.__dict__['admin'] = value
        elif name == 'caption':
            self.__dict__['caption'] = value
        elif name == 'description':
            self.__dict__['description'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_QUERY_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_QUERY_PATH, self.__dict__['path'])
        submsg.AddBool(MSG_KEY_RESULT_QUERY_HAS_PATH, self.__dict__['hasPath'])
        submsg.AddU8(MSG_KEY_RESULT_QUERY_TYPE, self.__dict__['type'])
        submsg.AddBool(MSG_KEY_RESULT_QUERY_ADMIN, self.__dict__['admin'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_QUERY_CAPTION, self.__dict__['caption'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_QUERY_DESCRIPTION, self.__dict__['description'])
        mmsg.AddMessage(MSG_KEY_RESULT_QUERY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_QUERY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_QUERY_NAME)
        self.__dict__['path'] = submsg.FindString(MSG_KEY_RESULT_QUERY_PATH)
        self.__dict__['hasPath'] = submsg.FindBool(MSG_KEY_RESULT_QUERY_HAS_PATH)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_QUERY_TYPE)
        self.__dict__['admin'] = submsg.FindBool(MSG_KEY_RESULT_QUERY_ADMIN)
        self.__dict__['caption'] = submsg.FindString(MSG_KEY_RESULT_QUERY_CAPTION)
        self.__dict__['description'] = submsg.FindString(MSG_KEY_RESULT_QUERY_DESCRIPTION)