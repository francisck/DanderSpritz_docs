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

class NetConnections(dsz.data.TaskReader):

    def __init__(self, cmd=None, id=None):
        dsz.data.TaskReader.__init__(self, cmd, id)
        self.__currentList = None
        self.__currentItem = None
        self.__currentEndPoint = None
        self.__timestamp = None
        self.__currentNamedItem = None
        self.StartConnectionListItem = FilteredIterator(self, ConnectionList, StartList)
        self.StopConnectionListItem = FilteredIterator(self, ConnectionList, StopList)
        self.InitialConnectionListItem = None
        for item in self:
            if self.InitialConnectionListItem != None:
                break

        return

    def startElement(self, name, attrs):
        dsz.data.TaskReader.startElement(self, name, attrs)
        self.__currentText = None
        if name == 'Connections':
            self.__timestamp = attrs['lptimestamp']
        if name == 'Initial':
            temp = ConnectionList(InitialList, self.__timestamp)
            self.InitialConnectionListItem = temp
            self.__currentList = temp
            self.currentItems.put(temp)
        elif name == 'Started':
            temp = ConnectionList(StartList, self.__timestamp)
            self.__currentList = temp
            self.currentItems.put(temp)
        elif name == 'Stopped':
            temp = ConnectionList(StopList, self.__timestamp)
            self.__currentList = temp
            self.currentItems.put(temp)
        elif name == 'Connection':
            temp = ConnectionItem()
            self.__currentItem = temp
            self.__currentList.Connection.append(temp)
            try:
                temp.State = attrs['state']
            except:
                temp.State = None

            try:
                temp.Type = attrs['type']
            except:
                temp.Type = None

            try:
                temp.Valid = attrs['valid'] == 'true'
            except:
                temp.Valid = False

        elif name == 'LocalAddress' or name == 'RemoteAddress':
            temp = EndPoint()
            self.__currentEndPoint = temp
        elif name == 'NamedPipe':
            temp = NamedItem('Pipe')
            self.__currentNamedItem = temp
            self.__currentList.Connection.append(temp)
        elif name == 'MailSlot':
            temp = NamedItem('Mail')
            self.__currentNamedItem = temp
            self.__currentList.Connection.append(temp)
        return

    def endElement(self, name):
        dsz.data.TaskReader.endElement(self, name)
        if name == 'LocalAddress':
            self.__currentItem.Local = self.__currentEndPoint
        elif name == 'RemoteAddress':
            self.__currentItem.Remote = self.__currentEndPoint
        elif name == 'IPv4Address':
            self.__currentEndPoint.IPv4 = self.__currentText
            self.__currentEndPoint.Address = self.__currentText
            self.__currentEndPoint.Type = Type_IPv4
        elif name == 'IPv6Address':
            items = self.__currentText.split('%')
            if len(items) == 3:
                self.__currentText = '%s%%%s' % (items[0], items[2])
            self.__currentEndPoint.IPv6 = self.__currentText
            self.__currentEndPoint.Address = self.__currentText
            self.__currentEndPoint.Type = Type_IPv6
        elif name == 'LocalPort' or name == 'RemotePort':
            self.__currentEndPoint.Port = int(self.__currentText)
            self.__currentEndPoint.Portv4 = int(self.__currentText)
            self.__currentEndPoint.Portv6 = int(self.__currentText)
        elif name == 'Pid':
            self.__currentItem.Pid = int(self.__currentText)
        elif name == 'Name':
            self.__currentNamedItem.Name = self.__currentText
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
        dsz.ui.Echo('  TYPE PROCESS  LOCAL                                REMOTE                                   STATE')
        dsz.ui.Echo('--------------------------------------------------------------------------------------------------------- -')
        for item in self:
            item.Display()


class ConnectionList(dsz.data.DataBean):

    def __init__(self, listType, timestamp):
        self.ListType = listType
        self.Timestamp = timestamp
        self.Connection = list()

    def Display(self):
        prefix = ' '
        if self.ListType == StartList:
            prefix = '+'
        elif self.ListType == StopList:
            prefix = '-'
        for conn in self.Connection:
            conn.Display(prefix)


class ConnectionItem(dsz.data.DataBean):

    def __init__(self):
        self.Pid = None
        self.Local = None
        self.Remote = None
        return

    def Display(self, prefix=''):
        valid = ''
        type = ''
        proc = ''
        local = ''
        remote = ''
        state = ''
        if not self.Valid:
            valid = '*'
        if self.Type != None:
            type = self.Type
        if self.Pid != None:
            proc = '%d' % self.Pid
        if self.Local != None:
            local = self.Local.toString()
        if self.Remote != None:
            remote = self.Remote.toString()
        if self.State != None:
            state = self.State
        dsz.ui.Echo('%s%1s%-4s  %5s    %-35s %-35s      %-14s' % (prefix, valid, type, proc, local, remote, state))
        return


class NamedItem(dsz.data.DataBean):

    def __init__(self, type):
        self.Name = None
        self.Type = type
        return

    def Display(self, prefix=''):
        dsz.ui.Echo('%s%-8s %s' % (prefix, self.Type, self.Name))


class EndPoint(dsz.data.DataBean):

    def __init__(self):
        self.Portv4 = None
        self.IPv4 = None
        self.Portv6 = None
        self.IPv6 = None
        self.Port = None
        self.Address = None
        self.Type = None
        return

    def toString(self):
        if self.Type == Type_IPv4:
            if len(self.Address) == 0:
                return '*:*'
            else:
                return '%s:%d' % (self.Address, self.Port)

        elif self.Type == Type_IPv6:
            if self.Address == '::' and (self.Port == 0 or self.Port == None):
                return '*:*'
            else:
                if self.Port == 0 or self.Port == None:
                    return '[%s]:*' % self.Address
                return '[%s]:%d' % (self.Address, self.Port)

        else:
            return '*:*'
        return


class FilteredIterator(dsz.data.IteratorBean):

    def __init__(self, item, iterType, listType):
        dsz.data.IteratorBean.__init__(self, item, iterType)
        self.listType = listType

    def evaluate(self, ret):
        return ret.ListType == self.listType


dsz.data.RegisterCommand('NetConnections', NetConnections, True)
NETCONNECTIONS = NetConnections
netconnections = NetConnections