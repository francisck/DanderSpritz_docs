# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
USAGE_STATUS_NONE = 0
USAGE_STATUS_SUCCESSFUL = 1
USAGE_STATUS_UNSUCCESSFUL = 2
USAGE_FLAG_ACCESSED = 1
USAGE_FLAG_DEPLOYED = 2
USAGE_FLAG_EXERCISED = 4
USAGE_FLAG_CHECKED = 8
USAGE_FLAG_QUEUED = 16
USAGE_FLAG_DELETED = 32

def GetVersion(toolName):
    import mcl_platform.tools
    return mcl_platform.tools.GetVersion(toolName)


def RecordUsage(toolName, toolVersion, usageMask=0, status=USAGE_STATUS_NONE, comments=None, location=None):
    import mcl_platform.tools
    mcl_platform.tools.RecordUsage(toolName, toolVersion, usageMask, status, comments, location)