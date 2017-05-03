# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import _dsz
import dsz
import dsz.cmd
import dsz.data
import dsz.lp
import mcl.tasking
import mcl.tasking.env
import os
import sys
import Queue
import xml
import xml.sax
import xml.sax.handler
CommandDataMapSimple = dict()
CommandDataMapComplex = dict()

def RegisterCommand(Name, obj, stopVariables=False):
    if stopVariables:
        if Name.lower() not in CommandDataMapComplex:
            CommandDataMapComplex[Name.lower()] = obj
    elif Name.lower() not in CommandDataMapSimple:
        CommandDataMapSimple[Name.lower()] = obj


def LoadCommand(cmdId):
    _GatherImports()
    retVal = None
    commandName = dsz.cmd.data.Get('CommandMetaData::Name', dsz.TYPE_STRING, cmdId)[0].lower()
    if commandName in CommandDataMapComplex:
        commandHandler = CommandDataMapComplex[commandName]
        return commandHandler(id=cmdId)
    else:
        if commandName in CommandDataMapSimple:
            commandHandler = CommandDataMapSimple[commandName]
        else:
            commandHandler = DefaultTask
        dsz.cmd.Run('generatedata -id %d' % cmdId, dsz.RUN_FLAG_RECORD)
        retVal = commandHandler()
        retVal.Id = cmdId
        retVal.LoadMetaData()
        return retVal


def StartCommand(cmd):
    dsz.cmd.Run(cmd)
    return LoadCommand(dsz.cmd.LastId())


def CreateCommand(cmdName, cmdStr):
    return StartCommand(cmdStr)


class CommandFailed(Exception):

    def __init__(self):
        Exception.__init__(self, 'Command Failed To Start')


class CommandNotFound(Exception):

    def __init__(self):
        Exception.__init__(self, 'CommandName Not Found')


class DataBean(object):

    def __init__(self):
        pass

    def Dump(self, space=''):
        beans = list()
        for key in self.__dict__:
            value = self.__dict__[key]
            if isinstance(value, DataBean):
                if self._shouldDisplay(key):
                    beans.append((key, value))
            else:
                dsz.ui.Echo('%s%s => %s' % (space, key, value))

        for key, value in beans:
            dsz.ui.Echo('%s%s' % (space, key))
            if not hasattr(value, '__call__'):
                value.Dump('%s | ' % space)
            else:
                dsz.ui.Echo('    (Function)')

    def __getattr__(self, name):
        for key in self.__dict__.keys():
            if name.lower() == key.lower():
                return self.__dict__[key]

        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        for key in self.__dict__.keys():
            if name.lower() == key.lower():
                self.__dict__[key] = value
                return value

        self.__dict__[name] = value
        return value

    def _shouldDisplay(self, name):
        return True


class IteratorBean(DataBean):

    def __init__(self, item, iterType):
        DataBean.__init__(self)
        self.item = item
        self.iterType = iterType

    def __iter__(self):
        self.iter = self.item.__iter__()
        return self

    def next(self):
        while 1:
            if True:
                ret = self.iter.next()
                return ret == None and None
            if type(ret) != self.iterType:
                continue
            if not self.evaluate(ret):
                continue
            return ret

        return None

    def evaluate(self, ret):
        return True

    def __len__(self):
        count = 0
        for x in self:
            count = count + 1

        return count

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('Index must be an integer')
        if key < 0:
            raise IndexError('Reverse indexing not allowed')
        init = key
        for x in self:
            if key == 0:
                return x
            key = key - 1

        raise IndexError('Index %d too large' % init)

    def _shouldDisplay(self, name):
        if name == 'item':
            return False
        return DataBean._shouldDisplay(self, name)


class TaskingInfo(DataBean):

    def __init__(self):
        DataBean.__init__(self)
        self.Recursive = False
        self.Local = None
        self.SearchMask = None
        self.SearchPath = None
        self.SearchParam = None
        self.SearchMaxMatches = None
        self.TaskType = None
        self.SearchBeforeDate = None
        self.SearchAfterDate = None
        return

    def Display(self):
        mcl.tasking.Echo('Tasking:')
        for k in self.__dict__.keys():
            mcl.tasking.Echo('  %s => %s' % (k, self.__dict__[k]))


class Time(DataBean):

    def __init__(self, type, text):
        DataBean.__init__(self)
        self.Type = type
        self.Time = text
        self.DateString, self.TimeString = text.split('T')
        self.TimeString, self.Nanoseconds = self.TimeString.split('.')


