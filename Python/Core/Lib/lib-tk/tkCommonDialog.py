# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: tkCommonDialog.py
from Tkinter import *

class Dialog:
    command = None

    def __init__(self, master=None, **options):
        if TkVersion < 4.2:
            raise TclError, 'this module requires Tk 4.2 or newer'
        self.master = master
        self.options = options
        if not master and options.get('parent'):
            self.master = options['parent']

    def _fixoptions(self):
        pass

    def _fixresult(self, widget, result):
        return result

    def show(self, **options):
        for k, v in options.items():
            self.options[k] = v

        self._fixoptions()
        w = Frame(self.master)
        try:
            s = w.tk.call(self.command, *w._options(self.options))
            s = self._fixresult(w, s)
        finally:
            try:
                w.destroy()
            except:
                pass

        return s