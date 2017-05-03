# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Services(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = Services.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        self.service = list()
        try:
            for x in dsz.cmd.data.Get('service', dsz.TYPE_OBJECT):
                self.service.append(Services.service(x))

        except:
            pass

        return

    class TaskingInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.recursive = dsz.cmd.data.ObjectGet(obj, 'recursive', dsz.TYPE_BOOL)[0]
            except:
                self.recursive = None

            try:
                self.Target = Services.TaskingInfo.Target(dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_OBJECT)[0])
            except:
                self.Target = None

            return

        class Target(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.local = dsz.cmd.data.ObjectGet(obj, 'local', dsz.TYPE_BOOL)[0]
                except:
                    self.local = None

                try:
                    self.location = dsz.cmd.data.ObjectGet(obj, 'location', dsz.TYPE_STRING)[0]
                except:
                    self.location = None

                return

    class service(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.serviceName = dsz.cmd.data.ObjectGet(obj, 'serviceName', dsz.TYPE_STRING)[0]
            except:
                self.serviceName = None

            try:
                self.state = dsz.cmd.data.ObjectGet(obj, 'state', dsz.TYPE_STRING)[0]
            except:
                self.state = None

            try:
                self.displayName = dsz.cmd.data.ObjectGet(obj, 'displayName', dsz.TYPE_STRING)[0]
            except:
                self.displayName = None

            try:
                self.AcceptedCodes = Services.service.AcceptedCodes(dsz.cmd.data.ObjectGet(obj, 'AcceptedCodes', dsz.TYPE_OBJECT)[0])
            except:
                self.AcceptedCodes = None

            try:
                self.ServiceType = Services.service.ServiceType(dsz.cmd.data.ObjectGet(obj, 'ServiceType', dsz.TYPE_OBJECT)[0])
            except:
                self.ServiceType = None

            return

        class AcceptedCodes(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.acceptsPowerEvent = dsz.cmd.data.ObjectGet(obj, 'acceptsPowerEvent', dsz.TYPE_BOOL)[0]
                except:
                    self.acceptsPowerEvent = None

                try:
                    self.acceptsShutdown = dsz.cmd.data.ObjectGet(obj, 'acceptsShutdown', dsz.TYPE_BOOL)[0]
                except:
                    self.acceptsShutdown = None

                try:
                    self.acceptsNetBindChange = dsz.cmd.data.ObjectGet(obj, 'acceptsNetBindChange', dsz.TYPE_BOOL)[0]
                except:
                    self.acceptsNetBindChange = None

                try:
                    self.acceptsPauseContinue = dsz.cmd.data.ObjectGet(obj, 'acceptsPauseContinue', dsz.TYPE_BOOL)[0]
                except:
                    self.acceptsPauseContinue = None

                try:
                    self.acceptsHardwareProfChange = dsz.cmd.data.ObjectGet(obj, 'acceptsHardwareProfChange', dsz.TYPE_BOOL)[0]
                except:
                    self.acceptsHardwareProfChange = None

                try:
                    self.acceptsParamChange = dsz.cmd.data.ObjectGet(obj, 'acceptsParamChange', dsz.TYPE_BOOL)[0]
                except:
                    self.acceptsParamChange = None

                try:
                    self.acceptsSessionChange = dsz.cmd.data.ObjectGet(obj, 'acceptsSessionChange', dsz.TYPE_BOOL)[0]
                except:
                    self.acceptsSessionChange = None

                try:
                    self.acceptsStop = dsz.cmd.data.ObjectGet(obj, 'acceptsStop', dsz.TYPE_BOOL)[0]
                except:
                    self.acceptsStop = None

                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_INT)[0]
                except:
                    self.value = None

                return

        class ServiceType(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.serviceSharesProcess = dsz.cmd.data.ObjectGet(obj, 'serviceSharesProcess', dsz.TYPE_BOOL)[0]
                except:
                    self.serviceSharesProcess = None

                try:
                    self.serviceFileSystemDriver = dsz.cmd.data.ObjectGet(obj, 'serviceFileSystemDriver', dsz.TYPE_BOOL)[0]
                except:
                    self.serviceFileSystemDriver = None

                try:
                    self.serviceOwnProcess = dsz.cmd.data.ObjectGet(obj, 'serviceOwnProcess', dsz.TYPE_BOOL)[0]
                except:
                    self.serviceOwnProcess = None

                try:
                    self.serviceDeviceDriver = dsz.cmd.data.ObjectGet(obj, 'serviceDeviceDriver', dsz.TYPE_BOOL)[0]
                except:
                    self.serviceDeviceDriver = None

                try:
                    self.serviceInteractiveProcess = dsz.cmd.data.ObjectGet(obj, 'serviceInteractiveProcess', dsz.TYPE_BOOL)[0]
                except:
                    self.serviceInteractiveProcess = None

                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_INT)[0]
                except:
                    self.value = None

                return


dsz.data.RegisterCommand('Services', Services)
SERVICES = Services
services = Services