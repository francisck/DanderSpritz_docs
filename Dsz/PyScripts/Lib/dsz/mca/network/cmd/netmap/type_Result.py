# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import array
import mcl.object.MclTime
RESULT_TYPE_ERROR = 0
RESULT_TYPE_DATA = 1
RESULT_MAX_ADDRS = 64
RESULT_FLAG_HAVE_OS_INFO = 1
RESULT_FLAG_HAVE_TIME = 2
RESULT_RESOURCETYPE_DISK = 1
RESULT_RESOURCETYPE_PRINT = 2
RESULT_RESOURCEDISPLAYTYPE_DOMAIN = 1
RESULT_RESOURCEDISPLAYTYPE_SERVER = 2
RESULT_RESOURCEDISPLAYTYPE_SHARE = 3
RESULT_RESOURCEDISPLAYTYPE_FILE = 4
RESULT_RESOURCEDISPLAYTYPE_GROUP = 5
RESULT_RESOURCEDISPLAYTYPE_NETWORK = 6
RESULT_RESOURCEDISPLAYTYPE_ROOT = 7
RESULT_RESOURCEDISPLAYTYPE_SHAREADMIN = 8
RESULT_RESOURCEDISPLAYTYPE_DIRECTORY = 9
RESULT_RESOURCEDISPLAYTYPE_TREE = 10
RESULT_RESOURCEDISPLAYTYPE_NDSCONTAINER = 11
RESULT_PLATFORM_UNKNOWN = 0
RESULT_PLATFORM_DOS = 1
RESULT_PLATFORM_OS2 = 2
RESULT_PLATFORM_NT = 3
RESULT_PLATFORM_OSF = 4
RESULT_PLATFORM_VMS = 5
RESULT_SOFTWARE_WORKSTATION = 1
RESULT_SOFTWARE_SERVER = 2
RESULT_SOFTWARE_SQL_SERVER = 4
RESULT_SOFTWARE_DOMAIN_CTRL = 8
RESULT_SOFTWARE_DOMAIN_BAKCTRL = 16
RESULT_SOFTWARE_TIME_SOURCE = 32
RESULT_SOFTWARE_AFP = 64
RESULT_SOFTWARE_NOVELL = 128
RESULT_SOFTWARE_DOMAIN_MEMBER = 256
RESULT_SOFTWARE_LOCAL_LIST_ONLY = 512
RESULT_SOFTWARE_PRINTQ_SERVER = 1024
RESULT_SOFTWARE_DIALIN_SERVER = 2048
RESULT_SOFTWARE_XENIX_SERVER = 4096
RESULT_SOFTWARE_SERVER_MFPN = 8192
RESULT_SOFTWARE_NT = 16384
RESULT_SOFTWARE_WFW = 32768
RESULT_SOFTWARE_SERVER_NT = 65536
RESULT_SOFTWARE_POTENTIAL_BROWSER = 131072
RESULT_SOFTWARE_BACKUP_BROWSER = 262144
RESULT_SOFTWARE_MASTER_BROWSER = 524288
RESULT_SOFTWARE_DOMAIN_MASTER = 1048576
RESULT_SOFTWARE_DOMAIN_ENUM = 2097152
RESULT_SOFTWARE_WINDOWS = 4194304
RESULT_SOFTWARE_TERMINALSERVER = 8388608
RESULT_SOFTWARE_CLUSTER_NT = 16777216
RESULT_SOFTWARE_CLUSTER_VS_NT = 33554432