class BaseTask(DataBean):

    def __init__(self, id):
        DataBean.__init__(self)
        self.Id = id
        self.LoadMetaData()

    def LoadMetaData(self):
        self.Name = dsz.cmd.data.Get('CommandMetaData::Name', dsz.TYPE_STRING, self.Id)[0]
        try:
            self.ScreenLog = dsz.cmd.data.Get('CommandMetaData::ScreenLog', dsz.TYPE_STRING, self.Id)[0]
        except:
            self.ScreenLog = None

        self.ParentId = dsz.cmd.data.Get('CommandMetaData::ParentId', dsz.TYPE_INT, self.Id)[0]
        self.TaskId = dsz.cmd.data.Get('CommandMetaData::TaskId', dsz.TYPE_STRING, self.Id)[0]
        self.Destination = dsz.cmd.data.Get('CommandMetaData::Destination', dsz.TYPE_STRING, self.Id)[0]
        self.Source = dsz.cmd.data.Get('CommandMetaData::Source', dsz.TYPE_STRING, self.Id)[0]
        self.FullCommand = dsz.cmd.data.Get('CommandMetaData::FullCommand', dsz.TYPE_STRING, self.Id)[0]
        try:
            self.Prefix = dsz.cmd.data.Get('CommandMetaData::Prefix', dsz.TYPE_STRING, self.Id)
        except:
            self.Prefix = []

        try:
            self.Argument = dsz.cmd.data.Get('CommandMetaData::Argument', dsz.TYPE_STRING, self.Id)
        except:
            self.Argument = []

        return

    def GetLogs(self):
        return _GetLogs(self.Id)

    def IsRunning(self):
        return _IsAlive(self.Id)

    def GetStatus(self):
        return dsz.cmd.data.Get('CommandMetaData::Status', dsz.TYPE_INT, self.Id)[0]

    def GetBytesSent(self):
        return dsz.cmd.data.Get('CommandMetaData::BytesSent', dsz.TYPE_INT, self.Id)[0]

    def GetBytesReceived(self):
        return dsz.cmd.data.Get('CommandMetaData::BytesReceived', dsz.TYPE_INT, self.Id)[0]

    def GetChildIds(self):
        return dsz.cmd.data.Get('CommandMetaData::Child::Id', dsz.TYPE_INT, self.Id)


class DefaultTask(BaseTask):

    def __init__(self):
        BaseTask.__init__(self, dsz.cmd.LastId())


class Task(BaseTask):

    def __init__(self, cmd=None):
        bFailed = False
        if cmd != None:
            self.cmd = cmd
            if not dsz.cmd.Run(cmd, dsz.RUN_FLAG_RECORD):
                bFailed = True
        BaseTask.__init__(self, dsz.cmd.LastId())
        while _IsAlive(self.Id):
            dsz.Sleep(100)

        self._LoadData()
        return

    def _LoadData(self):
        return True


