# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime
RESULT_ATJOB_FLAG_RUN_PERIODICALLY = 1
RESULT_ATJOB_FLAG_EXEC_ERROR = 2
RESULT_ATJOB_FLAG_RUNS_TODAY = 4
RESULT_ATJOB_FLAG_ADD_CURRENT_DATE = 8
RESULT_ATJOB_FLAG_NONINTERACTIVE = 16
RESULT_TASKSERVICEJOB_COMPAT_UNKNOWN = 0
RESULT_TASKSERVICEJOB_COMPAT_AT = 1
RESULT_TASKSERVICEJOB_COMPAT_V1 = 2
RESULT_TASKSERVICEJOB_COMPAT_V2 = 3
RESULT_TASKSERVICEJOB_STATE_UNKNOWN = 0
RESULT_TASKSERVICEJOB_STATE_DISABLED = 1
RESULT_TASKSERVICEJOB_STATE_QUEUED = 2
RESULT_TASKSERVICEJOB_STATE_READY = 3
RESULT_TASKSERVICEJOB_STATE_RUNNING = 4
RESULT_TASKSERVICEJOB_FLAG_ENABLED = 1
RESULT_TASKSERVICEJOB_FLAG_ALLOW_DEMAND_START = 2
RESULT_TASKSERVICEJOB_FLAG_ALLOW_HARD_TERMINATE = 4
RESULT_TASKSERVICEJOB_FLAG_DISALLOW_START_IF_ON_BATTERIES = 8
RESULT_TASKSERVICEJOB_FLAG_HIDDEN = 16
RESULT_TASKSERVICEJOB_FLAG_REQUIRE_NETWORK = 32
RESULT_TASKSERVICEJOB_FLAG_START_WHEN_AVAILABLE = 64
RESULT_TASKSERVICEJOB_FLAG_STOP_IF_GOING_ON_BATTERIES = 128
RESULT_TASKSERVICEJOB_FLAG_WAKE_TO_RUN = 256
RESULT_TASKSERVICEJOB_ACTION_TYPE_UNKNOWN = 0
RESULT_TASKSERVICEJOB_ACTION_TYPE_EXEC = 1
RESULT_TASKSERVICEJOB_ACTION_TYPE_COM_HANDLER = 2
RESULT_TASKSERVICEJOB_ACTION_TYPE_SEND_EMAIL = 3
RESULT_TASKSERVICEJOB_ACTION_TYPE_SHOW_MESSAGE = 4
RESULT_TASKSERVICEJOB_LOGONTYPE_UNKNOWN = 0
RESULT_TASKSERVICEJOB_LOGONTYPE_NONE = 1
RESULT_TASKSERVICEJOB_LOGONTYPE_PASSWORD = 2
RESULT_TASKSERVICEJOB_LOGONTYPE_S4U = 3
RESULT_TASKSERVICEJOB_LOGONTYPE_INTERACTIVE_TOKEN = 4
RESULT_TASKSERVICEJOB_LOGONTYPE_GROUP = 5
RESULT_TASKSERVICEJOB_LOGONTYPE_SERVICE_ACCOUNT = 6
RESULT_TASKSERVICEJOB_LOGONTYPE_INTERACTIVE_TOKEN_OR_PASSWORD = 7
RESULT_TASKSERVICEJOB_RUNLEVEL_UNKNOWN = 0
RESULT_TASKSERVICEJOB_RUNLEVEL_LEAST = 1
RESULT_TASKSERVICEJOB_RUNLEVEL_HIGHEST = 2
RESULT_TASKSERVICEJOB_TRIGGER_TYPE_UNKNOWN = 0
RESULT_TASKSERVICEJOB_TRIGGER_TYPE_EVENT = 1
RESULT_TASKSERVICEJOB_TRIGGER_TYPE_TIME = 2
RESULT_TASKSERVICEJOB_TRIGGER_TYPE_DAILY = 3
RESULT_TASKSERVICEJOB_TRIGGER_TYPE_WEEKLY = 4
RESULT_TASKSERVICEJOB_TRIGGER_TYPE_MONTHLY = 5
RESULT_TASKSERVICEJOB_TRIGGER_TYPE_MONTHLYDOW = 6
RESULT_TASKSERVICEJOB_TRIGGER_TYPE_IDLE = 7
RESULT_TASKSERVICEJOB_TRIGGER_TYPE_REGISTRATION = 8
RESULT_TASKSERVICEJOB_TRIGGER_TYPE_BOOT = 9
RESULT_TASKSERVICEJOB_TRIGGER_TYPE_LOGON = 10
RESULT_TASKSERVICEJOB_TRIGGER_TYPE_SESSION_STATE_CHANGE = 11
RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_UNKNOWN = 0
RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_CONSOLE_CONNECT = 1
RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_CONSOLE_DISCONNECT = 2
RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_REMOTE_CONNECT = 3
RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_REMOTE_DISCONNECT = 4
RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_SESSION_LOCK = 5
RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_SESSION_UNLOCK = 6

