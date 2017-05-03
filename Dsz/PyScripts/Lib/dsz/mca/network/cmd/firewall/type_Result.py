# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
RESULT_RULE_FLAG_IN = 1
RESULT_RULE_FLAG_OUT = 2
RESULT_RULE_FLAG_ALLOW = 4
RESULT_RULE_FLAG_ENABLED = 8
RESULT_RULE_FLAG_DOMAIN = 16
RESULT_RULE_FLAG_PUBLIC = 32
RESULT_RULE_FLAG_PRIVATE = 64
RESULT_PROFILE_TYPE_STANDARD = 1
RESULT_PROFILE_TYPE_DOMAIN = 2
RESULT_PROFILE_TYPE_PUBLIC = 3
RESULT_PROFILE_TYPE_PRIVATE = 4
RESULT_PROFILE_FLAG_ENABLED = 1
RESULT_PROFILE_FLAG_ALLOW_EXCEPTIONS = 2
RESULT_PROFILE_FLAG_ACTIVE = 4
RESULT_PROFILE_FLAG_INBOUND_BLOCK = 8
RESULT_PROFILE_FLAG_OUTBOUND_BLOCK = 16
RESULT_STATUS_FLAG_FIREWALL_ENABLED = 1
RESULT_STATUS_FLAG_NO_MODIFY = 2
RESULT_STATUS_FLAG_VISTA = 4

