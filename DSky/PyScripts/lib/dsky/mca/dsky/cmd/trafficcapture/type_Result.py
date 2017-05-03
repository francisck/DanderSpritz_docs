# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import array

class ResultGetStatus:

    def __init__(self):
        self.__dict__['filterActive'] = False
        self.__dict__['packetThreadRunning'] = False
        self.__dict__['maxCaptureFileSize'] = 0
        self.__dict__['captureFileSize'] = 0
        self.__dict__['maxPacketSize'] = 0
        self.__dict__['majorVersion'] = 0
        self.__dict__['minorVersion'] = 0
        self.__dict__['revision'] = 0
        self.__dict__['captureFile'] = ''
        self.__dict__['key'] = array.array('B')

    def __getattr__(self, name):
        if name == 'filterActive':
            return self.__dict__['filterActive']
        if name == 'packetThreadRunning':
            return self.__dict__['packetThreadRunning']
        if name == 'maxCaptureFileSize':
            return self.__dict__['maxCaptureFileSize']
        if name == 'captureFileSize':
            return self.__dict__['captureFileSize']
        if name == 'maxPacketSize':
            return self.__dict__['maxPacketSize']
        if name == 'majorVersion':
            return self.__dict__['majorVersion']
        if name == 'minorVersion':
            return self.__dict__['minorVersion']
        if name == 'revision':
            return self.__dict__['revision']
        if name == 'captureFile':
            return self.__dict__['captureFile']
        if name == 'key':
            return self.__dict__['key']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'filterActive':
            self.__dict__['filterActive'] = value
        elif name == 'packetThreadRunning':
            self.__dict__['packetThreadRunning'] = value
        elif name == 'maxCaptureFileSize':
            self.__dict__['maxCaptureFileSize'] = value
        elif name == 'captureFileSize':
            self.__dict__['captureFileSize'] = value
        elif name == 'maxPacketSize':
            self.__dict__['maxPacketSize'] = value
        elif name == 'majorVersion':
            self.__dict__['majorVersion'] = value
        elif name == 'minorVersion':
            self.__dict__['minorVersion'] = value
        elif name == 'revision':
            self.__dict__['revision'] = value
        elif name == 'captureFile':
            self.__dict__['captureFile'] = value
        elif name == 'key':
            self.__dict__['key'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_GET_STATUS_FILTER_ACTIVE, self.__dict__['filterActive'])
        submsg.AddBool(MSG_KEY_RESULT_GET_STATUS_PACKET_THREAD_RUNNING, self.__dict__['packetThreadRunning'])
        submsg.AddU64(MSG_KEY_RESULT_GET_STATUS_MAX_CAPTURE_FILE_SIZE, self.__dict__['maxCaptureFileSize'])
        submsg.AddU64(MSG_KEY_RESULT_GET_STATUS_CAPTURE_FILE_SIZE, self.__dict__['captureFileSize'])
        submsg.AddU32(MSG_KEY_RESULT_GET_STATUS_MAX_PACKET_SIZE, self.__dict__['maxPacketSize'])
        submsg.AddU8(MSG_KEY_RESULT_GET_STATUS_MAJOR_VERSION, self.__dict__['majorVersion'])
        submsg.AddU8(MSG_KEY_RESULT_GET_STATUS_MINOR_VERSION, self.__dict__['minorVersion'])
        submsg.AddU8(MSG_KEY_RESULT_GET_STATUS_REVISION, self.__dict__['revision'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_GET_STATUS_CAPTURE_FILE, self.__dict__['captureFile'])
        submsg.AddData(MSG_KEY_RESULT_GET_STATUS_KEY, self.__dict__['key'])
        mmsg.AddMessage(MSG_KEY_RESULT_GET_STATUS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_GET_STATUS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['filterActive'] = submsg.FindBool(MSG_KEY_RESULT_GET_STATUS_FILTER_ACTIVE)
        self.__dict__['packetThreadRunning'] = submsg.FindBool(MSG_KEY_RESULT_GET_STATUS_PACKET_THREAD_RUNNING)
        self.__dict__['maxCaptureFileSize'] = submsg.FindU64(MSG_KEY_RESULT_GET_STATUS_MAX_CAPTURE_FILE_SIZE)
        self.__dict__['captureFileSize'] = submsg.FindU64(MSG_KEY_RESULT_GET_STATUS_CAPTURE_FILE_SIZE)
        self.__dict__['maxPacketSize'] = submsg.FindU32(MSG_KEY_RESULT_GET_STATUS_MAX_PACKET_SIZE)
        self.__dict__['majorVersion'] = submsg.FindU8(MSG_KEY_RESULT_GET_STATUS_MAJOR_VERSION)
        self.__dict__['minorVersion'] = submsg.FindU8(MSG_KEY_RESULT_GET_STATUS_MINOR_VERSION)
        self.__dict__['revision'] = submsg.FindU8(MSG_KEY_RESULT_GET_STATUS_REVISION)
        self.__dict__['captureFile'] = submsg.FindString(MSG_KEY_RESULT_GET_STATUS_CAPTURE_FILE)
        self.__dict__['key'] = submsg.FindData(MSG_KEY_RESULT_GET_STATUS_KEY)


class ResultGetFilter:

    def __init__(self):
        self.__dict__['adapterFilter'] = 0
        self.__dict__['filter'] = array.array('B')

    def __getattr__(self, name):
        if name == 'adapterFilter':
            return self.__dict__['adapterFilter']
        if name == 'filter':
            return self.__dict__['filter']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'adapterFilter':
            self.__dict__['adapterFilter'] = value
        elif name == 'filter':
            self.__dict__['filter'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_GET_FILTER_ADAPTER_FILTER, self.__dict__['adapterFilter'])
        submsg.AddData(MSG_KEY_RESULT_GET_FILTER_FILTER, self.__dict__['filter'])
        mmsg.AddMessage(MSG_KEY_RESULT_GET_FILTER, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_GET_FILTER, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['adapterFilter'] = submsg.FindU32(MSG_KEY_RESULT_GET_FILTER_ADAPTER_FILTER)
        self.__dict__['filter'] = submsg.FindData(MSG_KEY_RESULT_GET_FILTER_FILTER)


class ResultValidateFilter:

    def __init__(self):
        self.__dict__['adapterFilter'] = 0
        self.__dict__['filter'] = array.array('B')

    def __getattr__(self, name):
        if name == 'adapterFilter':
            return self.__dict__['adapterFilter']
        if name == 'filter':
            return self.__dict__['filter']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'adapterFilter':
            self.__dict__['adapterFilter'] = value
        elif name == 'filter':
            self.__dict__['filter'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_VALIDATE_FILTER_ADAPTER_FILTER, self.__dict__['adapterFilter'])
        submsg.AddData(MSG_KEY_RESULT_VALIDATE_FILTER_FILTER, self.__dict__['filter'])
        mmsg.AddMessage(MSG_KEY_RESULT_VALIDATE_FILTER, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_VALIDATE_FILTER, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['adapterFilter'] = submsg.FindU32(MSG_KEY_RESULT_VALIDATE_FILTER_ADAPTER_FILTER)
        self.__dict__['filter'] = submsg.FindData(MSG_KEY_RESULT_VALIDATE_FILTER_FILTER)


class ResultSendControl:

    def __init__(self):
        self.__dict__['controlType'] = 0

    def __getattr__(self, name):
        if name == 'controlType':
            return self.__dict__['controlType']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'controlType':
            self.__dict__['controlType'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_SEND_CONTROL_CONTROL_TYPE, self.__dict__['controlType'])
        mmsg.AddMessage(MSG_KEY_RESULT_SEND_CONTROL, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_SEND_CONTROL, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['controlType'] = submsg.FindU8(MSG_KEY_RESULT_SEND_CONTROL_CONTROL_TYPE)