# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: ToolTip.py
from Tkinter import *

class ToolTipBase:

    def __init__(self, button):
        self.button = button
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self._id1 = self.button.bind('<Enter>', self.enter)
        self._id2 = self.button.bind('<Leave>', self.leave)
        self._id3 = self.button.bind('<ButtonPress>', self.leave)
        return

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.button.after(1500, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.button.after_cancel(id)
        return

    def showtip(self):
        if self.tipwindow:
            return
        x = self.button.winfo_rootx() + 20
        y = self.button.winfo_rooty() + self.button.winfo_height() + 1
        self.tipwindow = tw = Toplevel(self.button)
        tw.wm_overrideredirect(1)
        tw.wm_geometry('+%d+%d' % (x, y))
        self.showcontents()

    def showcontents(self, text='Your text here'):
        label = Label(self.tipwindow, text=text, justify=LEFT, background='#ffffe0', relief=SOLID, borderwidth=1)
        label.pack()

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
        return


class ToolTip(ToolTipBase):

    def __init__(self, button, text):
        ToolTipBase.__init__(self, button)
        self.text = text

    def showcontents(self):
        ToolTipBase.showcontents(self, self.text)


class ListboxToolTip(ToolTipBase):

    def __init__(self, button, items):
        ToolTipBase.__init__(self, button)
        self.items = items

    def showcontents(self):
        listbox = Listbox(self.tipwindow, background='#ffffe0')
        listbox.pack()
        for item in self.items:
            listbox.insert(END, item)


def main():
    root = Tk()
    b = Button(root, text='Hello', command=root.destroy)
    b.pack()
    root.update()
    tip = ListboxToolTip(b, ['Hello', 'world'])
    root.mainloop()


if __name__ == '__main__':
    main()