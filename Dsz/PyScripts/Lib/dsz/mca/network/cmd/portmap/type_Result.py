# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
RESULT_PORT_STATE_UNKNOWN = 0
RESULT_PORT_STATE_OPEN = 1
RESULT_PORT_STATE_BOUND = 2
RESULT_PORT_STATE_LISTENING = 3
RESULT_PORT_STATE_CONNECTED = 4
RESULT_PORT_STATE_CLEANUP = 5
RESULT_PORT_STATE_CLOSING = 6
RESULT_PORT_STATE_TRANSMIT_CLOSING = 7
RESULT_PORT_STATE_INVALID = 8
RESULT_PORT_TYPE_UNKNOWN = 0
RESULT_PORT_TYPE_UDP = 1
RESULT_PORT_TYPE_TCP = 2
RESULT_PORT_TYPE_RAW = 3

class Result:

    def __init__(self):
        self.__dict__['hitMax'] = False
        self.__dict__['processId'] = 0
        self.__dict__['srcPort'] = 0
        self.__dict__['state'] = RESULT_PORT_STATE_UNKNOWN
        self.__dict__['type'] = RESULT_PORT_TYPE_UNKNOWN
        self.__dict__['srcAddr'] = ''
        self.__dict__['procName'] = ''

    def __getattr__(self, name):
        if name == 'hitMax':
            return self.__dict__['hitMax']
        if name == 'processId':
            return self.__dict__['processId']
        if name == 'srcPort':
            return self.__dict__['srcPort']
        if name == 'state':
            return self.__dict__['state']
        if name == 'type':
            return self.__dict__['type']
        if name == 'srcAddr':
            return self.__dict__['srcAddr']
        if name == 'procName':
            return self.__dict__['procName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'hitMax':
            self.__dict__['hitMax'] = value
        elif name == 'processId':
            self.__dict__['processId'] = value
        elif name == 'srcPort':
            self.__dict__['srcPort'] = value
        elif name == 'state':
            self.__dict__['state'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        elif name == 'srcAddr':
            self.__dict__['srcAddr'] = value
        elif name == 'procName':
            self.__dict__['procName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_HIT_MAX, self.__dict__['hitMax'])
        submsg.AddU32(MSG_KEY_RESULT_PROCESS_ID, self.__dict__['processId'])
        submsg.AddU16(MSG_KEY_RESULT_SOURCE_PORT, self.__dict__['srcPort'])
        submsg.AddU8(MSG_KEY_RESULT_STATE, self.__dict__['state'])
        submsg.AddU8(MSG_KEY_RESULT_TYPE, self.__dict__['type'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_SOURCE_ADDRESS, self.__dict__['srcAddr'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_PROCESS_NAME, self.__dict__['procName'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['hitMax'] = submsg.FindBool(MSG_KEY_RESULT_HIT_MAX)
        self.__dict__['processId'] = submsg.FindU32(MSG_KEY_RESULT_PROCESS_ID)
        self.__dict__['srcPort'] = submsg.FindU16(MSG_KEY_RESULT_SOURCE_PORT)
        self.__dict__['state'] = submsg.FindU8(MSG_KEY_RESULT_STATE)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_TYPE)
        self.__dict__['srcAddr'] = submsg.FindString(MSG_KEY_RESULT_SOURCE_ADDRESS)
        self.__dict__['procName'] = submsg.FindString(MSG_KEY_RESULT_PROCESS_NAME)