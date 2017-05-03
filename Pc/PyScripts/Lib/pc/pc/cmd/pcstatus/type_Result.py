# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime
RESULT_TRIGGER_TYPE_UNKNOWN = 0
RESULT_TRIGGER_TYPE_DMGZ = 1
RESULT_TRIGGER_TYPE_FLAV = 2
RESULT_TRIGGER_TYPE_RAW = 4
RESULT_TRIGGER_TYPE_KNOCK = 8
RESULT_TRIGGER_STATUS_NONE = 0
RESULT_TRIGGER_STATUS_ACCEPTED = 1
RESULT_TRIGGER_STATUS_DECRYPT_FAILED = 2
RESULT_TRIGGER_STATUS_BAD_SIZE = 3
RESULT_TRIGGER_STATUS_BAD_ID = 4
RESULT_TRIGGER_STATUS_BAD_TIMESTAMP = 5
RESULT_TRIGGER_STATUS_BAD_DST_ADDRESS = 6
RESULT_TRIGGER_STATUS_DELIVERY_FAILED = 7
RESULT_TRIGGER_STATUS_UNSUPPORTED_TYPE = 8
RESULT_TRIGGER_STATUS_INVALID_AUTH = 9
RESULT_TRIGGER_STATUS_OTHER_FAILURE = 10

class Result:

    def __init__(self):
        self.__dict__['major'] = 0
        self.__dict__['minor'] = 0
        self.__dict__['build'] = 0
        self.__dict__['triggerType'] = RESULT_TRIGGER_TYPE_UNKNOWN
        self.__dict__['pcId'] = 0
        self.__dict__['lastTriggerTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['lastTriggerStatus'] = RESULT_TRIGGER_STATUS_NONE
        self.__dict__['numTriggersReceived'] = 0
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'major':
            return self.__dict__['major']
        if name == 'minor':
            return self.__dict__['minor']
        if name == 'build':
            return self.__dict__['build']
        if name == 'triggerType':
            return self.__dict__['triggerType']
        if name == 'pcId':
            return self.__dict__['pcId']
        if name == 'lastTriggerTime':
            return self.__dict__['lastTriggerTime']
        if name == 'lastTriggerStatus':
            return self.__dict__['lastTriggerStatus']
        if name == 'numTriggersReceived':
            return self.__dict__['numTriggersReceived']
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'major':
            self.__dict__['major'] = value
        elif name == 'minor':
            self.__dict__['minor'] = value
        elif name == 'build':
            self.__dict__['build'] = value
        elif name == 'triggerType':
            self.__dict__['triggerType'] = value
        elif name == 'pcId':
            self.__dict__['pcId'] = value
        elif name == 'lastTriggerTime':
            self.__dict__['lastTriggerTime'] = value
        elif name == 'lastTriggerStatus':
            self.__dict__['lastTriggerStatus'] = value
        elif name == 'numTriggersReceived':
            self.__dict__['numTriggersReceived'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_RESULT_MAJOR, self.__dict__['major'])
        submsg.AddU16(MSG_KEY_RESULT_MINOR, self.__dict__['minor'])
        submsg.AddU16(MSG_KEY_RESULT_BUILD, self.__dict__['build'])
        submsg.AddU8(MSG_KEY_RESULT_TRIGGER_TYPE, self.__dict__['triggerType'])
        submsg.AddU16(MSG_KEY_RESULT_PC_ID, self.__dict__['pcId'])
        submsg.AddTime(MSG_KEY_RESULT_LAST_TRIGGER_TIME, self.__dict__['lastTriggerTime'])
        submsg.AddU8(MSG_KEY_RESULT_LAST_TRIGGER_STATUS, self.__dict__['lastTriggerStatus'])
        submsg.AddU32(MSG_KEY_RESULT_NUM_TRIGGERS_RECEIVED, self.__dict__['numTriggersReceived'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['major'] = submsg.FindU16(MSG_KEY_RESULT_MAJOR)
        self.__dict__['minor'] = submsg.FindU16(MSG_KEY_RESULT_MINOR)
        self.__dict__['build'] = submsg.FindU16(MSG_KEY_RESULT_BUILD)
        self.__dict__['triggerType'] = submsg.FindU8(MSG_KEY_RESULT_TRIGGER_TYPE)
        self.__dict__['pcId'] = submsg.FindU16(MSG_KEY_RESULT_PC_ID)
        self.__dict__['lastTriggerTime'] = submsg.FindTime(MSG_KEY_RESULT_LAST_TRIGGER_TIME)
        self.__dict__['lastTriggerStatus'] = submsg.FindU8(MSG_KEY_RESULT_LAST_TRIGGER_STATUS)
        self.__dict__['numTriggersReceived'] = submsg.FindU32(MSG_KEY_RESULT_NUM_TRIGGERS_RECEIVED)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_NAME)