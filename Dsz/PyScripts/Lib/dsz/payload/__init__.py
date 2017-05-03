# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.lp
import dsz.path
import glob
import os
import re
import shutil
import xml.dom.minidom

class PayloadInfo:

    def __init__(self):
        self.name = []
        self.shortName = []
        self.description = []
        self.arch = []
        self.os = []
        self.binType = []
        self.type = []
        self.baseFile = []
        self.extraInfo = {}


def CreateConfigDir(info):
    logDir = dsz.lp.GetLogsDirectory()
    resDir = dsz.lp.GetResourcesDirectory()
    try:
        os.mkdir('%s/Payloads' % logDir)
    except:
        pass

    dirPath = '%s/Payloads/%s_%s' % (logDir, info.name[0], dsz.Timestamp())
    os.mkdir(dirPath)
    dir, file = dsz.path.Split(info.baseFile[0])
    shutil.copy('%s/%s/%s' % (resDir, info.shortName[0], info.baseFile[0]), '%s/%s.base' % (dirPath, file))
    return (
     dirPath, file)


def GetConfigured(params, callbackFunc=None):
    logDir = dsz.lp.GetLogsDirectory()
    allDirs = glob.glob('%s/Payloads/*' % logDir)
    dirs = list()
    for dir in allDirs:
        if len(glob.glob('%s/payload_info.xml' % dir)) == 0:
            continue
        if params.has_key('arch'):
            if not _checkInfo(dir, 'Arch', params['arch'][0]):
                continue
        if params.has_key('os'):
            if not _checkInfo(dir, 'Os', params['os'][0]):
                continue
        if params.has_key('type'):
            if not _checkInfo(dir, 'Type', params['type'][0]):
                continue
        if params.has_key('bintype'):
            if not _checkInfo(dir, 'BinType', params['bintype'][0]):
                continue
        if params.has_key('extra'):
            extraInfo = re.split('=', params['extra'][0], 1)
            if len(extraInfo) == 2:
                if not _checkInfo(dir, extraInfo[0], extraInfo[1]):
                    continue
        if callbackFunc != None:
            if not callbackFunc(params, dir):
                continue
        dirs.append(dir)

    return dirs


def GetInfo(payloadDir):
    info = PayloadInfo()
    info.arch.append(_getElement(payloadDir, 'Arch'))
    info.os.append(_getElement(payloadDir, 'Os'))
    info.description.append(_getElement(payloadDir, 'Description'))
    info.name.append(_getElement(payloadDir, 'Name'))
    info.shortName.append(_getElement(payloadDir, 'ShortName'))
    info.type.append(_getElement(payloadDir, 'Type'))
    info.binType.append(_getElement(payloadDir, 'BinType'))
    info.baseFile.append(_getElement(payloadDir, 'File'))
    return info


def GetPossible():
    projects = list()
    dataPaths = dsz.lp.GetProjectDirectories()
    for path in dataPaths:
        if len(glob.glob('%s/PyScripts/Payload/_Prep.py' % path)):
            dir, file = dsz.path.Split(path)
            projects.append(file)

    return projects


def GetPossibleChoice():
    projects = GetPossible()
    dsz.ui.Echo('Possible payloads:')
    dsz.ui.Echo('    0) - Quit')
    i = 0
    while i < len(projects):
        choice = i + 1
        dsz.ui.Echo('    %2u) - %s' % (choice, projects[i]))
        i = i + 1

    while True:
        choice = dsz.ui.GetInt('Pick the payload type')
        if choice == 0:
            return ''
        if choice < 0 or choice > len(projects):
            dsz.ui.Echo('* Invalid choice', dsz.ERROR)
        else:
            return projects[choice - 1]


def IsValid(params, info, index):
    if params.has_key('arch') and len(info.arch) > index:
        if params['arch'][0].lower() != info.arch[index].lower():
            return False
    if params.has_key('os') and len(info.os) > index:
        if params['os'][0].lower() != info.os[index].lower():
            return False
    if params.has_key('bintype') and len(info.binType) > index:
        if params['bintype'][0].lower() != info.binType[index].lower():
            return False
    if params.has_key('type') and len(info.type) > index:
        if params['type'][0].lower() != info.type[index].lower():
            return False
    if params.has_key('extra'):
        extraInfo = re.split('=', params['extra'][0], 1)
        if len(extraInfo) == 2:
            if not info.extraInfo.has_key(extraInfo[0]) or len(info.extraInfo[extraInfo[0]]) <= index or extraInfo[1].lower() != info.extraInfo[extraInfo[0]][index].lower():
                return False
    return True


