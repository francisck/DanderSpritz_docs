# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class DeviceQuery(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.deviceitem = list()
        try:
            for x in dsz.cmd.data.Get('deviceitem', dsz.TYPE_OBJECT):
                self.deviceitem.append(DeviceQuery.deviceitem(x))

        except:
            pass

    class deviceitem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.servicepath = dsz.cmd.data.ObjectGet(obj, 'servicepath', dsz.TYPE_STRING)[0]
            except:
                self.servicepath = None

            try:
                self.physdevobjname = dsz.cmd.data.ObjectGet(obj, 'physdevobjname', dsz.TYPE_STRING)[0]
            except:
                self.physdevobjname = None

            try:
                self.friendlyname = dsz.cmd.data.ObjectGet(obj, 'friendlyname', dsz.TYPE_STRING)[0]
            except:
                self.friendlyname = None

            try:
                self.devicedesc = dsz.cmd.data.ObjectGet(obj, 'devicedesc', dsz.TYPE_STRING)[0]
            except:
                self.devicedesc = None

            try:
                self.locationinfo = dsz.cmd.data.ObjectGet(obj, 'locationinfo', dsz.TYPE_STRING)[0]
            except:
                self.locationinfo = None

            try:
                self.driver = dsz.cmd.data.ObjectGet(obj, 'driver', dsz.TYPE_STRING)[0]
            except:
                self.driver = None

            try:
                self.mfg = dsz.cmd.data.ObjectGet(obj, 'mfg', dsz.TYPE_STRING)[0]
            except:
                self.mfg = None

            try:
                self.hardwareid = dsz.cmd.data.ObjectGet(obj, 'hardwareid', dsz.TYPE_STRING)[0]
            except:
                self.hardwareid = None

            return


dsz.data.RegisterCommand('DeviceQuery', DeviceQuery)
DEVICEQUERY = DeviceQuery
devicequery = DeviceQuery