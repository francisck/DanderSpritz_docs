# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: os2emxpath.py
"""Common pathname manipulations, OS/2 EMX version.

Instead of importing this module directly, import os and refer to this
module as os.path.
"""
import os
import stat
from genericpath import *
from ntpath import expanduser, expandvars, isabs, islink, splitdrive, splitext, split, walk
__all__ = [
 'normcase', 'isabs', 'join', 'splitdrive', 'split', 'splitext',
 'basename', 'dirname', 'commonprefix', 'getsize', 'getmtime',
 'getatime', 'getctime', 'islink', 'exists', 'lexists', 'isdir', 'isfile',
 'ismount', 'walk', 'expanduser', 'expandvars', 'normpath', 'abspath',
 'splitunc', 'curdir', 'pardir', 'sep', 'pathsep', 'defpath', 'altsep',
 'extsep', 'devnull', 'realpath', 'supports_unicode_filenames']
curdir = '.'
pardir = '..'
extsep = '.'
sep = '/'
altsep = '\\'
pathsep = ';'
defpath = '.;C:\\bin'
devnull = 'nul'

def normcase(s):
    """Normalize case of pathname.
    
    Makes all characters lowercase and all altseps into seps."""
    return s.replace('\\', '/').lower()


def join(a, *p):
    """Join two or more pathname components, inserting sep as needed"""
    path = a
    for b in p:
        if isabs(b):
            path = b
        elif path == '' or path[-1:] in '/\\:':
            path = path + b
        else:
            path = path + '/' + b

    return path


def splitunc(p):
    """Split a pathname into UNC mount point and relative path specifiers.
    
    Return a 2-tuple (unc, rest); either part may be empty.
    If unc is not empty, it has the form '//host/mount' (or similar
    using backslashes).  unc+rest is always the input path.
    Paths containing drive letters never have an UNC part.
    """
    if p[1:2] == ':':
        return ('', p)
    firstTwo = p[0:2]
    if firstTwo == '//' or firstTwo == '\\\\':
        normp = normcase(p)
        index = normp.find('/', 2)
        if index == -1:
            return (
             '', p)
        index = normp.find('/', index + 1)
        if index == -1:
            index = len(p)
        return (p[:index], p[index:])
    return ('', p)


def basename(p):
    """Returns the final component of a pathname"""
    return split(p)[1]


def dirname(p):
    """Returns the directory component of a pathname"""
    return split(p)[0]


lexists = exists

def ismount(path):
    """Test whether a path is a mount point (defined as root of drive)"""
    unc, rest = splitunc(path)
    if unc:
        return rest in ('', '/', '\\')
    p = splitdrive(path)[1]
    return len(p) == 1 and p[0] in '/\\'


def normpath(path):
    """Normalize path, eliminating double slashes, etc."""
    path = path.replace('\\', '/')
    prefix, path = splitdrive(path)
    while path[:1] == '/':
        prefix = prefix + '/'
        path = path[1:]

    comps = path.split('/')
    i = 0
    while i < len(comps):
        if comps[i] == '.':
            del comps[i]
        elif comps[i] == '..' and i > 0 and comps[i - 1] not in ('', '..'):
            del comps[i - 1:i + 1]
            i = i - 1
        elif comps[i] == '' and i > 0 and comps[i - 1] != '':
            del comps[i]
        else:
            i = i + 1

    if not prefix and not comps:
        comps.append('.')
    return prefix + '/'.join(comps)


def abspath(path):
    """Return the absolute version of a path"""
    if not isabs(path):
        if isinstance(path, unicode):
            cwd = os.getcwdu()
        else:
            cwd = os.getcwd()
        path = join(cwd, path)
    return normpath(path)


realpath = abspath
supports_unicode_filenames = False