# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
PARAMS_FLAG_REDIRECT = 1
PARAMS_FLAG_WAIT = 2
PARAMS_FLAG_CHANGE_USER = 4
PARAMS_STRING_TYPE_DEFAULT = 0
PARAMS_STRING_TYPE_UNICODE = 1
PARAMS_STRING_TYPE_OEM = 2
PARAMS_STRING_TYPE_UTF8 = 3

class StartParams:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['inputType'] = PARAMS_STRING_TYPE_DEFAULT
        self.__dict__['outputType'] = PARAMS_STRING_TYPE_DEFAULT
        self.__dict__['uid'] = 0
        self.__dict__['gid'] = 0
        self.__dict__['cmd'] = ''
        self.__dict__['dir'] = ''
        self.__dict__['readLoops'] = 20

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'inputType':
            return self.__dict__['inputType']
        if name == 'outputType':
            return self.__dict__['outputType']
        if name == 'uid':
            return self.__dict__['uid']
        if name == 'gid':
            return self.__dict__['gid']
        if name == 'cmd':
            return self.__dict__['cmd']
        if name == 'dir':
            return self.__dict__['dir']
        if name == 'readLoops':
            return self.__dict__['readLoops']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'inputType':
            self.__dict__['inputType'] = value
        elif name == 'outputType':
            self.__dict__['outputType'] = value
        elif name == 'uid':
            self.__dict__['uid'] = value
        elif name == 'gid':
            self.__dict__['gid'] = value
        elif name == 'cmd':
            self.__dict__['cmd'] = value
        elif name == 'dir':
            self.__dict__['dir'] = value
        elif name == 'readLoops':
            self.__dict__['readLoops'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_PARAMS_START_FLAGS, self.__dict__['flags'])
        submsg.AddU8(MSG_KEY_PARAMS_START_INPUT_TYPE, self.__dict__['inputType'])
        submsg.AddU8(MSG_KEY_PARAMS_START_OUTPUT_TYPE, self.__dict__['outputType'])
        submsg.AddU32(MSG_KEY_PARAMS_START_UID, self.__dict__['uid'])
        submsg.AddU32(MSG_KEY_PARAMS_START_GID, self.__dict__['gid'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_START_CMD, self.__dict__['cmd'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_START_DIR, self.__dict__['dir'])
        submsg.AddU8(MSG_KEY_PARAMS_READ_LOOPS, self.__dict__['readLoops'])
        mmsg.AddMessage(MSG_KEY_PARAMS_START, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_START, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_PARAMS_START_FLAGS)
        try:
            self.__dict__['inputType'] = submsg.FindU8(MSG_KEY_PARAMS_START_INPUT_TYPE)
        except:
            pass

        try:
            self.__dict__['outputType'] = submsg.FindU8(MSG_KEY_PARAMS_START_OUTPUT_TYPE)
        except:
            pass

        try:
            self.__dict__['uid'] = submsg.FindU32(MSG_KEY_PARAMS_START_UID)
        except:
            pass

        try:
            self.__dict__['gid'] = submsg.FindU32(MSG_KEY_PARAMS_START_GID)
        except:
            pass

        self.__dict__['cmd'] = submsg.FindString(MSG_KEY_PARAMS_START_CMD)
        try:
            self.__dict__['dir'] = submsg.FindString(MSG_KEY_PARAMS_START_DIR)
        except:
            pass

        try:
            self.__dict__['readLoops'] = submsg.FindU8(MSG_KEY_PARAMS_READ_LOOPS)
        except:
            pass


class InputParams:

    def __init__(self):
        self.__dict__['processId'] = 0
        self.__dict__['input'] = ''

    def __getattr__(self, name):
        if name == 'processId':
            return self.__dict__['processId']
        if name == 'input':
            return self.__dict__['input']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'processId':
            self.__dict__['processId'] = value
        elif name == 'input':
            self.__dict__['input'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU64(MSG_KEY_PARAMS_INPUT_PROCESS_ID, self.__dict__['processId'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_INPUT_INPUT, self.__dict__['input'])
        mmsg.AddMessage(MSG_KEY_PARAMS_INPUT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS_INPUT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['processId'] = submsg.FindU64(MSG_KEY_PARAMS_INPUT_PROCESS_ID)
        self.__dict__['input'] = submsg.FindString(MSG_KEY_PARAMS_INPUT_INPUT)