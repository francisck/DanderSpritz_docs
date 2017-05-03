# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Route(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.Route = list()
        try:
            for x in dsz.cmd.data.Get('Route', dsz.TYPE_OBJECT):
                self.Route.append(Route.Route(x))

        except:
            pass

    class Route(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.metric = dsz.cmd.data.ObjectGet(obj, 'metric', dsz.TYPE_INT)[0]
            except:
                self.metric = None

            try:
                self.gateway = dsz.cmd.data.ObjectGet(obj, 'gateway', dsz.TYPE_STRING)[0]
            except:
                self.gateway = None

            try:
                self.destination = dsz.cmd.data.ObjectGet(obj, 'destination', dsz.TYPE_STRING)[0]
            except:
                self.destination = None

            try:
                self.networkMask = dsz.cmd.data.ObjectGet(obj, 'networkMask', dsz.TYPE_STRING)[0]
            except:
                self.networkMask = None

            try:
                self.interface = dsz.cmd.data.ObjectGet(obj, 'interface', dsz.TYPE_STRING)[0]
            except:
                self.interface = None

            try:
                self.Origin = dsz.cmd.data.ObjectGet(obj, 'Origin', dsz.TYPE_STRING)[0]
            except:
                self.Origin = None

            try:
                self.RouteType = dsz.cmd.data.ObjectGet(obj, 'RouteType', dsz.TYPE_STRING)[0]
            except:
                self.RouteType = None

            try:
                self.FlagLoopback = dsz.cmd.data.ObjectGet(obj, 'FlagLoopback', dsz.TYPE_BOOL)[0]
            except:
                self.FlagLoopback = None

            try:
                self.FlagAutoConfigure = dsz.cmd.data.ObjectGet(obj, 'FlagAutoConfigure', dsz.TYPE_BOOL)[0]
            except:
                self.FlagAutoConfigure = None

            try:
                self.FlagPermanent = dsz.cmd.data.ObjectGet(obj, 'FlagPermanent', dsz.TYPE_BOOL)[0]
            except:
                self.FlagPermanent = None

            try:
                self.FlagPublish = dsz.cmd.data.ObjectGet(obj, 'FlagPublish', dsz.TYPE_BOOL)[0]
            except:
                self.FlagPublish = None

            return


dsz.data.RegisterCommand('Route', Route)
ROUTE = Route
route = Route