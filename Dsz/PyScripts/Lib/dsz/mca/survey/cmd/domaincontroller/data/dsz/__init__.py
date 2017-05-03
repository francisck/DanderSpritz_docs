# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class DomainController(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.domaincontroller = list()
        try:
            for x in dsz.cmd.data.Get('domaincontroller', dsz.TYPE_OBJECT):
                self.domaincontroller.append(DomainController.domaincontroller(x))

        except:
            pass

    class domaincontroller(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.domainname = dsz.cmd.data.ObjectGet(obj, 'domainname', dsz.TYPE_STRING)[0]
            except:
                self.domainname = None

            try:
                self.dcsitename = dsz.cmd.data.ObjectGet(obj, 'dcsitename', dsz.TYPE_STRING)[0]
            except:
                self.dcsitename = None

            try:
                self.dnsforestname = dsz.cmd.data.ObjectGet(obj, 'dnsforestname', dsz.TYPE_STRING)[0]
            except:
                self.dnsforestname = None

            try:
                self.dcname = dsz.cmd.data.ObjectGet(obj, 'dcname', dsz.TYPE_STRING)[0]
            except:
                self.dcname = None

            try:
                self.clientsitename = dsz.cmd.data.ObjectGet(obj, 'clientsitename', dsz.TYPE_STRING)[0]
            except:
                self.clientsitename = None

            try:
                self.dcaddress = dsz.cmd.data.ObjectGet(obj, 'dcaddress', dsz.TYPE_STRING)[0]
            except:
                self.dcaddress = None

            try:
                self.domainguid = dsz.cmd.data.ObjectGet(obj, 'domainguid', dsz.TYPE_STRING)[0]
            except:
                self.domainguid = None

            try:
                self.dcfullname = dsz.cmd.data.ObjectGet(obj, 'dcfullname', dsz.TYPE_STRING)[0]
            except:
                self.dcfullname = None

            return


dsz.data.RegisterCommand('DomainController', DomainController)
DOMAINCONTROLLER = DomainController
domaincontroller = DomainController