class ResultAdd:

    def __init__(self):
        self.__dict__['jobId'] = ''

    def __getattr__(self, name):
        if name == 'jobId':
            return self.__dict__['jobId']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'jobId':
            self.__dict__['jobId'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_ADD_JOB_ID, self.__dict__['jobId'])
        mmsg.AddMessage(MSG_KEY_RESULT_ADD, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_ADD, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['jobId'] = submsg.FindString(MSG_KEY_RESULT_ADD_JOB_ID)


class ResultAtJob:

    def __init__(self):
        self.__dict__['jobId'] = 0
        self.__dict__['jobTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['daysOfMonth'] = 0
        self.__dict__['daysOfWeek'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['cmd'] = ''

    def __getattr__(self, name):
        if name == 'jobId':
            return self.__dict__['jobId']
        if name == 'jobTime':
            return self.__dict__['jobTime']
        if name == 'daysOfMonth':
            return self.__dict__['daysOfMonth']
        if name == 'daysOfWeek':
            return self.__dict__['daysOfWeek']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'cmd':
            return self.__dict__['cmd']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'jobId':
            self.__dict__['jobId'] = value
        elif name == 'jobTime':
            self.__dict__['jobTime'] = value
        elif name == 'daysOfMonth':
            self.__dict__['daysOfMonth'] = value
        elif name == 'daysOfWeek':
            self.__dict__['daysOfWeek'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'cmd':
            self.__dict__['cmd'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_ATJOB_INFO_JOB_ID, self.__dict__['jobId'])
        submsg.AddTime(MSG_KEY_RESULT_ATJOB_INFO_JOB_TIME, self.__dict__['jobTime'])
        submsg.AddU32(MSG_KEY_RESULT_ATJOB_INFO_DAYS_OF_MONTH, self.__dict__['daysOfMonth'])
        submsg.AddU8(MSG_KEY_RESULT_ATJOB_INFO_DAYS_OF_WEEK, self.__dict__['daysOfWeek'])
        submsg.AddU8(MSG_KEY_RESULT_ATJOB_INFO_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_ATJOB_INFO_COMMAND, self.__dict__['cmd'])
        mmsg.AddMessage(MSG_KEY_RESULT_ATJOB_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_ATJOB_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['jobId'] = submsg.FindU32(MSG_KEY_RESULT_ATJOB_INFO_JOB_ID)
        self.__dict__['jobTime'] = submsg.FindTime(MSG_KEY_RESULT_ATJOB_INFO_JOB_TIME)
        self.__dict__['daysOfMonth'] = submsg.FindU32(MSG_KEY_RESULT_ATJOB_INFO_DAYS_OF_MONTH)
        self.__dict__['daysOfWeek'] = submsg.FindU8(MSG_KEY_RESULT_ATJOB_INFO_DAYS_OF_WEEK)
        self.__dict__['flags'] = submsg.FindU8(MSG_KEY_RESULT_ATJOB_INFO_FLAGS)
        self.__dict__['cmd'] = submsg.FindString(MSG_KEY_RESULT_ATJOB_INFO_COMMAND)


class ResultNetJob:

    def __init__(self):
        self.__dict__['nextRun'] = mcl.object.MclTime.MclTime()
        self.__dict__['flags'] = 0
        self.__dict__['exitCode'] = 0
        self.__dict__['numTriggers'] = 0
        self.__dict__['jobName'] = ''
        self.__dict__['displayName'] = ''
        self.__dict__['params'] = ''
        self.__dict__['accountName'] = ''

    def __getattr__(self, name):
        if name == 'nextRun':
            return self.__dict__['nextRun']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'exitCode':
            return self.__dict__['exitCode']
        if name == 'numTriggers':
            return self.__dict__['numTriggers']
        if name == 'jobName':
            return self.__dict__['jobName']
        if name == 'displayName':
            return self.__dict__['displayName']
        if name == 'params':
            return self.__dict__['params']
        if name == 'accountName':
            return self.__dict__['accountName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'nextRun':
            self.__dict__['nextRun'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'exitCode':
            self.__dict__['exitCode'] = value
        elif name == 'numTriggers':
            self.__dict__['numTriggers'] = value
        elif name == 'jobName':
            self.__dict__['jobName'] = value
        elif name == 'displayName':
            self.__dict__['displayName'] = value
        elif name == 'params':
            self.__dict__['params'] = value
        elif name == 'accountName':
            self.__dict__['accountName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddTime(MSG_KEY_RESULT_NETJOB_INFO_NEXT_RUN, self.__dict__['nextRun'])
        submsg.AddU32(MSG_KEY_RESULT_NETJOB_INFO_FLAGS, self.__dict__['flags'])
        submsg.AddS32(MSG_KEY_RESULT_NETJOB_INFO_EXIT_CODE, self.__dict__['exitCode'])
        submsg.AddU16(MSG_KEY_RESULT_NETJOB_INFO_NUM_TRIGGERS, self.__dict__['numTriggers'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NETJOB_INFO_JOB_NAME, self.__dict__['jobName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NETJOB_INFO_DISPLAY_NAME, self.__dict__['displayName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NETJOB_INFO_PARAMETERS, self.__dict__['params'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NETJOB_INFO_ACCOUNT_NAME, self.__dict__['accountName'])
        mmsg.AddMessage(MSG_KEY_RESULT_NETJOB_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_NETJOB_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['nextRun'] = submsg.FindTime(MSG_KEY_RESULT_NETJOB_INFO_NEXT_RUN)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_NETJOB_INFO_FLAGS)
        self.__dict__['exitCode'] = submsg.FindS32(MSG_KEY_RESULT_NETJOB_INFO_EXIT_CODE)
        self.__dict__['numTriggers'] = submsg.FindU16(MSG_KEY_RESULT_NETJOB_INFO_NUM_TRIGGERS)
        self.__dict__['jobName'] = submsg.FindString(MSG_KEY_RESULT_NETJOB_INFO_JOB_NAME)
        self.__dict__['displayName'] = submsg.FindString(MSG_KEY_RESULT_NETJOB_INFO_DISPLAY_NAME)
        self.__dict__['params'] = submsg.FindString(MSG_KEY_RESULT_NETJOB_INFO_PARAMETERS)
        self.__dict__['accountName'] = submsg.FindString(MSG_KEY_RESULT_NETJOB_INFO_ACCOUNT_NAME)


class ResultTaskServiceFolder:

    def __init__(self):
        self.__dict__['name'] = ''
        self.__dict__['path'] = ''

    def __getattr__(self, name):
        if name == 'name':
            return self.__dict__['name']
        if name == 'path':
            return self.__dict__['path']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'name':
            self.__dict__['name'] = value
        elif name == 'path':
            self.__dict__['path'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICE_FOLDER_INFO_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICE_FOLDER_INFO_PATH, self.__dict__['path'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICE_FOLDER_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICE_FOLDER_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICE_FOLDER_INFO_NAME)
        self.__dict__['path'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICE_FOLDER_INFO_PATH)


class ResultTaskServiceJob:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['name'] = ''
        self.__dict__['lastRunTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['lastRunResult'] = 0
        self.__dict__['nextRunTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['path'] = ''
        self.__dict__['state'] = 0
        self.__dict__['xml'] = ''
        self.__dict__['numMissedRuns'] = 0
        self.__dict__['compatibility'] = RESULT_TASKSERVICEJOB_COMPAT_UNKNOWN

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'name':
            return self.__dict__['name']
        if name == 'lastRunTime':
            return self.__dict__['lastRunTime']
        if name == 'lastRunResult':
            return self.__dict__['lastRunResult']
        if name == 'nextRunTime':
            return self.__dict__['nextRunTime']
        if name == 'path':
            return self.__dict__['path']
        if name == 'state':
            return self.__dict__['state']
        if name == 'xml':
            return self.__dict__['xml']
        if name == 'numMissedRuns':
            return self.__dict__['numMissedRuns']
        if name == 'compatibility':
            return self.__dict__['compatibility']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'lastRunTime':
            self.__dict__['lastRunTime'] = value
        elif name == 'lastRunResult':
            self.__dict__['lastRunResult'] = value
        elif name == 'nextRunTime':
            self.__dict__['nextRunTime'] = value
        elif name == 'path':
            self.__dict__['path'] = value
        elif name == 'state':
            self.__dict__['state'] = value
        elif name == 'xml':
            self.__dict__['xml'] = value
        elif name == 'numMissedRuns':
            self.__dict__['numMissedRuns'] = value
        elif name == 'compatibility':
            self.__dict__['compatibility'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_NAME, self.__dict__['name'])
        submsg.AddTime(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_LASTRUNTIME, self.__dict__['lastRunTime'])
        submsg.AddU32(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_LASTRUNRESULT, self.__dict__['lastRunResult'])
        submsg.AddTime(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_NEXTRUNTIME, self.__dict__['nextRunTime'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_PATH, self.__dict__['path'])
        submsg.AddU8(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_STATE, self.__dict__['state'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_XML, self.__dict__['xml'])
        submsg.AddU32(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_NUMMISSEDRUNS, self.__dict__['numMissedRuns'])
        submsg.AddU8(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_COMPATIBILITY, self.__dict__['compatibility'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_FLAGS)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_NAME)
        self.__dict__['lastRunTime'] = submsg.FindTime(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_LASTRUNTIME)
        self.__dict__['lastRunResult'] = submsg.FindU32(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_LASTRUNRESULT)
        self.__dict__['nextRunTime'] = submsg.FindTime(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_NEXTRUNTIME)
        self.__dict__['path'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_PATH)
        self.__dict__['state'] = submsg.FindU8(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_STATE)
        self.__dict__['xml'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_XML)
        self.__dict__['numMissedRuns'] = submsg.FindU32(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_NUMMISSEDRUNS)
        self.__dict__['compatibility'] = submsg.FindU8(MSG_KEY_RESULT_TASKSERVICEJOB_INFO_COMPATIBILITY)


class ResultTaskServiceAction:

    def __init__(self):
        self.__dict__['id'] = ''
        self.__dict__['type'] = RESULT_TASKSERVICEJOB_ACTION_TYPE_UNKNOWN

    def __getattr__(self, name):
        if name == 'id':
            return self.__dict__['id']
        if name == 'type':
            return self.__dict__['type']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'id':
            self.__dict__['id'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_INFO_ID, self.__dict__['id'])
        submsg.AddU8(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_INFO_TYPE, self.__dict__['type'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['id'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_INFO_ID)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_INFO_TYPE)


class ResultTaskServiceActionExec:

    def __init__(self):
        self.__dict__['arguments'] = ''
        self.__dict__['path'] = ''
        self.__dict__['workingDir'] = ''

    def __getattr__(self, name):
        if name == 'arguments':
            return self.__dict__['arguments']
        if name == 'path':
            return self.__dict__['path']
        if name == 'workingDir':
            return self.__dict__['workingDir']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'arguments':
            self.__dict__['arguments'] = value
        elif name == 'path':
            self.__dict__['path'] = value
        elif name == 'workingDir':
            self.__dict__['workingDir'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_EXEC_ARGUMENTS, self.__dict__['arguments'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_EXEC_PATH, self.__dict__['path'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_EXEC_WORKINGDIR, self.__dict__['workingDir'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_EXEC, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_EXEC, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['arguments'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_EXEC_ARGUMENTS)
        self.__dict__['path'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_EXEC_PATH)
        self.__dict__['workingDir'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_EXEC_WORKINGDIR)


class ResultTaskServiceActionCom:

    def __init__(self):
        self.__dict__['classId'] = ''
        self.__dict__['data'] = ''

    def __getattr__(self, name):
        if name == 'classId':
            return self.__dict__['classId']
        if name == 'data':
            return self.__dict__['data']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'classId':
            self.__dict__['classId'] = value
        elif name == 'data':
            self.__dict__['data'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_COM_CLASSID, self.__dict__['classId'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_COM_DATA, self.__dict__['data'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_COM, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_COM, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['classId'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_COM_CLASSID)
        self.__dict__['data'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_COM_DATA)


class ResultTaskServicePrincipal:

    def __init__(self):
        self.__dict__['displayName'] = ''
        self.__dict__['groupId'] = ''
        self.__dict__['id'] = ''
        self.__dict__['logonType'] = RESULT_TASKSERVICEJOB_LOGONTYPE_UNKNOWN
        self.__dict__['runLevel'] = RESULT_TASKSERVICEJOB_RUNLEVEL_UNKNOWN
        self.__dict__['userId'] = ''

    def __getattr__(self, name):
        if name == 'displayName':
            return self.__dict__['displayName']
        if name == 'groupId':
            return self.__dict__['groupId']
        if name == 'id':
            return self.__dict__['id']
        if name == 'logonType':
            return self.__dict__['logonType']
        if name == 'runLevel':
            return self.__dict__['runLevel']
        if name == 'userId':
            return self.__dict__['userId']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'displayName':
            self.__dict__['displayName'] = value
        elif name == 'groupId':
            self.__dict__['groupId'] = value
        elif name == 'id':
            self.__dict__['id'] = value
        elif name == 'logonType':
            self.__dict__['logonType'] = value
        elif name == 'runLevel':
            self.__dict__['runLevel'] = value
        elif name == 'userId':
            self.__dict__['userId'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_DISPLAYNAME, self.__dict__['displayName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_GROUPID, self.__dict__['groupId'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_ID, self.__dict__['id'])
        submsg.AddU8(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_LOGONTYPE, self.__dict__['logonType'])
        submsg.AddU8(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_RUNLEVEL, self.__dict__['runLevel'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_USERID, self.__dict__['userId'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['displayName'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_DISPLAYNAME)
        self.__dict__['groupId'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_GROUPID)
        self.__dict__['id'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_ID)
        self.__dict__['logonType'] = submsg.FindU8(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_LOGONTYPE)
        self.__dict__['runLevel'] = submsg.FindU8(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_RUNLEVEL)
        self.__dict__['userId'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_USERID)


class ResultTaskServiceRepetition:

    def __init__(self):
        self.__dict__['stopAtDurationEnd'] = False
        self.__dict__['duration'] = ''
        self.__dict__['interval'] = ''

    def __getattr__(self, name):
        if name == 'stopAtDurationEnd':
            return self.__dict__['stopAtDurationEnd']
        if name == 'duration':
            return self.__dict__['duration']
        if name == 'interval':
            return self.__dict__['interval']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'stopAtDurationEnd':
            self.__dict__['stopAtDurationEnd'] = value
        elif name == 'duration':
            self.__dict__['duration'] = value
        elif name == 'interval':
            self.__dict__['interval'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_TASKSERVICEJOB_REPETITION_STOP_AT_DURATION_END, self.__dict__['stopAtDurationEnd'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_REPETITION_DURATION, self.__dict__['duration'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_REPETITION_INTERVAL, self.__dict__['interval'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_REPETITION, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_REPETITION, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['stopAtDurationEnd'] = submsg.FindBool(MSG_KEY_RESULT_TASKSERVICEJOB_REPETITION_STOP_AT_DURATION_END)
        self.__dict__['duration'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_REPETITION_DURATION)
        self.__dict__['interval'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_REPETITION_INTERVAL)


class ResultTaskServiceTrigger:

    def __init__(self):
        self.__dict__['enabled'] = False
        self.__dict__['id'] = ''
        self.__dict__['type'] = RESULT_TASKSERVICEJOB_TRIGGER_TYPE_UNKNOWN
        self.__dict__['startBoundary'] = ''
        self.__dict__['endBoundary'] = ''
        self.__dict__['execTimeLimit'] = ''
        self.__dict__['repetition'] = ResultTaskServiceRepetition()

    def __getattr__(self, name):
        if name == 'enabled':
            return self.__dict__['enabled']
        if name == 'id':
            return self.__dict__['id']
        if name == 'type':
            return self.__dict__['type']
        if name == 'startBoundary':
            return self.__dict__['startBoundary']
        if name == 'endBoundary':
            return self.__dict__['endBoundary']
        if name == 'execTimeLimit':
            return self.__dict__['execTimeLimit']
        if name == 'repetition':
            return self.__dict__['repetition']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'enabled':
            self.__dict__['enabled'] = value
        elif name == 'id':
            self.__dict__['id'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        elif name == 'startBoundary':
            self.__dict__['startBoundary'] = value
        elif name == 'endBoundary':
            self.__dict__['endBoundary'] = value
        elif name == 'execTimeLimit':
            self.__dict__['execTimeLimit'] = value
        elif name == 'repetition':
            self.__dict__['repetition'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_ENABLED, self.__dict__['enabled'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_ID, self.__dict__['id'])
        submsg.AddU8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_TYPE, self.__dict__['type'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_START_BOUNDARY, self.__dict__['startBoundary'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_END_BOUNDARY, self.__dict__['endBoundary'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_EXEC_TIME_LIMIT, self.__dict__['execTimeLimit'])
        submsg2 = MarshalMessage()
        self.__dict__['repetition'].Marshal(submsg2)
        submsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_REPETITION, submsg2)
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['enabled'] = submsg.FindBool(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_ENABLED)
        self.__dict__['id'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_ID)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_TYPE)
        self.__dict__['startBoundary'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_START_BOUNDARY)
        self.__dict__['endBoundary'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_END_BOUNDARY)
        self.__dict__['execTimeLimit'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_EXEC_TIME_LIMIT)
        submsg2 = submsg.FindMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_REPETITION)
        self.__dict__['repetition'].Demarshal(submsg2)


class ResultTaskServiceTriggerEvent:

    def __init__(self):
        self.__dict__['subscription'] = ''

    def __getattr__(self, name):
        if name == 'subscription':
            return self.__dict__['subscription']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'subscription':
            self.__dict__['subscription'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_EVENT_SUBSCRIPTION, self.__dict__['subscription'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_EVENT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_EVENT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['subscription'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_EVENT_SUBSCRIPTION)


class ResultTaskServiceTriggerTime:

    def __init__(self):
        self.__dict__['randomDelay'] = ''

    def __getattr__(self, name):
        if name == 'randomDelay':
            return self.__dict__['randomDelay']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'randomDelay':
            self.__dict__['randomDelay'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_TIME_RANDOM_DELAY, self.__dict__['randomDelay'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_TIME, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_TIME, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['randomDelay'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_TIME_RANDOM_DELAY)


class ResultTaskServiceTriggerDaily:

    def __init__(self):
        self.__dict__['randomDelay'] = ''
        self.__dict__['daysInterval'] = 0

    def __getattr__(self, name):
        if name == 'randomDelay':
            return self.__dict__['randomDelay']
        if name == 'daysInterval':
            return self.__dict__['daysInterval']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'randomDelay':
            self.__dict__['randomDelay'] = value
        elif name == 'daysInterval':
            self.__dict__['daysInterval'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_DAILY_RANDOM_DELAY, self.__dict__['randomDelay'])
        submsg.AddS16(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_DAILY_DAYS_INTERVAL, self.__dict__['daysInterval'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_DAILY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_DAILY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['randomDelay'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_DAILY_RANDOM_DELAY)
        self.__dict__['daysInterval'] = submsg.FindS16(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_DAILY_DAYS_INTERVAL)


class ResultTaskServiceTriggerWeekly:

    def __init__(self):
        self.__dict__['randomDelay'] = ''
        self.__dict__['daysOfWeek'] = 0

    def __getattr__(self, name):
        if name == 'randomDelay':
            return self.__dict__['randomDelay']
        if name == 'daysOfWeek':
            return self.__dict__['daysOfWeek']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'randomDelay':
            self.__dict__['randomDelay'] = value
        elif name == 'daysOfWeek':
            self.__dict__['daysOfWeek'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_WEEKLY_RANDOM_DELAY, self.__dict__['randomDelay'])
        submsg.AddS16(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_WEEKLY_DAYS_OF_WEEK, self.__dict__['daysOfWeek'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_WEEKLY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_WEEKLY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['randomDelay'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_WEEKLY_RANDOM_DELAY)
        self.__dict__['daysOfWeek'] = submsg.FindS16(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_WEEKLY_DAYS_OF_WEEK)


class ResultTaskServiceTriggerMonthly:

    def __init__(self):
        self.__dict__['randomDelay'] = ''
        self.__dict__['daysOfMonth'] = 0
        self.__dict__['monthsOfYear'] = 0
        self.__dict__['runOnLastDayOfMonth'] = False

    def __getattr__(self, name):
        if name == 'randomDelay':
            return self.__dict__['randomDelay']
        if name == 'daysOfMonth':
            return self.__dict__['daysOfMonth']
        if name == 'monthsOfYear':
            return self.__dict__['monthsOfYear']
        if name == 'runOnLastDayOfMonth':
            return self.__dict__['runOnLastDayOfMonth']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'randomDelay':
            self.__dict__['randomDelay'] = value
        elif name == 'daysOfMonth':
            self.__dict__['daysOfMonth'] = value
        elif name == 'monthsOfYear':
            self.__dict__['monthsOfYear'] = value
        elif name == 'runOnLastDayOfMonth':
            self.__dict__['runOnLastDayOfMonth'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY_RANDOM_DELAY, self.__dict__['randomDelay'])
        submsg.AddS32(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY_DAYS_OF_MONTH, self.__dict__['daysOfMonth'])
        submsg.AddS16(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY_MONTHS_OF_YEAR, self.__dict__['monthsOfYear'])
        submsg.AddBool(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY_RUN_ON_LAST_DAY_OF_MONTH, self.__dict__['runOnLastDayOfMonth'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['randomDelay'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY_RANDOM_DELAY)
        self.__dict__['daysOfMonth'] = submsg.FindS32(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY_DAYS_OF_MONTH)
        self.__dict__['monthsOfYear'] = submsg.FindS16(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY_MONTHS_OF_YEAR)
        self.__dict__['runOnLastDayOfMonth'] = submsg.FindBool(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY_RUN_ON_LAST_DAY_OF_MONTH)


class ResultTaskServiceTriggerMonthlyDOW:

    def __init__(self):
        self.__dict__['randomDelay'] = ''
        self.__dict__['daysOfWeek'] = 0
        self.__dict__['monthsOfYear'] = 0
        self.__dict__['weeksOfMonth'] = 0
        self.__dict__['runOnLastWeekOfMonth'] = False

    def __getattr__(self, name):
        if name == 'randomDelay':
            return self.__dict__['randomDelay']
        if name == 'daysOfWeek':
            return self.__dict__['daysOfWeek']
        if name == 'monthsOfYear':
            return self.__dict__['monthsOfYear']
        if name == 'weeksOfMonth':
            return self.__dict__['weeksOfMonth']
        if name == 'runOnLastWeekOfMonth':
            return self.__dict__['runOnLastWeekOfMonth']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'randomDelay':
            self.__dict__['randomDelay'] = value
        elif name == 'daysOfWeek':
            self.__dict__['daysOfWeek'] = value
        elif name == 'monthsOfYear':
            self.__dict__['monthsOfYear'] = value
        elif name == 'weeksOfMonth':
            self.__dict__['weeksOfMonth'] = value
        elif name == 'runOnLastWeekOfMonth':
            self.__dict__['runOnLastWeekOfMonth'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_RANDOM_DELAY, self.__dict__['randomDelay'])
        submsg.AddS16(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_DAYS_OF_WEEK, self.__dict__['daysOfWeek'])
        submsg.AddS16(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_MONTHS_OF_YEAR, self.__dict__['monthsOfYear'])
        submsg.AddS16(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_WEEKS_OF_MONTH, self.__dict__['weeksOfMonth'])
        submsg.AddBool(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_RUN_ON_LAST_WEEK_OF_MONTH, self.__dict__['runOnLastWeekOfMonth'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['randomDelay'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_RANDOM_DELAY)
        self.__dict__['daysOfWeek'] = submsg.FindS16(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_DAYS_OF_WEEK)
        self.__dict__['monthsOfYear'] = submsg.FindS16(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_MONTHS_OF_YEAR)
        self.__dict__['weeksOfMonth'] = submsg.FindS16(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_WEEKS_OF_MONTH)
        self.__dict__['runOnLastWeekOfMonth'] = submsg.FindBool(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_RUN_ON_LAST_WEEK_OF_MONTH)


class ResultTaskServiceTriggerRegistration:

    def __init__(self):
        self.__dict__['delay'] = ''

    def __getattr__(self, name):
        if name == 'delay':
            return self.__dict__['delay']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'delay':
            self.__dict__['delay'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_REGISTRATION_DELAY, self.__dict__['delay'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_REGISTRATION, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_REGISTRATION, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['delay'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_REGISTRATION_DELAY)


class ResultTaskServiceTriggerBoot:

    def __init__(self):
        self.__dict__['delay'] = ''

    def __getattr__(self, name):
        if name == 'delay':
            return self.__dict__['delay']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'delay':
            self.__dict__['delay'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_BOOT_DELAY, self.__dict__['delay'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_BOOT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_BOOT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['delay'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_BOOT_DELAY)


class ResultTaskServiceTriggerLogon:

    def __init__(self):
        self.__dict__['delay'] = ''
        self.__dict__['userId'] = ''

    def __getattr__(self, name):
        if name == 'delay':
            return self.__dict__['delay']
        if name == 'userId':
            return self.__dict__['userId']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'delay':
            self.__dict__['delay'] = value
        elif name == 'userId':
            self.__dict__['userId'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_LOGON_DELAY, self.__dict__['delay'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_LOGON_USER_ID, self.__dict__['userId'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_LOGON, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_LOGON, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['delay'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_LOGON_DELAY)
        self.__dict__['userId'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_LOGON_USER_ID)


class ResultTaskServiceTriggerSessionStateChange:

    def __init__(self):
        self.__dict__['delay'] = ''
        self.__dict__['userId'] = ''
        self.__dict__['change'] = RESULT_TASKSERVICEJOB_TRIGGER_CHANGE_UNKNOWN

    def __getattr__(self, name):
        if name == 'delay':
            return self.__dict__['delay']
        if name == 'userId':
            return self.__dict__['userId']
        if name == 'change':
            return self.__dict__['change']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'delay':
            self.__dict__['delay'] = value
        elif name == 'userId':
            self.__dict__['userId'] = value
        elif name == 'change':
            self.__dict__['change'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_SESSION_STATE_CHANGE_DELAY, self.__dict__['delay'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_SESSION_STATE_CHANGE_USER_ID, self.__dict__['userId'])
        submsg.AddU8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_SESSION_STATE_CHANGE_CHANGE, self.__dict__['change'])
        mmsg.AddMessage(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_SESSION_STATE_CHANGE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_SESSION_STATE_CHANGE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['delay'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_SESSION_STATE_CHANGE_DELAY)
        self.__dict__['userId'] = submsg.FindString(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_SESSION_STATE_CHANGE_USER_ID)
        self.__dict__['change'] = submsg.FindU8(MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_SESSION_STATE_CHANGE_CHANGE)