# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _Shared.py
import dsz
import dsz.windows.sid
TAB = '\t'
SYSTEM_ACCESS = 'system access'
EVENT_AUDIT = 'event audit'
KERBEROS_POLICY = 'kerberos policy'
REGISTRY_VALUES = 'registry values'
PRIVILEGE_RIGHTS = 'privilege rights'
APPLICATION_LOG = 'application log'
SECURITY_LOG = 'security log'
SYSTEM_LOG = 'system log'
FILE_SECURITY = 'file security'
REGISTRY_KEYS = 'registry keys'
SERVICES = 'service general setting'
RESTRICTED = 'group membership'
sidDict = {'da': 'Domain admins','dg': 'Domain guests',
   'du': 'Domain users',
   'ed': 'Enterprise domain controllers',
   'dd': 'Domain domain controllers',
   'dc': 'Domain computers',
   'ba': 'Builtin (local ) administrators',
   'bg': 'Builtin (local ) guests',
   'bu': 'Builtin (local ) users',
   'la': 'Local administrator account',
   'lg': 'Local group account',
   'ao': 'Account operators',
   'bo': 'Backup operators',
   'po': 'Printer operators',
   'so': 'Server operators',
   'au': 'Authenticated users',
   'ps': 'Personal self',
   'co': 'Creator owner',
   'cg': 'Creator group',
   'sy': 'Local system',
   'pu': 'Power users',
   'wd': 'Everyone ( World )',
   're': 'Replicator',
   'iu': 'Interactive logon user',
   'nu': 'Nework logon user',
   'su': 'Service logon user',
   'rc': 'Restricted code',
   'wr': 'Write Restricted code',
   'an': 'Anonymous Logon',
   'sa': 'Schema Administrators',
   'ca': 'Certificate Server Administrators',
   'rs': 'RAS servers group',
   'ea': 'Enterprise administrators',
   'pa': 'Group Policy administrators',
   'ru': 'alias to allow previous windows 2000',
   'ls': 'Local service account (for services)',
   'ns': 'Network service account (for services)',
   'rd': 'Remote desktop users (for terminal server)',
   'no': 'Network configuration operators ( to manage configuration of networking features)',
   'mu': 'Performance Monitor Users',
   'lu': 'Performance Log Users',
   'is': 'Anonymous Internet Users',
   'cy': 'Crypto Operators',
   'ow': 'Owner Rights SID',
   'er': 'Event log readers',
   'ro': 'Enterprise Read-only domain controllers',
   'cd': 'Users who can connect to certification authorities using DCOM'
   }

class PolicyType():

    def __init__(self, hive):
        pass

    @classmethod
    def getQueryPaths(cls, hive):
        dsz.ui.Echo('Warning, getQueryPaths() not implemented', dsz.WARNING)

    def getActualPaths(self):
        dsz.ui.Echo('Warning, getActualPaths() not implemented', dsz.WARNING)

    def process(self, Reader, ignoreList=[]):
        dsz.ui.Echo('Error, process() not implemented', dsz.WARNING)

    def store(self, TABCNT):
        dsz.ui.Echo('Error, store() not implemented', dsz.WARNING)


