# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class MatchFileTimes(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.MatchFileTimesResults = MatchFileTimes.MatchFileTimesResults(dsz.cmd.data.Get('MatchFileTimesResults', dsz.TYPE_OBJECT)[0])
        except:
            self.MatchFileTimesResults = None

        return

    class MatchFileTimesResults(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.destfile = dsz.cmd.data.ObjectGet(obj, 'destfile', dsz.TYPE_STRING)[0]
            except:
                self.destfile = None

            try:
                self.sourcefile = dsz.cmd.data.ObjectGet(obj, 'sourcefile', dsz.TYPE_STRING)[0]
            except:
                self.sourcefile = None

            return


dsz.data.RegisterCommand('MatchFileTimes', MatchFileTimes)
MATCHFILETIMES = MatchFileTimes
matchfiletimes = MatchFileTimes