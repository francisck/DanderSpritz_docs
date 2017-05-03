# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.lp.alias
import dsz.lp.cmdline
import dsz.lp.mutex
import dsz.path
import dsz.version
import os
import re
import sys
import xml.dom.minidom

def _getNodeText(element):
    txt = ''
    for node in element.childNodes:
        if node.nodeType == node.TEXT_NODE:
            txt = txt + node.data

    return txt


def AddResDirToPath(newDir):
    resDir = GetResourcesDirectory()
    libDir = dsz.path.Normalize('%s/%s/PyScripts/Lib' % (resDir, newDir), dsz.version.checks.IsWindows(dsz.script.Env['local_address']))
    testLibDir = dsz.path.Normalize('%s/%s/PyTestScripts/Lib' % (resDir, newDir), dsz.version.checks.IsWindows(dsz.script.Env['local_address']))
    sys.path.append(libDir)
    sys.path.append(testLibDir)


def GetDirectory(type):
    envName = '_lpDir_%s' % type
    if dsz.env.Check(envName):
        return dsz.env.Get(envName)
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not dsz.cmd.Run('lpdirectory -%s' % type, dsz.RUN_FLAG_RECORD):
        raise RuntimeError, 'Command failed'
    dir = dsz.cmd.data.Get('DirectoryItem::Dir', dsz.TYPE_STRING)
    dsz.env.Set(envName, dir[0])
    return dir[0]


def GetLogsDirectory():
    if dsz.env.Check('_LOGPATH'):
        return dsz.env.Get('_LOGPATH')
    else:
        return GetDirectory('logs')


def GetProjectDirectories():
    resDir = GetResourcesDirectory()
    res = dsz.env.Get('_RES_DIRS')
    parts = re.split(';', res)
    dirs = list()
    if parts != None:
        for part in parts:
            fullDir = dsz.path.Normalize('%s/%s' % (resDir, part), dsz.version.checks.IsWindows(dsz.script.Env['local_address']))
            dirs.append(fullDir)

    return dirs


def GetResourceName(subdir):
    resDir = dsz.lp.GetResourcesDirectory()
    xmlPath = '%s/%s/Names.xml' % (resDir, subdir)
    if dsz.script.IsLocal():
        elemName = 'Local'
    else:
        elemName = 'Remote'
    dom1 = xml.dom.minidom.parse(xmlPath)
    nodelist = dom1.getElementsByTagName(elemName)
    return _getNodeText(nodelist[0])


def GetResourcesDirectory():
    return GetDirectory('resources')


def RecordToolUse(name, version, usage='', status='', comment='', location=''):
    if name == '':
        dsz.ui.Echo('* No name given -- cannot record tool use', dsz.ERROR)
        return False
    usedToolDir = 'UsedTools'
    fixedName = re.sub(' ', '_', name)
    fixedName = re.sub('\\\\', '_', fixedName)
    fixedName = re.sub('/', '_', fixedName)
    fixedName = re.sub(':', '_', fixedName)
    fixedName = re.sub('\\*', '_', fixedName)
    fixedName = re.sub('"', '_', fixedName)
    fixedName = re.sub('<', '_', fixedName)
    fixedName = re.sub('>', '_', fixedName)
    fixedName = re.sub('\\|', '_', fixedName)
    filename = '%s_%s.xml' % (fixedName, dsz.Timestamp())
    try:
        logDir = GetLogsDirectory()
    except:
        dsz.ui.Echo('* Failed to get logs directory', dsz.ERROR)
        return False

    try:
        os.mkdir('%s/%s' % (logDir, usedToolDir))
    except:
        pass

    xmlName = name
    xmlName = re.sub('&', '&amp;', xmlName)
    xmlName = re.sub('<', '&lt;', xmlName)
    xmlName = re.sub('>', '&gt;', xmlName)
    xmlVersion = version
    xmlVersion = re.sub('&', '&amp;', xmlVersion)
    xmlVersion = re.sub('<', '&lt;', xmlVersion)
    xmlVersion = re.sub('>', '&gt;', xmlVersion)
    xmlUsage = ''
    if len(usage) > 0:
        xmlUsage = usage
        xmlUsage = re.sub('&', '&amp;', xmlUsage)
        xmlUsage = re.sub('<', '&lt;', xmlUsage)
        xmlUsage = re.sub('>', '&gt;', xmlUsage)
    xmlStatus = ''
    if len(status) > 0:
        xmlStatus = status
        xmlStatus = re.sub('&', '&amp;', xmlStatus)
        xmlStatus = re.sub('<', '&lt;', xmlStatus)
        xmlStatus = re.sub('>', '&gt;', xmlStatus)
    xmlLocation = ''
    if len(location) > 0:
        xmlLocation = location
        xmlLocation = re.sub('&', '&amp;', xmlLocation)
        xmlLocation = re.sub('<', '&lt;', xmlLocation)
        xmlLocation = re.sub('>', '&gt;', xmlLocation)
    xmlComment = ''
    if len(comment) > 0:
        xmlComment = comment
        xmlComment = re.sub('&', '&amp;', xmlComment)
        xmlComment = re.sub('<', '&lt;', xmlComment)
        xmlComment = re.sub('>', '&gt;', xmlComment)
    try:
        f = open('%s/%s/%s' % (logDir, usedToolDir, filename), 'wb')
        try:
            f.write('\xef\xbb\xbf')
            f.write('<?xml version="1.0" ?>\n')
            f.write('<UsedTool>\n')
            f.write('  <Name>%s</Name>\n' % xmlName)
            f.write('  <Version>%s</Version>\n' % xmlVersion)
            if len(xmlUsage) > 0:
                f.write('  <Usage>%s</Usage>\n' % xmlUsage)
            if len(xmlStatus) > 0:
                f.write('  <ToolStatus>%s</ToolStatus>\n' % xmlStatus)
            if len(xmlLocation) > 0:
                f.write('  <ToolLocation>%s</ToolLocation>\n' % xmlLocation)
            if len(xmlComment) > 0:
                f.write('  <ToolComments>%s</ToolComments>\n' % xmlComment)
            f.write('</UsedTool>\n')
        finally:
            f.close()

    except:
        dsz.ui.Echo('* Failed to write tool use information', dsz.ERROR)
        return False

    return True