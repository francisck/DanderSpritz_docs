# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *

class Result:

    def __init__(self):
        self.__dict__['friendlyName'] = ''
        self.__dict__['deviceDesc'] = ''
        self.__dict__['hardwareId'] = ''
        self.__dict__['servicePath'] = ''
        self.__dict__['driver'] = ''
        self.__dict__['location'] = ''
        self.__dict__['mfg'] = ''
        self.__dict__['physicalDeviceObjectName'] = ''

    def __getattr__(self, name):
        if name == 'friendlyName':
            return self.__dict__['friendlyName']
        if name == 'deviceDesc':
            return self.__dict__['deviceDesc']
        if name == 'hardwareId':
            return self.__dict__['hardwareId']
        if name == 'servicePath':
            return self.__dict__['servicePath']
        if name == 'driver':
            return self.__dict__['driver']
        if name == 'location':
            return self.__dict__['location']
        if name == 'mfg':
            return self.__dict__['mfg']
        if name == 'physicalDeviceObjectName':
            return self.__dict__['physicalDeviceObjectName']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'friendlyName':
            self.__dict__['friendlyName'] = value
        elif name == 'deviceDesc':
            self.__dict__['deviceDesc'] = value
        elif name == 'hardwareId':
            self.__dict__['hardwareId'] = value
        elif name == 'servicePath':
            self.__dict__['servicePath'] = value
        elif name == 'driver':
            self.__dict__['driver'] = value
        elif name == 'location':
            self.__dict__['location'] = value
        elif name == 'mfg':
            self.__dict__['mfg'] = value
        elif name == 'physicalDeviceObjectName':
            self.__dict__['physicalDeviceObjectName'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddStringUtf8(MSG_KEY_RESULT_FRIENDLY_NAME, self.__dict__['friendlyName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DEVICE_DESCRIPTION, self.__dict__['deviceDesc'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_HARDWARE_ID, self.__dict__['hardwareId'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_SERVICE_PATH, self.__dict__['servicePath'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DRIVER, self.__dict__['driver'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_LOCATION, self.__dict__['location'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_MANUFACTURER, self.__dict__['mfg'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_PHYSICAL_DEVICE_OBJECT_NAME, self.__dict__['physicalDeviceObjectName'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['friendlyName'] = submsg.FindString(MSG_KEY_RESULT_FRIENDLY_NAME)
        self.__dict__['deviceDesc'] = submsg.FindString(MSG_KEY_RESULT_DEVICE_DESCRIPTION)
        self.__dict__['hardwareId'] = submsg.FindString(MSG_KEY_RESULT_HARDWARE_ID)
        self.__dict__['servicePath'] = submsg.FindString(MSG_KEY_RESULT_SERVICE_PATH)
        self.__dict__['driver'] = submsg.FindString(MSG_KEY_RESULT_DRIVER)
        self.__dict__['location'] = submsg.FindString(MSG_KEY_RESULT_LOCATION)
        self.__dict__['mfg'] = submsg.FindString(MSG_KEY_RESULT_MANUFACTURER)
        self.__dict__['physicalDeviceObjectName'] = submsg.FindString(MSG_KEY_RESULT_PHYSICAL_DEVICE_OBJECT_NAME)