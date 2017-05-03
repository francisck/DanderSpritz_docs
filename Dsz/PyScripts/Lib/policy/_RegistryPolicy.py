# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _RegistryPolicy.py
import dsz
import dsz.lp
import dsz.script
import xml.dom.minidom
import sys
from _Shared import PolicyType
from _Shared import SecurityPolicyType
from _Shared import REGISTRY_VALUES, SYSTEM_ACCESS
KEY_INDEX = 0
VALUE_INDEX = 1
TAB = '\t'
SECURITY_XML_PATH = 'PyScripts/lib/policy/_GroupPolicy_security_settings.xml'

class AdminTemplates(PolicyType):
    COMPUTER_PATHS = [
     'software\\microsoft\\windows\\currentversion\\policies',
     'software\\policies\\microsoft',
     'system\\currentcontrolset\\policies']
    USER_PATHS = [
     'software\\microsoft\\windows\\currentversion\\policies',
     'software\\policies\\microsoft']

    def __init__(self, hive, path):
        self.hive = hive + '\\'
        if hive == 'hklm':
            self.otherHive = 'hkcu\\'
        else:
            self.otherHive = 'hklm\\'
        self.knownList = list()
        self.unknownList = list()
        self.ActualPaths = list()
        self.settingList = list()
        templateFile = '%s/%s/PyScripts/lib/policy/_GroupPolicy_admin_templates.xml' % (dsz.lp.GetResourcesDirectory(), path)
        xmldoc = xml.dom.minidom.parse(templateFile)
        settingElements = xmldoc.getElementsByTagName('Setting')
        for setting in settingElements:
            regKey = setting.getElementsByTagName('RegistryKey')[0].firstChild.data
            self.ActualPaths.append(regKey)
            self.settingList.append(setting)

    @classmethod
    def getQueryPaths(cls, hive):
        if hive == 'hklm':
            return cls.COMPUTER_PATHS
        else:
            if hive == 'hkcu':
                return cls.USER_PATHS
            return []

    def getActualPaths(self):
        return self.ActualPaths

    def process(self, Reader, ignoreList=[]):
        kvList = Reader.get(REGISTRY_VALUES)
        for pair in kvList:
            key = pair[KEY_INDEX]
            ignore = False
            for path in ignoreList:
                if key.__contains__(path):
                    ignore = True
                    break

            if ignore:
                continue
            wildcard = key.split('!')[0] + '!*'
            value = pair[VALUE_INDEX]
            specificPath = self.hive + key
            specificWildcard = self.hive + wildcard
            otherPath = self.otherHive + key
            otherWildcard = self.otherHive + wildcard
            if self.ActualPaths.__contains__(specificPath):
                self.knownList.append([specificPath, self.ActualPaths.index(specificPath), self.ActualPaths.count(specificPath), value])
            elif self.ActualPaths.__contains__(specificWildcard):
                self.knownList.append([specificPath, self.ActualPaths.index(specificWildcard), self.ActualPaths.count(specificWildcard), value])
            elif self.ActualPaths.__contains__(otherPath):
                self.knownList.append([specificPath, self.ActualPaths.index(otherPath), self.ActualPaths.count(otherPath), value])
            elif self.ActualPaths.__contains__(otherWildcard):
                self.knownList.append([specificPath, self.ActualPaths.index(otherWildcard), self.ActualPaths.count(otherWildcard), value])
            else:
                self.unknownList.append([specificPath, value])

    def store(self, TABCNT):
        dsz.script.data.Start('admintemplates')
        dsz.ui.Echo(TAB * TABCNT + 'Administrative Templates')
        dsz.ui.Echo(TAB * TABCNT + '----------------------------------------------------------------------------------------')
        self.storeKnown(TABCNT)
        self.storeUnknown(TABCNT)
        dsz.script.data.End()

    def storeKnown(self, TABCNT):
        TABCNT += 1
        for setting in self.knownList:
            key = setting[0]
            index = setting[1]
            count = setting[2]
            value = setting[3]
            for i in range(index, index + count):
                path = self.settingList[i].getElementsByTagName('Path')[0].firstChild.data
                name = self.settingList[i].getElementsByTagName('Name')[0].firstChild.data
                support = self.settingList[i].getElementsByTagName('SupportedOn')[0].firstChild.data
                storedkey = self.settingList[i].getElementsByTagName('RegistryKey')[0].firstChild.data
                if key != storedkey:
                    dsz.ui.Echo(TAB * TABCNT + 'Policy expected to be in different registry hive, may not apply', dsz.WARNING)
                dsz.script.data.Start('Setting')
                dsz.script.data.Add('Path', path, dsz.TYPE_STRING)
                dsz.script.data.Add('Name', name, dsz.TYPE_STRING)
                dsz.script.data.Add('SupportedOn', support, dsz.TYPE_STRING)
                dsz.script.data.Add('Key', key, dsz.TYPE_STRING)
                dsz.script.data.Add('Value', value, dsz.TYPE_STRING)
                dsz.script.data.End()
                applied = checkSupport(support)
                if applied == 'True':
                    dsz.ui.Echo(TAB * TABCNT + 'Policy:   ' + path + '/' + name)
                    dsz.ui.Echo(TAB * TABCNT + 'Key:      ' + key)
                    dsz.ui.Echo(TAB * TABCNT + 'Value:    ' + value)
                    dsz.ui.Echo('')
                else:
                    dsz.ui.Echo(TAB * TABCNT + 'Policy:   ' + path + '/' + name, dsz.WARNING)
                    dsz.ui.Echo(TAB * TABCNT + 'Key:      ' + key, dsz.WARNING)
                    dsz.ui.Echo(TAB * TABCNT + 'Value:    ' + value, dsz.WARNING)
                    dsz.ui.Echo(TAB * TABCNT + 'Supported On: ' + support, dsz.WARNING)
                    dsz.ui.Echo('')

    def storeUnknown(self, TABCNT):
        TABCNT += 1
        dsz.script.data.Start('Unknown')
        dsz.ui.Echo(TAB * TABCNT + 'Unknown Settings')
        dsz.ui.Echo(TAB * TABCNT + '----------------------------------------------------------------------------------------')
        TABCNT += 1
        for pair in self.unknownList:
            key = pair[0]
            value = pair[1]
            dsz.script.data.Start('Key')
            dsz.script.data.Add('Key', key, dsz.TYPE_STRING)
            dsz.script.data.Add('Value', value, dsz.TYPE_STRING)
            dsz.script.data.End()
            dsz.ui.Echo(TAB * TABCNT + 'Key:   ' + key)
            dsz.ui.Echo(TAB * TABCNT + 'Value: ' + value + '\n')

        dsz.script.data.End()


