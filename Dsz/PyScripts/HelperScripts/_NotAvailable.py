# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _NotAvailable.py
import dsz
import sys

def main():
    try:
        cmdId = int(sys.argv[1])
        cmdName = dsz.cmd.data.Get('CommandMetaData::Name', dsz.TYPE_STRING, cmdId=cmdId, checkForStop=False)[0]
    except:
        cmdName = ''

    if len(sys.argv) > 2:
        reason = ' (%s)' % sys.argv[2]
    else:
        reason = ''
    dsz.ui.Echo("Command '%s' is not available on this platform%s" % (cmdName, reason), dsz.ERROR)
    return False


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)