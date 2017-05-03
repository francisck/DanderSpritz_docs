# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime

class ResultLogStatus:

    def __init__(self):
        self.__dict__['opened'] = False
        self.__dict__['error'] = 0
        self.__dict__['logName'] = ''

    def __getattr__(self, name):
        if name == 'opened':
            return self.__dict__['opened']
        if name == 'error':
            return self.__dict__['error']
        if name == 'logName':
            return self.__dict__['logName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'opened':
            self.__dict__['opened'] = value
        elif name == 'error':
            self.__dict__['error'] = value
        elif name == 'logName':
            self.__dict__['logName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_LOG_STATUS_OPENED, self.__dict__['opened'])
        submsg.AddU32(MSG_KEY_RESULT_LOG_STATUS_ERROR, self.__dict__['error'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_LOG_STATUS_NAME, self.__dict__['logName'])
        mmsg.AddMessage(MSG_KEY_RESULT_LOG_STATUS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_LOG_STATUS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['opened'] = submsg.FindBool(MSG_KEY_RESULT_LOG_STATUS_OPENED)
        self.__dict__['error'] = submsg.FindU32(MSG_KEY_RESULT_LOG_STATUS_ERROR)
        self.__dict__['logName'] = submsg.FindString(MSG_KEY_RESULT_LOG_STATUS_NAME)


class ResultLogInfo:

    def __init__(self):
        self.__dict__['numRecords'] = 0
        self.__dict__['mostRecentRecTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['oldestRecNum'] = 0
        self.__dict__['mostRecentRecNum'] = 0

    def __getattr__(self, name):
        if name == 'numRecords':
            return self.__dict__['numRecords']
        if name == 'mostRecentRecTime':
            return self.__dict__['mostRecentRecTime']
        if name == 'oldestRecNum':
            return self.__dict__['oldestRecNum']
        if name == 'mostRecentRecNum':
            return self.__dict__['mostRecentRecNum']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'numRecords':
            self.__dict__['numRecords'] = value
        elif name == 'mostRecentRecTime':
            self.__dict__['mostRecentRecTime'] = value
        elif name == 'oldestRecNum':
            self.__dict__['oldestRecNum'] = value
        elif name == 'mostRecentRecNum':
            self.__dict__['mostRecentRecNum'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_LOG_INFO_NUM_RECORDS, self.__dict__['numRecords'])
        submsg.AddTime(MSG_KEY_RESULT_LOG_INFO_MOST_RECENT_RECORD_TIME, self.__dict__['mostRecentRecTime'])
        submsg.AddU64(MSG_KEY_RESULT_LOG_INFO_OLDEST_RECORD_NUMBER, self.__dict__['oldestRecNum'])
        submsg.AddU64(MSG_KEY_RESULT_LOG_INFO_MOST_RECENT_RECORD_NUMBER, self.__dict__['mostRecentRecNum'])
        mmsg.AddMessage(MSG_KEY_RESULT_LOG_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_LOG_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['numRecords'] = submsg.FindU64(MSG_KEY_RESULT_LOG_INFO_NUM_RECORDS)
        self.__dict__['mostRecentRecTime'] = submsg.FindTime(MSG_KEY_RESULT_LOG_INFO_MOST_RECENT_RECORD_TIME)
        self.__dict__['oldestRecNum'] = submsg.FindU64(MSG_KEY_RESULT_LOG_INFO_OLDEST_RECORD_NUMBER)
        self.__dict__['mostRecentRecNum'] = submsg.FindU64(MSG_KEY_RESULT_LOG_INFO_MOST_RECENT_RECORD_NUMBER)


class ResultRecord:

    def __init__(self):
        self.__dict__['RecordNumber'] = 0
        self.__dict__['TimeGenerated'] = mcl.object.MclTime.MclTime()
        self.__dict__['TimeWritten'] = mcl.object.MclTime.MclTime()
        self.__dict__['EventID'] = 0
        self.__dict__['EventType'] = 0
        self.__dict__['EventCategory'] = 0
        self.__dict__['ProcessId'] = 0
        self.__dict__['ThreadId'] = 0
        self.__dict__['SourceName'] = ''
        self.__dict__['ComputerName'] = ''
        self.__dict__['UserSid'] = ''

    def __getattr__(self, name):
        if name == 'RecordNumber':
            return self.__dict__['RecordNumber']
        if name == 'TimeGenerated':
            return self.__dict__['TimeGenerated']
        if name == 'TimeWritten':
            return self.__dict__['TimeWritten']
        if name == 'EventID':
            return self.__dict__['EventID']
        if name == 'EventType':
            return self.__dict__['EventType']
        if name == 'EventCategory':
            return self.__dict__['EventCategory']
        if name == 'ProcessId':
            return self.__dict__['ProcessId']
        if name == 'ThreadId':
            return self.__dict__['ThreadId']
        if name == 'SourceName':
            return self.__dict__['SourceName']
        if name == 'ComputerName':
            return self.__dict__['ComputerName']
        if name == 'UserSid':
            return self.__dict__['UserSid']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'RecordNumber':
            self.__dict__['RecordNumber'] = value
        elif name == 'TimeGenerated':
            self.__dict__['TimeGenerated'] = value
        elif name == 'TimeWritten':
            self.__dict__['TimeWritten'] = value
        elif name == 'EventID':
            self.__dict__['EventID'] = value
        elif name == 'EventType':
            self.__dict__['EventType'] = value
        elif name == 'EventCategory':
            self.__dict__['EventCategory'] = value
        elif name == 'ProcessId':
            self.__dict__['ProcessId'] = value
        elif name == 'ThreadId':
            self.__dict__['ThreadId'] = value
        elif name == 'SourceName':
            self.__dict__['SourceName'] = value
        elif name == 'ComputerName':
            self.__dict__['ComputerName'] = value
        elif name == 'UserSid':
            self.__dict__['UserSid'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_RESULT_RECORD_INFO_RECORD_NUMBER, self.__dict__['RecordNumber'])
        submsg.AddTime(MSG_KEY_RESULT_RECORD_INFO_TIME_GENERATED, self.__dict__['TimeGenerated'])
        submsg.AddTime(MSG_KEY_RESULT_RECORD_INFO_TIME_WRITTEN, self.__dict__['TimeWritten'])
        submsg.AddU32(MSG_KEY_RESULT_RECORD_INFO_EVENT_ID, self.__dict__['EventID'])
        submsg.AddU16(MSG_KEY_RESULT_RECORD_INFO_EVENT_TYPE, self.__dict__['EventType'])
        submsg.AddU16(MSG_KEY_RESULT_RECORD_INFO_EVENT_CATEGORY, self.__dict__['EventCategory'])
        submsg.AddU32(MSG_KEY_RESULT_RECORD_INFO_PROCESS_ID, self.__dict__['ProcessId'])
        submsg.AddU32(MSG_KEY_RESULT_RECORD_INFO_THREAD_ID, self.__dict__['ThreadId'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_RECORD_INFO_SOURCE_NAME, self.__dict__['SourceName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_RECORD_INFO_COMPUTER_NAME, self.__dict__['ComputerName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_RECORD_INFO_USER_SID, self.__dict__['UserSid'])
        mmsg.AddMessage(MSG_KEY_RESULT_RECORD_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_RECORD_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['RecordNumber'] = submsg.FindU64(MSG_KEY_RESULT_RECORD_INFO_RECORD_NUMBER)
        self.__dict__['TimeGenerated'] = submsg.FindTime(MSG_KEY_RESULT_RECORD_INFO_TIME_GENERATED)
        self.__dict__['TimeWritten'] = submsg.FindTime(MSG_KEY_RESULT_RECORD_INFO_TIME_WRITTEN)
        self.__dict__['EventID'] = submsg.FindU32(MSG_KEY_RESULT_RECORD_INFO_EVENT_ID)
        self.__dict__['EventType'] = submsg.FindU16(MSG_KEY_RESULT_RECORD_INFO_EVENT_TYPE)
        self.__dict__['EventCategory'] = submsg.FindU16(MSG_KEY_RESULT_RECORD_INFO_EVENT_CATEGORY)
        self.__dict__['ProcessId'] = submsg.FindU32(MSG_KEY_RESULT_RECORD_INFO_PROCESS_ID)
        self.__dict__['ThreadId'] = submsg.FindU32(MSG_KEY_RESULT_RECORD_INFO_THREAD_ID)
        self.__dict__['SourceName'] = submsg.FindString(MSG_KEY_RESULT_RECORD_INFO_SOURCE_NAME)
        self.__dict__['ComputerName'] = submsg.FindString(MSG_KEY_RESULT_RECORD_INFO_COMPUTER_NAME)
        self.__dict__['UserSid'] = submsg.FindString(MSG_KEY_RESULT_RECORD_INFO_USER_SID)