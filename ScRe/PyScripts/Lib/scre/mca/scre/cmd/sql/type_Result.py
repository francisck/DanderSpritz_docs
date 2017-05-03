# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime
RESULT_CELL_INFO_FLAG_IS_TRUNCATED = 1
RESULT_CELL_INFO_FLAG_IS_NULL = 2

class ResultError:

    def __init__(self):
        self.__dict__['errorCode'] = 0
        self.__dict__['sqlState'] = ''
        self.__dict__['msg'] = ''

    def __getattr__(self, name):
        if name == 'errorCode':
            return self.__dict__['errorCode']
        if name == 'sqlState':
            return self.__dict__['sqlState']
        if name == 'msg':
            return self.__dict__['msg']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'errorCode':
            self.__dict__['errorCode'] = value
        elif name == 'sqlState':
            self.__dict__['sqlState'] = value
        elif name == 'msg':
            self.__dict__['msg'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddS32(MSG_KEY_RESULT_ERROR_ERROR_CODE, self.__dict__['errorCode'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_ERROR_SQL_STATE, self.__dict__['sqlState'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_ERROR_MSG, self.__dict__['msg'])
        mmsg.AddMessage(MSG_KEY_RESULT_ERROR, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_ERROR, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['errorCode'] = submsg.FindS32(MSG_KEY_RESULT_ERROR_ERROR_CODE)
        self.__dict__['sqlState'] = submsg.FindString(MSG_KEY_RESULT_ERROR_SQL_STATE)
        self.__dict__['msg'] = submsg.FindString(MSG_KEY_RESULT_ERROR_MSG)


class ResultConnection:

    def __init__(self):
        self.__dict__['handleId'] = 0
        self.__dict__['connectionString'] = ''
        self.__dict__['connectionType'] = 0
        self.__dict__['accessType'] = 0
        self.__dict__['autoCommit'] = True
        self.__dict__['createTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['lastUseTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['maxIdleDuration'] = mcl.object.MclTime.MclTime()

    def __getattr__(self, name):
        if name == 'handleId':
            return self.__dict__['handleId']
        if name == 'connectionString':
            return self.__dict__['connectionString']
        if name == 'connectionType':
            return self.__dict__['connectionType']
        if name == 'accessType':
            return self.__dict__['accessType']
        if name == 'autoCommit':
            return self.__dict__['autoCommit']
        if name == 'createTime':
            return self.__dict__['createTime']
        if name == 'lastUseTime':
            return self.__dict__['lastUseTime']
        if name == 'maxIdleDuration':
            return self.__dict__['maxIdleDuration']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'handleId':
            self.__dict__['handleId'] = value
        elif name == 'connectionString':
            self.__dict__['connectionString'] = value
        elif name == 'connectionType':
            self.__dict__['connectionType'] = value
        elif name == 'accessType':
            self.__dict__['accessType'] = value
        elif name == 'autoCommit':
            self.__dict__['autoCommit'] = value
        elif name == 'createTime':
            self.__dict__['createTime'] = value
        elif name == 'lastUseTime':
            self.__dict__['lastUseTime'] = value
        elif name == 'maxIdleDuration':
            self.__dict__['maxIdleDuration'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_CONNECTION_HANDLE_ID, self.__dict__['handleId'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_CONNECTION_CONNECTION_STRING, self.__dict__['connectionString'])
        submsg.AddU8(MSG_KEY_RESULT_CONNECTION_CONNECTION_TYPE, self.__dict__['connectionType'])
        submsg.AddU8(MSG_KEY_RESULT_CONNECTION_ACCESS_TYPE, self.__dict__['accessType'])
        submsg.AddBool(MSG_KEY_RESULT_CONNECTION_AUTO_COMMIT, self.__dict__['autoCommit'])
        submsg.AddTime(MSG_KEY_RESULT_CONNECTION_CREATE_TIME, self.__dict__['createTime'])
        submsg.AddTime(MSG_KEY_RESULT_CONNECTION_LAST_USE_TIME, self.__dict__['lastUseTime'])
        submsg.AddTime(MSG_KEY_RESULT_CONNECTION_MAX_IDLE_DURATION, self.__dict__['maxIdleDuration'])
        mmsg.AddMessage(MSG_KEY_RESULT_CONNECTION, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_CONNECTION, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['handleId'] = submsg.FindU32(MSG_KEY_RESULT_CONNECTION_HANDLE_ID)
        self.__dict__['connectionString'] = submsg.FindString(MSG_KEY_RESULT_CONNECTION_CONNECTION_STRING)
        self.__dict__['connectionType'] = submsg.FindU8(MSG_KEY_RESULT_CONNECTION_CONNECTION_TYPE)
        self.__dict__['accessType'] = submsg.FindU8(MSG_KEY_RESULT_CONNECTION_ACCESS_TYPE)
        self.__dict__['autoCommit'] = submsg.FindBool(MSG_KEY_RESULT_CONNECTION_AUTO_COMMIT)
        self.__dict__['createTime'] = submsg.FindTime(MSG_KEY_RESULT_CONNECTION_CREATE_TIME)
        self.__dict__['lastUseTime'] = submsg.FindTime(MSG_KEY_RESULT_CONNECTION_LAST_USE_TIME)
        self.__dict__['maxIdleDuration'] = submsg.FindTime(MSG_KEY_RESULT_CONNECTION_MAX_IDLE_DURATION)


class ResultDrivers:

    def __init__(self):
        self.__dict__['driver'] = ''
        self.__dict__['attribute'] = ''

    def __getattr__(self, name):
        if name == 'driver':
            return self.__dict__['driver']
        if name == 'attribute':
            return self.__dict__['attribute']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'driver':
            self.__dict__['driver'] = value
        elif name == 'attribute':
            self.__dict__['attribute'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_DRIVERS_DRIVER, self.__dict__['driver'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DRIVERS_ATTRIBUTE, self.__dict__['attribute'])
        mmsg.AddMessage(MSG_KEY_RESULT_DRIVERS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_DRIVERS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['driver'] = submsg.FindString(MSG_KEY_RESULT_DRIVERS_DRIVER)
        self.__dict__['attribute'] = submsg.FindString(MSG_KEY_RESULT_DRIVERS_ATTRIBUTE)


class ResultSource:

    def __init__(self):
        self.__dict__['datasource'] = ''
        self.__dict__['description'] = ''

    def __getattr__(self, name):
        if name == 'datasource':
            return self.__dict__['datasource']
        if name == 'description':
            return self.__dict__['description']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'datasource':
            self.__dict__['datasource'] = value
        elif name == 'description':
            self.__dict__['description'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_SOURCE_DATA_SOURCE, self.__dict__['datasource'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_SOURCE_DESCRIPTION, self.__dict__['description'])
        mmsg.AddMessage(MSG_KEY_RESULT_SOURCE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_SOURCE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['datasource'] = submsg.FindString(MSG_KEY_RESULT_SOURCE_DATA_SOURCE)
        self.__dict__['description'] = submsg.FindString(MSG_KEY_RESULT_SOURCE_DESCRIPTION)


class ResultServer:

    def __init__(self):
        self.__dict__['server'] = ''

    def __getattr__(self, name):
        if name == 'server':
            return self.__dict__['server']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'server':
            self.__dict__['server'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_SERVER_SERVER, self.__dict__['server'])
        mmsg.AddMessage(MSG_KEY_RESULT_SERVER, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_SERVER, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['server'] = submsg.FindString(MSG_KEY_RESULT_SERVER_SERVER)


class ResultExecute:

    def __init__(self):
        self.__dict__['totalColumns'] = 0
        self.__dict__['startRow'] = 0
        self.__dict__['endRow'] = 0
        self.__dict__['rowsModified'] = 0
        self.__dict__['queryString'] = ''
        self.__dict__['connectionString'] = ''

    def __getattr__(self, name):
        if name == 'totalColumns':
            return self.__dict__['totalColumns']
        if name == 'startRow':
            return self.__dict__['startRow']
        if name == 'endRow':
            return self.__dict__['endRow']
        if name == 'rowsModified':
            return self.__dict__['rowsModified']
        if name == 'queryString':
            return self.__dict__['queryString']
        if name == 'connectionString':
            return self.__dict__['connectionString']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'totalColumns':
            self.__dict__['totalColumns'] = value
        elif name == 'startRow':
            self.__dict__['startRow'] = value
        elif name == 'endRow':
            self.__dict__['endRow'] = value
        elif name == 'rowsModified':
            self.__dict__['rowsModified'] = value
        elif name == 'queryString':
            self.__dict__['queryString'] = value
        elif name == 'connectionString':
            self.__dict__['connectionString'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_EXECUTE_TOTAL_COLUMNS, self.__dict__['totalColumns'])
        submsg.AddU64(MSG_KEY_RESULT_EXECUTE_START_ROW, self.__dict__['startRow'])
        submsg.AddU64(MSG_KEY_RESULT_EXECUTE_END_ROW, self.__dict__['endRow'])
        submsg.AddU64(MSG_KEY_RESULT_EXECUTE_ROWS_MODIFIED, self.__dict__['rowsModified'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_EXECUTE_QUERY_STRING, self.__dict__['queryString'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_EXECUTE_CONNECTION_STRING, self.__dict__['connectionString'])
        mmsg.AddMessage(MSG_KEY_RESULT_EXECUTE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_EXECUTE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['totalColumns'] = submsg.FindU32(MSG_KEY_RESULT_EXECUTE_TOTAL_COLUMNS)
        self.__dict__['startRow'] = submsg.FindU64(MSG_KEY_RESULT_EXECUTE_START_ROW)
        self.__dict__['endRow'] = submsg.FindU64(MSG_KEY_RESULT_EXECUTE_END_ROW)
        self.__dict__['rowsModified'] = submsg.FindU64(MSG_KEY_RESULT_EXECUTE_ROWS_MODIFIED)
        self.__dict__['queryString'] = submsg.FindString(MSG_KEY_RESULT_EXECUTE_QUERY_STRING)
        self.__dict__['connectionString'] = submsg.FindString(MSG_KEY_RESULT_EXECUTE_CONNECTION_STRING)


class ResultColumnInfo:

    def __init__(self):
        self.__dict__['width'] = 0
        self.__dict__['dataType'] = 0
        self.__dict__['isNullable'] = False
        self.__dict__['name'] = ''
        self.__dict__['index'] = 0

    def __getattr__(self, name):
        if name == 'width':
            return self.__dict__['width']
        if name == 'dataType':
            return self.__dict__['dataType']
        if name == 'isNullable':
            return self.__dict__['isNullable']
        if name == 'name':
            return self.__dict__['name']
        if name == 'index':
            return self.__dict__['index']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'width':
            self.__dict__['width'] = value
        elif name == 'dataType':
            self.__dict__['dataType'] = value
        elif name == 'isNullable':
            self.__dict__['isNullable'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'index':
            self.__dict__['index'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_COLUMN_INFO_WIDTH, self.__dict__['width'])
        submsg.AddS16(MSG_KEY_RESULT_COLUMN_INFO_DATA_TYPE, self.__dict__['dataType'])
        submsg.AddBool(MSG_KEY_RESULT_COLUMN_INFO_IS_NULLABLE, self.__dict__['isNullable'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_COLUMN_INFO_NAME, self.__dict__['name'])
        submsg.AddU32(MSG_KEY_RESULT_COLUMN_INFO_INDEX, self.__dict__['index'])
        mmsg.AddMessage(MSG_KEY_RESULT_COLUMN_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_COLUMN_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['width'] = submsg.FindU32(MSG_KEY_RESULT_COLUMN_INFO_WIDTH)
        self.__dict__['dataType'] = submsg.FindS16(MSG_KEY_RESULT_COLUMN_INFO_DATA_TYPE)
        self.__dict__['isNullable'] = submsg.FindBool(MSG_KEY_RESULT_COLUMN_INFO_IS_NULLABLE)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_COLUMN_INFO_NAME)
        self.__dict__['index'] = submsg.FindU32(MSG_KEY_RESULT_COLUMN_INFO_INDEX)


class ResultCellInfo:

    def __init__(self):
        self.__dict__['dataType'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['columnnIndex'] = 0

    def __getattr__(self, name):
        if name == 'dataType':
            return self.__dict__['dataType']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'columnnIndex':
            return self.__dict__['columnnIndex']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'dataType':
            self.__dict__['dataType'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'columnnIndex':
            self.__dict__['columnnIndex'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddS16(MSG_KEY_RESULT_CELL_INFO_DATA_TYPE, self.__dict__['dataType'])
        submsg.AddU32(MSG_KEY_RESULT_CELL_INFO_FLAGS, self.__dict__['flags'])
        submsg.AddU32(MSG_KEY_RESULT_CELL_INFO_COLUMN_INDEX, self.__dict__['columnnIndex'])
        mmsg.AddMessage(MSG_KEY_RESULT_CELL_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_CELL_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['dataType'] = submsg.FindS16(MSG_KEY_RESULT_CELL_INFO_DATA_TYPE)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_CELL_INFO_FLAGS)
        self.__dict__['columnnIndex'] = submsg.FindU32(MSG_KEY_RESULT_CELL_INFO_COLUMN_INDEX)