# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: linecache.py
"""Cache lines from files.

This is intended to read lines from modules imported -- hence if a filename
is not found, it will look down the module search path for a file by
that name.
"""
import sys
import os
__all__ = [
 'getline', 'clearcache', 'checkcache']

def getline(filename, lineno, module_globals=None):
    lines = getlines(filename, module_globals)
    if 1 <= lineno <= len(lines):
        return lines[lineno - 1]
    else:
        return ''


cache = {}

def clearcache():
    """Clear the cache entirely."""
    global cache
    cache = {}


def getlines(filename, module_globals=None):
    """Get the lines for a file from the cache.
    Update the cache if it doesn't contain an entry for this file already."""
    if filename in cache:
        return cache[filename][2]
    else:
        return updatecache(filename, module_globals)


def checkcache(filename=None):
    """Discard cache entries that are out of date.
    (This is not checked upon each call!)"""
    if filename is None:
        filenames = cache.keys()
    elif filename in cache:
        filenames = [
         filename]
    else:
        return
    for filename in filenames:
        size, mtime, lines, fullname = cache[filename]
        if mtime is None:
            continue
        try:
            stat = os.stat(fullname)
        except os.error:
            del cache[filename]
            continue

        if size != stat.st_size or mtime != stat.st_mtime:
            del cache[filename]

    return


def updatecache(filename, module_globals=None):
    """Update a cache entry and return its list of lines.
    If something's wrong, print a message, discard the cache entry,
    and return an empty list."""
    if filename in cache:
        del cache[filename]
    if not filename or filename.startswith('<') and filename.endswith('>'):
        return []
    else:
        fullname = filename
        try:
            stat = os.stat(fullname)
        except OSError:
            basename = filename
            if module_globals and '__loader__' in module_globals:
                name = module_globals.get('__name__')
                loader = module_globals['__loader__']
                get_source = getattr(loader, 'get_source', None)
                if name and get_source:
                    try:
                        data = get_source(name)
                    except (ImportError, IOError):
                        pass
                    else:
                        if data is None:
                            return []
                        cache[filename] = (
                         len(data), None, [ line + '\n' for line in data.splitlines() ], fullname)
                        return cache[filename][2]

            if os.path.isabs(filename):
                return []
            for dirname in sys.path:
                try:
                    fullname = os.path.join(dirname, basename)
                except (TypeError, AttributeError):
                    continue

                try:
                    stat = os.stat(fullname)
                    break
                except os.error:
                    pass

            else:
                return []

        try:
            with open(fullname, 'rU') as fp:
                lines = fp.readlines()
        except IOError:
            return []

        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'
        size, mtime = stat.st_size, stat.st_mtime
        cache[filename] = (size, mtime, lines, fullname)
        return lines