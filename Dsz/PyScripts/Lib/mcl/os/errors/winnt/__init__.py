# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py


def getErrorString(error):
    import winnt_system1_errors
    errorStr = winnt_system1_errors.getErrorString(error)
    if errorStr != None:
        return errorStr
    else:
        import winnt_system2_errors
        errorStr = winnt_system2_errors.getErrorString(error)
        if errorStr != None:
            return errorStr
        import winnt_wsa_errors
        errorStr = winnt_wsa_errors.getErrorString(error)
        if errorStr != None:
            return errorStr
        import winnt_net_errors
        errorStr = winnt_net_errors.getErrorString(error)
        if errorStr != None:
            return errorStr
        import winnt_wmi_errors
        errorStr = winnt_wmi_errors.getErrorString(error)
        if errorStr != None:
            return errorStr
        return