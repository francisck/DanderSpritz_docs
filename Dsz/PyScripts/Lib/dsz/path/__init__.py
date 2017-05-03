# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.path.windows
import re

def IsFullPath(path):
    return re.match('^[A-Za-z]:.*$', path) != None or re.match('^/.*$', path) != None


def Normalize(path, isWindows=False):
    if isWindows:
        delimiter = '\\'
    else:
        delimiter = '/'
    origPath = path
    start = ''
    obj = re.match('^/(.*)$', path)
    if obj != None:
        start = '%s' % delimiter
        path = obj.group(1)
    else:
        obj = re.match('^([A-Za-z]:)(.*)$', path)
        if obj != None:
            isWindows = True
            start = '%s%s' % (obj.group(1), delimiter)
            path = obj.group(2)
    parts = re.split('[\\\\/]', path)
    if len(parts) == 0:
        return origPath
    else:
        fixedPaths = list()
        onIndex = 0
        i = 0
        while i < len(parts):
            if parts[i] == '.' or parts[i] == '':
                pass
            elif parts[i] == '..' and onIndex > 0:
                onIndex = onIndex - 1
                if fixedPaths[onIndex] == '..':
                    onIndex = onIndex + 1
                    if onIndex >= len(fixedPaths):
                        fixedPaths.append(parts[i])
                    else:
                        fixedPaths[onIndex] = parts[i]
                    onIndex = onIndex + 1
                else:
                    fixedPaths.pop()
            else:
                fixedPaths.append(parts[i])
                onIndex = onIndex + 1
            i = i + 1

        newPath = ''
        for part in fixedPaths:
            if len(newPath) > 0:
                if len(part) > 0:
                    newPath = '%s%s%s' % (newPath, delimiter, part)
            elif len(start) > 0:
                if len(part) > 0:
                    newPath = '%s%s' % (start, part)
                else:
                    newPath = start
            else:
                newPath = part

        if len(newPath) == 0:
            return start
        return newPath
        return


def Split(path):
    if len(path) == 0:
        return ('', '')
    else:
        obj = re.match('^(.*)[\\\\/]([^\\\\/]*)$', path)
        if obj == None:
            obj = re.match('^[a-zA-Z]:$', path)
            if obj != None:
                return (
                 path, '')
            else:
                return ('', path)

        else:
            if len(obj.group(1)) == 0:
                obj2 = re.match('^/.*$', path)
                if obj2 != None:
                    return (
                     '/', obj.group(2))
            return (obj.group(1), obj.group(2))
        return