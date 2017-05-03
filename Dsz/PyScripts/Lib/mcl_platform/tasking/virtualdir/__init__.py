# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
VIRTUAL_DIR_ENV_NAME = '_VIRTUAL_DIRECTORY'

def GetFullPath(relativePath):
    fullPath = _GetFullPathBase(relativePath)
    if len(fullPath) > 250:
        import os.path
        normPath = os.path.normpath(fullPath)
        if len(normPath) > 250:
            if len(fullPath) > 1 and fullPath[0] == '\\' and fullPath[1] == '\\':
                return '\\\\?\\UNC\\%s' % normPath[2:]
            else:
                return '\\\\?\\%s' % normPath

        else:
            return normPath
    else:
        if len(fullPath) == 0:
            return fullPath
        import os.path
        return os.path.normpath(fullPath)


def Set(dir):
    import dsz
    if len(dir) > 4 and dir[0] == '\\' and dir[1] == '\\' and dir[2] == '?' and dir[3] == '\\':
        dsz.env.Set(VIRTUAL_DIR_ENV_NAME, dir[4:])
    else:
        dsz.env.Set(VIRTUAL_DIR_ENV_NAME, dir)


def _GetFullPathBase(relativePath):
    try:
        if len(relativePath) > 0:
            if relativePath[0] == '/' or relativePath[0] == '\\':
                return relativePath
            if len(relativePath) > 1:
                if relativePath[0] >= 'A' and relativePath[0] <= 'Z' or relativePath[0] >= 'a' and relativePath[0] <= 'z':
                    if relativePath[1] == ':':
                        return relativePath
        import dsz
        if dsz.env.Check(VIRTUAL_DIR_ENV_NAME):
            virtualDir = dsz.env.Get(VIRTUAL_DIR_ENV_NAME)
            if len(relativePath) > 0:
                fullPath = '%s/%s' % (virtualDir, relativePath)
                if len(fullPath) > 1 and fullPath[0] == '\\' and fullPath[1] == '\\':
                    import os.path
                    ret = os.path.normpath(fullPath)
                    return ret
                else:
                    return fullPath

            else:
                return virtualDir
        else:
            return relativePath
    except Exception as ex:
        raise ex