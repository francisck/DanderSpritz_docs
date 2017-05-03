# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: macurl2path.py
"""Macintosh-specific module for conversion between pathnames and URLs.

Do not import directly; use urllib instead."""
import urllib
import os
__all__ = [
 'url2pathname', 'pathname2url']

def url2pathname(pathname):
    """OS-specific conversion from a relative URL of the 'file' scheme
    to a file system path; not recommended for general use."""
    tp = urllib.splittype(pathname)[0]
    if tp and tp != 'file':
        raise RuntimeError, 'Cannot convert non-local URL to pathname'
    if pathname[:3] == '///':
        pathname = pathname[2:]
    else:
        if pathname[:2] == '//':
            raise RuntimeError, 'Cannot convert non-local URL to pathname'
        components = pathname.split('/')
        i = 0
        while i < len(components):
            if components[i] == '.':
                del components[i]
            elif components[i] == '..' and i > 0 and components[i - 1] not in ('',
                                                                               '..'):
                del components[i - 1:i + 1]
                i = i - 1
            elif components[i] == '' and i > 0 and components[i - 1] != '':
                del components[i]
            else:
                i = i + 1

        if not components[0]:
            rv = ':'.join(components[1:])
        else:
            i = 0
            while i < len(components) and components[i] == '..':
                components[i] = ''
                i = i + 1

        rv = ':' + ':'.join(components)
    return urllib.unquote(rv)


def pathname2url(pathname):
    """OS-specific conversion from a file system path to a relative URL
    of the 'file' scheme; not recommended for general use."""
    if '/' in pathname:
        raise RuntimeError, 'Cannot convert pathname containing slashes'
    components = pathname.split(':')
    if components[0] == '':
        del components[0]
    if components[-1] == '':
        del components[-1]
    for i in range(len(components)):
        if components[i] == '':
            components[i] = '..'

    components = map(_pncomp2url, components)
    if os.path.isabs(pathname):
        return '/' + '/'.join(components)
    else:
        return '/'.join(components)


def _pncomp2url(component):
    component = urllib.quote(component[:31], safe='')
    return component


def test():
    for url in ['index.html',
     'bar/index.html',
     '/foo/bar/index.html',
     '/foo/bar/',
     '/']:
        print '%r -> %r' % (url, url2pathname(url))

    for path in ['drive:', 'drive:dir:',
     'drive:dir:file',
     'drive:file',
     'file',
     ':file',
     ':dir:',
     ':dir:file']:
        print '%r -> %r' % (path, pathname2url(path))


if __name__ == '__main__':
    test()