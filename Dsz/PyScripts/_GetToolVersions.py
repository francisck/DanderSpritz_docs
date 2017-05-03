# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _GetToolVersions.py
import dsz
import dsz.lp
import fnmatch
import os
import sys
import xml.dom.minidom as dom

def findVersionFiles(projDir):
    versionFiles = list()
    try:
        matches = fnmatch.filter(os.listdir(projDir), '*version.xml')
        if len(matches) > 0:
            versionFiles.append(projDir + '\\' + matches[0])
        if os.path.exists(projDir + '\\Version'):
            matches = fnmatch.filter(os.listdir(projDir + '\\Version'), '*.xml')
            for match in matches:
                versionFiles.append(projDir + '\\Version\\' + match)

    except:
        pass

    return versionFiles


def getProjectVersionElement(verFile, proj):
    try:
        proj = proj[proj.rfind('\\') + 1:]
        xml = dom.parse(verFile)
        elems = xml.getElementsByTagName('Version')
        if len(elems) > 0:
            verElem = elems.pop()
            element = dom.Element('Project')
            element.setAttribute('name', proj)
            element.appendChild(verElem)
            return element
    except:
        pass

    return None


def createXmlFile(verList):
    doc = dom.Document()
    base = doc.createElement('ToolVersions')
    doc.appendChild(base)
    for elem in verList:
        base.appendChild(elem)

    return doc


def main():
    versionList = list()
    projDirs = dsz.lp.GetProjectDirectories()
    for dir in projDirs:
        verFiles = findVersionFiles(dir)
        for file in verFiles:
            verElem = getProjectVersionElement(file, dir)
            if verElem != None:
                versionList.append(verElem)

    doc = createXmlFile(versionList)
    try:
        try:
            currTime = dsz.Timestamp()
            logDir = open(dsz.lp.GetLogsDirectory() + '\\tool_versions_' + currTime + '.xml', 'w')
            logDir.write(doc.toprettyxml(newl='\n'))
        except:
            print 'Unable to write version information'

    finally:
        if logDir != None:
            logDir.close()

    return True


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)