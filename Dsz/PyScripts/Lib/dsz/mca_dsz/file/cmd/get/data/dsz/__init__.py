# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Get(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.LocalGetDirectory = Get.LocalGetDirectory(dsz.cmd.data.Get('LocalGetDirectory', dsz.TYPE_OBJECT)[0])
        except:
            self.LocalGetDirectory = None

        self.FileStart = list()
        try:
            for x in dsz.cmd.data.Get('FileStart', dsz.TYPE_OBJECT):
                self.FileStart.append(Get.FileStart(x))

        except:
            pass

        self.FileLocalName = list()
        try:
            for x in dsz.cmd.data.Get('FileLocalName', dsz.TYPE_OBJECT):
                self.FileLocalName.append(Get.FileLocalName(x))

        except:
            pass

        self.FileWrite = list()
        try:
            for x in dsz.cmd.data.Get('FileWrite', dsz.TYPE_OBJECT):
                self.FileWrite.append(Get.FileWrite(x))

        except:
            pass

        self.FileStop = list()
        try:
            for x in dsz.cmd.data.Get('FileStop', dsz.TYPE_OBJECT):
                self.FileStop.append(Get.FileStop(x))

        except:
            pass

        try:
            self.Conclusion = Get.Conclusion(dsz.cmd.data.Get('Conclusion', dsz.TYPE_OBJECT)[0])
        except:
            self.Conclusion = None

        return

    class LocalGetDirectory(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Path = dsz.cmd.data.ObjectGet(obj, 'Path', dsz.TYPE_STRING)[0]
            except:
                self.Path = None

            return

    class FileStart(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
            except:
                self.Id = None

            try:
                self.FileName = dsz.cmd.data.ObjectGet(obj, 'FileName', dsz.TYPE_STRING)[0]
            except:
                self.FileName = None

            try:
                self.OriginalName = dsz.cmd.data.ObjectGet(obj, 'OriginalName', dsz.TYPE_STRING)[0]
            except:
                self.OriginalName = None

            try:
                self.size = dsz.cmd.data.ObjectGet(obj, 'size', dsz.TYPE_INT)[0]
            except:
                self.size = None

            return

    class FileLocalName(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
            except:
                self.Id = None

            try:
                self.LocalName = dsz.cmd.data.ObjectGet(obj, 'LocalName', dsz.TYPE_STRING)[0]
            except:
                self.LocalName = None

            try:
                self.SubDir = dsz.cmd.data.ObjectGet(obj, 'SubDir', dsz.TYPE_STRING)[0]
            except:
                self.SubDir = None

            return

    class FileWrite(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
            except:
                self.Id = None

            try:
                self.Bytes = dsz.cmd.data.ObjectGet(obj, 'Bytes', dsz.TYPE_INT)[0]
            except:
                self.Bytes = None

            return

    class FileStop(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
            except:
                self.Id = None

            try:
                self.Successful = dsz.cmd.data.ObjectGet(obj, 'Successful', dsz.TYPE_BOOL)[0]
            except:
                self.Successful = None

            try:
                self.Written = dsz.cmd.data.ObjectGet(obj, 'Written', dsz.TYPE_INT)[0]
            except:
                self.Written = None

            return

    class Conclusion(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.NumSuccesses = dsz.cmd.data.ObjectGet(obj, 'NumSuccesses', dsz.TYPE_INT)[0]
            except:
                self.NumSuccesses = None

            try:
                self.NumPartial = dsz.cmd.data.ObjectGet(obj, 'NumPartial', dsz.TYPE_INT)[0]
            except:
                self.NumPartial = None

            try:
                self.NumFailed = dsz.cmd.data.ObjectGet(obj, 'NumFailed', dsz.TYPE_INT)[0]
            except:
                self.NumFailed = None

            try:
                self.NumSkipped = dsz.cmd.data.ObjectGet(obj, 'NumSkipped', dsz.TYPE_INT)[0]
            except:
                self.NumSkipped = None

            return


dsz.data.RegisterCommand('Get', Get)
GET = Get
get = Get