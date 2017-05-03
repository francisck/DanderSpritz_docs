# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py


def GetVersion(toolName):
    import dsz.lp
    import glob
    import os.path
    versionFileName = '%s_version.xml' % toolName.lower()
    resPath = os.path.abspath('%s/%s/Version' % (dsz.lp.GetResourcesDirectory(), dsz.script.Env['script_project']))
    versionFiles = glob.glob('%s/*_?ersion.xml' % resPath)
    for verFile in versionFiles:
        if os.path.basename(verFile).lower() == versionFileName:
            import xml.dom.minidom
            dom1 = xml.dom.minidom.parse(verFile)
            versionList = dom1.getElementsByTagName('Version')
            if len(versionList) == 0:
                continue
            verInfo = {}
            verInfo['major'] = int(versionList[0].getAttribute('major'))
            verInfo['minor'] = int(versionList[0].getAttribute('minor'))
            verInfo['fix'] = int(versionList[0].getAttribute('fix'))
            verInfo['build'] = int(versionList[0].getAttribute('build'))
            rc = []
            for node in versionList[0].childNodes:
                if node.nodeType == node.TEXT_NODE:
                    rc.append(node.data.encode('utf_8'))

            verInfo['full'] = ''.join(rc)
            return verInfo

    return


def RecordUsage(toolName, toolVersion, usageMask, status, comments, location):
    import mcl.tools
    infoLines = list()
    infoLines.append("<?xml version='1.0' encoding='UTF-8' ?>\n")
    infoLines.append('<UsedTool>\n')
    infoLines.append('    <Name>%s</Name>\n' % _fixStringForXml(toolName))
    infoLines.append('    <Version>%s</Version>\n' % _fixStringForXml(toolVersion))
    usageStr = ''
    if usageMask & mcl.tools.USAGE_FLAG_ACCESSED:
        usageStr = usageStr + 'ACCESSED'
    if usageMask & mcl.tools.USAGE_FLAG_DEPLOYED:
        if len(usageStr) > 0:
            usageStr = usageStr + ','
        usageStr = usageStr + 'DEPLOYED'
    if usageMask & mcl.tools.USAGE_FLAG_EXERCISED:
        if len(usageStr) > 0:
            usageStr = usageStr + ','
        usageStr = usageStr + 'EXERCISED'
    if usageMask & mcl.tools.USAGE_FLAG_CHECKED:
        if len(usageStr) > 0:
            usageStr = usageStr + ','
        usageStr = usageStr + 'CHECKED'
    if usageMask & mcl.tools.USAGE_FLAG_QUEUED:
        if len(usageStr) > 0:
            usageStr = usageStr + ','
        usageStr = usageStr + 'QUEUED'
    if usageMask & mcl.tools.USAGE_FLAG_DELETED:
        if len(usageStr) > 0:
            usageStr = usageStr + ','
        usageStr = usageStr + 'DELETED'
    if len(usageStr) > 0:
        infoLines.append('    <Usage>%s</Usage>\n' % _fixStringForXml(usageStr))
    if status == mcl.tools.USAGE_STATUS_SUCCESSFUL:
        infoLines.append('    <ToolStatus>Successful</ToolStatus>\n')
    elif status == mcl.tools.USAGE_STATUS_UNSUCCESSFUL:
        infoLines.append('    <ToolStatus>Unsuccessful</ToolStatus>\n')
    if location != None and len(location) > 0:
        infoLines.append('    <ToolLocation>%s</ToolLocation>\n' % _fixStringForXml(location))
    if comments != None and len(comments) > 0:
        infoLines.append('    <ToolComments>%s</ToolComments>\n' % _fixStringForXml(comments))
    infoLines.append('</UsedTool>\n')
    import mcl.data.Output
    output = mcl.data.Output.DszDataHandlerOutput(None)
    logFile, logPath, logName = output.CreateLogFile(toolName, 'xml', subDir='UsedTools', utf8=True)
    try:
        for line in infoLines:
            logFile.write(line)

    finally:
        logFile.close()

    return


def _fixStringForXml(origStr):
    import re
    newStr = origStr
    if len(newStr) > 0:
        newStr = re.sub('&', '&amp;', newStr)
        newStr = re.sub('<', '&lt;', newStr)
        newStr = re.sub('>', '&gt;', newStr)
    return newStr