def PickForPrep(project, params):
    resDir = dsz.lp.GetResourcesDirectory()
    allFiles = glob.glob('%s/%s/Payloads/*/payload_*.xml' % (resDir, project))
    if len(allFiles) == 0:
        dsz.ui.Echo('* Failed to find any payloads for ' % project, dsz.ERROR)
        return None
    else:
        info = PayloadInfo()
        valid = list()
        onIndex = 0
        for f in allFiles:
            try:
                dom1 = xml.dom.minidom.parse(f)
                nodelist = dom1.getElementsByTagName('Payload')
                for node in nodelist:
                    if _getPayloadInfo(node, info, onIndex):
                        if IsValid(params, info, onIndex):
                            valid.append(True)
                            onIndex = onIndex + 1
                        else:
                            keys = info.extraInfo.keys()
                            for key in keys:
                                if len(info.extraInfo[key]) > onIndex and info.extraInfo[key][onIndex] != '':
                                    del info.extraInfo[key][onIndex]

            except:
                dsz.ui.Echo('Exception parsing %s' % f, dsz.WARNING)

        dsz.ui.Echo('Possible payloads:')
        dsz.ui.Echo('     0) - Quit')
        i = 0
        while i < len(valid):
            dsz.ui.Echo('    %2u) - %s (%s-%s %s %s)' % (i + 1, info.description[i], info.arch[i], info.os[i], info.type[i], info.binType[i]))
            i = i + 1

        while True:
            choice = dsz.ui.GetInt('Pick the payload type')
            if choice == 0:
                return None
            if choice < 0 or choice > len(valid):
                dsz.ui.Echo('* Invalid choice', dsz.ERROR)
            else:
                payloadInfo = PayloadInfo()
                payloadInfo.name.append(info.name[choice - 1])
                payloadInfo.shortName.append(info.shortName[choice - 1])
                payloadInfo.description.append(info.description[choice - 1])
                payloadInfo.arch.append(info.arch[choice - 1])
                payloadInfo.os.append(info.os[choice - 1])
                payloadInfo.type.append(info.type[choice - 1])
                payloadInfo.binType.append(info.binType[choice - 1])
                payloadInfo.baseFile.append(info.baseFile[choice - 1])
                keys = info.extraInfo.keys()
                for key in keys:
                    if len(info.extraInfo[key]) > choice - 1 and info.extraInfo[key][choice - 1] != '':
                        payloadInfo.extraInfo[key] = list()
                        payloadInfo.extraInfo[key].append(info.extraInfo[key][choice - 1])

                return payloadInfo

        return None


def StoreInfo(payloadInfo, path, finalBinary):
    infoLines = list()
    infoLines.append("<?xml version='1.0' encoding='UTF-8' ?>\n")
    infoLines.append('<Payload>\n')
    infoLines.append('    <Description>%s</Description>\n' % payloadInfo.description[0])
    infoLines.append('    <Name>%s</Name>\n' % payloadInfo.name[0])
    infoLines.append('    <ShortName>%s</ShortName>\n' % payloadInfo.shortName[0])
    infoLines.append('    <Arch>%s</Arch>\n' % payloadInfo.arch[0])
    infoLines.append('    <Os>%s</Os>\n' % payloadInfo.os[0])
    infoLines.append('    <BinType>%s</BinType>\n' % payloadInfo.binType[0])
    infoLines.append('    <Type>%s</Type>\n' % payloadInfo.type[0])
    infoLines.append('    <File>%s</File>\n' % finalBinary)
    for key in payloadInfo.extraInfo.keys():
        infoLines.append('    <%s>%s</%s>\n' % (key, payloadInfo.extraInfo[key][0], key))

    infoLines.append('</Payload>\n')
    try:
        f = open('%s/payload_info.xml' % path, 'w')
        try:
            f.writelines(infoLines)
        finally:
            f.close()

    except:
        dsz.ui.Echo('* Failed to write configuration file', dsz.ERROR)
        return ''

    return '%s/payload_info.xml' % path


def _checkInfo(dir, name, value):
    try:
        txt = _getElement(dir, name)
        if txt.lower() == value.lower():
            return True
    except:
        pass

    return False


def _getElement(dir, name):
    dom1 = xml.dom.minidom.parse('%s/payload_info.xml' % dir)
    element = dom1.getElementsByTagName(name)
    return _getNodeText(element[0])


def _getNodeText(element):
    txt = ''
    for node in element.childNodes:
        if node.nodeType == node.TEXT_NODE:
            txt = txt + node.data

    return txt


def _getPayloadInfo(payloadNode, info, index):
    txt = _getPayloadNodeInfo(payloadNode, 'Name')
    while len(info.name) < index + 1:
        info.name.append('')

    info.name[index] = txt
    txt = _getPayloadNodeInfo(payloadNode, 'Description')
    while len(info.description) < index + 1:
        info.description.append('')

    info.description[index] = txt
    txt = _getPayloadNodeInfo(payloadNode, 'ShortName')
    while len(info.shortName) < index + 1:
        info.shortName.append('')

    info.shortName[index] = txt
    txt = _getPayloadNodeInfo(payloadNode, 'Arch')
    while len(info.arch) < index + 1:
        info.arch.append('')

    info.arch[index] = txt
    txt = _getPayloadNodeInfo(payloadNode, 'Os')
    while len(info.os) < index + 1:
        info.os.append('')

    info.os[index] = txt
    txt = _getPayloadNodeInfo(payloadNode, 'BinType')
    while len(info.binType) < index + 1:
        info.binType.append('')

    info.binType[index] = txt
    txt = _getPayloadNodeInfo(payloadNode, 'Type')
    while len(info.type) < index + 1:
        info.type.append('')

    info.type[index] = txt
    txt = _getPayloadNodeInfo(payloadNode, 'BaseFile')
    while len(info.baseFile) < index + 1:
        info.baseFile.append('')

    info.baseFile[index] = txt
    try:
        extraNodeList = payloadNode.getElementsByTagName('Extra')
        for extra in extraNodeList:
            txt = _getNodeText(extra)
            key = extra.getAttribute('name')
            if key != '':
                if not info.extraInfo.has_key(key):
                    info.extraInfo[key] = list()
                while len(info.extraInfo[key]) < index + 1:
                    info.extraInfo[key].append('')

                info.extraInfo[key][index] = txt

    except:
        dsz.ui.Echo("Exception parsing 'Extra' nodes in payload", dsz.WARNING)

    return True


def _getPayloadNodeInfo(topNode, name):
    try:
        element = topNode.getElementsByTagName(name)
        return _getNodeText(element[0])
    except:
        return ''