# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime
RESULT_STATE_UNKNOWN = 0
RESULT_STATE_STANDARD = 1
RESULT_STATE_DAYLIGHT = 2

class Result:

    def __init__(self):
        self.__dict__['systemTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['localTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['bias'] = mcl.object.MclTime.MclTime()
        self.__dict__['standardName'] = ''
        self.__dict__['standardBias'] = mcl.object.MclTime.MclTime()
        self.__dict__['standardMonth'] = 0
        self.__dict__['standardWeek'] = 0
        self.__dict__['standardDay'] = 0
        self.__dict__['daylightName'] = ''
        self.__dict__['daylightBias'] = mcl.object.MclTime.MclTime()
        self.__dict__['daylightMonth'] = 0
        self.__dict__['daylightWeek'] = 0
        self.__dict__['daylightDay'] = 0
        self.__dict__['state'] = 0

    def __getattr__(self, name):
        if name == 'systemTime':
            return self.__dict__['systemTime']
        if name == 'localTime':
            return self.__dict__['localTime']
        if name == 'bias':
            return self.__dict__['bias']
        if name == 'standardName':
            return self.__dict__['standardName']
        if name == 'standardBias':
            return self.__dict__['standardBias']
        if name == 'standardMonth':
            return self.__dict__['standardMonth']
        if name == 'standardWeek':
            return self.__dict__['standardWeek']
        if name == 'standardDay':
            return self.__dict__['standardDay']
        if name == 'daylightName':
            return self.__dict__['daylightName']
        if name == 'daylightBias':
            return self.__dict__['daylightBias']
        if name == 'daylightMonth':
            return self.__dict__['daylightMonth']
        if name == 'daylightWeek':
            return self.__dict__['daylightWeek']
        if name == 'daylightDay':
            return self.__dict__['daylightDay']
        if name == 'state':
            return self.__dict__['state']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'systemTime':
            self.__dict__['systemTime'] = value
        elif name == 'localTime':
            self.__dict__['localTime'] = value
        elif name == 'bias':
            self.__dict__['bias'] = value
        elif name == 'standardName':
            self.__dict__['standardName'] = value
        elif name == 'standardBias':
            self.__dict__['standardBias'] = value
        elif name == 'standardMonth':
            self.__dict__['standardMonth'] = value
        elif name == 'standardWeek':
            self.__dict__['standardWeek'] = value
        elif name == 'standardDay':
            self.__dict__['standardDay'] = value
        elif name == 'daylightName':
            self.__dict__['daylightName'] = value
        elif name == 'daylightBias':
            self.__dict__['daylightBias'] = value
        elif name == 'daylightMonth':
            self.__dict__['daylightMonth'] = value
        elif name == 'daylightWeek':
            self.__dict__['daylightWeek'] = value
        elif name == 'daylightDay':
            self.__dict__['daylightDay'] = value
        elif name == 'state':
            self.__dict__['state'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddTime(MSG_KEY_RESULT_SYSTEM_TIME, self.__dict__['systemTime'])
        submsg.AddTime(MSG_KEY_RESULT_LOCAL_TIME, self.__dict__['localTime'])
        submsg.AddTime(MSG_KEY_RESULT_BIAS, self.__dict__['bias'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_STANDARD_NAME, self.__dict__['standardName'])
        submsg.AddTime(MSG_KEY_RESULT_STANDARD_BIAS, self.__dict__['standardBias'])
        submsg.AddU16(MSG_KEY_RESULT_STANDARD_MONTH, self.__dict__['standardMonth'])
        submsg.AddU16(MSG_KEY_RESULT_STANDARD_WEEK, self.__dict__['standardWeek'])
        submsg.AddU16(MSG_KEY_RESULT_STANDARD_DAY, self.__dict__['standardDay'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DAYLIGHT_NAME, self.__dict__['daylightName'])
        submsg.AddTime(MSG_KEY_RESULT_DAYLIGHT_BIAS, self.__dict__['daylightBias'])
        submsg.AddU16(MSG_KEY_RESULT_DAYLIGHT_MONTH, self.__dict__['daylightMonth'])
        submsg.AddU16(MSG_KEY_RESULT_DAYLIGHT_WEEK, self.__dict__['daylightWeek'])
        submsg.AddU16(MSG_KEY_RESULT_DAYLIGHT_DAY, self.__dict__['daylightDay'])
        submsg.AddU8(MSG_KEY_RESULT_STATE, self.__dict__['state'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['systemTime'] = submsg.FindTime(MSG_KEY_RESULT_SYSTEM_TIME)
        self.__dict__['localTime'] = submsg.FindTime(MSG_KEY_RESULT_LOCAL_TIME)
        self.__dict__['bias'] = submsg.FindTime(MSG_KEY_RESULT_BIAS)
        self.__dict__['standardName'] = submsg.FindString(MSG_KEY_RESULT_STANDARD_NAME)
        self.__dict__['standardBias'] = submsg.FindTime(MSG_KEY_RESULT_STANDARD_BIAS)
        self.__dict__['standardMonth'] = submsg.FindU16(MSG_KEY_RESULT_STANDARD_MONTH)
        self.__dict__['standardWeek'] = submsg.FindU16(MSG_KEY_RESULT_STANDARD_WEEK)
        self.__dict__['standardDay'] = submsg.FindU16(MSG_KEY_RESULT_STANDARD_DAY)
        self.__dict__['daylightName'] = submsg.FindString(MSG_KEY_RESULT_DAYLIGHT_NAME)
        self.__dict__['daylightBias'] = submsg.FindTime(MSG_KEY_RESULT_DAYLIGHT_BIAS)
        self.__dict__['daylightMonth'] = submsg.FindU16(MSG_KEY_RESULT_DAYLIGHT_MONTH)
        self.__dict__['daylightWeek'] = submsg.FindU16(MSG_KEY_RESULT_DAYLIGHT_WEEK)
        self.__dict__['daylightDay'] = submsg.FindU16(MSG_KEY_RESULT_DAYLIGHT_DAY)
        self.__dict__['state'] = submsg.FindU8(MSG_KEY_RESULT_STATE)