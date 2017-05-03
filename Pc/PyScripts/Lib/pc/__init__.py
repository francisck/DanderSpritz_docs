# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
# Compiled at: 2012-04-27 13:25:42


def IsValidIpAddress(addr):
    import re
    if re.match('^[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}$', addr) != None or re.match('^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$', addr) != None or re.match('^::$', addr) != None or re.match('^::([a-fA-F0-9]){1,4}(:([a-f]|[A-F]|[0-9]){1,4}){0,6}$', addr) != None or re.match('^([a-fA-F0-9]){1,4}::([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,5}$', addr) != None or re.match('^([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,1}::([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,4}$', addr) != None or re.match('^([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,2}::([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,3}$', addr) != None or re.match('^([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,3}::([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,2}$', addr) != None or re.match('^([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,4}::([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,1}$', addr) != None or re.match('^([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,4}::([a-fA-F0-9]){1,4}:([a-fA-F0-9]){1,4}$', addr) != None or re.match('^([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,5}::([a-fA-F0-9]){1,4}$', addr) != None or re.match('^([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,6}::$', addr) != None or re.match('^([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){5}:[0-9]{1,3}(\\.[0-9]{1,3}){3}$', addr) != None or re.match('^::([0-9]){1,3}(\\.[0-9]{1,3}){3}$', addr) != None or re.match('^::([a-fA-F0-9]){1,4}(:)([0-9]){1,3}(\\.[0-9]{1,3}){3}$', addr) != None or re.match('^([a-fA-F0-9]){1,4}::([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,3}:[0-9]{1,3}(\\.[0-9]{1,3}){3}$', addr) != None or re.match('^([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,1}::([a-fA-F0-9]){1,4}(:[a-fA-F0-9]){0,2}:[0-9]{1,3}(\\.[0-9]{1,3}){3}$', addr) != None or re.match('^([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,2}::([a-fA-F0-9]){1,4}(:[a-fA-F0-9]){0,1}:[0-9]{1,3}(\\.[0-9]{1,3}){3}$', addr) != None or re.match('^([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,3}::([a-fA-F0-9]){1,4}:[0-9]{1,3}(\\.[0-9]{1,3}){3}$', addr) != None or re.match('^([a-fA-F0-9]){1,4}(:([a-fA-F0-9]){1,4}){0,4}::[0-9]{1,3}(\\.[0-9]{1,3}){3}$', addr) != None:
        return True
    else:
        dsz.ui.Echo('Invalid IP address', dsz.ERROR)
        return False
        return