# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Audit(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Status = Audit.Status(dsz.cmd.data.Get('Status', dsz.TYPE_OBJECT)[0])
        except:
            self.Status = None

        return

    class Status(dsz.data.DataBean):

        def __init__(self, obj):
            self.event = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'event', dsz.TYPE_OBJECT):
                    self.event.append(Audit.Status.event(x))

            except:
                pass

            try:
                self.audit_mode = dsz.cmd.data.ObjectGet(obj, 'audit_mode', dsz.TYPE_BOOL)[0]
            except:
                self.audit_mode = None

            try:
                self.audit_status_avail = dsz.cmd.data.ObjectGet(obj, 'audit_status_avail', dsz.TYPE_BOOL)[0]
            except:
                self.audit_status_avail = None

            return

        class event(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.audit_event_success = dsz.cmd.data.ObjectGet(obj, 'audit_event_success', dsz.TYPE_BOOL)[0]
                except:
                    self.audit_event_success = None

                try:
                    self.audit_event_failure = dsz.cmd.data.ObjectGet(obj, 'audit_event_failure', dsz.TYPE_BOOL)[0]
                except:
                    self.audit_event_failure = None

                try:
                    self.category = dsz.cmd.data.ObjectGet(obj, 'category', dsz.TYPE_STRING)[0]
                except:
                    self.category = None

                try:
                    self.categoryNative = dsz.cmd.data.ObjectGet(obj, 'categoryNative', dsz.TYPE_STRING)[0]
                except:
                    self.categoryNative = None

                try:
                    self.subcategory = dsz.cmd.data.ObjectGet(obj, 'subcategory', dsz.TYPE_STRING)[0]
                except:
                    self.subcategory = None

                try:
                    self.subcategoryNative = dsz.cmd.data.ObjectGet(obj, 'subcategoryNative', dsz.TYPE_STRING)[0]
                except:
                    self.subcategoryNative = None

                try:
                    self.categoryGUID = dsz.cmd.data.ObjectGet(obj, 'categoryGUID', dsz.TYPE_STRING)[0]
                except:
                    self.categoryGUID = None

                try:
                    self.subcategoryGUID = dsz.cmd.data.ObjectGet(obj, 'subcategoryGUID', dsz.TYPE_STRING)[0]
                except:
                    self.subcategoryGUID = None

                return


dsz.data.RegisterCommand('Audit', Audit)
AUDIT = Audit
audit = Audit