class SecurityOptions(PolicyType, SecurityPolicyType):
    RecursiveQueries = [
     'software\\policies\\microsoft',
     '"software\\microsoft\\windows nt\\currentversion"',
     'software\\microsoft\\windows\\currentversion\\policies',
     'system\\currentcontrolset\\control',
     'system\\currentcontrolset\\services',
     'security']
    RegularQueries = [
     'software\\microsoft\\driver signing']

    def __init__(self, hive):
        self.hive = hive + '\\'
        self.known = list()

    @classmethod
    def getQueryPaths(cls, hive):
        return cls.QueryPaths

    @classmethod
    def getActualPaths(cls, path):
        ActualPaths = list()
        xmldoc = xml.dom.minidom.parse('%s/%s/%s' % (dsz.lp.GetResourcesDirectory(), path, SECURITY_XML_PATH))
        settingElements = xmldoc.getElementsByTagName('Setting')
        for setting in settingElements:
            regKey = setting.getElementsByTagName('RegistryKey')[0].firstChild.data
            if regKey[:5] == 'hklm\\':
                ActualPaths.append(regKey[5:])

        return ActualPaths

    def process(self, Reader, settingDict):
        kvList = Reader.get(SYSTEM_ACCESS) + Reader.get(REGISTRY_VALUES)
        if Reader.grabLocal:
            kvList = self.getLocal(Reader, kvList, settingDict)
        for pair in kvList:
            key, value = pair
            if key == 'forcelogoffwhenhourexpire' or key == 'lsaanonymousnamelookup' or key == 'enableguestaccount' or key == 'enableadminaccount' or key == 'enableguestaccount' or key == 'enableadminaccount':
                valueString = 'Disabled' if value == '0' else 'Enabled'
                self.known.append(settingDict[key] + [value, valueString])
                continue
            if key == 'newguestname' or key == 'newadministratorname':
                self.known.append(settingDict[key] + [value, ''])
                continue
            key = self.hive + key
            if settingDict.has_key(key):
                valueString = ''
                if key == 'hklm\\system\\currentcontrolset\\control\\lsa!limitblankpassworduse' or key == 'hklm\\system\\currentcontrolset\\control\\lsa!auditbaseobjects' or key == 'hklm\\system\\currentcontrolset\\control\\lsa!fullprivilegeauditing' or key == 'hklm\\system\\currentcontrolset\\control\\lsa!scenoapplylegacyauditpolicy' or key == 'hklm\\system\\currentcontrolset\\control\\lsa!crashonauditfail' or key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!undockwithoutlogon' or key == 'hklm\\system\\currentcontrolset\\control\\print\\providers\\lanman print services\\servers!addprinterdrivers' or key == 'hklm\\software\\microsoft\\windows nt\\currentversion\\winlogon!allocatecdroms' or key == 'hklm\\software\\microsoft\\windows nt\\currentversion\\winlogon!allocatefloppies' or key == 'hklm\\system\\currentcontrolset\\control\\lsa!submitcontrol' or key == 'hklm\\system\\currentcontrolset\\services\\netlogon\\parameters!refusepasswordchange' or key == 'hklm\\system\\currentcontrolset\\services\\netlogon\\parameters!requiresignorseal' or key == 'hklm\\system\\currentcontrolset\\services\\netlogon\\parameters!sealsecurechannel' or key == 'hklm\\system\\currentcontrolset\\services\\netlogon\\parameters!signsecurechannel' or key == 'hklm\\system\\currentcontrolset\\services\\netlogon\\parameters!disablepasswordchange' or key == 'hklm\\system\\currentcontrolset\\services\\netlogon\\parameters!requirestrongkey' or key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!dontdisplaylastusername' or key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!disablecad' or key == 'hklm\\software\\microsoft\\windows nt\\currentversion\\winlogon!forceunlocklogon' or key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!scforceoption' or key == 'hklm\\system\\currentcontrolset\\services\\lanmanworkstation\\parameters!requiresecuritysignature' or key == 'hklm\\system\\currentcontrolset\\services\\lanmanworkstation\\parameters!enablesecuritysignature' or key == 'hklm\\system\\currentcontrolset\\services\\lanmanworkstation\\parameters!enableplaintextpassword' or key == 'hklm\\system\\currentcontrolset\\services\\lanmanserver\\parameters!requiresecuritysignature' or key == 'hklm\\system\\currentcontrolset\\services\\lanmanserver\\parameters!enablesecuritysignature' or key == 'hklm\\system\\currentcontrolset\\services\\lanmanserver\\parameters!enableforcedlogoff' or key == 'hklm\\system\\currentcontrolset\\control\\lsa!restrictanonymoussam' or key == 'hklm\\system\\currentcontrolset\\control\\lsa!restrictanonymous' or key == 'hklm\\system\\currentcontrolset\\control\\lsa!disabledomaincreds' or key == 'hklm\\system\\currentcontrolset\\control\\lsa!everyoneincludesanonymous' or key == 'hklm\\system\\currentcontrolset\\control\\lsa!nolmhash' or key == 'hklm\\software\\microsoft\\windows nt\\currentversion\\setup\\recoveryconsole!securitylevel' or key == 'hklm\\software\\microsoft\\windows nt\\currentversion\\setup\\recoveryconsole!setcommand' or key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!shutdownwithoutlogon' or key == 'hklm\\system\\currentcontrolset\\control\\session manager\\memory management!clearpagefileatshutdown' or key == 'hklm\\system\\currentcontrolset\\control\\lsa\\fipsalgorithmpolicy!enabled' or key == 'hklm\\system\\currentcontrolset\\control\\session manager\\kernel!obcaseinsensitive' or key == 'hklm\\system\\currentcontrolset\\control\\session manager!protectionmode' or key == 'hklm\\software\\policies\\microsoft\\windows\\safer\\codeidentifiers!authenticodeenabled' or key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!filteradministratortoken' or key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!enableuiadesktoptoggle' or key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!enableinstallerdetection' or key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!validateadmincodesignatures' or key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!enablesecureuiapaths' or key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!enablelua' or key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!promptonsecuredesktop' or key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!enablevirtualization' or key == 'hklm\\system\\currentcontrolset\\control\\lsa!usehklmid' or key == 'hklm\\system\\currentcontrolset\\control\\lsa\\msv1_0!allownullsessionfallback' or key == 'hklm\\system\\currentcontrolset\\control\\lsa\\pku2u!allowonlineid' or key == 'hklm\\system\\currentcontrolset\\control\\lsa!fipsalgorithmpolicy':
                    valueString = 'Disabled' if value == '0' else 'Enabled'
                elif key == 'hklm\\system\\currentcontrolset\\services\\netlogon\\parameters!maximumpasswordage':
                    valueString = value + ' days'
                elif key == 'hklm\\software\\microsoft\\windows nt\\currentversion\\winlogon!cachedlogonscount':
                    valueString = value + ' logons'
                elif key == 'hklm\\software\\microsoft\\windows nt\\currentversion\\winlogon!passwordexpirywarning':
                    valueString = value + ' days'
                elif key == 'hklm\\system\\currentcontrolset\\services\\lanmanserver\\parameters!autodisconnect':
                    valueString = value + ' minutes'
                elif key == 'hklm\\software\\microsoft\\driver signing!policy':
                    if value == '0':
                        valueString = 'Silently succeed'
                    elif value == '1':
                        valueString = 'Warn but allow installation'
                    elif value == '2':
                        valueString = 'Do not allow installation'
                elif key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!dontdisplaylockeduserid':
                    if value == '1':
                        valueString = 'User display name,domain and user names'
                    elif value == '2':
                        valueString = 'User display name only'
                    elif value == '3':
                        valueString = 'Do not display user information'
                elif key == 'hklm\\system\\currentcontrolset\\services\\lanmanserver\\parameters!smbservernamehardeninglevel':
                    if value == '0':
                        valueString = 'Off'
                    elif value == '1':
                        valueString = 'Accept if provided by client'
                    elif value == '2':
                        valueString = 'Required from client'
                elif key == 'hklm\\system\\currentcontrolset\\services\\netlogon\\parameters!restrictntlmindomain':
                    if value == '0':
                        valueString = 'Disable'
                    elif value == '1':
                        valueString = 'Deny for domain accounts to domain servers'
                    elif value == '3':
                        valueString = 'Deny for domain accounts'
                    elif value == '5':
                        valueString = 'Deny for domain servers'
                    elif value == '7':
                        valueString = 'Deny all'
                elif key == 'hklm\\system\\currentcontrolset\\control\\lsa\\msv1_0!auditreceivingntlmtraffic':
                    if value == '0':
                        valueString = 'Disable'
                    elif value == '1':
                        valueString = 'Enable auditing for domain accounts'
                    elif value == '2':
                        valueString = 'Enable auditing for all accounts'
                elif key == 'hklm\\system\\currentcontrolset\\services\\netlogon\\parameters!auditntlmindomain':
                    if value == '0':
                        valueString = 'Disable'
                    elif value == '1':
                        valueString = 'Enable for domain accounts to domain servers'
                    elif value == '3':
                        valueString = 'Enable for domain accounts'
                    elif value == '5':
                        valueString = 'Enable for domain servers'
                    elif value == '7':
                        valueString = 'Enable all'
                elif key == 'hklm\\system\\currentcontrolset\\control\\lsa\\msv1_0!restrictreceivingntlmtraffic':
                    if value == '0':
                        valueString = 'Disable'
                    elif value == '1':
                        valueString = 'Deny all domain accounts'
                    elif value == '2':
                        valueString = 'Deny all accounts'
                elif key == 'hklm\\system\\currentcontrolset\\control\\lsa\\msv1_0!restrictsendingntlmtraffic':
                    if value == '0':
                        valueString = 'Allow all'
                    elif value == '1':
                        valueString = 'Audit all'
                    elif value == '2':
                        valueString = 'Deny all'
                elif key == 'hklm\\system\\currentcontrolset\\control\\lsa!nodefaultadminowner':
                    if value == '1':
                        valueString = 'Object creator'
                    elif value == '0':
                        valueString = 'Administrator group'
                elif key == 'hklm\\software\\microsoft\\windows nt\\currentversion\\winlogon!allocatedasd':
                    if value == '0':
                        valueString = 'Administrators'
                    elif value == '1':
                        valueString = 'Administrators and Power Users'
                    elif value == '2':
                        valueString = 'Administrators and Interactive Users'
                elif key == 'hklm\\system\\currentcontrolset\\services\\ntds\\parameters!ldapserverintegrity':
                    if value == '1':
                        valueString = 'None'
                    elif value == '2':
                        valueString = 'Require Signing'
                elif key == 'hklm\\software\\microsoft\\windows nt\\currentversion\\winlogon!scremoveoption':
                    if value == '0':
                        valueString = 'No Action'
                    elif value == '1':
                        valueString = 'Lock Workstation'
                    elif value == '2':
                        valueString = 'Force Logoff'
                    elif value == '3':
                        valueString = 'Disconnect if a remote Terminal Services session'
                elif key == 'hklm\\system\\currentcontrolset\\control\\lsa!forceguest':
                    if value == '0':
                        valueString = 'Classic - local users authenticate as themselves'
                    elif value == '1':
                        valueString = 'Guest only - local users authenticate as Guest'
                elif key == 'hklm\\system\\currentcontrolset\\control\\lsa!lmcompatibilitylevel':
                    if value == '0':
                        valueString = 'Send LM and NTLM responses'
                    elif value == '1':
                        valueString = 'Send LM and NTLM - use NTLMv2 session security if negotiable'
                    elif value == '2':
                        valueString = 'Send NTLM response only'
                    elif value == '3':
                        valueString = 'Send NTLMv2 response only'
                    elif value == '4':
                        valueString = 'Send NTLMv2 response only. Refuse LM'
                    elif value == '5':
                        valueString = 'Send NTLMv2 response only. Refuse LM and NTLM'
                elif key == 'hklm\\system\\currentcontrolset\\services\\ldap!ldapclientintegrity':
                    if value == '0':
                        valueString = 'None'
                    elif value == '1':
                        valueString = 'Negotiate Signing'
                    elif value == '2':
                        valueString = 'Require Signing'
                elif key == 'hklm\\system\\currentcontrolset\\control\\lsa\\msv1_0!ntlmminclientsec':
                    if value == '0':
                        valueString = 'No Minimum'
                    elif value == '524288':
                        valueString = 'Require NTLMv2 session security'
                    elif value == '536870912':
                        valueString = 'Require 128-bit encryption'
                    elif value == '537395200':
                        valueString = 'Require NTLMv2 session security,Require 128-bit encryption'
                elif key == 'hklm\\system\\currentcontrolset\\control\\lsa\\msv1_0!ntlmminserversec':
                    if value == '0':
                        valueString = 'No Minimum'
                    elif value == '524288':
                        valueString = 'Require NTLMv2 session security'
                    elif value == '536870912':
                        valueString = 'Require 128-bit encryption'
                    elif value == '537395200':
                        valueString = 'Require NTLMv2 session security,Require 128-bit encryption'
                elif key == 'hklm\\software\\policies\\microsoft\\cryptography!forcekeyprotection':
                    if value == '0':
                        valueString = 'User input is not required when new keys are stored and used'
                    elif value == '1':
                        valueString = 'User is prompted when key is first used'
                    elif value == '2':
                        valueString = 'User must enter a password each time they use a key'
                elif key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!consentpromptbehavioradmin':
                    if value == '0':
                        valueString = 'Elevate without prompting'
                    elif value == '1':
                        valueString = 'Prompt for credentials'
                    elif value == '2':
                        valueString = 'Prompt for consent'
                elif key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system!consentpromptbehavioruser':
                    if value == '0':
                        valueString = 'Automatically deny elevation requests'
                    elif value == '1':
                        valueString = 'Prompt for credentials'
                elif key == 'hklm\\software\\microsoft\\windows\\currentversion\\policies\\system\\kerberos\\parameters!supportedencryptiontypes':
                    num = int(value)
                    valueString = value + ' '
                    if (num and 0) == 0:
                        valueString += 'No minimum'
                    if (num and 1) == 1:
                        valueString += 'DES_CBC_CRC, '
                    if (num and 2) == 2:
                        valueString += 'DES_CBC_MD5, '
                    if (num and 4) == 4:
                        valueString += 'RC4_HMAC_MD5, '
                    if (num and 8) == 8:
                        valueString += 'AES128_HMAC_SHA1, '
                    if (num and 16) == 16:
                        valueString += 'AES256_HMAC_SHA1, '
                    if (num and 2147483616) == 2147483616:
                        valueString += 'Future encryption types'
                elif Reader.getType(key[5:]) == 'reg_multi_sz':
                    for i, char1 in enumerate(value):
                        if i % 4 != 0:
                            continue
                        char2 = value[i + 1]
                        if char1 + char2 == '00':
                            valueString += ' '
                        else:
                            valueString += chr(int(char1 + char2, 16))

                self.known.append(settingDict[key] + [value, valueString])

    def getLocal(self, Reader, kvList, settingDict):
        kvDict = dict(kvList)
        recursive = Reader.registryQuery(SecurityOptions.RecursiveQueries, Reader.RECURSIVE)
        nonrecursive = Reader.registryQuery(SecurityOptions.RegularQueries, not Reader.RECURSIVE)
        localDict = dict(recursive.items() + nonrecursive.items())
        for setting in settingDict.iterkeys():
            setting = setting[5:]
            if not kvDict.has_key(setting) and localDict.has_key(setting):
                kvList.append([setting, localDict[setting]])

        if not kvDict.has_key('forcelogoffwhenhourexpire') and localDict.has_key('security\\sam\\domains\\account!f'):
            F = localDict['security\\sam\\domains\\account!f']
            temp = int(F[94:95]) >> 3
            if temp == 1:
                kvList.append(['forcelogoffwhenhourexpire', '0'])
            else:
                kvList.append(['forcelogoffwhenhourexpire', '1'])
        if not kvDict.has_key('lsaanonymousnamelookup') and localDict.has_key('security\\policy\\secdesc!'):
            secdesc = localDict['security\\policy\\secdesc!']
            temp = int(secdesc[57:58]) & 1
            if temp == 1:
                kvList.append(['lsaanonymousnamelookup', '0'])
            else:
                kvList.append(['lsaanonymousnamelookup', '1'])
        if not kvDict.has_key('newguestname'):
            namesList = [ key for key in localDict.keys() if key.__contains__('security\\sam\\domains\\account\\users\\names') ]
            for name in namesList:
                if Reader.getTypevalue(name) == 501:
                    name = name.split('!')[0]
                    name = name.split('\\')[-1]
                    kvList.append(['newguestname', name])
                    break

        if not kvDict.has_key('newadministratorname'):
            namesList = [ key for key in localDict.keys() if key.__contains__('security\\sam\\domains\\account\\users\\names') ]
            for name in namesList:
                if Reader.getTypevalue(name) == 500:
                    name = name.split('!')[0]
                    name = name.split('\\')[-1]
                    kvList.append(['newadministratorname', name])
                    break

        if not kvDict.has_key('enableguestaccount') and localDict.has_key('security\\sam\\domains\\account\\users\\000001f5!f'):
            key = localDict['security\\sam\\domains\\account\\users\\000001f5!f']
            disabled = int(key[113:114]) & 1
            if disabled == 1:
                kvList.append(['enableadminaccount', '0'])
            else:
                kvList.append(['enableadminaccount', '1'])
        if not kvDict.has_key('enableadminaccount') and localDict.has_key('security\\sam\\domains\\account\\users\\000001f4!f'):
            key = localDict['security\\sam\\domains\\account\\users\\000001f4!f']
            disabled = int(key[113:114]) & 1
            if disabled == 1:
                kvList.append(['enableadminaccount', '0'])
            else:
                kvList.append(['enableadminaccount', '1'])
        return kvList

    def store(self, TABCNT):
        dsz.script.data.Start('options')
        dsz.ui.Echo(TAB * TABCNT + 'Options')
        dsz.ui.Echo(TAB * TABCNT + '----------------------------------------------------------------------------------------')
        self.storeKnown(TABCNT)
        dsz.script.data.End()


