# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
RESULT_WIN32_FLAG_DOMAIN_CONTROLLER = 1
RESULT_WIN32_FLAG_SERVER = 2
RESULT_WIN32_FLAG_WORKSTATION = 4
RESULT_WIN32_FLAG_BACKOFFICE = 8
RESULT_WIN32_FLAG_BLADE = 16
RESULT_WIN32_FLAG_CASE_DATACENTER = 32
RESULT_WIN32_FLAG_CASE_ENTERPRISE = 64
RESULT_WIN32_FLAG_EMBEDDEDNT = 128
RESULT_WIN32_FLAG_PERSONAL = 256
RESULT_WIN32_FLAG_SINGLEUSERTS = 512
RESULT_WIN32_FLAG_SMALLBUSINESS = 1024
RESULT_WIN32_FLAG_SMALLBUSINESS_RESTRICTED = 2048
RESULT_WIN32_FLAG_TERMINAL = 4096
RESULT_SOLARIS_FLAG_RUNNING_64BIT = 1
RESULT_SOLARIS_FLAG_CAPABLE_64BIT = 2
RESULT_SOLARIS_FLAG_ARCH_SUN4M = 4
RESULT_SOLARIS_FLAG_ARCH_SUN4D = 8
RESULT_SOLARIS_FLAG_ARCH_4U = 16
RESULT_SOLARIS_FLAG_ARCH_4C = 32
RESULT_SOLARIS_FLAG_ARCH_SUN4E = 64
RESULT_SOLARIS_FLAG_ARCH_SUN4V = 128
RESULT_SOLARIS_FLAG_ARCH_X86 = 256
RESULT_SOLARIS_FLAG_ARCH_IA64 = 512

class Result:

    def __init__(self):
        import mcl.os
        self.__dict__['arch'] = mcl.os.MCL_OS_ARCH_UNKNOWN
        self.__dict__['os'] = mcl.os.MCL_OS_UNKNOWN
        self.__dict__['majorVersion'] = 0
        self.__dict__['minorVersion'] = 0
        self.__dict__['revisionMajor'] = 0
        self.__dict__['revisionMinor'] = 0
        self.__dict__['build'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['extraInfo'] = ''

    def __getattr__(self, name):
        if name == 'arch':
            return self.__dict__['arch']
        if name == 'os':
            return self.__dict__['os']
        if name == 'majorVersion':
            return self.__dict__['majorVersion']
        if name == 'minorVersion':
            return self.__dict__['minorVersion']
        if name == 'revisionMajor':
            return self.__dict__['revisionMajor']
        if name == 'revisionMinor':
            return self.__dict__['revisionMinor']
        if name == 'build':
            return self.__dict__['build']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'extraInfo':
            return self.__dict__['extraInfo']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'arch':
            self.__dict__['arch'] = value
        elif name == 'os':
            self.__dict__['os'] = value
        elif name == 'majorVersion':
            self.__dict__['majorVersion'] = value
        elif name == 'minorVersion':
            self.__dict__['minorVersion'] = value
        elif name == 'revisionMajor':
            self.__dict__['revisionMajor'] = value
        elif name == 'revisionMinor':
            self.__dict__['revisionMinor'] = value
        elif name == 'build':
            self.__dict__['build'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'extraInfo':
            self.__dict__['extraInfo'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_RESULT_ARCH, self.__dict__['arch'])
        submsg.AddU16(MSG_KEY_RESULT_OS, self.__dict__['os'])
        submsg.AddU32(MSG_KEY_RESULT_VERSION_MAJOR, self.__dict__['majorVersion'])
        submsg.AddU32(MSG_KEY_RESULT_VERSION_MINOR, self.__dict__['minorVersion'])
        submsg.AddU32(MSG_KEY_RESULT_REVISION_MAJOR, self.__dict__['revisionMajor'])
        submsg.AddU32(MSG_KEY_RESULT_REVISION_MINOR, self.__dict__['revisionMinor'])
        submsg.AddU32(MSG_KEY_RESULT_BUILD, self.__dict__['build'])
        submsg.AddU32(MSG_KEY_RESULT_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_EXTRA_INFO, self.__dict__['extraInfo'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['arch'] = submsg.FindU16(MSG_KEY_RESULT_ARCH)
        self.__dict__['os'] = submsg.FindU16(MSG_KEY_RESULT_OS)
        self.__dict__['majorVersion'] = submsg.FindU32(MSG_KEY_RESULT_VERSION_MAJOR)
        self.__dict__['minorVersion'] = submsg.FindU32(MSG_KEY_RESULT_VERSION_MINOR)
        self.__dict__['revisionMajor'] = submsg.FindU32(MSG_KEY_RESULT_REVISION_MAJOR)
        self.__dict__['revisionMinor'] = submsg.FindU32(MSG_KEY_RESULT_REVISION_MINOR)
        self.__dict__['build'] = submsg.FindU32(MSG_KEY_RESULT_BUILD)
        self.__dict__['flags'] = submsg.FindU32(MSG_KEY_RESULT_FLAGS)
        self.__dict__['extraInfo'] = submsg.FindString(MSG_KEY_RESULT_EXTRA_INFO)