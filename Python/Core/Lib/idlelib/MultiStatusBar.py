# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: MultiStatusBar.py
from Tkinter import *

class MultiStatusBar(Frame):

    def __init__(self, master=None, **kw):
        if master is None:
            master = Tk()
        Frame.__init__(self, master, **kw)
        self.labels = {}
        return

    def set_label(self, name, text='', side=LEFT):
        if name not in self.labels:
            label = Label(self, bd=1, relief=SUNKEN, anchor=W)
            label.pack(side=side)
            self.labels[name] = label
        else:
            label = self.labels[name]
        label.config(text=text)


def _test():
    b = Frame()
    c = Text(b)
    c.pack(side=TOP)
    a = MultiStatusBar(b)
    a.set_label('one', 'hello')
    a.set_label('two', 'world')
    a.pack(side=BOTTOM, fill=X)
    b.pack()
    b.mainloop()


if __name__ == '__main__':
    _test()