class Ipsec(PolicyType):
    QueryPaths = [
     'software\\policies\\microsoft']
    PathList = [
     'software\\policies\\microsoft\\windows\\ipsec\\policy']

    def __init__(self, hive):
        self.hive = hive + '\\'
        self.ipsecDict = dict()

    @classmethod
    def getQueryPaths(cls, hive):
        return cls.QueryPaths

    @classmethod
    def getActualPaths(cls):
        return cls.PathList

    def process(self, Reader, ignoreList=[]):
        kvList = Reader.get(REGISTRY_VALUES)
        for pair in kvList:
            key = pair[KEY_INDEX]
            value = pair[VALUE_INDEX]
            for path in self.__class__.PathList:
                if key.__contains__(path):
                    path = key.split('!')[0]
                    if self.ipsecDict.has_key(path):
                        self.ipsecDict[path].append([key, value])
                    else:
                        self.ipsecDict[path] = [
                         [
                          key, value]]
                    break

    def store(self, TABCNT):
        dsz.script.data.Start('IPSec')
        dsz.ui.Echo(TAB * TABCNT + 'IPSec')
        dsz.ui.Echo(TAB * TABCNT + '----------------------------------------------------------------------------------------')
        for path, pairList in self.ipsecDict.iteritems():
            classname = ''
            name = ''
            descrip = ''
            dsz.script.data.Start('Policy')
            dsz.script.data.Add('path', path, dsz.TYPE_STRING)
            for item in pairList:
                key = item[0]
                value = item[1]
                dsz.script.data.Start('Setting')
                dsz.script.data.Add('Key', self.hive + key, dsz.TYPE_STRING)
                dsz.script.data.Add('Value', value, dsz.TYPE_STRING)
                dsz.script.data.End()
                if key[-9:] == 'classname':
                    classname = value
                elif key[-9:] == 'ipsecname':
                    name = value
                elif key[-11:] == 'description':
                    descrip = value

            dsz.script.data.End()
            TABCNT += 1
            dsz.ui.Echo(TAB * TABCNT + self.hive + path)
            TABCNT += 1
            dsz.ui.Echo(TAB * TABCNT + '      Class: ' + classname)
            dsz.ui.Echo(TAB * TABCNT + '       Name: ' + name)
            dsz.ui.Echo(TAB * TABCNT + 'Description: ' + descrip)
            dsz.ui.Echo('')
            TABCNT -= 2

        dsz.script.data.End()


