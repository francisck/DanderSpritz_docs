# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime
RESULT_STATUS_TRIGGER_NONE = 0
RESULT_STATUS_TRIGGER_ACCEPTED = 1
RESULT_STATUS_TRIGGER_DECRYPT_FAILED = 2
RESULT_STATUS_TRIGGER_BAD_SIZE = 3
RESULT_STATUS_TRIGGER_BAD_ID = 4
RESULT_STATUS_TRIGGER_BAD_TIMESTAMP = 5
RESULT_STATUS_TRIGGER_BAD_DST_ADDRESS = 6
RESULT_STATUS_TRIGGER_DELIVERY_FAILED = 7
RESULT_STATUS_TRIGGER_UNSUPPORTED_TYPE = 8
RESULT_STATUS_TRIGGER_INVALID_AUTH = 9
RESULT_STATUS_TRIGGER_OTHER_FAILURE = 10

class ResultStatus:

    def __init__(self):
        self.__dict__['index'] = 0
        self.__dict__['boundProcess'] = 0
        self.__dict__['lastTriggerTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['lastTriggerStatus'] = RESULT_STATUS_TRIGGER_NONE
        self.__dict__['commsPath'] = ''

    def __getattr__(self, name):
        if name == 'index':
            return self.__dict__['index']
        if name == 'boundProcess':
            return self.__dict__['boundProcess']
        if name == 'lastTriggerTime':
            return self.__dict__['lastTriggerTime']
        if name == 'lastTriggerStatus':
            return self.__dict__['lastTriggerStatus']
        if name == 'commsPath':
            return self.__dict__['commsPath']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'index':
            self.__dict__['index'] = value
        elif name == 'boundProcess':
            self.__dict__['boundProcess'] = value
        elif name == 'lastTriggerTime':
            self.__dict__['lastTriggerTime'] = value
        elif name == 'lastTriggerStatus':
            self.__dict__['lastTriggerStatus'] = value
        elif name == 'commsPath':
            self.__dict__['commsPath'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_STATUS_INDEX, self.__dict__['index'])
        submsg.AddU32(MSG_KEY_RESULT_STATUS_BOUND_PROCESS, self.__dict__['boundProcess'])
        submsg.AddTime(MSG_KEY_RESULT_STATUS_LAST_TRIGGER_TIME, self.__dict__['lastTriggerTime'])
        submsg.AddU32(MSG_KEY_RESULT_STATUS_LAST_TRIGGER_STATUS, self.__dict__['lastTriggerStatus'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_STATUS_COMMS_PATH, self.__dict__['commsPath'])
        mmsg.AddMessage(MSG_KEY_RESULT_STATUS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_STATUS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['index'] = submsg.FindU8(MSG_KEY_RESULT_STATUS_INDEX)
        self.__dict__['boundProcess'] = submsg.FindU32(MSG_KEY_RESULT_STATUS_BOUND_PROCESS)
        self.__dict__['lastTriggerTime'] = submsg.FindTime(MSG_KEY_RESULT_STATUS_LAST_TRIGGER_TIME)
        self.__dict__['lastTriggerStatus'] = submsg.FindU32(MSG_KEY_RESULT_STATUS_LAST_TRIGGER_STATUS)
        self.__dict__['commsPath'] = submsg.FindString(MSG_KEY_RESULT_STATUS_COMMS_PATH)


class ResultVersion:

    def __init__(self):
        self.__dict__['major'] = 0
        self.__dict__['minor'] = 0
        self.__dict__['fix'] = 0

    def __getattr__(self, name):
        if name == 'major':
            return self.__dict__['major']
        if name == 'minor':
            return self.__dict__['minor']
        if name == 'fix':
            return self.__dict__['fix']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'major':
            self.__dict__['major'] = value
        elif name == 'minor':
            self.__dict__['minor'] = value
        elif name == 'fix':
            self.__dict__['fix'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_VERSION_MAJOR, self.__dict__['major'])
        submsg.AddU8(MSG_KEY_RESULT_VERSION_MINOR, self.__dict__['minor'])
        submsg.AddU8(MSG_KEY_RESULT_VERSION_FIX, self.__dict__['fix'])
        mmsg.AddMessage(MSG_KEY_RESULT_VERSION, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_VERSION, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['major'] = submsg.FindU8(MSG_KEY_RESULT_VERSION_MAJOR)
        self.__dict__['minor'] = submsg.FindU8(MSG_KEY_RESULT_VERSION_MINOR)
        self.__dict__['fix'] = submsg.FindU8(MSG_KEY_RESULT_VERSION_FIX)


class ResultFilterInfo:

    def __init__(self):
        self.__dict__['filterActive'] = False
        self.__dict__['threadRunning'] = False

    def __getattr__(self, name):
        if name == 'filterActive':
            return self.__dict__['filterActive']
        if name == 'threadRunning':
            return self.__dict__['threadRunning']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'filterActive':
            self.__dict__['filterActive'] = value
        elif name == 'threadRunning':
            self.__dict__['threadRunning'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_FILTER_INFO_FILTER_ACTIVE, self.__dict__['filterActive'])
        submsg.AddBool(MSG_KEY_RESULT_FILTER_INFO_THREAD_RUNNING, self.__dict__['threadRunning'])
        mmsg.AddMessage(MSG_KEY_RESULT_FILTER_INFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_FILTER_INFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['filterActive'] = submsg.FindBool(MSG_KEY_RESULT_FILTER_INFO_FILTER_ACTIVE)
        self.__dict__['threadRunning'] = submsg.FindBool(MSG_KEY_RESULT_FILTER_INFO_THREAD_RUNNING)