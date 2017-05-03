# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class KiSu_Survey(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Persistence = KiSu_Survey.Persistence(dsz.cmd.data.Get('Persistence', dsz.TYPE_OBJECT)[0])
        except:
            self.Persistence = None

        return

    class Persistence(dsz.data.DataBean):

        def __init__(self, obj):
            self.Method = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Method', dsz.TYPE_OBJECT):
                    self.Method.append(KiSu_Survey.Persistence.Method(x))

            except:
                pass

        class Method(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Compatible = dsz.cmd.data.ObjectGet(obj, 'Compatible', dsz.TYPE_BOOL)[0]
                except:
                    self.Compatible = None

                try:
                    self.Type = dsz.cmd.data.ObjectGet(obj, 'Type', dsz.TYPE_STRING)[0]
                except:
                    self.Type = None

                try:
                    self.Reason = dsz.cmd.data.ObjectGet(obj, 'Reason', dsz.TYPE_STRING)[0]
                except:
                    self.Reason = None

                return


dsz.data.RegisterCommand('KiSu_Survey', KiSu_Survey)
KISU_SURVEY = KiSu_Survey
kisu_survey = KiSu_Survey