class Srp(PolicyType):
    QueryPaths = [
     'software\\policies\\microsoft']
    PathList = [
     'software\\policies\\microsoft\\windows\\safer\\codeidentifiers',
     'software\\policies\\microsoft\\systemcertificates\\trustedpublisher\\safer!authenticodeflags']
    SAFER_UNRESTRICTED = '262144'
    SAFER_BASIC = '131072'
    SAFER_DISALLOWED = '0'

    def __init__(self, hive):
        self.srpList = list()
        self.hive = hive + '\\'

    @classmethod
    def getQueryPaths(cls, hive):
        return cls.QueryPaths

    @classmethod
    def getActualPaths(cls):
        return cls.PathList

    def process(self, Reader, ignoreList=[]):
        kvList = Reader.get(REGISTRY_VALUES)
        for pair in kvList:
            key = pair[KEY_INDEX]
            value = pair[VALUE_INDEX]
            for path in self.__class__.PathList:
                if key.__contains__(path):
                    self.srpList.append([key, value])
                    break

    def store(self, TABCNT):
        additionalRules = dict()
        dsz.script.data.Start('SRP')
        dsz.ui.Echo(TAB * TABCNT + 'Software Restriction Policies')
        dsz.ui.Echo(TAB * TABCNT + '----------------------------------------------------------------------------------------')
        for pair in self.srpList:
            key = pair[0]
            value = pair[1]
            if key.__contains__('software\\policies\\microsoft\\windows\\safer\\codeidentifiers!executabletypes'):
                self.designatedFileTypes(TABCNT, key, value)
            elif key.__contains__('software\\policies\\microsoft\\windows\\safer\\codeidentifiers!transparentenabled'):
                self.transparent(TABCNT, key, value)
            elif key.__contains__('software\\policies\\microsoft\\windows\\safer\\codeidentifiers!policyscope'):
                self.scope(TABCNT, key, value)
            elif key.__contains__('software\\policies\\microsoft\\windows\\safer\\codeidentifiers!authenticodeenabled'):
                self.authenticode(TABCNT, key, value)
            elif key.__contains__('software\\policies\\microsoft\\systemcertificates\\trustedpublisher\\safer!authenticodeflags'):
                self.authenticodeFlags(TABCNT, key, value)
            elif key.__contains__('software\\policies\\microsoft\\windows\\safer\\codeidentifiers!defaultlevel'):
                self.securityLevel(TABCNT, key, value)
            elif key.__contains__('software\\policies\\microsoft\\windows\\safer\\codeidentifiers\\' + self.__class__.SAFER_DISALLOWED) or key.__contains__('software\\policies\\microsoft\\windows\\safer\\codeidentifiers\\' + self.__class__.SAFER_BASIC) or key.__contains__('software\\policies\\microsoft\\windows\\safer\\codeidentifiers\\' + self.__class__.SAFER_UNRESTRICTED):
                rule = key.split('!')[0]
                if additionalRules.has_key(rule):
                    additionalRules[rule].append([key, value])
                else:
                    additionalRules[rule] = [
                     [
                      key, value]]
            else:
                dsz.script.data.Start('unknown')
                dsz.script.data.Add('key', self.hive + key, dsz.TYPE_STRING)
                dsz.script.data.Add('value', value, dsz.TYPE_STRING)
                dsz.script.data.End()
                dsz.ui.Echo(TAB * TABCNT + 'Unrecognized Software Restriction Policy', dsz.WARNING)
                dsz.ui.Echo(TAB * TABCNT + '  Key: ' + self.hive + key, dsz.WARNING)
                dsz.ui.Echo(TAB * TABCNT + 'Value: ' + value, dsz.WARNING)

        dsz.ui.Echo('')
        self.processAdditional(TABCNT, additionalRules)
        dsz.script.data.End()

    def designatedFileTypes(self, TABCNT, key, value):
        TABCNT += 1
        extensions = ''
        for i, char1 in enumerate(value):
            if i % 4 != 0:
                continue
            char2 = value[i + 1]
            if char1 + char2 == '00':
                extensions += ' '
            else:
                extensions += chr(int(char1 + char2, 16))

        extensions = extensions.strip(' ').split(' ')
        dsz.script.data.Start('Setting')
        dsz.script.data.Add('Name', 'Designated File Types', dsz.TYPE_STRING)
        dsz.script.data.Add('Key', key, dsz.TYPE_STRING)
        dsz.script.data.Add('Value', value, dsz.TYPE_STRING)
        for ext in extensions:
            dsz.script.data.Add('Extension', ext, dsz.TYPE_STRING)

        dsz.script.data.End()
        dsz.ui.Echo(TAB * TABCNT + 'Designated File Types: ' + ' '.join(extensions))

    def transparent(self, TABCNT, key, value):
        TABCNT += 1
        dsz.script.data.Start('Setting')
        dsz.script.data.Add('Name', 'Enforcement: Apply software restriction policies to:', dsz.TYPE_STRING)
        dsz.script.data.Add('Key', key, dsz.TYPE_STRING)
        dsz.script.data.Add('Value', value, dsz.TYPE_STRING)
        if value == '1':
            dsz.script.data.Add('explanation', 'All software files except libraries (such as DLLs)', dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'Enforcement: Apply software restriction policies to all software files except libraries (such as DLLs)')
        elif value == '2':
            dsz.script.data.Add('explanation', 'All software files', dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'Enforcement: Apply software restriction policies to all software files')
        dsz.script.data.End()

    def scope(self, TABCNT, key, value):
        TABCNT += 1
        dsz.script.data.Start('Setting')
        dsz.script.data.Add('Name', 'Enforcement: Apply software restriction policies to the following users:', dsz.TYPE_STRING)
        dsz.script.data.Add('Key', key, dsz.TYPE_STRING)
        dsz.script.data.Add('Value', value, dsz.TYPE_STRING)
        if value == '0':
            dsz.script.data.Add('explanation', 'All users', dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'Enforcement: Apply software restriction policies to all users')
        elif value == '1':
            dsz.script.data.Add('explanation', 'All users except local administrators', dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'Enforcement: Apply software restriction policies to all users except local adminstrators')
        dsz.script.data.End()

    def authenticode(self, TABCNT, key, value):
        TABCNT += 1
        dsz.script.data.Start('Setting')
        dsz.script.data.Add('Name', 'Enforcement: When applying software restriction policies:', dsz.TYPE_STRING)
        dsz.script.data.Add('Key', key, dsz.TYPE_STRING)
        dsz.script.data.Add('Value', value, dsz.TYPE_STRING)
        if value == '0':
            dsz.script.data.Add('explanation', 'Ignore certificate rules', dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'Enforcement: When applying software restriction policies ignore certificate rules')
        elif value == '1':
            dsz.script.data.Add('explanation', 'Enforce certificate rules', dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'Enforcement: When applying software restriction policies enforce certificate rules')
        dsz.script.data.End()

    def authenticodeFlags(self, TABCNT, key, value):
        TABCNT += 1
        dsz.script.data.Start('Setting')
        dsz.script.data.Add('Name', 'Trusted Publisher management:', dsz.TYPE_STRING)
        dsz.script.data.Add('Key', key, dsz.TYPE_STRING)
        dsz.script.data.Add('Value', value, dsz.TYPE_STRING)
        if int(value) & 3 == 0:
            dsz.script.data.Add('explanation', "Allow all administrators and users to manage user's own Trusted Publishers", dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + "Trusted Publisher management: Allow all administrators and users to manage user's own Trusted Publishers")
        elif int(value) & 3 == 1:
            dsz.script.data.Add('explanation', 'Allow only all administrators to manage Trusted Publishers', dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'Trusted Publisher management: Allow only all administrators to manage Trusted Publishers')
        elif int(value) & 3 == 2:
            dsz.script.data.Add('explanation', 'Allow only enterprise administrators to manage Trusted Publishers', dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'Trusted Publisher management: Allow only enterprise administrators to manage Trusted Publishers')
        dsz.script.data.End()
        if int(value) & 768:
            dsz.script.data.Start('Setting')
            dsz.script.data.Add('Name', 'Certificate verification:', dsz.TYPE_STRING)
            dsz.script.data.Add('Key', key, dsz.TYPE_STRING)
            dsz.script.data.Add('Value', value, dsz.TYPE_STRING)
            if int(value) & 256 == 256:
                dsz.script.data.Add('explanation', 'Verify that the certificate is not revoked when adding', dsz.TYPE_STRING)
                dsz.ui.Echo(TAB * TABCNT + 'Certificate verification: Verify that the certificate is not revoked when adding')
            if int(value) & 512 == 512:
                dsz.script.data.Add('explanation', 'Verify that certificate has a valid time stamp when adding', dsz.TYPE_STRING)
                dsz.ui.Echo(TAB * TABCNT + 'Certificate verification: Verify that certificate has a valid time stamp when adding')
            dsz.script.data.End()

    def securityLevel(self, TABCNT, key, value):
        TABCNT += 1
        dsz.script.data.Start('Setting')
        dsz.script.data.Add('Name', 'Software Restriction Policies\\Security Levels', dsz.TYPE_STRING)
        dsz.script.data.Add('Key', key, dsz.TYPE_STRING)
        dsz.script.data.Add('Value', value, dsz.TYPE_STRING)
        if value == self.__class__.SAFER_UNRESTRICTED:
            dsz.script.data.Add('explanation', 'Unrestricted: Software access rights are determined by the access rights of the user', dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'Unrestricted: Software access rights are determined by the access rights of the user')
        elif value == self.__class__.SAFER_BASIC:
            dsz.script.data.Add('explanation', 'Basic User: Allows programs to execute as a user that does not have Administrator access rights, but can still access resouces available by normal users', dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'Basic User: Allows programs to execute as a user that does not have Administrator access rights, but can still access resouces available by normal users')
        elif value == self.__class__.SAFER_DISALLOWED:
            dsz.script.data.Add('explanation', 'Disallowed: Software will not run, regardless of the access rights of the user', dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + 'Disallowed: Software will not run, regardless of the access rights of the user')
        dsz.script.data.End()

    def processAdditional(self, TABCNT, additionalRules):
        TABCNT += 1
        dsz.ui.Echo(TAB * TABCNT + 'Additional Rules')
        TABCNT += 1
        for path, keyValue in additionalRules.iteritems():
            level = path.split('\\')[6]
            if level == self.__class__.SAFER_UNRESTRICTED:
                levelString = 'Unrestricted'
            elif level == self.__class__.SAFER_BASIC:
                levelString = 'Basic User'
            elif level == self.__class__.SAFER_DISALLOWED:
                levelString = 'Disallowed'
            dsz.script.data.Start('Rule')
            dsz.script.data.Add('SecurityLevel', level, dsz.TYPE_STRING)
            dsz.script.data.Add('explanation', levelString, dsz.TYPE_STRING)
            dsz.script.data.Add('path', self.hive + path, dsz.TYPE_STRING)
            dsz.ui.Echo(TAB * TABCNT + self.hive + path)
            dsz.ui.Echo(TAB * TABCNT + 'Security Level: ' + levelString)
            for pair in keyValue:
                key = pair[0]
                value = pair[1]
                dsz.script.data.Start('Setting')
                dsz.script.data.Add('Key', self.hive + key, dsz.TYPE_STRING)
                dsz.script.data.Add('Value', value, dsz.TYPE_STRING)
                dsz.script.data.End()
                TABCNT += 1
                name = key.split('!')[1]
                dsz.ui.Echo(TAB * TABCNT + ' ' * (12 - len(name)) + name + ' = ' + value)
                TABCNT -= 1

            dsz.ui.Echo('')
            dsz.script.data.End()


