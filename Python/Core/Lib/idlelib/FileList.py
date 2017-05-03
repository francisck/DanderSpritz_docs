# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: FileList.py
import os
from Tkinter import *
import tkMessageBox

class FileList:
    from idlelib.EditorWindow import EditorWindow

    def __init__(self, root):
        self.root = root
        self.dict = {}
        self.inversedict = {}
        self.vars = {}

    def open(self, filename, action=None):
        filename = self.canonize(filename)
        if os.path.isdir(filename):
            tkMessageBox.showerror('File Error', '%r is a directory.' % (filename,), master=self.root)
            return None
        else:
            key = os.path.normcase(filename)
            if key in self.dict:
                edit = self.dict[key]
                edit.top.wakeup()
                return edit
            if action:
                return action(filename)
            return self.EditorWindow(self, filename, key)
            return None

    def gotofileline(self, filename, lineno=None):
        edit = self.open(filename)
        if edit is not None and lineno is not None:
            edit.gotoline(lineno)
        return

    def new(self, filename=None):
        return self.EditorWindow(self, filename)

    def close_all_callback(self, *args, **kwds):
        for edit in self.inversedict.keys():
            reply = edit.close()
            if reply == 'cancel':
                break

        return 'break'

    def unregister_maybe_terminate(self, edit):
        try:
            key = self.inversedict[edit]
        except KeyError:
            print "Don't know this EditorWindow object.  (close)"
            return

        if key:
            del self.dict[key]
        del self.inversedict[edit]
        if not self.inversedict:
            self.root.quit()

    def filename_changed_edit(self, edit):
        edit.saved_change_hook()
        try:
            key = self.inversedict[edit]
        except KeyError:
            print "Don't know this EditorWindow object.  (rename)"
            return

        filename = edit.io.filename
        if not filename:
            if key:
                del self.dict[key]
            self.inversedict[edit] = None
            return
        else:
            filename = self.canonize(filename)
            newkey = os.path.normcase(filename)
            if newkey == key:
                return
            if newkey in self.dict:
                conflict = self.dict[newkey]
                self.inversedict[conflict] = None
                tkMessageBox.showerror('Name Conflict', 'You now have multiple edit windows open for %r' % (filename,), master=self.root)
            self.dict[newkey] = edit
            self.inversedict[edit] = newkey
            if key:
                try:
                    del self.dict[key]
                except KeyError:
                    pass

            return

    def canonize(self, filename):
        if not os.path.isabs(filename):
            try:
                pwd = os.getcwd()
            except os.error:
                pass
            else:
                filename = os.path.join(pwd, filename)

        return os.path.normpath(filename)


def _test():
    from idlelib.EditorWindow import fixwordbreaks
    import sys
    root = Tk()
    fixwordbreaks(root)
    root.withdraw()
    flist = FileList(root)
    if sys.argv[1:]:
        for filename in sys.argv[1:]:
            flist.open(filename)

    else:
        flist.new()
    if flist.inversedict:
        root.mainloop()


if __name__ == '__main__':
    _test()