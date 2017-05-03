# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz

def Is9xFamily(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'win9x':
        return True
    else:
        return False


def IsNtFamily(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt':
        return True
    else:
        return False


def IsNt4(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and ver.major == 4:
        return True
    else:
        return False


def Is2000(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and ver.major == 5 and ver.minor == 0:
        return True
    else:
        return False


def Is2000OrGreater(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and ver.major >= 5:
        return True
    else:
        return False


def IsXp(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and ver.major == 5 and ver.minor == 1:
        return True
    else:
        return False


def IsXpOrGreater(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and (ver.major == 5 and ver.minor >= 1 or ver.major > 5):
        return True
    else:
        return False


def Is2003(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and ver.major == 5 and ver.minor == 2:
        return True
    else:
        return False


def Is2003OrGreater(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and (ver.major == 5 and ver.minor >= 2 or ver.major > 5):
        return True
    else:
        return False


def IsVista(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and ver.major == 6 and ver.minor == 0:
        return True
    else:
        return False


def IsVistaOrGreater(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and ver.major >= 6:
        return True
    else:
        return False


def Is2008(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and ver.major == 6 and ver.minor == 0 and ver.other >= 1:
        return True
    else:
        return False


def Is2008OrGreater(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt':
        if ver.major == 6 and ver.minor == 0 and ver.other >= 1:
            return True
        if ver.major == 6 and ver.minor > 0:
            return True
        if ver.major > 6:
            return True
    return False


def Is7(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and ver.major == 6 and ver.minor == 1:
        return True
    else:
        return False


def Is7OrGreater(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and (ver.major == 6 and ver.minor >= 1 or ver.major > 6):
        return True
    else:
        return False


def Is8(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and ver.major == 6 and ver.minor == 2:
        return True
    else:
        return False


def Is8OrGreater(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' and (ver.major == 6 and ver.minor >= 2 or ver.major > 6):
        return True
    else:
        return False


def IsHome(addr=dsz.script.Env['target_address']):
    try:
        return bool(dsz.env.Get('_VERSION_HOME'))
    except:
        pass

    if not dsz.cmd.Run('systemversion', dsz.RUN_FLAG_RECORD):
        return False
    try:
        home = dsz.cmd.data.Get('VersionInfo::Flags::Personal', dsz.TYPE_BOOL)
        try:
            dsz.env.Set('_VERSION_HOME', home)
        except:
            pass

        return home
    except:
        return False


def IsWow64(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    return ver.compiledArch != ver.arch