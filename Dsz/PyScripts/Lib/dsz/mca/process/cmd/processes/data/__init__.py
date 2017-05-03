# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import _dsz
import dsz
import dsz.data
import dsz.lp
import mcl.tasking
import re
import sys
import Queue
import xml
import xml.sax
import xml.sax.handler
InitialList = 1
StartList = 2
StopList = 3
Type_IPv4 = 'IPv4'
Type_IPv6 = 'IPv6'

class Processes(dsz.data.TaskReader):

    def __init__(self, cmd=None, id=None):
        dsz.data.TaskReader.__init__(self, cmd, id)
        self.__currentList = None
        self.__currentItem = None
        self.StartProcessListItem = FilteredIterator(self, ProcessList, StartList)
        self.StopProcessListItem = FilteredIterator(self, ProcessList, StopList)
        self.InitialProcessListItem = None
        for item in self:
            if self.InitialProcessListItem != None:
                break

        return

    def startElement(self, name, attrs):
        dsz.data.TaskReader.startElement(self, name, attrs)
        self.__currentText = None
        if name == 'Initial':
            temp = ProcessList(InitialList, attrs['lptimestamp'])
            self.InitialProcessListItem = temp
            self.__currentList = temp
            self.currentItems.put(temp)
        elif name == 'Started':
            temp = ProcessList(StartList, attrs['lptimestamp'])
            self.__currentList = temp
            self.currentItems.put(temp)
        elif name == 'Stopped':
            temp = ProcessList(StopList, attrs['lptimestamp'])
            self.__currentList = temp
            self.currentItems.put(temp)
        elif name == 'Process':
            temp = Process(attrs)
            self.__currentItem = temp
            self.__currentList.ProcessItem.append(temp)
        elif name == 'CreateTime':
            self.__currentType = attrs['type']
            try:
                self.__currentTypeValue = int(attrs['typeValue'])
            except:
                self.__currentTypeValue = 0

        elif name == 'CpuTime':
            self.__currentType = attrs['type']
        elif name == 'Is64Bit':
            self.__currentItem.Is64Bit = True
        return

    def endElement(self, name):
        dsz.data.TaskReader.endElement(self, name)
        if name == 'Name':
            self.__currentItem.Name = self.__currentText
        elif name == 'ExecutablePath':
            self.__currentItem.Path = self.__currentText
        elif name == 'Description':
            self.__currentItem.Description = self.__currentText
        elif name == 'CreateTime':
            temp = dsz.data.DataBean()
            self.__currentItem.Created = temp
            temp.TypeValue = self.__currentTypeValue
            temp.Type = self.__currentType
            items = self.__currentText.split('T')
            temp.Date = items[0]
            items = items[1].split('.')
            temp.Time = items[0]
            try:
                temp.Nanoseconds = items[1]
            except:
                temp.Nanoseconds = 0

        elif name == 'CpuTime':
            items = re.findall('\\d+', self.__currentText)
            temp = dsz.data.DataBean()
            self.__currentItem.CpuTime = temp
            temp.Days = int(items[0], 10)
            temp.Hours = int(items[1], 10)
            temp.Minutes = int(items[2], 10)
            temp.Seconds = int(items[3], 10)
            temp.Nanoseconds = int(items[4], 10)
        self.__currentText = None
        return

    def characters(self, content):
        dsz.data.TaskReader.characters(self, content)
        content = ''.join(content.encode('utf-8'))
        if self.__currentText == None:
            self.__currentText = content
        else:
            self.__currentText += content
        return

    def Display(self):
        dsz.ui.Echo('           PID          PPID        CREATED           CPU TIME        USER')
        dsz.ui.Echo('-------------------------------------------------------------------------------------')
        for item in self:
            if isinstance(item, ProcessList):
                item.Display()


class ProcessList(dsz.data.DataBean):

    def __init__(self, listType, timestamp):
        self.ListType = listType
        self.Timestamp = timestamp
        self.ProcessItem = list()

    def Display(self):
        prefix = ' '
        if self.ListType == StartList:
            prefix = '+'
        elif self.ListType == StopList:
            prefix = '-'
        for procItem in self.ProcessItem:
            procItem.DisplayFunction(prefix)


class Process(dsz.data.DataBean):

    def __init__(self, attrs):
        self.Is64Bit = False
        self.Description = None
        self.Name = None
        self.Path = None
        self.Created = None
        self.CpuTime = None
        try:
            self.Id = int(attrs['id'])
        except:
            self.Id = None

        try:
            self.ParentId = int(attrs['parent'])
        except:
            self.ParentId = None

        try:
            self.Display = attrs['display']
        except:
            self.Display = None

        try:
            self.User = attrs['user']
        except:
            self.User = None

        return

    def DisplayFunction(self, prefix=' '):
        try:
            time = '%s %s' % (self.Created.Date, self.Created.Time)
        except:
            time = ''

        try:
            cpuTime = '%4d.%02d:%02d:%02d' % (self.CpuTime.Days, self.CpuTime.Hours, self.CpuTime.Minutes, self.CpuTime.Seconds)
        except:
            cpuTime = '0.00:00:00'

        if self.User == None:
            user = ''
        else:
            user = self.User
        if self.Path == None:
            path = ''
        else:
            path = self.Path
        if self.Name == None:
            name = ''
        else:
            name = self.Name
        if self.Id == 0 and (self.Name == None or len(self.Name) == 0):
            procString = 'System Idle Process'
        elif self.Path == None or len(self.Path) == 0:
            procString = '%s' % name
        elif '\\' in path:
            procString = '%s\\%s' % (path, name)
        else:
            procString = '%s/%s' % (path, name)
        if self.Is64Bit:
            procString = '%s (64-bit)' % procString
        dsz.ui.Echo('%s %12d%12d     %s%s     %s' % (prefix, self.Id, self.ParentId, time, cpuTime, user))
        dsz.ui.Echo('  %s' % procString)
        dsz.ui.Echo('      -------------------------------------------------------------------------------')
        return


class FilteredIterator(dsz.data.IteratorBean):

    def __init__(self, item, iterType, listType):
        dsz.data.IteratorBean.__init__(self, item, iterType)
        self.listType = listType

    def evaluate(self, ret):
        return ret.ListType == self.listType


dsz.data.RegisterCommand('Processes', Processes, True)
PROCESSES = Processes
processes = Processes