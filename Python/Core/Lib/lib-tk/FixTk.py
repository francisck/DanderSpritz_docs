# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: FixTk.py
import sys
import os
try:
    import ctypes
    ctypes.windll.kernel32.GetFinalPathNameByHandleW
except (ImportError, AttributeError):

    def convert_path(s):
        return s


else:

    def convert_path(s):
        udir = s.decode('mbcs')
        hdir = ctypes.windll.kernel32.CreateFileW(udir, 128, 1, None, 3, 33554432, None)
        if hdir == -1:
            return s
        else:
            buf = ctypes.create_unicode_buffer(u'', 32768)
            res = ctypes.windll.kernel32.GetFinalPathNameByHandleW(hdir, buf, len(buf), 0)
            ctypes.windll.kernel32.CloseHandle(hdir)
            if res == 0:
                return s
            s = buf[:res].encode('mbcs')
            if s.startswith('\\\\?\\'):
                s = s[4:]
            if s.startswith('UNC'):
                s = '\\' + s[3:]
            return s


prefix = os.path.join(sys.prefix, 'tcl')
if not os.path.exists(prefix):
    prefix = os.path.join(sys.prefix, os.path.pardir, 'tcltk', 'lib')
    prefix = os.path.abspath(prefix)
if os.path.exists(prefix):
    prefix = convert_path(prefix)
    if 'TCL_LIBRARY' not in os.environ:
        for name in os.listdir(prefix):
            if name.startswith('tcl'):
                tcldir = os.path.join(prefix, name)
                if os.path.isdir(tcldir):
                    os.environ['TCL_LIBRARY'] = tcldir

    import _tkinter
    ver = str(_tkinter.TCL_VERSION)
    if 'TK_LIBRARY' not in os.environ:
        v = os.path.join(prefix, 'tk' + ver)
        if os.path.exists(os.path.join(v, 'tclIndex')):
            os.environ['TK_LIBRARY'] = v
    if 'TIX_LIBRARY' not in os.environ:
        for name in os.listdir(prefix):
            if name.startswith('tix'):
                tixdir = os.path.join(prefix, name)
                if os.path.isdir(tixdir):
                    os.environ['TIX_LIBRARY'] = tixdir