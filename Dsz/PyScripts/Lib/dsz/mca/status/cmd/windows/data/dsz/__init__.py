# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Windows(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.WindowStation = list()
        try:
            for x in dsz.cmd.data.Get('WindowStation', dsz.TYPE_OBJECT):
                self.WindowStation.append(Windows.WindowStation(x))

        except:
            pass

        try:
            self.Screenshot = Windows.Screenshot(dsz.cmd.data.Get('Screenshot', dsz.TYPE_OBJECT)[0])
        except:
            self.Screenshot = None

        try:
            self.Window = Windows.Window(dsz.cmd.data.Get('Window', dsz.TYPE_OBJECT)[0])
        except:
            self.Window = None

        return

    class WindowStation(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.visible = dsz.cmd.data.ObjectGet(obj, 'visible', dsz.TYPE_BOOL)[0]
            except:
                self.visible = None

            try:
                self.status = dsz.cmd.data.ObjectGet(obj, 'status', dsz.TYPE_STRING)[0]
            except:
                self.status = None

            try:
                self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
            except:
                self.name = None

            self.Desktop = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Desktop', dsz.TYPE_OBJECT):
                    self.Desktop.append(Windows.WindowStation.Desktop(x))

            except:
                pass

            return

        class Desktop(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
                except:
                    self.name = None

                return

    class Screenshot(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.filename = dsz.cmd.data.ObjectGet(obj, 'filename', dsz.TYPE_STRING)[0]
            except:
                self.filename = None

            try:
                self.path = dsz.cmd.data.ObjectGet(obj, 'path', dsz.TYPE_STRING)[0]
            except:
                self.path = None

            try:
                self.subdir = dsz.cmd.data.ObjectGet(obj, 'subdir', dsz.TYPE_STRING)
            except:
                self.subdir = None

            return

    class Window(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.visible = dsz.cmd.data.ObjectGet(obj, 'visible', dsz.TYPE_BOOL)[0]
            except:
                self.visible = None

            try:
                self.minimized = dsz.cmd.data.ObjectGet(obj, 'minimized', dsz.TYPE_BOOL)[0]
            except:
                self.minimized = None

            try:
                self.hParent = dsz.cmd.data.ObjectGet(obj, 'hParent', dsz.TYPE_INT)[0]
            except:
                self.hParent = None

            try:
                self.hWnd = dsz.cmd.data.ObjectGet(obj, 'hWnd', dsz.TYPE_INT)[0]
            except:
                self.hWnd = None

            try:
                self.pid = dsz.cmd.data.ObjectGet(obj, 'pid', dsz.TYPE_INT)[0]
            except:
                self.pid = None

            try:
                self.text = dsz.cmd.data.ObjectGet(obj, 'text', dsz.TYPE_STRING)[0]
            except:
                self.text = None

            return


dsz.data.RegisterCommand('Windows', Windows)
WINDOWS = Windows
windows = Windows