class SecurityPolicyType():

    def storeKnown(self, TABCNT):
        TABCNT += 1
        for setting in self.known:
            path, name, key, value, valueString = setting
            dsz.script.data.Start('Setting')
            dsz.script.data.Add('path', path, dsz.TYPE_STRING)
            dsz.script.data.Add('name', name, dsz.TYPE_STRING)
            dsz.script.data.Add('key', key, dsz.TYPE_STRING)
            dsz.script.data.Add('value', value, dsz.TYPE_STRING)
            if len(valueString):
                dsz.script.data.Add('valuestring', valueString, dsz.TYPE_STRING)
            dsz.script.data.End()
            dsz.ui.Echo(TAB * TABCNT + ' Path: ' + path + '/' + name)
            dsz.ui.Echo(TAB * TABCNT + '  Key: ' + key)
            if len(valueString):
                dsz.ui.Echo(TAB * TABCNT + 'Value: ' + valueString)
            else:
                dsz.ui.Echo(TAB * TABCNT + 'Value: ' + value)
            dsz.ui.Echo('')

    def storeUnknown(self, TABCNT):
        if len(self.unknown):
            TABCNT += 1
            for setting in self.unknown:
                key, value = setting
                dsz.script.data.Start('Unknown')
                dsz.script.data.Add('key', key, dsz.TYPE_STRING)
                dsz.script.data.Add('value', value, dsz.TYPE_STRING)
                dsz.script.data.End()
                dsz.ui.Echo(TAB * TABCNT + '  Key: ' + key, dsz.WARNING)
                dsz.ui.Echo(TAB * TABCNT + 'Value: ' + value, dsz.WARNING)
                dsz.ui.Echo('')


