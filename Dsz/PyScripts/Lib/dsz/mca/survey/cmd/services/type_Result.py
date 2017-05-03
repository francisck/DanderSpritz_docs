# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
RESULT_SERVICE_STATE_STOPPED = 1
RESULT_SERVICE_STATE_START_PENDING = 2
RESULT_SERVICE_STATE_STOP_PENDING = 3
RESULT_SERVICE_STATE_RUNNING = 4
RESULT_SERVICE_STATE_CONTINUE_PENDING = 5
RESULT_SERVICE_STATE_PAUSE_PENDING = 6
RESULT_SERVICE_STATE_PAUSED = 7
RESULT_SERVICE_TYPE_KERNEL_DRIVER = 1
RESULT_SERVICE_TYPE_FILE_SYSTEM_DRIVER = 2
RESULT_SERVICE_TYPE_OWN_PROCESS = 16
RESULT_SERVICE_TYPE_SHARE_PROCESS = 32
RESULT_SERVICE_TYPE_INTERACTIVE_PROCESS = 256
RESULT_CONTROL_ACCEPT_STOP = 1
RESULT_CONTROL_ACCEPT_PAUSE_CONTINUE = 2
RESULT_CONTROL_ACCEPT_SHUTDOWN = 4
RESULT_CONTROL_ACCEPT_PARAMCHANGE = 8
RESULT_CONTROL_ACCEPT_NETBINDCHANGE = 16
RESULT_CONTROL_ACCEPT_HARDWAREPROFILECHANGE = 32
RESULT_CONTROL_ACCEPT_POWEREVENT = 64
RESULT_CONTROL_ACCEPT_SESSIONCHANGE = 128

class Result:

    def __init__(self):
        self.__dict__['serviceState'] = 0
        self.__dict__['serviceType'] = 0
        self.__dict__['serviceControls'] = 0
        self.__dict__['name'] = ''
        self.__dict__['displayName'] = ''

    def __getattr__(self, name):
        if name == 'serviceState':
            return self.__dict__['serviceState']
        if name == 'serviceType':
            return self.__dict__['serviceType']
        if name == 'serviceControls':
            return self.__dict__['serviceControls']
        if name == 'name':
            return self.__dict__['name']
        if name == 'displayName':
            return self.__dict__['displayName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'serviceState':
            self.__dict__['serviceState'] = value
        elif name == 'serviceType':
            self.__dict__['serviceType'] = value
        elif name == 'serviceControls':
            self.__dict__['serviceControls'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        elif name == 'displayName':
            self.__dict__['displayName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_SERVICE_STATE, self.__dict__['serviceState'])
        submsg.AddU32(MSG_KEY_RESULT_SERVICE_TYPE, self.__dict__['serviceType'])
        submsg.AddU32(MSG_KEY_RESULT_SERVICE_CONTROLS, self.__dict__['serviceControls'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_NAME, self.__dict__['name'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DISPLAY_NAME, self.__dict__['displayName'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['serviceState'] = submsg.FindU32(MSG_KEY_RESULT_SERVICE_STATE)
        self.__dict__['serviceType'] = submsg.FindU32(MSG_KEY_RESULT_SERVICE_TYPE)
        self.__dict__['serviceControls'] = submsg.FindU32(MSG_KEY_RESULT_SERVICE_CONTROLS)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_NAME)
        self.__dict__['displayName'] = submsg.FindString(MSG_KEY_RESULT_DISPLAY_NAME)