class ResultError:

    def __init__(self):
        self.__dict__['pluginError'] = 0
        self.__dict__['osError'] = 0

    def __getattr__(self, name):
        if name == 'pluginError':
            return self.__dict__['pluginError']
        if name == 'osError':
            return self.__dict__['osError']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'pluginError':
            self.__dict__['pluginError'] = value
        elif name == 'osError':
            self.__dict__['osError'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_ERROR_MODULE, self.__dict__['pluginError'])
        submsg.AddU32(MSG_KEY_RESULT_ERROR_OS, self.__dict__['osError'])
        mmsg.AddMessage(MSG_KEY_RESULT_ERROR, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_ERROR, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['pluginError'] = submsg.FindU32(MSG_KEY_RESULT_ERROR_MODULE)
        self.__dict__['osError'] = submsg.FindU32(MSG_KEY_RESULT_ERROR_OS)


class ResultData:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['scope'] = 0
        self.__dict__['type'] = 0
        self.__dict__['displayType'] = 0
        self.__dict__['usage'] = 0
        self.__dict__['level'] = 0
        self.__dict__['remoteName'] = ''
        self.__dict__['comment'] = ''
        self.__dict__['provider'] = ''
        self.__dict__['localName'] = ''
        self.__dict__['parentName'] = ''
        self.__dict__['addrs'] = list()
        i = 0
        while i < RESULT_MAX_ADDRS:
            self.__dict__['addrs'].append('')
            i = i + 1

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'scope':
            return self.__dict__['scope']
        if name == 'type':
            return self.__dict__['type']
        if name == 'displayType':
            return self.__dict__['displayType']
        if name == 'usage':
            return self.__dict__['usage']
        if name == 'level':
            return self.__dict__['level']
        if name == 'remoteName':
            return self.__dict__['remoteName']
        if name == 'comment':
            return self.__dict__['comment']
        if name == 'provider':
            return self.__dict__['provider']
        if name == 'localName':
            return self.__dict__['localName']
        if name == 'parentName':
            return self.__dict__['parentName']
        if name == 'addrs':
            return self.__dict__['addrs']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'scope':
            self.__dict__['scope'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        elif name == 'displayType':
            self.__dict__['displayType'] = value
        elif name == 'usage':
            self.__dict__['usage'] = value
        elif name == 'level':
            self.__dict__['level'] = value
        elif name == 'remoteName':
            self.__dict__['remoteName'] = value
        elif name == 'comment':
            self.__dict__['comment'] = value
        elif name == 'provider':
            self.__dict__['provider'] = value
        elif name == 'localName':
            self.__dict__['localName'] = value
        elif name == 'parentName':
            self.__dict__['parentName'] = value
        elif name == 'addrs':
            self.__dict__['addrs'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU32(MSG_KEY_RESULT_DATA_FLAGS, self.__dict__['flags'])
        submsg.AddU32(MSG_KEY_RESULT_DATA_SCOPE, self.__dict__['scope'])
        submsg.AddU32(MSG_KEY_RESULT_DATA_TYPE, self.__dict__['type'])
        submsg.AddU32(MSG_KEY_RESULT_DATA_DISPLAY_TYPE, self.__dict__['displayType'])
        submsg.AddU32(MSG_KEY_RESULT_DATA_USAGE, self.__dict__['usage'])
        submsg.AddU16(MSG_KEY_RESULT_DATA_LEVEL, self.__dict__['level'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DATA_REMOTE_NAME, self.__dict__['remoteName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DATA_COMMENT, self.__dict__['comment'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DATA_PROVIDER, self.__dict__['provider'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DATA_LOCAL_NAME, self.__dict__['localName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DATA_PARENT_NAME, self.__dict__['parentName'])
        i = 0
        while i < RESULT_MAX_ADDRS:
            submsg.AddStringUtf8(MSG_KEY_RESULT_DATA_ADDRESSES, self.__dict__['addrs'][i])
            i = i + 1

        mmsg.AddMessage(MSG_KEY_RESULT_DATA, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_DATA, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_DATA_FLAGS)
        self.__dict__['scope'] = submsg.FindU32(MSG_KEY_RESULT_DATA_SCOPE)
        self.__dict__['type'] = submsg.FindU32(MSG_KEY_RESULT_DATA_TYPE)
        self.__dict__['displayType'] = submsg.FindU32(MSG_KEY_RESULT_DATA_DISPLAY_TYPE)
        self.__dict__['usage'] = submsg.FindU32(MSG_KEY_RESULT_DATA_USAGE)
        self.__dict__['level'] = submsg.FindU16(MSG_KEY_RESULT_DATA_LEVEL)
        self.__dict__['remoteName'] = submsg.FindString(MSG_KEY_RESULT_DATA_REMOTE_NAME)
        self.__dict__['comment'] = submsg.FindString(MSG_KEY_RESULT_DATA_COMMENT)
        self.__dict__['provider'] = submsg.FindString(MSG_KEY_RESULT_DATA_PROVIDER)
        self.__dict__['localName'] = submsg.FindString(MSG_KEY_RESULT_DATA_LOCAL_NAME)
        self.__dict__['parentName'] = submsg.FindString(MSG_KEY_RESULT_DATA_PARENT_NAME)
        i = 0
        while i < RESULT_MAX_ADDRS:
            self.__dict__['addrs'][i] = submsg.FindString(MSG_KEY_RESULT_DATA_ADDRESSES)
            i = i + 1


class ResultOsInfo:

    def __init__(self):
        self.__dict__['platformType'] = RESULT_PLATFORM_UNKNOWN
        self.__dict__['osMajor'] = 0
        self.__dict__['osMinor'] = 0
        self.__dict__['software'] = 0

    def __getattr__(self, name):
        if name == 'platformType':
            return self.__dict__['platformType']
        if name == 'osMajor':
            return self.__dict__['osMajor']
        if name == 'osMinor':
            return self.__dict__['osMinor']
        if name == 'software':
            return self.__dict__['software']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'platformType':
            self.__dict__['platformType'] = value
        elif name == 'osMajor':
            self.__dict__['osMajor'] = value
        elif name == 'osMinor':
            self.__dict__['osMinor'] = value
        elif name == 'software':
            self.__dict__['software'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_OSINFO_PLATFORM_TYPE, self.__dict__['platformType'])
        submsg.AddU32(MSG_KEY_RESULT_OSINFO_OS_MAJOR_VERSION, self.__dict__['osMajor'])
        submsg.AddU32(MSG_KEY_RESULT_OSINFO_OS_MINOR_VERSION, self.__dict__['osMinor'])
        submsg.AddU64(MSG_KEY_RESULT_OSINFO_SOFTWARE, self.__dict__['software'])
        mmsg.AddMessage(MSG_KEY_RESULT_OSINFO, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_OSINFO, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['platformType'] = submsg.FindU8(MSG_KEY_RESULT_OSINFO_PLATFORM_TYPE)
        self.__dict__['osMajor'] = submsg.FindU32(MSG_KEY_RESULT_OSINFO_OS_MAJOR_VERSION)
        self.__dict__['osMinor'] = submsg.FindU32(MSG_KEY_RESULT_OSINFO_OS_MINOR_VERSION)
        self.__dict__['software'] = submsg.FindU64(MSG_KEY_RESULT_OSINFO_SOFTWARE)


class ResultTime:

    def __init__(self):
        self.__dict__['timeOfDay'] = mcl.object.MclTime.MclTime()
        self.__dict__['tzOffset'] = mcl.object.MclTime.MclTime()

    def __getattr__(self, name):
        if name == 'timeOfDay':
            return self.__dict__['timeOfDay']
        if name == 'tzOffset':
            return self.__dict__['tzOffset']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'timeOfDay':
            self.__dict__['timeOfDay'] = value
        elif name == 'tzOffset':
            self.__dict__['tzOffset'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddTime(MSG_KEY_RESULT_TIME_TIMEOFDAY, self.__dict__['timeOfDay'])
        submsg.AddTime(MSG_KEY_RESULT_TIME_TIMEZONE_OFFSET, self.__dict__['tzOffset'])
        mmsg.AddMessage(MSG_KEY_RESULT_TIME, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_TIME, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['timeOfDay'] = submsg.FindTime(MSG_KEY_RESULT_TIME_TIMEOFDAY)
        self.__dict__['tzOffset'] = submsg.FindTime(MSG_KEY_RESULT_TIME_TIMEZONE_OFFSET)