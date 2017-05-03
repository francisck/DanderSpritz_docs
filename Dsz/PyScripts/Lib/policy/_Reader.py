# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _Reader.py
import dsz
import dsz.lp
import dsz.script
from _RegistryPolicy import AdminTemplates
from _RegistryPolicy import Ipsec
from _RegistryPolicy import Srp
from _Shared import SYSTEM_ACCESS, EVENT_AUDIT, KERBEROS_POLICY, REGISTRY_VALUES, PRIVILEGE_RIGHTS, APPLICATION_LOG, SECURITY_LOG, SYSTEM_LOG, FILE_SECURITY, REGISTRY_KEYS, SERVICES, RESTRICTED
ENV_DICT = {'software\\policies\\microsoft': '_POLICY_SPM_PATH','security': '_POLICY_SECURITY_PATH',
   'sam': '_POLICY_SAM_PATH',
   'software\\microsoft\\windows\\currentversion\\policies': '_POLICY_CV_PATH'
   }
ENV_DOMAIN_LOGS = '_POLICY_DOMAIN_LOGS'
GETFILESPATH = dsz.lp.GetLogsDirectory() + '\\GetFiles\\'

class Reader:
    RECURSIVE = True

    def __init__(self, hive, params):
        self.cmdList = list()
        self.typeDict = dict()
        self.typevalueDict = dict()
        self.grabSecurityLogs = False
        if hive == 'hklm':
            self.hive = 'L'
            self.queryPaths = self.hklmQuery(params)
        else:
            self.hive = 'C'
            self.queryPaths = self.hkcuQuery(params)
        self.headerDict = dict()
        self.headerDict[REGISTRY_VALUES] = self.registryQuery(self.queryPaths)
        if self.grabSecurityLogs:
            self.logQuery()
        self.grabLocal = params['local'] and (params['account'] or params['options'] or params['privileges'])

    def hklmQuery(self, params):
        paths = set()
        if params['software']:
            paths = paths.union(set(Srp.getQueryPaths('hklm')))
        if params['templates']:
            paths = paths.union(set(AdminTemplates.getQueryPaths('hklm')))
        if params['ipsec']:
            paths = paths.union(set(Ipsec.getQueryPaths('hklm')))
        if params['account'] or params['privileges'] or params['restricted'] or params['permissions'] or params['audit'] or params['options'] or params['log']:
            self.grabSecurityLogs = True
        return paths

    def hkcuQuery(self, params):
        paths = set()
        if params['software']:
            paths = paths.union(set(Srp.getQueryPaths('hkcu')))
        if params['templates']:
            paths = paths.union(set(AdminTemplates.getQueryPaths('hkcu')))
        return paths

    def registryQuery(self, pathSet, recurse=RECURSIVE):
        kvDict = dict()
        if recurse == Reader.RECURSIVE:
            recurse = ' -recursive'
        else:
            recurse = ''
        for path in pathSet:
            if self.hive is 'L' and ENV_DICT.has_key(path):
                if dsz.env.Check(ENV_DICT[path]):
                    self.cmdList.append(int(dsz.env.Get(ENV_DICT[path])))
                else:
                    status, id = dsz.cmd.RunEx('registryquery -hive ' + self.hive + ' -key ' + path + ' -recursive', dsz.RUN_FLAG_RECORD | dsz.RUN_FLAG_RECORD_NO_CLEAR)
                    if not status:
                        dsz.ui.Echo('Failed getting: ' + path, dsz.WARNING)
                    else:
                        self.cmdList.append(id)
                        dsz.env.Set(ENV_DICT[path], str(id))
            elif dsz.cmd.Run('registryquery -hive ' + self.hive + ' -key ' + path + recurse, dsz.RUN_FLAG_RECORD | dsz.RUN_FLAG_RECORD_NO_CLEAR):
                self.cmdList.append(dsz.cmd.LastId())
            else:
                dsz.ui.Echo('Failed getting: ' + path, dsz.WARNING)

        for cmd in self.cmdList:
            keyList = dsz.cmd.data.Get('key', dsz.TYPE_OBJECT, cmd)
            for key in keyList:
                try:
                    dir = dsz.cmd.data.ObjectGet(key, 'name', dsz.TYPE_STRING, cmd)[0].lower()
                    valueList = dsz.cmd.data.ObjectGet(key, 'value', dsz.TYPE_OBJECT, cmd)
                    for v in valueList:
                        try:
                            value = dsz.cmd.data.ObjectGet(v, 'value', dsz.TYPE_STRING, cmd)[0].lower()
                            name = dsz.cmd.data.ObjectGet(v, 'name', dsz.TYPE_STRING, cmd)[0].lower()
                            type = dsz.cmd.data.ObjectGet(v, 'type', dsz.TYPE_STRING, cmd)[0].lower()
                            typevalue = dsz.cmd.data.ObjectGet(v, 'typevalue', dsz.TYPE_INT, cmd)[0]
                            path = dir + '!' + name
                            kvDict[path] = value
                            self.typeDict[path] = type
                            self.typevalueDict[path] = typevalue
                        except:
                            continue

                except:
                    continue

        return kvDict

    def getType(self, key):
        if self.typeDict.has_key(key):
            return self.typeDict[key]
        else:
            return None
            return None

    def getTypevalue(self, key):
        if self.typevalueDict.has_key(key):
            return self.typevalueDict[key]
        else:
            return None
            return None

    def cleanup(self):
        env_cmds = list()
        for env_var in ENV_DICT.itervalues():
            if dsz.env.Check(env_var):
                env_cmds.append(int(dsz.env.Get(env_var)))

        for i in self.cmdList:
            if env_cmds.count(i):
                continue
            dsz.cmd.data.Clear(i)

    def logQuery(self):
        fileList = self.getFileList()
        self.processFiles(fileList)

    def getFileList(self):
        fileList = ''
        if dsz.env.Check(ENV_DOMAIN_LOGS):
            fileList = dsz.env.Get(ENV_DOMAIN_LOGS)
            if fileList == '':
                return []
        fileList = fileList.split(';')
        try:
            try:
                for file in fileList:
                    test = open(file, 'r')
                    test.close()

            except IOError:
                windir = dsz.path.windows.GetSystemPaths()[0]
                cmd = 'get ' + windir + '\\security\\templates\\policies\\gpt*'
                status, id = dsz.cmd.RunEx(cmd, dsz.RUN_FLAG_RECORD)
                if status == 0:
                    dsz.ui.Echo('Warning: Could not get domain security settings log in: ' + windir + '\\security\\templates\\policies', dsz.WARNING)
                getIddict = dict()
                filestarts = dsz.cmd.data.Get('filestart', dsz.TYPE_OBJECT, id)
                for start in filestarts:
                    path = dsz.cmd.data.ObjectGet(start, 'originalname', dsz.TYPE_STRING)[0]
                    path = path.split('\\')
                    original = path[len(path) - 1]
                    getId = dsz.cmd.data.ObjectGet(start, 'id', dsz.TYPE_STRING)[0]
                    getIddict[getId] = [original]

                filelocalnames = dsz.cmd.data.Get('filelocalname', dsz.TYPE_OBJECT, id)
                for name in filelocalnames:
                    local = dsz.cmd.data.ObjectGet(name, 'localname', dsz.TYPE_STRING)[0]
                    getId = dsz.cmd.data.ObjectGet(name, 'id', dsz.TYPE_STRING)[0]
                    if not getIddict.has_key(getId):
                        dsz.ui.Echo('Error: Missing filestart', dsz.ERROR)
                    else:
                        getIddict[getId].append(local)

                result = getIddict.values()
                result.sort(Reader.fcmp)
                fileList = ';'.join([ GETFILESPATH + name[1] for name in result ])
                dsz.env.Set(ENV_DOMAIN_LOGS, fileList)
                if fileList != '':
                    fileList = fileList.split(';')
                else:
                    fileList = []

        finally:
            return fileList

    @staticmethod
    def fcmp(a, b):
        if a[0] < b[0]:
            return -1
        else:
            if a[0] > b[0]:
                return 1
            return 0

    def processFiles(self, fileList):
        for file in fileList:
            domainLog = open(file, 'r')
            input = domainLog.read()
            domainLog.close()
            lineList = input.decode('utf-16').split('\n')
            for line in lineList:
                line = line.lower().split('=')
                setting = line[0].rstrip().lstrip()
                if len(setting) == 0:
                    continue
                value = ''
                if len(line) == 2:
                    value = line[1].rstrip().lstrip()
                if setting[0] == '[' and setting[len(setting) - 1] == ']':
                    HEADER = setting[1:len(setting) - 1]
                    if not self.headerDict.has_key(HEADER):
                        self.headerDict[HEADER] = dict()
                    continue
                if self.headerDict[HEADER].has_key(setting):
                    continue
                else:
                    if HEADER == REGISTRY_VALUES:
                        setting, value = self.normalize(setting, value)
                    self.headerDict[HEADER][setting] = value

    def normalize(self, setting, value):
        if setting[:8] == 'machine\\':
            setting = setting[8:]
        else:
            failNormalize(setting, value)
            return (
             setting, value)
        if setting.find('!') == -1:
            key = setting.split('\\')[-1]
            path = setting[:setting.find(key) - 1]
            setting = path + '!' + key
        value = value[2:].strip("'").strip('"')
        return (
         setting, value)

    def failNormalize(self, setting, value):
        dsz.ui.Echo("Error: Parsing domain log's Registry values", dsz.ERROR)
        dsz.ui.Echo(' key: ' + setting, dsz.ERROR)
        dsz.ui.Echo('Value: ' + value, dsz.ERROR)
        dsz.script.data.Start('Unknown')
        dsz.script.data.Add('registrykey', setting, dsz.TYPE_STRING)
        dsz.script.data.Add('value', value, dsz.TYPE_STRING)

    def get(self, header):
        if self.headerDict.has_key(header):
            return self.headerDict[header].items()
        else:
            return []