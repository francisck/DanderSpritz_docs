# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
OPEN_RES_FLAG_USE_ARCH = 1
OPEN_RES_FLAG_USE_OS = 2
OPEN_RES_FLAG_USE_COMPILED = 4
OPEN_RES_FLAG_USE_LIBC = 8

def GetDir(subdir=None):
    import mcl_platform.tasking.resource
    return mcl_platform.tasking.resource.GetDir(subdir)


def GetName(resName=None):
    import mcl_platform.tasking.resource
    return mcl_platform.tasking.resource.GetName(resName)


def Open(filename, flags, subdir=None, project=None):
    import mcl_platform.tasking.resource
    return mcl_platform.tasking.resource.Open(filename, flags, subdir, project)