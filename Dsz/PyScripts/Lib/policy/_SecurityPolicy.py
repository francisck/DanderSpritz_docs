# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _SecurityPolicy.py
import dsz
import dsz.lp
import dsz.script
import dsz.file
import xml.dom.minidom
import re
import sys
from _Shared import Permissions
from _Shared import getSidNames
from _Shared import PolicyType
from _Shared import SecurityPolicyType
from _Shared import SYSTEM_ACCESS, EVENT_AUDIT, KERBEROS_POLICY, REGISTRY_VALUES, PRIVILEGE_RIGHTS, APPLICATION_LOG, SECURITY_LOG, SYSTEM_LOG, FILE_SECURITY, REGISTRY_KEYS, SERVICES, RESTRICTED
TAB = '\t'

class SystemAccess(PolicyType, SecurityPolicyType):
    QueryPath = [
     'security']

    def __init__(self, hive):
        self.known = list()
        self.unknown = list()

    def process(self, Reader, settingDict):
        kvList = Reader.get(SYSTEM_ACCESS)
        if Reader.grabLocal:
            kvList = self.getLocal(Reader, kvList)
        for pair in kvList:
            key, value = pair
            if settingDict.has_key(key):
                valueString = ''
                if key == 'lockoutduration':
                    valueString = value + ' minutes'
                elif key == 'lockoutbadcount':
                    valueString = value + ' invalid login attempts'
                elif key == 'resetlockoutcount':
                    valueString = value + ' minutes'
                elif key == 'passwordhistorysize':
                    valueString = value + ' passwords remembered'
                elif key == 'maximumpasswordage':
                    valueString = value + ' days'
                elif key == 'minimumpasswordage':
                    valueString = value + ' days'
                elif key == 'minimumpasswordlength':
                    valueString = value + ' characters'
                elif key == 'passwordcomplexity' or key == 'cleartextpassword' or key == 'enableadminaccount' or key == 'enableguestaccount' or key == 'lsaanonymousnamelookup' or key == 'forcelogoffwhenhourexpire':
                    valueString = 'Disabled' if value == '0' else 'Enabled'
                self.known.append(settingDict[key] + [value, valueString])
            else:
                self.unknown.append([key, value])

    def getLocal(self, Reader, kvList):
        localDict = Reader.registryQuery(SystemAccess.QueryPath, Reader.RECURSIVE)
        kvDict = dict(kvList)
        kvList += self.getLocalAcct(Reader, localDict, kvDict)
        return kvList

    def getLocalAcct(self, Reader, localDict, kvDict):
        addList = list()
        if localDict.has_key('security\\sam\\domains\\account!f'):
            F = localDict['security\\sam\\domains\\account!f']
            if not kvDict.has_key('passwordhistorysize'):
                addList.append(['passwordhistorysize', str(int(F[164:166], 16))])
            if not kvDict.has_key('minimumpasswordlength'):
                addList.append(['minimumpasswordlength', str(int(F[160:162], 16))])
            if not kvDict.has_key('passwordcomplexity'):
                addList.append(['passwordcomplexity', str(int(F[153:154], 2))])
            if not kvDict.has_key('cleartextpassword'):
                addList.append(['cleartextpassword', str(int(F[152:153], 2))])
            if not kvDict.has_key('lockoutbadcount'):
                addList.append(['lockoutbadcount', str(int(F[170:172] + F[168:170], 16))])
            if not kvDict.has_key('maximumpasswordage'):
                temp = F[48:64]
                temp = ''.join([ temp[len(temp) - 2 - i] + temp[len(temp) - 1 - i] for i in range(0, len(temp)) if i % 2 == 0 ])
                temp = (int('FFFFFFFFFFFFFFFF', 16) + 1 - int(temp, 16)) / 864000000000L
                if temp > 999:
                    temp = 0
                addList.append(['maximumpasswordage', str(temp)])
            if not kvDict.has_key('minimumpasswordage'):
                temp = F[64:80]
                temp = ''.join([ temp[len(temp) - 2 - i] + temp[len(temp) - 1 - i] for i in range(0, len(temp)) if i % 2 == 0 ])
                temp = (int('FFFFFFFFFFFFFFFF', 16) + 1 - int(temp, 16)) / 864000000000L
                if temp > 998:
                    temp = 0
                addList.append(['minimumpasswordage', str(temp)])
            if not kvDict.has_key('lockoutduration'):
                temp = F[96:112]
                temp = ''.join([ temp[len(temp) - 2 - i] + temp[len(temp) - 1 - i] for i in range(0, len(temp)) if i % 2 == 0 ])
                temp = (int('FFFFFFFFFFFFFFFF', 16) + 1 - int(temp, 16)) / 600000000
                if temp > 99999:
                    temp = 0
                addList.append(['lockoutduration', str(temp)])
            if not kvDict.has_key('resetlockoutcount'):
                temp = F[112:128]
                temp = ''.join([ temp[len(temp) - 2 - i] + temp[len(temp) - 1 - i] for i in range(0, len(temp)) if i % 2 == 0 ])
                temp = (int('FFFFFFFFFFFFFFFF', 16) + 1 - int(temp, 16)) / 600000000
                if temp > 99999:
                    temp = 0
                addList.append(['resetlockoutcount', str(temp)])
            if not kvDict.has_key('forcelogoffwhenhourexpire'):
                temp = int(F[94:95]) >> 3
                if temp == 1:
                    addList.append(['forcelogoffwhenhourexpire', '0'])
                else:
                    addList.append(['forcelogoffwhenhourexpire', '1'])
        if not kvDict.has_key('lsaanonymousnamelookup') and localDict.has_key('security\\policy\\secdesc!'):
            secdesc = localDict['security\\policy\\secdesc!']
            temp = int(secdesc[57:58]) & 1
            if temp == 1:
                addList.append(['lsaanonymousnamelookup', '0'])
            else:
                addList.append(['lsaanonymousnamelookup', '1'])
        if not kvDict.has_key('newguestname'):
            namesList = [ key for key in localDict.keys() if key.__contains__('security\\sam\\domains\\account\\users\\names') ]
            for name in namesList:
                if Reader.getTypevalue(name) == 501:
                    name = name.split('!')[0]
                    name = name.split('\\')[-1]
                    addList.append(['newguestname', name])
                    break

        if not kvDict.has_key('newadministratorname'):
            namesList = [ key for key in localDict.keys() if key.__contains__('security\\sam\\domains\\account\\users\\names') ]
            for name in namesList:
                if Reader.getTypevalue(name) == 500:
                    name = name.split('!')[0]
                    name = name.split('\\')[-1]
                    addList.append(['newadministratorname', name])
                    break

        if not kvDict.has_key('enableguestaccount') and localDict.has_key('security\\sam\\domains\\account\\users\\000001f5!f'):
            key = localDict['security\\sam\\domains\\account\\users\\000001f5!f']
            disabled = int(key[113:114]) & 1
            if disabled == 1:
                addList.append(['enableguestaccount', '0'])
            else:
                addList.append(['enableguestaccount', '1'])
        if not kvDict.has_key('enableadminaccount') and localDict.has_key('security\\sam\\domains\\account\\users\\000001f4!f'):
            key = localDict['security\\sam\\domains\\account\\users\\000001f4!f']
            disabled = int(key[113:114]) & 1
            if disabled == 1:
                addList.append(['enableadminaccount', '0'])
            else:
                addList.append(['enableadminaccount', '1'])
        return addList

    def store(self, TABCNT):
        self.storeKnown(TABCNT)
        self.storeUnknown(TABCNT)


