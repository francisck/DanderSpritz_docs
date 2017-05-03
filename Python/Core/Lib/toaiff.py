# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: toaiff.py
"""Convert "arbitrary" sound files to AIFF (Apple and SGI's audio format).

Input may be compressed.
Uncompressed file type may be AIFF, WAV, VOC, 8SVX, NeXT/Sun, and others.
An exception is raised if the file is not of a recognized type.
Returned filename is either the input filename or a temporary filename;
in the latter case the caller must ensure that it is removed.
Other temporary files used are removed by the function.
"""
from warnings import warnpy3k
warnpy3k('the toaiff module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
import os
import tempfile
import pipes
import sndhdr
__all__ = [
 'error', 'toaiff']
table = {}
t = pipes.Template()
t.append('sox -t au - -t aiff -r 8000 -', '--')
table['au'] = t
t = pipes.Template()
t.append('sox -t hcom - -t aiff -r 22050 -', '--')
table['hcom'] = t
t = pipes.Template()
t.append('sox -t voc - -t aiff -r 11025 -', '--')
table['voc'] = t
t = pipes.Template()
t.append('sox -t wav - -t aiff -', '--')
table['wav'] = t
t = pipes.Template()
t.append('sox -t 8svx - -t aiff -r 16000 -', '--')
table['8svx'] = t
t = pipes.Template()
t.append('sox -t sndt - -t aiff -r 16000 -', '--')
table['sndt'] = t
t = pipes.Template()
t.append('sox -t sndr - -t aiff -r 16000 -', '--')
table['sndr'] = t
uncompress = pipes.Template()
uncompress.append('uncompress', '--')

class error(Exception):
    pass


def toaiff(filename):
    temps = []
    ret = None
    try:
        ret = _toaiff(filename, temps)
    finally:
        for temp in temps[:]:
            if temp != ret:
                try:
                    os.unlink(temp)
                except os.error:
                    pass

                temps.remove(temp)

    return ret


def _toaiff(filename, temps):
    if filename[-2:] == '.Z':
        fd, fname = tempfile.mkstemp()
        os.close(fd)
        temps.append(fname)
        sts = uncompress.copy(filename, fname)
        if sts:
            raise error, filename + ': uncompress failed'
    else:
        fname = filename
    try:
        ftype = sndhdr.whathdr(fname)
        if ftype:
            ftype = ftype[0]
    except IOError as msg:
        if type(msg) == type(()) and len(msg) == 2 and type(msg[0]) == type(0) and type(msg[1]) == type(''):
            msg = msg[1]
        if type(msg) != type(''):
            msg = repr(msg)
        raise error, filename + ': ' + msg

    if ftype == 'aiff':
        return fname
    else:
        if ftype is None or ftype not in table:
            raise error, '%s: unsupported audio file type %r' % (filename, ftype)
        fd, temp = tempfile.mkstemp()
        os.close(fd)
        temps.append(temp)
        sts = table[ftype].copy(fname, temp)
        if sts:
            raise error, filename + ': conversion to aiff failed'
        return temp