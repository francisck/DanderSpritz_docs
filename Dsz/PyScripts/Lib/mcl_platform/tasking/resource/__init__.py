# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py


def GetDir(subdir=None):
    import dsz
    import os.path
    resDir = dsz.env.Get('_LPDIR_RESOURCES')
    if subdir != None and len(subdir) > 0:
        resDir = resDir + '/%s' % subdir
    return os.path.normpath(resDir)


def GetName(resName):
    import dsz
    from xml.dom.minidom import parse
    if resName != None and len(resName) > 0:
        xmlPath = GetDir(resName)
    else:
        xmlPath = GetDir('Dsz')
    xmlPath = xmlPath + '/Names.xml'
    doc = parse(xmlPath)
    if dsz.script.IsLocal():
        nodeName = 'Local'
    else:
        nodeName = 'Remote'
    nodeList = doc.getElementsByTagName(nodeName)
    return _getNodeText(nodeList[0])


def Open(filename, flags, subdir=None, project=None):
    import dsz
    import mcl.tasking.resource
    import os.path
    if filename == None or len(filename) == 0:
        raise RuntimeError('Invalid filename specified')
    file = None
    if filename.find(':') == -1 and filename[0] != '/':
        resPath = GetDir()
        resDirs = ''
        if project != None:
            resDirs = project
        elif dsz.env.Check('_RES_DIRS'):
            resDirs = dsz.env.Get('_RES_DIRS')
        archStr = ''
        if flags & mcl.tasking.resource.OPEN_RES_FLAG_USE_ARCH:
            envName = ''
            if flags & mcl.tasking.resource.OPEN_RES_FLAG_USE_COMPILED:
                envName = envName + '_COMPILED'
            envName = envName + '_ARCH'
            archStr = dsz.env.Get(envName)
        osStr = ''
        if flags & mcl.tasking.resource.OPEN_RES_FLAG_USE_OS:
            envName = ''
            if flags & mcl.tasking.resource.OPEN_RES_FLAG_USE_COMPILED:
                envName = envName + '_COMPILED'
            envName = envName + '_OS'
            osStr = dsz.env.Get(envName)
        libcStr = ''
        if flags & mcl.tasking.resource.OPEN_RES_FLAG_USE_LIBC:
            if osStr.lower() == 'linux':
                majorVersion = dsz.env.Get('_CLIB_MAJOR_VERSION')
                minorVersion = dsz.env.Get('_CLIB_MINOR_VERSION')
                revVersion = dsz.env.Get('_CLIB_REVISION_VERSION')
                libcStr = 'glibc%u.%u.%u' % (majorVersion, minorVersion, revVersion)
        while len(resDirs) > 0:
            loc = resDirs.find(';')
            if loc == -1:
                dir = resDirs
                resDirs = ''
            else:
                dir = resDirs[0:loc]
                resDirs = resDirs[loc + 1:]
            fullPath = resPath + '/' + dir + '/'
            if subdir != None and len(subdir) > 0:
                fullPath = fullPath + subdir + '/'
            if len(archStr) > 0:
                fullPath = fullPath + archStr + '/'
            if len(osStr) > 0:
                fullPath = fullPath + osStr + '/'
            if len(libcStr) > 0:
                fullPath = fullPath + libcStr + '/'
            fullPath = os.path.normpath(fullPath + filename)
            try:
                _f = os.open(fullPath, os.O_RDONLY | os.O_BINARY)
                f = os.fdopen(_f, 'rb')
                try:
                    openedFile = os.path.abspath(fullPath)
                except:
                    openedFile = fullPath

                return (
                 f, openedFile, dir)
            except:
                pass

    try:
        _f = os.open(filename, os.O_RDONLY | os.O_BINARY)
        f = os.fdopen(_f, 'rb')
        try:
            openedFile = os.path.abspath(filename)
        except:
            openedFile = filename

        return (
         f, openedFile, None)
    except:
        pass

    return (None, None, None)


def _getNodeText(element):
    txt = ''
    for node in element.childNodes:
        if node.nodeType == node.TEXT_NODE:
            txt = txt + node.data

    return txt