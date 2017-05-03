# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: OutputWindow.py
from Tkinter import *
from idlelib.EditorWindow import EditorWindow
import re
import tkMessageBox
from idlelib import IOBinding

class OutputWindow(EditorWindow):
    """An editor window that can serve as an output file.
    
    Also the future base class for the Python shell window.
    This class has no input facilities.
    """

    def __init__(self, *args):
        EditorWindow.__init__(self, *args)
        self.text.bind('<<goto-file-line>>', self.goto_file_line)

    def ispythonsource(self, filename):
        return 0

    def short_title(self):
        return 'Output'

    def maybesave(self):
        if self.get_saved():
            return 'yes'
        else:
            return 'no'

    def write(self, s, tags=(), mark='insert'):
        if isinstance(s, str):
            try:
                s = unicode(s, IOBinding.encoding)
            except UnicodeError:
                pass

        self.text.insert(mark, s, tags)
        self.text.see(mark)
        self.text.update()

    def writelines(self, lines):
        for line in lines:
            self.write(line)

    def flush(self):
        pass

    rmenu_specs = [
     ('Go to file/line', '<<goto-file-line>>')]
    file_line_pats = [
     'file "([^"]*)", line (\\d+)',
     '([^\\s]+)\\((\\d+)\\)',
     '^(\\s*\\S.*?):\\s*(\\d+):',
     '([^\\s]+):\\s*(\\d+):',
     '^\\s*(\\S.*?):\\s*(\\d+):']
    file_line_progs = None

    def goto_file_line(self, event=None):
        if self.file_line_progs is None:
            l = []
            for pat in self.file_line_pats:
                l.append(re.compile(pat, re.IGNORECASE))

            self.file_line_progs = l
        line = self.text.get('insert linestart', 'insert lineend')
        result = self._file_line_helper(line)
        if not result:
            line = self.text.get('insert -1line linestart', 'insert -1line lineend')
            result = self._file_line_helper(line)
            if not result:
                tkMessageBox.showerror('No special line', "The line you point at doesn't look like a valid file name followed by a line number.", master=self.text)
                return
        filename, lineno = result
        edit = self.flist.open(filename)
        edit.gotoline(lineno)
        return

    def _file_line_helper(self, line):
        for prog in self.file_line_progs:
            match = prog.search(line)
            if match:
                filename, lineno = match.group(1, 2)
                try:
                    f = open(filename, 'r')
                    f.close()
                    break
                except IOError:
                    continue

        else:
            return None

        try:
            return (
             filename, int(lineno))
        except TypeError:
            return None

        return None


class OnDemandOutputWindow:
    tagdefs = {'stdout': {'foreground': 'blue'},'stderr': {'foreground': '#007700'}}

    def __init__(self, flist):
        self.flist = flist
        self.owin = None
        return

    def write(self, s, tags, mark):
        if not self.owin:
            self.setup()
        self.owin.write(s, tags, mark)

    def setup(self):
        self.owin = owin = OutputWindow(self.flist)
        text = owin.text
        for tag, cnf in self.tagdefs.items():
            if cnf:
                text.tag_configure(tag, **cnf)

        text.tag_raise('sel')
        self.write = self.owin.write