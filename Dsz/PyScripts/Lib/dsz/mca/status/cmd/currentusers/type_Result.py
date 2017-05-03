# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime

class Result:

    def __init__(self):
        self.__dict__['pid'] = 0
        self.__dict__['sessionId'] = 0
        self.__dict__['loginTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['idleTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['lastActivity'] = mcl.object.MclTime.MclTime()
        self.__dict__['userName'] = ''
        self.__dict__['hostName'] = ''
        self.__dict__['devName'] = ''

    def __getattr__(self, name):
        if name == 'pid':
            return self.__dict__['pid']
        if name == 'sessionId':
            return self.__dict__['sessionId']
        if name == 'loginTime':
            return self.__dict__['loginTime']
        if name == 'idleTime':
            return self.__dict__['idleTime']
        if name == 'lastActivity':
            return self.__dict__['lastActivity']
        if name == 'userName':
            return self.__dict__['userName']
        if name == 'hostName':
            return self.__dict__['hostName']
        if name == 'devName':
            return self.__dict__['devName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'pid':
            self.__dict__['pid'] = value
        elif name == 'sessionId':
            self.__dict__['sessionId'] = value
        elif name == 'loginTime':
            self.__dict__['loginTime'] = value
        elif name == 'idleTime':
            self.__dict__['idleTime'] = value
        elif name == 'lastActivity':
            self.__dict__['lastActivity'] = value
        elif name == 'userName':
            self.__dict__['userName'] = value
        elif name == 'hostName':
            self.__dict__['hostName'] = value
        elif name == 'devName':
            self.__dict__['devName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_PROCESS_ID, self.__dict__['pid'])
        submsg.AddU32(MSG_KEY_RESULT_SESSION_ID, self.__dict__['sessionId'])
        submsg.AddTime(MSG_KEY_RESULT_LOGIN_TIME, self.__dict__['loginTime'])
        submsg.AddTime(MSG_KEY_RESULT_IDLE_TIME, self.__dict__['idleTime'])
        submsg.AddTime(MSG_KEY_RESULT_LAST_ACTIVITY, self.__dict__['lastActivity'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_USER_NAME, self.__dict__['userName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_HOST_NAME, self.__dict__['hostName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DEVICE_NAME, self.__dict__['devName'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['pid'] = submsg.FindU32(MSG_KEY_RESULT_PROCESS_ID)
        self.__dict__['sessionId'] = submsg.FindU32(MSG_KEY_RESULT_SESSION_ID)
        self.__dict__['loginTime'] = submsg.FindTime(MSG_KEY_RESULT_LOGIN_TIME)
        self.__dict__['idleTime'] = submsg.FindTime(MSG_KEY_RESULT_IDLE_TIME)
        self.__dict__['lastActivity'] = submsg.FindTime(MSG_KEY_RESULT_LAST_ACTIVITY)
        self.__dict__['userName'] = submsg.FindString(MSG_KEY_RESULT_USER_NAME)
        self.__dict__['hostName'] = submsg.FindString(MSG_KEY_RESULT_HOST_NAME)
        self.__dict__['devName'] = submsg.FindString(MSG_KEY_RESULT_DEVICE_NAME)