class EventAudit(PolicyType, SecurityPolicyType):
    QueryPath = [
     'security']

    def __init__(self, hive):
        self.known = list()
        self.unknown = list()

    def process(self, Reader, settingDict):
        kvList = Reader.get(EVENT_AUDIT)
        if Reader.grabLocal:
            kvList = self.getLocal(Reader, kvList)
        for pair in kvList:
            key, value = pair
            if settingDict.has_key(key):
                valueString = ''
                if value == '0':
                    valueString = 'No auditing'
                elif value == '1':
                    valueString = 'Success'
                elif value == '2':
                    valueString = 'Failure'
                elif value == '3':
                    valueString = 'Success, Failure'
                self.known.append(settingDict[key] + [value, valueString])
            else:
                self.unknown.append([key, value])

    def getLocal(self, Reader, kvList):
        nonrecursive = Reader.registryQuery(EventAudit.QueryPath, Reader.RECURSIVE)
        if not nonrecursive.has_key('security\\policy\\poladtev!'):
            return kvList
        value = nonrecursive['security\\policy\\poladtev!']
        value = value[8:-8]
        value = value[1::8]
        if not len(value) == 9:
            dsz.ui.Echo('Error processing local audit policy', dsz.WARNING)
            return kvList
        auditList = [
         'auditsystemevents',
         'auditlogonevents',
         'auditobjectaccess',
         'auditprivilegeuse',
         'auditprocesstracking',
         'auditpolicychange',
         'auditaccountmanage',
         'auditdsaccess',
         'auditlogonevents']
        kvDict = dict(kvList)
        for index, audit in enumerate(auditList):
            if not kvDict.has_key(audit):
                kvList.append((audit, value[index]))

        return kvList

    def store(self, TABCNT):
        dsz.script.data.Start('Audit')
        dsz.ui.Echo(TAB * TABCNT + 'Audit Policy')
        dsz.ui.Echo(TAB * TABCNT + '----------------------------------------------------------------------------------------')
        self.storeKnown(TABCNT)
        self.storeUnknown(TABCNT)
        dsz.script.data.End()


