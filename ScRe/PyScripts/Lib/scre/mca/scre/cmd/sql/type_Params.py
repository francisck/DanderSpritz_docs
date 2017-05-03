# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_CONNECT_FLAG_AUTOCOMMIT = 1
PARAMS_CONNECT_FLAG_USE_EXISTING = 2

class ParamsConnect:

    def __init__(self):
        self.__dict__['connectionString'] = ''
        self.__dict__['flags'] = PARAMS_CONNECT_FLAG_AUTOCOMMIT
        self.__dict__['accessType'] = SQL_ACCESS_TYPE_READ_ONLY
        self.__dict__['timeoutSeconds'] = 10800

    def __getattr__(self, name):
        if name == 'connectionString':
            return self.__dict__['connectionString']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'accessType':
            return self.__dict__['accessType']
        if name == 'timeoutSeconds':
            return self.__dict__['timeoutSeconds']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'connectionString':
            self.__dict__['connectionString'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'accessType':
            self.__dict__['accessType'] = value
        elif name == 'timeoutSeconds':
            self.__dict__['timeoutSeconds'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_PARAMS_CONNECT_CONNECTION_STRING, self.__dict__['connectionString'])
        submsg.AddU16(MSG_KEY_PARAMS_CONNECT_FLAGS, self.__dict__['flags'])
        submsg.AddU8(MSG_KEY_PARAMS_CONNECT_ACCESS_TYPE, self.__dict__['accessType'])
        submsg.AddU32(MSG_KEY_PARAMS_CONNECT_TIMEOUT, self.__dict__['timeoutSeconds'])
        mmsg.AddMessage(MSG_KEY_PARAMS_CONNECT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_CONNECT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['connectionString'] = submsg.FindString(MSG_KEY_PARAMS_CONNECT_CONNECTION_STRING)
        try:
            self.__dict__['flags'] = submsg.FindU16(MSG_KEY_PARAMS_CONNECT_FLAGS)
        except:
            pass

        try:
            self.__dict__['accessType'] = submsg.FindU8(MSG_KEY_PARAMS_CONNECT_ACCESS_TYPE)
        except:
            pass

        try:
            self.__dict__['timeoutSeconds'] = submsg.FindU32(MSG_KEY_PARAMS_CONNECT_TIMEOUT)
        except:
            pass


class ParamsQueryBase:

    def __init__(self):
        self.__dict__['connectInfo'] = ParamsConnect()
        self.__dict__['maxColumnSize'] = 64000
        self.__dict__['chunkSize'] = 66560

    def __getattr__(self, name):
        if name == 'connectInfo':
            return self.__dict__['connectInfo']
        if name == 'maxColumnSize':
            return self.__dict__['maxColumnSize']
        if name == 'chunkSize':
            return self.__dict__['chunkSize']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'connectInfo':
            self.__dict__['connectInfo'] = value
        elif name == 'maxColumnSize':
            self.__dict__['maxColumnSize'] = value
        elif name == 'chunkSize':
            self.__dict__['chunkSize'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg2 = MarshalMessage()
        self.__dict__['connectInfo'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_PARAMS_QUERY_BASE_CONNECTION_INFO, submsg2)
        submsg.AddU32(MSG_KEY_PARAMS_QUERY_BASE_MAX_COLUMN_SIZE, self.__dict__['maxColumnSize'])
        submsg.AddU32(MSG_KEY_PARAMS_QUERY_BASE_MAX_CHUNK_SIZE, self.__dict__['chunkSize'])
        mmsg.AddMessage(MSG_KEY_PARAMS_QUERY_BASE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_QUERY_BASE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        submsg2 = submsg.FindMessage(MSG_KEY_PARAMS_QUERY_BASE_CONNECTION_INFO)
        self.__dict__['connectInfo'].Demarshal(submsg2)
        try:
            self.__dict__['maxColumnSize'] = submsg.FindU32(MSG_KEY_PARAMS_QUERY_BASE_MAX_COLUMN_SIZE)
        except:
            pass

        try:
            self.__dict__['chunkSize'] = submsg.FindU32(MSG_KEY_PARAMS_QUERY_BASE_MAX_CHUNK_SIZE)
        except:
            pass


class ParamsQueryColumns:

    def __init__(self):
        self.__dict__['baseInfo'] = ParamsQueryBase()
        self.__dict__['tableName'] = ''

    def __getattr__(self, name):
        if name == 'baseInfo':
            return self.__dict__['baseInfo']
        if name == 'tableName':
            return self.__dict__['tableName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'baseInfo':
            self.__dict__['baseInfo'] = value
        elif name == 'tableName':
            self.__dict__['tableName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg2 = MarshalMessage()
        self.__dict__['baseInfo'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_PARAMS_QUERY_COLUMNS_BASE_INFO, submsg2)
        submsg.AddStringUtf8(MSG_KEY_PARAMS_QUERY_COLUMNS_TABLE_NAME, self.__dict__['tableName'])
        mmsg.AddMessage(MSG_KEY_PARAMS_QUERY_COLUMNS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_QUERY_COLUMNS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        submsg2 = submsg.FindMessage(MSG_KEY_PARAMS_QUERY_COLUMNS_BASE_INFO)
        self.__dict__['baseInfo'].Demarshal(submsg2)
        self.__dict__['tableName'] = submsg.FindString(MSG_KEY_PARAMS_QUERY_COLUMNS_TABLE_NAME)


class ParamsQueryStatement:

    def __init__(self):
        self.__dict__['baseInfo'] = ParamsQueryBase()
        self.__dict__['queryString'] = ''

    def __getattr__(self, name):
        if name == 'baseInfo':
            return self.__dict__['baseInfo']
        if name == 'queryString':
            return self.__dict__['queryString']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'baseInfo':
            self.__dict__['baseInfo'] = value
        elif name == 'queryString':
            self.__dict__['queryString'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg2 = MarshalMessage()
        self.__dict__['baseInfo'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_PARAMS_QUERY_STATEMENT_BASE_INFO, submsg2)
        submsg.AddStringUtf8(MSG_KEY_PARAMS_QUERY_STATEMENT_QUERY_STRING, self.__dict__['queryString'])
        mmsg.AddMessage(MSG_KEY_PARAMS_QUERY_STATEMENT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_QUERY_STATEMENT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        submsg2 = submsg.FindMessage(MSG_KEY_PARAMS_QUERY_STATEMENT_BASE_INFO)
        self.__dict__['baseInfo'].Demarshal(submsg2)
        self.__dict__['queryString'] = submsg.FindString(MSG_KEY_PARAMS_QUERY_STATEMENT_QUERY_STRING)