class TaskReader(BaseTask, xml.sax.handler.ContentHandler):

    def __init__(self, cmd=None, id=None):
        if id == None and cmd == None:
            tempId = dsz.cmd.LastId()
        elif id == None:
            if not dsz.cmd.Run(cmd):
                raise Exception('Command failed')
            tempId = dsz.cmd.LastId()
        else:
            tempId = id
        BaseTask.__init__(self, tempId)
        self.files = list()
        self.__currentText = None
        self.__currentTasking = None
        self.__taskingSubmitted = False
        self.currentIndex = None
        self.currentItems = Queue.Queue()
        self.Tasking = IteratorBean(self, TaskingInfo)
        return

    def __setLogs(self):
        bChanged = False
        files = self.GetLogs()
        if len(files) > len(self.files):
            self.files = files
            bChanged = True
        return bChanged

    def __iter__(self):
        self.currentIndex = None
        self.currentItems = Queue.Queue()
        self.__taskingSubmitted = False
        return self

    def next(self):
        if not self.currentItems.empty():
            return self.currentItems.get()
        else:
            if self.currentIndex == None:
                self.currentIndex = 0
            else:
                self.currentIndex = self.currentIndex + 1
            if self.currentIndex >= len(self.files):
                while self.IsRunning():
                    if dsz.script.CheckStop():
                        raise StopIteration
                    if self.__setLogs():
                        return self.next()
                    dsz.Sleep(5000)

                self.__setLogs()
                if self.currentIndex >= len(self.files):
                    self.currentIndex = None
                    raise StopIteration
            self.__parseFile(self.files[self.currentIndex])
            return self.next()

    def __parseFile(self, dataFile):
        fullFile = '%s/%s' % (_GetLogPath(), dataFile)
        try:
            xml.sax.parse(fullFile, self)
        except Exception as e:
            pass

    def _GetValue(self, attributes, key):
        try:
            value = ''.join(attributes.getValue(unicode(key)).encode('utf-8'))
            return value
        except Exception as Err:
            return None

        return None

    def startElement(self, name, attrs):
        self.__currentText = None
        if self.__taskingSubmitted:
            return
        else:
            if not self.__taskingSubmitted and name == 'TaskingInfo':
                self.__currentTasking = TaskingInfo()
            elif name == 'CommandTarget':
                if self._GetValue(attrs, 'type').lower() == 'local':
                    self.__currentTasking.Location = 'localhost'
                    self.__currentTasking.Local = True
                else:
                    self.__currentTasking.Local = False
            elif name == 'SearchAfterDate' or name == 'SearchBeforeDate':
                self.__currentTimeType = self._GetValue(attrs, 'type')
            return

    def endElement(self, name):
        if self.__taskingSubmitted or self.__currentTasking == None:
            self.__currentText = None
            return
        else:
            if name == 'TaskingInfo':
                self.__taskingSubmitted = True
                self.currentItems.put(self.__currentTasking)
            elif name == 'SearchRecursive':
                self.__currentTasking.Recursive = True
            elif name == 'CommandTarget':
                if not self.__currentTasking.Local:
                    self.__currentTasking.Location = self.__currentText
            elif name == 'SearchMask':
                self.__currentTasking.SearchMask = self.__currentText
            elif name == 'SearchPath':
                self.__currentTasking.SearchPath = self.__currentText
            elif name == 'SearchParam':
                self.__currentTasking.SearchParam = self.__currentText
            elif name == 'SearchMaxMatches':
                self.__currentTasking.SearchMaxMatches = int(self.__currentText)
            elif name == 'TaskType':
                self.__currentTasking.TaskType = self.__currentText
            elif name == 'SearchAfterDate':
                self.__currentTasking.SearchAfterDate = Time(self.__currentTimeType, self.__currentText)
            elif name == 'SearchBeforeDate':
                self.__currentTasking.SearchBeforeDate = Time(self.__currentTimeType, self.__currentText)
            self.__currentText = None
            return

    def characters(self, content):
        content = ''.join(content.encode('utf-8'))
        if self.__currentText == None:
            self.__currentText = content
        else:
            self.__currentText += content
        return


def _GetLogs(id):
    return dsz.cmd.data.Get('CommandMetaData::XmlLog', dsz.TYPE_STRING, id)


def _IsAlive(id):
    return dsz.cmd.data.Get('CommandMetaData::IsRunning', dsz.TYPE_BOOL, id)[0]


def _GetLogPath():
    return dsz.env.Get('_LOGPATH', addr='')


_bGathered = False

def _GatherImports():
    global _bGathered
    if _bGathered:
        return
    _bGathered = True
    _ResourceDir = dsz.env.Get('_LPDIR_RESOURCES')
    _Resources = dsz.env.Get('_RES_DIRS').split(';')
    for _Res in _Resources:
        paths = sys.path
        try:
            packageDir = dsz.path.Normalize('%s/%s/PyScripts/Lib/' % (_ResourceDir, _Res))
            sys.path.append(packageDir)
            for subDir in ['mca']:
                try:
                    for package in os.listdir(packageDir):
                        targetDir = dsz.path.Normalize('%s/%s/%s' % (packageDir, package, subDir))
                        try:
                            for grouping in os.listdir(targetDir):
                                groupDir = dsz.path.Normalize('%s/%s/cmd' % (targetDir, grouping))
                                try:
                                    for command in os.listdir(groupDir):
                                        if command == '.svn':
                                            continue
                                        pythonPath = '%s.%s.%s.cmd.%s.data.dsz' % (package, subDir, grouping, command)
                                        try:
                                            __import__(pythonPath)
                                        except AttributeError as AE:
                                            dsz.ui.Echo('Failed to load %s:  %s' % (pythonPath, AE), dsz.ERROR)
                                        except ImportError as IE:
                                            pass

                                except WindowsError as WE:
                                    pass

                        except WindowsError as WE:
                            pass

                except Exception as E:
                    pass

            for subDir in ['mcf']:
                try:
                    targetDir = dsz.path.Normalize('%s/%s/%s/cmd' % (packageDir, package, subDir))
                    for command in os.listdir(targetDir):
                        if command == '.svn':
                            continue
                        pythonPath = '%s.%s.cmd.%s.data.dsz' % (package, subDir, command)
                        try:
                            __import__(pythonPath)
                        except AttributeError as AE:
                            dsz.ui.Echo('Failed to load %s:  %s' % (pythonPath, AE), dsz.ERROR)
                        except ImportError as IE:
                            pass

                except Exception as E:
                    pass

        finally:
            sys.path = paths