class Kerberos(PolicyType, SecurityPolicyType):

    def __init__(self, hive):
        self.known = list()
        self.unknown = list()

    def process(self, Reader, settingDict):
        kvList = Reader.get(KERBEROS_POLICY)
        for pair in kvList:
            key, value = pair
            if settingDict.has_key(key):
                valueString = ''
                if key == 'ticketvalidateclient':
                    if value == '0':
                        valueString = 'Disabled'
                    elif value == '1':
                        valueString = 'Enabled'
                elif key == 'maxserviceage':
                    valueString = value + ' minutes'
                elif key == 'maxticketage':
                    valueString = value + ' hours'
                elif key == 'maxrenewage':
                    valueString = value + ' days'
                elif key == 'maxclockskew':
                    valueString = value + ' minutes'
                self.known.append(settingDict[key] + [value, valueString])
            else:
                self.unknown.append([key, value])

    def store(self, TABCNT):
        self.storeKnown(TABCNT)
        self.storeUnknown(TABCNT)


class EventLog(PolicyType, SecurityPolicyType):

    def __init__(self, hive):
        self.known = list()
        self.unknown = list()

    def process(self, Reader, settingDict):
        self.processHeader(Reader.get(APPLICATION_LOG), settingDict[APPLICATION_LOG])
        self.processHeader(Reader.get(SECURITY_LOG), settingDict[SECURITY_LOG])
        self.processHeader(Reader.get(SYSTEM_LOG), settingDict[SYSTEM_LOG])

    def processHeader(self, kvList, settingDict):
        for pair in kvList:
            key, value = pair
            if settingDict.has_key(key):
                valueString = ''
                if key == 'maximumlogsize':
                    valueString = value + ' kilobytes'
                elif key == 'restrictguestaccess':
                    if value == '0':
                        valueString = 'Disabled'
                    elif value == '1':
                        valueString = 'Enabled'
                elif key == 'retentiondays':
                    valueString = value + ' days'
                elif key == 'auditlogretentionperiod':
                    if value == '0':
                        valueString = 'Overwrite events as needed'
                    elif value == '1':
                        valueString = 'Overwrite events by days'
                    elif value == '2':
                        valueString = 'Do not overwrite events (clear log manually)'
                self.known.append(settingDict[key] + [value, valueString])
            else:
                self.unknown.append([key, value])

    def store(self, TABCNT):
        dsz.script.data.Start('EventLog')
        dsz.ui.Echo(TAB * TABCNT + 'Event Log ( Application, Security, System )')
        dsz.ui.Echo(TAB * TABCNT + '----------------------------------------------------------------------------------------')
        self.storeKnown(TABCNT)
        self.storeUnknown(TABCNT)
        dsz.script.data.End()


