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
Directory = 'Directory'
AccessDenied = 'Access Denied'
ReparsePoint = 'Reparse Point'
Compressed = 'Compressed'
Archive = 'Archive'
Encrypted = 'Encrypted'
Hidden = 'Hidden'
Offline = 'Offline'
ReadOnly = 'Read-Only'
System = 'System'
Temporary = 'Temporary'
Virtual = 'Virtual'
NotIndexed = 'NotIndexed'
Device = 'Device'
SymbolicLink = 'Symbolic Link'
BlockSpecialFile = 'Block Special File'
CharacterSpecialFile = 'Character Special File'
NamedPipe = 'Named Pipe'
AFUnixFamilySocket = 'AF Unix Family Socket'
_AttributeDisplay = [
 (
  Archive, 'A'),
 (
  Compressed, 'C'),
 (
  Encrypted, 'E'),
 (
  Hidden, 'H'),
 (
  Offline, 'O'),
 (
  ReadOnly, 'R'),
 (
  System, 'S'),
 (
  Temporary, 'T')]
_AttributeMap = [
 (
  'FileAttributeDirectory', Directory),
 (
  'AccessDenied', AccessDenied),
 (
  'FileAttributeReparsePoint', ReparsePoint),
 (
  'FileAttributeCompressed', Compressed),
 (
  'FileAttributeArchive', Archive),
 (
  'FileAttributeEncrypted', Encrypted),
 (
  'FileAttributeHidden', Hidden),
 (
  'FileAttributeOffline', Offline),
 (
  'FileAttributeReadonly', ReadOnly),
 (
  'FileAttributeSystem', System),
 (
  'FileAttributeTemporary', Temporary),
 (
  'FileAttributeVirtual', Virtual),
 (
  'FileAttributeNotIndexed', NotIndexed),
 (
  'FileAttributeDevice', Device),
 (
  'FileAttributeSymbolicLink', SymbolicLink),
 (
  'FileAttributeBlockSpecialFile', BlockSpecialFile),
 (
  'FileAttributeCharacterSpecialFile', CharacterSpecialFile),
 (
  'FileAttributeNamedPipeFile', NamedPipe),
 (
  'FileAttributeAFUnixFamilySocket', AFUnixFamilySocket)]

class Dir(dsz.data.TaskReader):

    def __init__(self, cmd=None, id=None):
        dsz.data.TaskReader.__init__(self, cmd, id)
        self.__currentDir = None
        self.__currentFile = None
        self.__currentText = None
        self.__timestamp = None
        self.DirItem = dsz.data.IteratorBean(self, DirItem)
        return

    def startElement(self, name, attrs):
        dsz.data.TaskReader.startElement(self, name, attrs)
        self.__currentText = None
        if name == 'Directories':
            self.__timestamp = attrs['lptimestamp']
        if name == 'Directory':
            try:
                allowed = bool(self._GetValue(attrs, 'denied'))
            except:
                allowed = True

            dir = DirItem(self.__timestamp, self._GetValue(attrs, 'path'), allowed)
            self.__currentDir = dir
            self.currentItems.put(dir)
        elif name == 'File':
            file = FileItem(self._GetValue(attrs, 'name'))
            file.Size = int(self._GetValue(attrs, 'size'))
            file.AltName = self._GetValue(attrs, 'shortName')
            file.Path = self.__currentDir.Path
            self.__currentFile = file
            self.__currentDir.FileItem.append(file)
        elif name == 'Hash':
            self.__currentHashSize = int(self._GetValue(attrs, 'size'))
            self.__currentHashType = self._GetValue(attrs, 'type')
        elif name == 'Modified' or name == 'Accessed' or name == 'Created':
            self.__currentTimeType = self._GetValue(attrs, 'type')
        else:
            for item, flag in _AttributeMap:
                if name == item:
                    self.__currentFile.Attributes.SetFlag(flag)

        return

    def endElement(self, name):
        dsz.data.TaskReader.endElement(self, name)
        if name == 'Hash':
            self.__currentFile.Hash.append(Hash(self.__currentHashSize, self.__currentHashType, self.__currentText))
        if name == 'Modified' or name == 'Accessed' or name == 'Created':
            self.__currentFile.FileTimes.set(name, self.__currentTimeType, self.__currentText)
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


class DirItem(dsz.data.DataBean):

    def __init__(self, timestamp, path, allowed):
        self.Timestamp = timestamp
        self.Path = path
        self.Denied = allowed
        self.FileItem = list()

    def __iter__(self):
        return self.FileItem.__iter__()

    def __getitem__(self, item):
        return self.FileItem[item]

    def Display(self, timeType='Modified'):
        mcl.tasking.Echo('Directory : %s' % self.Path)
        mcl.tasking.Echo('')
        if not self.Allowed:
            mcl.tasking.Echo('    ACCESS_DENIED')
            return
        for file in self.FileItem:
            file.Display(timeType)


class Attributes(dsz.data.DataBean):

    def __init__(self):
        for ignore, str in _AttributeMap:
            self.__dict__[str] = False

    def SetFlag(self, str):
        self.__dict__[str] = True

    def GetFlag(self, str):
        if str in self.__dict__:
            return self.__dict__[str]
        return False


class FileItem(dsz.data.DataBean):

    def __init__(self, name):
        self.Name = name
        self.AltName = None
        self.Size = None
        self.Hash = list()
        self.FileTimes = FileTimes()
        self.Attributes = Attributes()
        return

    def Display(self, timeType='Modified'):
        typeString = '%14d' % self.Size
        if Directory in self.Attributes:
            typeString = '<DIR>         '
        if ReparsePoint in self.Attributes:
            typeString = '<JUNCTION>    '
        attrString = ''
        for Flag, Ch in _AttributeDisplay:
            if Flag in self.Attributes:
                attrString += Ch
            else:
                attrString += ' '

        suffix = ''
        mcl.tasking.Echo('%s %s %8s%s %-12s %s %s' % (
         self.FileTimes.get(timeType).DateString,
         self.FileTimes.get(timeType).TimeString,
         ''.join(attrString),
         typeString,
         self.AltName,
         self.Name,
         suffix))
        for hash in self.Hash:
            hash.Display()


class FileTimes(dsz.data.DataBean):

    def __init__(self):
        pass

    def set(self, name, type, text):
        self.__dict__[name] = dsz.data.Time(type, text)

    def get(self, name='Modified'):
        return self.__dict__[name]


class Hash(dsz.data.DataBean):

    def __init__(self, size, type, value):
        self.Size = size
        self.Type = type
        self.Value = value

    def Display(self):
        mcl.tasking.Echo('%8s: %s' % (self.Type, self.Value))


dsz.data.RegisterCommand('Dir', Dir, True)
DIR = Dir
dir = Dir