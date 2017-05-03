# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.version.checks
import dsz.version.checks.windows
import dsz.version.checks.unix

def _getenvvalue(name, addr):
    if dsz.env.Check(name, 0, addr):
        return dsz.env.Get(name, 0, addr)
    else:
        return 'UNKNOWN'


def _getArch(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_ARCH', addr)


def _getCompiledArch(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_COMPILED_ARCH', addr)


def _getOs(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_OS', addr)


def _getCompiledOs(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_COMPILED_OS', addr)


def _getMajorVersion(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_MAJOR_VERSION', addr)


def _getMinorVersion(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_MINOR_VERSION', addr)


def _getOtherVersion(addr=dsz.script.Env['target_address']):
    return _getenvvalue('_OTHER_VERSION', addr)


class Info:

    def __init__(self, addr=dsz.script.Env['target_address']):
        self.addr = addr
        self.arch = _getArch(addr)
        self.compiledArch = _getCompiledArch(addr)
        self.os = _getOs(addr)
        self.compiledOs = _getCompiledOs(addr)
        self.majorStr = _getMajorVersion(addr)
        self.minorStr = _getMinorVersion(addr)
        self.otherStr = _getOtherVersion(addr)
        try:
            self.major = int(self.majorStr)
        except:
            self.major = 0

        try:
            self.minor = int(self.minorStr)
        except:
            self.minor = 0

        try:
            self.other = int(self.otherStr)
        except:
            self.other = 0