class Privileges(PolicyType, SecurityPolicyType):
    QueryPath = [
     'security']
    ACTSYSAC = 0
    PRIVILGS = 1

    def __init__(self, hive):
        self.known = list()
        self.unknown = list()

    def process(self, Reader, settingDict):
        kvList = Reader.get(PRIVILEGE_RIGHTS)
        if Reader.grabLocal:
            kvList = self.getLocal(Reader, kvList)
        for pair in kvList:
            key, value = pair
            sidNames = getSidNames(value)
            if settingDict.has_key(key):
                self.known.append(settingDict[key] + [value, sidNames])
            else:
                self.unknown.append([key, value])

    def getLocal(self, Reader, kvList):
        kvDict = dict(kvList)
        sidDict = self.queryRegistry(Reader)
        if sidDict is None:
            return kvList
        else:
            processList = [['senetworklogonright', '02000000'],
             [
              'seinteractivelogonright', '01000000'],
             [
              'seremoteinteractivelogonright', '00040000'],
             [
              'sedenynetworklogonright', '80000000'],
             [
              'sedenybatchlogonright', '00010000'],
             [
              'sedenyservicelogonright', '00020000'],
             [
              'sedenyinteractivelogonright', '40000000'],
             [
              'sedenyremoteinteractivelogonright', '00080000'],
             [
              'sebatchlogonright', '04000000'],
             [
              'seservicelogonright', '10000000']]
            for pair in processList:
                right, hexvalue = pair
                if not kvDict.has_key(right):
                    sids = self.searchActSysAc(sidDict, hexvalue)
                    if sids != '':
                        kvList.append([right, sids])

            privileges = self.getPrivilgs(sidDict)
            processList = [['setrustedcredmanaccessprivilege', '1f'],
             [
              'setcbprivilege', '07'],
             [
              'semachineaccountprivilege', '06'],
             [
              'seincreasequotaprivilege', '05'],
             [
              'sebackupprivilege', '11'],
             [
              'sechangenotifyprivilege', '17'],
             [
              'sesystemtimeprivilege', '0c'],
             [
              'setimezoneprivilege', '22'],
             [
              'secreatepagefileprivilege', '0f'],
             [
              'secreatetokenprivilege', '02'],
             [
              'secreateglobalprivilege', '1e'],
             [
              'secreatepermanentprivilege', '10'],
             [
              'secreatesymboliclinkprivilege', '23'],
             [
              'sedebugprivilege', '14'],
             [
              'seenabledelegationprivilege', '1b'],
             [
              'seremoteshutdownprivilege', '18'],
             [
              'seauditprivilege', '15'],
             [
              'seimpersonateprivilege', '1d'],
             [
              'seincreaseworkingsetprivilege', '21'],
             [
              'seincreasebasepriorityprivilege', '0e'],
             [
              'seloaddriverprivilege', '0a'],
             [
              'selockmemoryprivilege', '04'],
             [
              'sesecurityprivilege', '08'],
             [
              'serelabelprivilege', '20'],
             [
              'sesystemenvironmentprivilege', '16'],
             [
              'semanagevolumeprivilege', '1c'],
             [
              'seprofilesingleprocessprivilege', '0d'],
             [
              'sesystemprofileprivilege', '0b'],
             [
              'seundockprivilege', '19'],
             [
              'seassignprimarytokenprivilege', '03'],
             [
              'serestoreprivilege', '12'],
             [
              'seshutdownprivilege', '13'],
             [
              'sesyncagentprivilege', '1a'],
             [
              'setakeownershipprivilege', '09']]
            for pair in processList:
                right, byte = pair
                if privileges.has_key(byte):
                    if kvDict.has_key(right):
                        privileges.pop(byte)
                    else:
                        kvList.append([right, privileges.pop(byte)])

            for key, value in privileges.iteritems():
                self.unknown.append([key, value])

            return kvList

    def queryRegistry(self, Reader):
        sidDict = dict()
        kvDict = Reader.registryQuery(Privileges.QueryPath, Reader.RECURSIVE)
        for key, value in kvDict.iteritems():
            folder = key.split('\\')[-1]
            sid = key.split('\\')[-2]
            if folder == 'actsysac!':
                if sidDict.has_key(sid):
                    sidDict[sid][Privileges.ACTSYSAC] = value
                else:
                    sidDict[sid] = [
                     value, '0']
            elif folder == 'privilgs!':
                if sidDict.has_key(sid):
                    sidDict[sid][Privileges.PRIVILGS] = value
                else:
                    sidDict[sid] = [
                     '0', value]

        return sidDict

    def searchActSysAc(self, sidDict, mask):
        sidString = ''
        mask = int(mask, 16)
        for key, value in sidDict.iteritems():
            value = int(value[Privileges.ACTSYSAC], 16)
            if value & mask == mask:
                sidString += '*' + key + ','

        if sidString:
            sidString = sidString[:-1]
        return sidString

    def getPrivilgs(self, sidDict):
        priv = dict()
        for key, value in sidDict.iteritems():
            value = value[Privileges.PRIVILGS]
            cnt = value[:16]
            rights = value[16:]
            if cnt == '0':
                continue
            else:
                cnt = int(cnt.rstrip('0'), 16)
            for i in range(0, cnt):
                privNum = rights[i * 24:(i + 1) * 24][:2].lower()
                if priv.has_key(privNum):
                    priv[privNum] += '*' + key + ','
                else:
                    priv[privNum] = '*' + key + ','

        for key in priv.iterkeys():
            priv[key] = priv[key][:-1]

        return priv

    def store(self, TABCNT):
        dsz.script.data.Start('Privileges')
        dsz.ui.Echo(TAB * TABCNT + 'Privileges (User Right Assignments)')
        dsz.ui.Echo(TAB * TABCNT + '----------------------------------------------------------------------------------------')
        self.storeKnown(TABCNT)
        self.storeUnknown(TABCNT)
        dsz.script.data.End()


