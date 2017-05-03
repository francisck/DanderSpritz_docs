# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py


def GetFullPath(relativePath):
    if relativePath == '*':
        return relativePath
    else:
        import mcl_platform.tasking.virtualdir
        return mcl_platform.tasking.virtualdir.GetFullPath(relativePath)


def GetMaskAndPath(bothPathAndMask, onlyMask, onlyPath, noDefaultMask=False, assumePath=False):
    outMask = ''
    outPath = ''
    if bothPathAndMask != None:
        if onlyMask != None or onlyPath != None:
            raise RuntimeError('Mask and path may not be specified separately when a combined mask/path is used')
        winList = bothPathAndMask.rsplit('\\', 1)
        if len(winList) == 2:
            winPath = winList[0]
            winMask = winList[1]
        else:
            winPath = ''
            winMask = winList[0]
        unixList = bothPathAndMask.rsplit('/', 1)
        if len(unixList) == 2:
            unixPath = unixList[0]
            unixMask = unixList[1]
        else:
            unixPath = ''
            unixMask = unixList[0]
        if len(winPath) > len(unixPath):
            usePath = winPath
            useMask = winMask
        else:
            usePath = unixPath
            useMask = unixMask
        if len(usePath) == 0:
            if len(bothPathAndMask) == 2 and bothPathAndMask[1] == ':':
                if not noDefaultMask:
                    outMask = '*'
                outPath = bothPathAndMask
            elif assumePath and bothPathAndMask.find('*') == -1 and bothPathAndMask.find('?') == -1:
                if not noDefaultMask:
                    outMask = '*'
                outPath = bothPathAndMask
            else:
                outMask = bothPathAndMask
                outPath = ''
        else:
            if assumePath and useMask.find('*') == -1 and useMask.find('?') == -1:
                usePath = usePath + '/' + useMask
                useMask = ''
            outMask = useMask
            outPath = usePath
    else:
        if onlyMask != None:
            outMask = onlyMask
        if onlyPath != None:
            outPath = onlyPath
    if len(outPath) > 0 and outPath != '*':
        if outPath[len(outPath) - 1] != '\\' and outPath[len(outPath) - 1] != '/':
            outPath = outPath + '/'
    if not noDefaultMask:
        if len(outMask) == 0:
            outMask = '*'
    return (outPath, outMask)


def Set(dir):
    import mcl_platform.tasking.virtualdir
    mcl_platform.tasking.virtualdir.Set(dir)