class ResultNoAction:

    def __init__(self):
        self.__dict__['cleanup'] = True

    def __getattr__(self, name):
        if name == 'cleanup':
            return self.__dict__['cleanup']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'cleanup':
            self.__dict__['cleanup'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_NOACTION_CLEANUP, self.__dict__['cleanup'])
        mmsg.AddMessage(MSG_KEY_RESULT_NOACTION, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_NOACTION, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['cleanup'] = submsg.FindBool(MSG_KEY_RESULT_NOACTION_CLEANUP)


class ResultEnable:

    def __init__(self):
        self.__dict__['cleanup'] = True
        self.__dict__['portNum'] = 0
        self.__dict__['protocol'] = FIREWALL_PROTOCOL_TCP

    def __getattr__(self, name):
        if name == 'cleanup':
            return self.__dict__['cleanup']
        if name == 'portNum':
            return self.__dict__['portNum']
        if name == 'protocol':
            return self.__dict__['protocol']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'cleanup':
            self.__dict__['cleanup'] = value
        elif name == 'portNum':
            self.__dict__['portNum'] = value
        elif name == 'protocol':
            self.__dict__['protocol'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_ENABLE_CLEANUP, self.__dict__['cleanup'])
        submsg.AddU16(MSG_KEY_RESULT_ENABLE_PORT, self.__dict__['portNum'])
        submsg.AddU8(MSG_KEY_RESULT_ENABLE_PROTOCOL, self.__dict__['protocol'])
        mmsg.AddMessage(MSG_KEY_RESULT_ENABLE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_ENABLE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['cleanup'] = submsg.FindBool(MSG_KEY_RESULT_ENABLE_CLEANUP)
        self.__dict__['portNum'] = submsg.FindU16(MSG_KEY_RESULT_ENABLE_PORT)
        self.__dict__['protocol'] = submsg.FindU8(MSG_KEY_RESULT_ENABLE_PROTOCOL)


class ResultDelete:

    def __init__(self):
        self.__dict__['cleanup'] = True
        self.__dict__['portNum'] = 0
        self.__dict__['protocol'] = FIREWALL_PROTOCOL_TCP
        self.__dict__['name'] = ''

    def __getattr__(self, name):
        if name == 'cleanup':
            return self.__dict__['cleanup']
        if name == 'portNum':
            return self.__dict__['portNum']
        if name == 'protocol':
            return self.__dict__['protocol']
        if name == 'name':
            return self.__dict__['name']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'cleanup':
            self.__dict__['cleanup'] = value
        elif name == 'portNum':
            self.__dict__['portNum'] = value
        elif name == 'protocol':
            self.__dict__['protocol'] = value
        elif name == 'name':
            self.__dict__['name'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddBool(MSG_KEY_RESULT_DELETE_CLEANUP, self.__dict__['cleanup'])
        submsg.AddU16(MSG_KEY_RESULT_DELETE_PORT, self.__dict__['portNum'])
        submsg.AddU8(MSG_KEY_RESULT_DELETE_PROTOCOL, self.__dict__['protocol'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_DELETE_NAME, self.__dict__['name'])
        mmsg.AddMessage(MSG_KEY_RESULT_DELETE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_DELETE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['cleanup'] = submsg.FindBool(MSG_KEY_RESULT_DELETE_CLEANUP)
        self.__dict__['portNum'] = submsg.FindU16(MSG_KEY_RESULT_DELETE_PORT)
        self.__dict__['protocol'] = submsg.FindU8(MSG_KEY_RESULT_DELETE_PROTOCOL)
        self.__dict__['name'] = submsg.FindString(MSG_KEY_RESULT_DELETE_NAME)


class ResultRule:

    def __init__(self):
        self.__dict__['protocol'] = 0
        self.__dict__['flags'] = 0
        self.__dict__['ruleName'] = ''
        self.__dict__['applicationName'] = ''
        self.__dict__['ports'] = ''
        self.__dict__['scope'] = ''
        self.__dict__['ruleString'] = ''
        self.__dict__['group'] = ''

    def __getattr__(self, name):
        if name == 'protocol':
            return self.__dict__['protocol']
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'ruleName':
            return self.__dict__['ruleName']
        if name == 'applicationName':
            return self.__dict__['applicationName']
        if name == 'ports':
            return self.__dict__['ports']
        if name == 'scope':
            return self.__dict__['scope']
        if name == 'ruleString':
            return self.__dict__['ruleString']
        if name == 'group':
            return self.__dict__['group']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'protocol':
            self.__dict__['protocol'] = value
        elif name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'ruleName':
            self.__dict__['ruleName'] = value
        elif name == 'applicationName':
            self.__dict__['applicationName'] = value
        elif name == 'ports':
            self.__dict__['ports'] = value
        elif name == 'scope':
            self.__dict__['scope'] = value
        elif name == 'ruleString':
            self.__dict__['ruleString'] = value
        elif name == 'group':
            self.__dict__['group'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_RESULT_RULE_PROTOCOL, self.__dict__['protocol'])
        submsg.AddU16(MSG_KEY_RESULT_RULE_FLAGS, self.__dict__['flags'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_RULE_RULE_NAME, self.__dict__['ruleName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_RULE_APPLICATION_NAME, self.__dict__['applicationName'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_RULE_PORTS, self.__dict__['ports'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_RULE_SCOPE, self.__dict__['scope'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_RULE_RULE_STRING, self.__dict__['ruleString'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_RULE_GROUP, self.__dict__['group'])
        mmsg.AddMessage(MSG_KEY_RESULT_RULE, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_RULE, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['protocol'] = submsg.FindU8(MSG_KEY_RESULT_RULE_PROTOCOL)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_RESULT_RULE_FLAGS)
        self.__dict__['ruleName'] = submsg.FindString(MSG_KEY_RESULT_RULE_RULE_NAME)
        self.__dict__['applicationName'] = submsg.FindString(MSG_KEY_RESULT_RULE_APPLICATION_NAME)
        self.__dict__['ports'] = submsg.FindString(MSG_KEY_RESULT_RULE_PORTS)
        self.__dict__['scope'] = submsg.FindString(MSG_KEY_RESULT_RULE_SCOPE)
        self.__dict__['ruleString'] = submsg.FindString(MSG_KEY_RESULT_RULE_RULE_STRING)
        self.__dict__['group'] = submsg.FindString(MSG_KEY_RESULT_RULE_GROUP)


class ResultProfileHeader:

    def __init__(self):
        self.__dict__['flags'] = 0
        self.__dict__['type'] = 0

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        if name == 'type':
            return self.__dict__['type']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        elif name == 'type':
            self.__dict__['type'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_RESULT_PROFILE_HEADER_FLAGS, self.__dict__['flags'])
        submsg.AddU8(MSG_KEY_RESULT_PROFILE_HEADER_TYPE, self.__dict__['type'])
        mmsg.AddMessage(MSG_KEY_RESULT_PROFILE_HEADER, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_PROFILE_HEADER, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_RESULT_PROFILE_HEADER_FLAGS)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_RESULT_PROFILE_HEADER_TYPE)


class ResultStatusHeader:

    def __init__(self):
        self.__dict__['flags'] = 0

    def __getattr__(self, name):
        if name == 'flags':
            return self.__dict__['flags']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'flags':
            self.__dict__['flags'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_RESULT_STATUS_HEADER_FLAGS, self.__dict__['flags'])
        mmsg.AddMessage(MSG_KEY_RESULT_STATUS_HEADER, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT_STATUS_HEADER, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['flags'] = submsg.FindU16(MSG_KEY_RESULT_STATUS_HEADER_FLAGS)