class SystemServices(PolicyType):

    def __init__(self, hive):
        self.serviceList = list()

    def process(self, Reader, ignoreList=[]):
        kvList = Reader.get(SERVICES)
        for pair in kvList:
            key = pair[0]
            service, startup, permissions = key.split(',')
            startupString = ''
            if startup == '2':
                startupString = 'Automatic'
            elif startup == '3':
                startupString = 'Manual'
            elif startup == '4':
                startupString = 'Disabled'
            self.serviceList.append([key, service, startup, startupString, permissions])

    def store(self, TABCNT):
        dsz.ui.Echo(TAB * TABCNT + 'System Service Permissions')
        dsz.ui.Echo(TAB * TABCNT + '----------------------------------------------------------------------------------------')
        for setting in self.serviceList:
            key, service, startup, startupString, permissions = setting
            dsz.script.data.Start('SystemServices')
            dsz.script.data.Add('Key', key, dsz.TYPE_STRING)
            dsz.script.data.Add('service', service, dsz.TYPE_STRING)
            dsz.script.data.Add('startup', startup, dsz.TYPE_STRING)
            dsz.script.data.Add('startupString', startupString, dsz.TYPE_STRING)
            dsz.script.data.Add('Permissions', permissions, dsz.TYPE_STRING)
            TABCNT += 1
            dsz.ui.Echo(TAB * TABCNT + '     Service: ' + service)
            dsz.ui.Echo(TAB * TABCNT + 'Startup Mode: ' + startupString)
            dsz.ui.Echo(TAB * TABCNT + ' Permissions: ' + permissions)
            per = Permissions(permissions)
            per.parse(TABCNT)
            TABCNT -= 1
            dsz.script.data.End()


class FileSecurity(PolicyType):

    def __init__(self, hive):
        self.fileList = list()

    def process(self, Reader, ignoreList=[]):
        kvList = Reader.get(FILE_SECURITY)
        for pair in kvList:
            key = pair[0]
            file, config, permissions = key.split(',')
            configString = ''
            if config == '0':
                configString = 'Configure this file or folder then: Propagate inheritable permissions to all subfolders and files'
            elif config == '1':
                configString = 'Do not all permissions on this file or folder to be replaced'
            elif config == '2':
                configString = 'Configure this file or folder then: Replace existing permissions on all subfolders and files with inheritable permissions'
            self.fileList.append([key, file, config, configString, permissions])

    def store(self, TABCNT):
        dsz.ui.Echo(TAB * TABCNT + 'File System Permissions')
        dsz.ui.Echo(TAB * TABCNT + '----------------------------------------------------------------------------------------')
        for setting in self.fileList:
            key, file, config, configString, permissions = setting
            dsz.script.data.Start('FileSecurity')
            dsz.script.data.Add('Key', key, dsz.TYPE_STRING)
            dsz.script.data.Add('file', file, dsz.TYPE_STRING)
            dsz.script.data.Add('config', config, dsz.TYPE_STRING)
            dsz.script.data.Add('configString', configString, dsz.TYPE_STRING)
            dsz.script.data.Add('Permissions', permissions, dsz.TYPE_STRING)
            TABCNT += 1
            dsz.ui.Echo(TAB * TABCNT + '         File: ' + file)
            dsz.ui.Echo(TAB * TABCNT + 'Configuration: ' + configString)
            dsz.ui.Echo(TAB * TABCNT + '  Permissions: ' + permissions)
            per = Permissions(permissions)
            per.parse(TABCNT)
            TABCNT -= 1
            dsz.script.data.End()


