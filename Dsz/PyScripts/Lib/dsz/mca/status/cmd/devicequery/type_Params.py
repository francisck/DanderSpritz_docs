# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Params.py
from types import *
import array
PARAMS_DEVICE_TYPE_USER_SPECIFIC = 0
PARAMS_DEVICE_TYPE_U1394 = 1
PARAMS_DEVICE_TYPE_ADAPTER = 2
PARAMS_DEVICE_TYPE_ALL = 255
PARAMS_DEVICE_TYPE_APM_SUPPORT = 3
PARAMS_DEVICE_TYPE_BATTERY = 4
PARAMS_DEVICE_TYPE_CDROM = 5
PARAMS_DEVICE_TYPE_COMPUTER = 6
PARAMS_DEVICE_TYPE_DECODER = 7
PARAMS_DEVICE_TYPE_DISK_DRIVE = 8
PARAMS_DEVICE_TYPE_DISPLAY = 9
PARAMS_DEVICE_TYPE_FDC = 10
PARAMS_DEVICE_TYPE_FLOPPY = 11
PARAMS_DEVICE_TYPE_GPS = 12
PARAMS_DEVICE_TYPE_HDC = 13
PARAMS_DEVICE_TYPE_HID_CLASS = 14
PARAMS_DEVICE_TYPE_IMAGE = 15
PARAMS_DEVICE_TYPE_INFRARED = 16
PARAMS_DEVICE_TYPE_KEYBOARD = 17
PARAMS_DEVICE_TYPE_LEGACY_DRIVER = 18
PARAMS_DEVICE_TYPE_MEDIA = 19
PARAMS_DEVICE_TYPE_MEDIUM_CHANGER = 20
PARAMS_DEVICE_TYPE_MODEM = 21
PARAMS_DEVICE_TYPE_MONITOR = 22
PARAMS_DEVICE_TYPE_MOUSE = 23
PARAMS_DEVICE_TYPE_MTD = 24
PARAMS_DEVICE_TYPE_MULTIFUNCTION = 25
PARAMS_DEVICE_TYPE_MULTIPORT_SERIAL = 26
PARAMS_DEVICE_TYPE_NET = 27
PARAMS_DEVICE_TYPE_NET_CLIENT = 28
PARAMS_DEVICE_TYPE_NET_SERVICE = 29
PARAMS_DEVICE_TYPE_NET_TRANS = 30
PARAMS_DEVICE_TYPE_NO_DRIVER = 31
PARAMS_DEVICE_TYPE_PARALLEL = 32
PARAMS_DEVICE_TYPE_PCMCIA = 33
PARAMS_DEVICE_TYPE_PORTS = 34
PARAMS_DEVICE_TYPE_PRINTER = 35
PARAMS_DEVICE_TYPE_PRINTER_UPGRADE = 36
PARAMS_DEVICE_TYPE_SCSI_ADAPTER = 37
PARAMS_DEVICE_TYPE_SMART_CARD_READER = 38
PARAMS_DEVICE_TYPE_SOUND = 39
PARAMS_DEVICE_TYPE_STILL_IMAGE = 40
PARAMS_DEVICE_TYPE_SYSTEM = 41
PARAMS_DEVICE_TYPE_TAPE_DRIVE = 42
PARAMS_DEVICE_TYPE_UNKNOWN = 43
PARAMS_DEVICE_TYPE_USB = 44
PARAMS_DEVICE_TYPE_VOLUME = 45
PARAMS_DEVICE_TYPE_U1394DEBUG = 46
PARAMS_DEVICE_TYPE_U61883 = 47
PARAMS_DEVICE_TYPE_AVC = 48
PARAMS_DEVICE_TYPE_BIOMETRIC = 49
PARAMS_DEVICE_TYPE_BLUETOOTH = 50
PARAMS_DEVICE_TYPE_DOT4 = 51
PARAMS_DEVICE_TYPE_DOT4PRINT = 52
PARAMS_DEVICE_TYPE_ENUM1394 = 53
PARAMS_DEVICE_TYPE_INFINIBAND = 54
PARAMS_DEVICE_TYPE_PNPPRINTERS = 55
PARAMS_DEVICE_TYPE_PROCESSOR = 56
PARAMS_DEVICE_TYPE_SBP2 = 57
PARAMS_DEVICE_TYPE_SECURITYACCELERATOR = 58
PARAMS_DEVICE_TYPE_VOLUMESNAPSHOT = 59
PARAMS_DEVICE_TYPE_WCEUSBS = 60
PARAMS_GUID_LEN = 16

class Params:

    def __init__(self):
        self.__dict__['choice'] = PARAMS_DEVICE_TYPE_USER_SPECIFIC
        self.__dict__['guid'] = array.array('B')
        i = 0
        while i < PARAMS_GUID_LEN:
            self.__dict__['guid'].append(0)
            i = i + 1

    def __getattr__(self, name):
        if name == 'choice':
            return self.__dict__['choice']
        if name == 'guid':
            return self.__dict__['guid']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'choice':
            self.__dict__['choice'] = value
        elif name == 'guid':
            self.__dict__['guid'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_PARAMS_CHOICE, self.__dict__['choice'])
        submsg.AddData(MSG_KEY_PARAMS_GUID, self.__dict__['guid'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['choice'] = submsg.FindU32(MSG_KEY_PARAMS_CHOICE)
        try:
            self.__dict__['guid'] = submsg.FindData(MSG_KEY_PARAMS_GUID)
        except:
            pass