class Permissions():

    def __init__(self, securityDesc):
        self.secdesc = securityDesc

    def parse(self, TABCNT):
        TABCNT += 1
        self.secdesc = self.secdesc.lower().strip('"')
        owner = ''
        group = ''
        dacl = ''
        sacl = ''
        unknown = ''
        while True:
            component, colon, tail = self.secdesc.partition(':')
            if colon == '':
                break
            value = ''
            if tail.find(':') == -1:
                value = tail
                self.secdesc = ''
            else:
                value = tail[:tail.find(':') - 1]
                self.secdesc = tail[tail.find(':') - 1:]
            if component == 'o':
                owner = getSidNames(value)
            elif component == 'g':
                group = getSidNames(value)
            elif component == 'd':
                dacl = value
            elif component == 's':
                sacl = value
            else:
                unknown += value

        dsz.script.data.Start('object')
        if owner != '':
            dsz.script.data.Add('owner', owner, dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'Owner: ' + owner)
        if group != '':
            dsz.script.data.Add('group', group, dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'Group: ' + group)
        if dacl != '':
            dsz.script.data.Start('acl')
            dsz.script.data.Add('type', 'DACL', dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + '--------------------------------------------')
            dsz.ui.Echo(TAB * TABCNT + 'DACL')
            self.parseAcl(TABCNT, 'DACL', dacl)
            dsz.ui.Echo('')
            dsz.script.data.End()
        if sacl != '':
            dsz.script.data.Start('acl')
            dsz.script.data.Add('type', 'SACL', dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + '--------------------------------------------')
            dsz.ui.Echo(TAB * TABCNT + 'SACL')
            self.parseAcl(TABCNT, 'SACL', sacl)
            dsz.ui.Echo('')
            dsz.script.data.End()
        dsz.script.data.End()

    def parseAcl(self, TABCNT, type, acl):
        TABCNT += 1
        acl = acl.split('(')
        self.parseAclFlags(TABCNT, type, acl[0])
        acl = acl[1:]
        for ace in acl:
            ace = ace.rstrip(')')
            ace = ace.split(';')
            ace_type = ace[0]
            ace_flags = ace[1]
            rights = ace[2]
            sid = getSidNames(ace[5])
            dsz.script.data.Start('ace')
            dsz.script.data.Add('user', sid, dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'User/Group: ' + sid)
            self.parseAceType(TABCNT, ace_type)
            self.parseAceFlags(TABCNT, ace_flags)
            self.parseAceRights(TABCNT, rights)
            dsz.script.data.End()

    def parseAclFlags(self, TABCNT, type, flags):
        flagDict = {'p': ['SE_DACL_PROTECTED', 'ACL protected from inheritance'],'ar': [
                'SE_DACL_AUTO_INHERIT_REQ', 'ACL must be inherited by child objects'],
           'ai': [
                'SE_DACL_AUTO_INHERITED', 'ACL was inherited from a parent object']
           }
        dsz.script.data.Start('controlflags')
        for k, v in flagDict.iteritems():
            v[0] = v[0][:3] + type + v[0][7:]
            if flags.find(k) == -1:
                dsz.script.data.Add(v[0], 'False', dsz.TYPE_BOOL)
            else:
                dsz.script.data.Add(v[0], 'True', dsz.TYPE_BOOL)
                dsz.ui.Echo(TAB * TABCNT + v[1])

        dsz.script.data.End()

    def parseAceType(self, TABCNT, ace_type):
        TABCNT += 1
        ACCESS_ALLOWED_ACE_TYPE = 0
        ACCESS_DENIED_ACE_TYPE = 1
        SYSTEM_AUDIT_ACE_TYPE = 2
        SYSTEM_ALARM_ACE_TYPE = 3
        ACCESS_ALLOWED_OBJECT_ACE_TYPE = 5
        ACCESS_DENIED_OBJECT_ACE_TYPE = 6
        SYSTEM_AUDIT_OBJECT_ACE_TYPE = 7
        SYSTEM_ALARM_OBJECT_ACE_TYPE = 8
        typeDict = {'a': ['ACCESS_ALLOWED_ACE_TYPE', ACCESS_ALLOWED_ACE_TYPE],'d': [
               'ACCESS_DENIED_ACE_TYPE', ACCESS_DENIED_ACE_TYPE],
           'oa': [
                'ACCESS_ALLOWED_OBJECT_ACE_TYPE', ACCESS_ALLOWED_OBJECT_ACE_TYPE],
           'od': [
                'ACCESS_DENIED_OBJECT_ACE_TYPE', ACCESS_DENIED_OBJECT_ACE_TYPE],
           'au': [
                'SYSTEM_AUDIT_ACE_TYPE', SYSTEM_AUDIT_ACE_TYPE],
           'al': [
                'SYSTEM_ALARM_ACE_TYPE', SYSTEM_ALARM_ACE_TYPE],
           'ou': [
                'SYSTEM_AUDIT_OBJECT_ACE_TYPE', SYSTEM_AUDIT_OBJECT_ACE_TYPE],
           'ol': [
                'SYSTEM_ALARM_OBJECT_ACE_TYPE', SYSTEM_ALARM_OBJECT_ACE_TYPE]
           }
        if typeDict.has_key(ace_type):
            type, typevalue = typeDict[ace_type]
            dsz.script.data.Add('type', type, dsz.TYPE_STRING)
            dsz.script.data.Add('typevalue', str(typevalue), dsz.TYPE_INT)
            dsz.ui.Echo(TAB * TABCNT + 'Type : ' + type)
        else:
            dsz.script.data.Add('type', ace_type, dsz.TYPE_STRING)
            dsz.ui.Echo('Unrecognized ACE_TYPE: ' + ace_type, dsz.WARNING)

    def parseAceFlags(self, TABCNT, ace_flags):
        TABCNT += 1
        fList = [ ace_flags[i] + ace_flags[i + 1] for i in range(0, len(ace_flags)) if i % 2 == 0 ]
        OBJECT_INHERIT_ACE = 1
        CONTAINER_INHERIT_ACE = 2
        NO_PROPAGATE_INHERIT_ACE = 4
        INHERIT_ONLY_ACE = 8
        INHERITED_ACE = 16
        VALID_INHERIT_FLAGS = 31
        SUCCESSFUL_ACCESS_ACE_FLAG = 64
        FAILED_ACCESS_ACE_FLAG = 128
        flagDict = {'ci': ['CONTAINER_INHERIT_ACE', CONTAINER_INHERIT_ACE],'oi': [
                'OBJECT_INHERIT_ACE', OBJECT_INHERIT_ACE],
           'np': [
                'NO_PROPAGATE_INHERIT_ACE', NO_PROPAGATE_INHERIT_ACE],
           'io': [
                'INHERIT_ONLY_ACE', INHERIT_ONLY_ACE],
           'id': [
                'INHERITED_ACE', INHERITED_ACE],
           'sa': [
                'SUCCESSFUL_ACCESS_ACE_FLAG', SUCCESSFUL_ACCESS_ACE_FLAG],
           'fa': [
                'FAILED_ACCESS_ACE_FLAG', FAILED_ACCESS_ACE_FLAG]
           }
        dsz.script.data.Start('flags')
        dsz.ui.Echo(TAB * TABCNT + 'Flags: ')
        TABCNT += 1
        for k, v in flagDict.iteritems():
            if fList.count(k):
                dsz.script.data.Add(v[0], 'True', dsz.TYPE_BOOL)
                dsz.ui.Echo(TAB * TABCNT + v[0])
            else:
                dsz.script.data.Add(v[0], 'False', dsz.TYPE_BOOL)

        dsz.script.data.End()

    def parseAceRights(self, TABCNT, rights):
        TABCNT += 1
        isNum = False
        rightNum = 0
        rightList = []
        if rights[:2] == '0x':
            isNum = True
            rightNum = int(rights, 16)
        else:
            isNum = False
            rightList = [ rights[i] + rights[i + 1] for i in range(0, len(rights)) if i % 2 == 0 ]
        GENERIC_ALL = 268435456L
        GENERIC_READ = 2147483648L
        GENERIC_WRITE = 1073741824L
        GENERIC_EXECUTE = 536870912L
        READ_CONTROL = 131072L
        DELETE = 65536L
        WRITE_DAC = 262144L
        WRITE_OWNER = 524288L
        STANDARD_RIGHTS_REQUIRED = 983040L
        STANDARD_RIGHTS_READ = READ_CONTROL
        STANDARD_RIGHTS_WRITE = READ_CONTROL
        STANDARD_RIGHTS_EXECUTE = READ_CONTROL
        STANDARD_RIGHTS_ALL = 2031616L
        SYNCHRONIZE = 1048576L
        FILE_READ_DATA = 1L
        FILE_WRITE_DATA = 2L
        FILE_APPEND_DATA = 4L
        FILE_READ_EA = 8L
        FILE_WRITE_EA = 16L
        FILE_EXECUTE = 32L
        FILE_READ_ATTRIBUTES = 128L
        FILE_WRITE_ATTRIBUTES = 256L
        KEY_QUERY_VALUE = 1L
        KEY_SET_VALUE = 2L
        KEY_CREATE_SUB_KEY = 4L
        KEY_ENUMERATE_SUB_KEYS = 8L
        KEY_NOTIFY = 16L
        KEY_CREATE_LINK = 32L
        ADS_RIGHT_DS_CREATE_CHILD = 1L
        ADS_RIGHT_DS_DELETE_CHILD = 2L
        ADS_RIGHT_ACTRL_DS_LIST = 4L
        ADS_RIGHT_DS_SELF = 8L
        ADS_RIGHT_DS_READ_PROP = 16L
        ADS_RIGHT_DS_WRITE_PROP = 32L
        ADS_RIGHT_DS_DELETE_TREE = 64L
        ADS_RIGHT_DS_LIST_OBJECT = 128L
        ADS_RIGHT_DS_CONTROL_ACCESS = 256L
        rightsDict = {'ga': ['GENERIC_ALL', GENERIC_ALL],'gr': [
                'GENERIC_READ', GENERIC_READ],
           'gw': [
                'GENERIC_WRITE', GENERIC_WRITE],
           'gx': [
                'GENERIC_EXECUTE', GENERIC_EXECUTE],
           'rc': [
                'READ_CONTROL', READ_CONTROL],
           'sd': [
                'DELETE', DELETE],
           'wd': [
                'WRITE_DAC', WRITE_DAC],
           'wo': [
                'WRITE_OWNER', WRITE_OWNER],
           'rp': [
                'ADS_RIGHT_DS_READ_PROP', ADS_RIGHT_DS_READ_PROP],
           'wp': [
                'ADS_RIGHT_DS_WRITE_PROP', ADS_RIGHT_DS_WRITE_PROP],
           'cc': [
                'ADS_RIGHT_DS_CREATE_CHILD', ADS_RIGHT_DS_CREATE_CHILD],
           'dc': [
                'ADS_RIGHT_DS_DELETE_CHILD', ADS_RIGHT_DS_DELETE_CHILD],
           'lc': [
                'ADS_RIGHT_ACTRL_DS_LIST', ADS_RIGHT_ACTRL_DS_LIST],
           'sw': [
                'ADS_RIGHT_DS_SELF', ADS_RIGHT_DS_SELF],
           'lo': [
                'ADS_RIGHT_DS_LIST_OBJECT', ADS_RIGHT_DS_LIST_OBJECT],
           'dt': [
                'ADS_RIGHT_DS_DELETE_TREE', ADS_RIGHT_DS_DELETE_TREE],
           'cr': [
                'ADS_RIGHT_DS_CONTROL_ACCESS', ADS_RIGHT_DS_CONTROL_ACCESS],
           'fa': [
                'FILE_ALL_ACCESS', STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 511],
           'fr': [
                'FILE_GENERIC_READ', STANDARD_RIGHTS_READ | FILE_READ_DATA | FILE_READ_ATTRIBUTES | FILE_READ_EA | SYNCHRONIZE],
           'fw': [
                'FILE_GENERIC_WRITE', STANDARD_RIGHTS_WRITE | FILE_WRITE_DATA | FILE_WRITE_ATTRIBUTES | FILE_WRITE_EA | FILE_APPEND_DATA | SYNCHRONIZE],
           'fx': [
                'FILE_GENERIC_EXECUTE', STANDARD_RIGHTS_EXECUTE | FILE_READ_ATTRIBUTES | FILE_EXECUTE | SYNCHRONIZE],
           'ka': [
                'KEY_ALL_ACCESS', (STANDARD_RIGHTS_ALL | KEY_QUERY_VALUE | KEY_SET_VALUE | KEY_CREATE_SUB_KEY | KEY_ENUMERATE_SUB_KEYS | KEY_NOTIFY) & ~SYNCHRONIZE],
           'kr': [
                'KEY_READ', (STANDARD_RIGHTS_READ | KEY_QUERY_VALUE | KEY_ENUMERATE_SUB_KEYS | KEY_NOTIFY) & ~SYNCHRONIZE],
           'kw': [
                'KEY_WRITE', (STANDARD_RIGHTS_WRITE | KEY_SET_VALUE | KEY_CREATE_SUB_KEY) & ~SYNCHRONIZE],
           'kx': [
                'KEY_EXECUTE', (STANDARD_RIGHTS_READ | KEY_QUERY_VALUE | KEY_ENUMERATE_SUB_KEYS | KEY_NOTIFY) & ~SYNCHRONIZE]
           }
        dsz.script.data.Start('rights')
        dsz.ui.Echo(TAB * TABCNT + 'Rights: ')
        TABCNT += 1
        if isNum:
            for k, v in rightsDict.iteritems():
                if v[1] == v[1] & rightNum:
                    dsz.script.data.Add(v[0], 'True', dsz.TYPE_BOOL)
                    dsz.ui.Echo(TAB * TABCNT + v[0])
                else:
                    dsz.script.data.Add(v[0], 'False', dsz.TYPE_BOOL)

        else:
            for k, v in rightsDict.iteritems():
                if rightList.count(k):
                    dsz.script.data.Add(v[0], 'True', dsz.TYPE_BOOL)
                    dsz.ui.Echo(TAB * TABCNT + v[0])
                else:
                    dsz.script.data.Add(v[0], 'False', dsz.TYPE_BOOL)

        dsz.script.data.End()


def getSidNames(sids):
    global sidDict
    if len(sids) == 0:
        return ''
    result = ''
    sidlist = sids.split(',')
    for sid in sidlist:
        if sidDict.has_key(sid):
            result += sidDict[sid] + ','
            continue
        if sid[0] == '*':
            sid = sid[1:]
        name = dsz.windows.sid.GetUserSid(sid)
        sidDict[sid] = name
        result += sidDict[sid] + ','

    if result:
        result = result[:-1]
    return result