class RegistrySecurity(PolicyType):

    def __init__(self, hive):
        self.registryList = list()

    def process(self, Reader, ignoreList=[]):
        kvList = Reader.get(REGISTRY_KEYS)
        for pair in kvList:
            key = pair[0]
            registry, config, permissions = key.split(',')
            configString = ''
            if config == '0':
                configString = 'Configure this key then: Propagate inheritable permissions to all subkeys'
            elif config == '1':
                configString = 'Do not all permissions on this key to be replaced'
            elif config == '2':
                configString = 'Configure this key then: Replace existing permissions on all subkeys with inheritable permissions'
            self.registryList.append([key, registry, config, configString, permissions])

    def store(self, TABCNT):
        dsz.ui.Echo(TAB * TABCNT + 'Registry Permissions')
        dsz.ui.Echo(TAB * TABCNT + '----------------------------------------------------------------------------------------')
        for setting in self.registryList:
            key, registry, config, configString, permissions = setting
            dsz.script.data.Start('RegistrySecurity')
            dsz.script.data.Add('Key', key, dsz.TYPE_STRING)
            dsz.script.data.Add('RegistryKey', registry, dsz.TYPE_STRING)
            dsz.script.data.Add('config', config, dsz.TYPE_STRING)
            dsz.script.data.Add('configString', configString, dsz.TYPE_STRING)
            dsz.script.data.Add('Permissions', permissions, dsz.TYPE_STRING)
            TABCNT += 1
            dsz.ui.Echo(TAB * TABCNT + 'Registry Key: ' + registry)
            dsz.ui.Echo(TAB * TABCNT + '      Config: ' + configString)
            dsz.ui.Echo(TAB * TABCNT + ' Permissions: ' + permissions)
            per = Permissions(permissions)
            per.parse(TABCNT)
            TABCNT -= 1
            dsz.script.data.End()


class RestrictedGroups(PolicyType):

    def __init__(self, hive):
        self.groupDict = dict()

    def process(self, Reader, ignoreList=[]):
        kvList = Reader.get(RESTRICTED)
        for pair in kvList:
            key, value = pair
            group, type = key.split('__')
            if self.groupDict.has_key(group):
                self.groupDict[group].append((key, value, type))
            else:
                self.groupDict[group] = [
                 (
                  key, value, type)]

    def store(self, TABCNT):
        dsz.script.data.Start('RestrictedGroups')
        dsz.ui.Echo(TAB * TABCNT + 'RestrictedGroups')
        dsz.ui.Echo(TAB * TABCNT + '----------------------------------------------------------------------------------------')
        for group, setting in self.groupDict.iteritems():
            dsz.script.data.Start('setting')
            dsz.ui.Echo(TAB * TABCNT + '                    Group: ' + group)
            dsz.script.data.Add('group', group, dsz.TYPE_STRING)
            for member in setting:
                key, value, type = member
                dsz.script.data.Add('key', key, dsz.TYPE_STRING)
                dsz.script.data.Add('value', value, dsz.TYPE_STRING)
                if type.lower() == 'memberof':
                    dsz.ui.Echo(TAB * TABCNT + 'This group is a member of: ' + value)
                    dsz.script.data.Add('memberof', value, dsz.TYPE_STRING)
                elif type.lower() == 'members':
                    dsz.ui.Echo(TAB * TABCNT + '    Members of this group: ' + value)
                    dsz.script.data.Add('members', value, dsz.TYPE_STRING)

            dsz.script.data.End()

        dsz.ui.Echo('')
        dsz.script.data.End()