SP = dsz.version.Info().other

def checkSupport(support):
    if support == 'Windows 2000 only':
        return str(dsz.version.checks.windows.Is2000())
    if support == 'At least Windows 2000':
        return str(dsz.version.checks.windows.Is2000OrGreater())
    if support == 'At least Windows 2000 Service Pack 1':
        return str(dsz.version.checks.windows.IsXpOrGreater() or dsz.version.checks.windows.Is2000() and SP >= 1)
    if support == 'At least Windows 2000 Service Pack 3':
        return str(dsz.version.checks.windows.IsXpOrGreater() or dsz.version.checks.windows.Is2000() and SP >= 3)
    if support == '"Windows Server 2003, Windows XP, and Windows 2000 operating systems only"':
        return str(dsz.version.checks.windows.Is2000() or dsz.version.checks.windows.IsXp() or dsz.version.checks.windows.Is2003())
    if support == '"Windows Server 2008, Windows Vista, Windows Server 2003, Windows XP, and Windows 2000"':
        return str(dsz.version.checks.windows.Is2008() or dsz.version.checks.windows.Is2003() or dsz.version.checks.windows.IsVista() or dsz.version.checks.windows.Is2000())
    if support == '"Microsoft Windows Server 2003, Windows XP, and Windows 2000 Service Pack 1 operating systems only"':
        return str(dsz.version.checks.windows.Is2003() or dsz.version.checks.windows.IsXp() or dsz.version.checks.windows.Is2000() and SP == 1)
    if support == 'At least Windows 2000 Service Pack 3 or Windows XP Professional Service Pack 1':
        return str(dsz.version.checks.windows.Is2003OrGreater() or dsz.version.checks.windows.IsXp() and SP >= 1 or dsz.version.checks.windows.Is2000() and SP >= 3)
    if support == '"At least Windows 2000 Service Pack 3, Windows XP Professional Service Pack 1 or Windows Server 2003 family"':
        return str(dsz.version.checks.windows.Is2003OrGreater() or dsz.version.checks.windows.IsXp() and SP >= 1 or dsz.version.checks.windows.Is2000() and SP >= 3)
    if support == '"At least Windows 2000 Service Pack 4, Windows XP Professional Service Pack 1 or Windows Server 2003 family"':
        return str(dsz.version.checks.windows.Is2003OrGreater() or dsz.version.checks.windows.IsXp() and SP >= 1 or dsz.version.checks.windows.Is2000() and SP >= 4)
    if support == '"At least Windows 2000 Service Pack 5, Windows XP Professional Service Pack 2 or Windows Server 2003 family Service Pack 1"':
        return str(dsz.version.checks.windows.IsVistaOrGreater() or dsz.version.checks.windows.Is2003() and SP >= 1 or dsz.version.checks.windows.IsXp() and SP >= 2 or dsz.version.checks.windows.is2000() and SP >= 5)
    if support == 'Windows XP Professional only':
        return str(dsz.version.checks.windows.IsXp())
    if support == 'At least Microsoft Windows XP and Windows Server 2003 only':
        return support
    if support == '"Windows XP SP2, Windows Server 2003"':
        return str(dsz.version.checks.windows.Is2003() or dsz.version.checks.windows.IsXp() and SP >= 2)
    if support == 'Windows Server 2003 and Windows XP only':
        return str(dsz.version.checks.windows.Is2003() or dsz.version.checks.windows.IsXp())
    if support == 'Windows Server 2003 and Windows XP operating systems only':
        return str(dsz.version.checks.windows.Is2003() or dsz.version.checks.windows.IsXp())
    if support == 'At least Windows XP Professional or Windows Server 2003 family':
        return str(dsz.version.checks.windows.IsXpOrGreater())
    if support == '"Windows Server 2008, Windows Vista, Windows Server 2003, and Windows XP"':
        return str(dsz.version.checks.windows.IsXp() or dsz.version.checks.windows.IsVista() or dsz.version.checks.windows.Is2008() or dsz.version.checks.windows.Is2003())
    if support == 'At least Windows XP Professional with SP1 or Windows Server 2003 family':
        return str(dsz.version.checks.windows.Is2003() or dsz.version.checks.windows.IsXp() and SP >= 1)
    if support == 'Supported Windows XP SP1 through Windows Server 2008 RTM':
        return str(dsz.version.checks.windows.IsXp() and SP >= 1 or dsz.version.checks.windows.Is2003() or dsz.version.checks.windows.IsVista() or dsz.version.checks.windows.Is2008())
    if support == '"Windows Server 2008, Windows Vista, Windows Server 2003, and Windows XP SP2"':
        return str(dsz.version.checks.windows.Is2008() or dsz.version.checks.windows.IsVista() or dsz.version.checks.windows.Is2003() or dsz.version.checks.windows.IsXp() and SP >= 2)
    if support == 'At least Windows XP Professional with SP2':
        return str(dsz.version.checks.windows.Is2003OrGreater() or dsz.version.checks.windows.IsXp() and SP >= 2)
    if support == 'Microsoft Windows XP Professional with SP2 and Windows Server 2003 family only':
        return str(dsz.version.checks.windows.Is2003() or dsz.version.checks.windows.IsXp() and SP >= 2)
    if support == 'At least Windows XP Professional with SP2 or Windows Server 2003 family':
        return str(dsz.version.checks.windows.Is2003OrGreater() or dsz.version.checks.windows.IsXp() and SP >= 2)
    if support == 'At least Windows XP Professional with SP2 or Windows Server 2003 family with SP1':
        return str(dsz.version.checks.windows.IsVistaOrGreater() or dsz.version.checks.windows.IsXp() and SP >= 2 or dsz.version.checks.windows.Is2003() and SP >= 1)
    if support == 'Windows Server 2003 only':
        return str(dsz.version.checks.windows.Is2003())
    if support == 'Windows Server 2003':
        return str(dsz.version.checks.windows.Is2003())
    if support == 'At least Windows Server 2003':
        return str(dsz.version.checks.windows.Is2003OrGreater())
    if support == 'Microsoft Windows Server 2003 with Service Pack 1 only':
        return str(dsz.version.checks.windows.Is2003() and SP == 1)
    if support == 'At least Microsoft Windows Server 2003 with SP1':
        return str(dsz.version.checks.windows.IsVistaOrGreater() or dsz.version.checks.windows.Is2003() and SP >= 1)
    if support == 'At least Microsoft Windows Server 2003 with Service Pack 2':
        return str(dsz.version.checks.windows.IsVistaOrGreater() or dsz.version.checks.windows.Is2003() and SP >= 2)
    if support == '"At least Microsoft Windows Server 2003, Enterprise Edition"':
        return str(dsz.version.checks.windows.Is2003OrGreater())
    if support == 'At least Microsoft Windows Server 2003 R2':
        return str(dsz.version.checks.windows.Is2003OrGreater())
    if support == 'Windows Vista only':
        return str(dsz.version.checks.windows.IsVista())
    if support == 'At least Windows Vista Service Pack 1':
        return str(dsz.version.checks.windows.Is2008OrGreater() or dsz.version.checks.windows.IsVista() and SP >= 1)
    if support == 'At least Microsoft Windows Vista with Service Pack 1':
        return str(dsz.version.checks.windows.Is2008OrGreater() or dsz.version.checks.windows.IsVista() and SP >= 1)
    if support == 'Windows Vista Service Pack 1':
        return str(dsz.version.checks.windows.IsVista() and SP == 1)
    if support == 'At least Windows Vista':
        return str(dsz.version.checks.windows.IsVistaOrGreater())
    if support == 'Windows Vista and Windows Server 2008':
        return str(dsz.version.checks.windows.IsVista() or dsz.version.checks.windows.Is2008())
    if support == 'Windows Server 2008 with Desktop Experience installed or Windows Vista':
        if dsz.version.checks.windows.IsVista():
            return str(dsz.version.checks.windows.IsVista())
        else:
            return support

    else:
        if support == 'At least Microsoft Windows Server 2008':
            return str(dsz.version.checks.windows.Is2008OrGreater())
        if support == 'At least Windows Server 2008 or Windows 7':
            return str(dsz.version.checks.windows.Is2008OrGreater())
        if support == 'At least Windows 7 or Windows Server 2008 R2':
            return str(dsz.version.checks.windows.Is7OrGreater())
        if support == 'Windows 7 family':
            return str(dsz.version.checks.windows.Is7())
        if support == 'Microsoft Windows 7 or later':
            return str(dsz.version.checks.windows.Is7OrGreater())
        return support