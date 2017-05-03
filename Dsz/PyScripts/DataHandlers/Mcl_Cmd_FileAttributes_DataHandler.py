# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_FileAttributes_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.file.cmd.fileattributes', globals())
    ATTRIBS_TO_XML = {ATTRIB_ARCHIVE: 'FILE_ATTRIBUTE_ARCHIVE',
       ATTRIB_COMPRESSED: 'FILE_ATTRIBUTE_COMPRESSED',
       ATTRIB_DIRECTORY: 'FILE_ATTRIBUTE_DIRECTORY',
       ATTRIB_ENCRYPTED: 'FILE_ATTRIBUTE_ENCRYPTED',
       ATTRIB_HIDDEN: 'FILE_ATTRIBUTE_HIDDEN',
       ATTRIB_NORMAL: 'FILE_ATTRIBUTE_NORMAL',
       ATTRIB_OFFLINE: 'FILE_ATTRIBUTE_OFFLINE',
       ATTRIB_READONLY: 'FILE_ATTRIBUTE_READONLY',
       ATTRIB_REPARSE_POINT: 'FILE_ATTRIBUTE_REPARSE_POINT',
       ATTRIB_SPARSE_FILE: 'FILE_ATTRIBUTE_SPARSE_FILE',
       ATTRIB_SYSTEM: 'FILE_ATTRIBUTE_SYSTEM',
       ATTRIB_TEMPORARY: 'FILE_ATTRIBUTE_TEMPORARY',
       ATTRIB_NOT_INDEXED: 'FILE_ATTRIBUTE_NOT_CONTENT_INDEXED',
       ATTRIB_DEVICE: 'FILE_ATTRIBUTE_DEVICE',
       ATTRIB_OWNER_READ: 'FILE_ATTRIBUTE_OWNER_READ',
       ATTRIB_OWNER_WRITE: 'FILE_ATTRIBUTE_OWNER_WRITE',
       ATTRIB_OWNER_EXEC: 'FILE_ATTRIBUTE_OWNER_EXEC',
       ATTRIB_GROUP_READ: 'FILE_ATTRIBUTE_GROUP_READ',
       ATTRIB_GROUP_WRITE: 'FILE_ATTRIBUTE_GROUP_WRITE',
       ATTRIB_GROUP_EXEC: 'FILE_ATTRIBUTE_GROUP_EXEC',
       ATTRIB_WORLD_READ: 'FILE_ATTRIBUTE_WORLD_READ',
       ATTRIB_WORLD_WRITE: 'FILE_ATTRIBUTE_WORLD_WRITE',
       ATTRIB_WORLD_EXEC: 'FILE_ATTRIBUTE_WORLD_EXEC',
       ATTRIB_SET_UID: 'FILE_ATTRIBUTE_SET_UID',
       ATTRIB_SET_GID: 'FILE_ATTRIBUTE_SET_GID',
       ATTRIB_STICKY_BIT: 'FILE_ATTRIBUTE_STICKY_BIT'
       }
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('FileAttributes', 'fileattributes', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    results = Result()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    if results.set:
        xml.Start('OriginalFileAttribs')
    else:
        xml.Start('FileAttribs')
    xml.AddAttribute('file', results.file)
    xml.AddAttribute('size', '%u' % results.size)
    if len(results.owner) > 0:
        xml.AddAttribute('owner', results.owner)
    if len(results.group) > 0:
        xml.AddAttribute('group', results.group)
    xml.AddTimeElement('Accessed', results.ftAccessed)
    xml.AddTimeElement('Created', results.ftCreated)
    xml.AddTimeElement('Modified', results.ftModified)
    xml.AddAttribute('attributeMask', '0x%08x' % results.attributes)
    for attrib in ATTRIBS_TO_XML.keys():
        if results.attributes & attrib:
            xml.AddSubElement(ATTRIBS_TO_XML[attrib])

    if results.attributes & ATTRIB_REPARSE_POINT:
        reparse = ReparseResult()
        reparse.Demarshal(msg)
        if reparse.type != REPARSE_TYPE_COULD_NOT_READ:
            sub = xml.AddSubElement('Reparse')
            sub.AddAttribute('flags', '0x%08x' % reparse.flags)
            if reparse.type == REPARSE_TYPE_MICROSOFT:
                sub.AddAttribute('type', 'windows')
                if reparse.flags & REPARSE_FLAG_SURROGATE:
                    sub.AddSubElement('FILE_REPARSE_FLAG_SURROGATE')
                if reparse.flags & REPARSE_FLAG_MOUNT_POINT:
                    sub.AddSubElement('FILE_REPARSE_FLAG_MOUNT_POINT')
                if reparse.flags & REPARSE_FLAG_MICROSOFT_HSM:
                    sub.AddSubElement('FILE_REPARSE_FLAG_MICROSOFT_HSM')
                if reparse.flags & REPARSE_FLAG_MICROSOFT_SIS:
                    sub.AddSubElement('FILE_REPARSE_FLAG_MICROSOFT_SIS')
                if reparse.flags & REPARSE_FLAG_MICROSOFT_DFS:
                    sub.AddSubElement('FILE_REPARSE_FLAG_MICROSOFT_DFS')
                if reparse.flags & REPARSE_FLAG_SYMLINK:
                    sub.AddSubElement('FILE_REPARSE_FLAG_SYMLINK')
                if reparse.flags & REPARSE_FLAG_DFSR:
                    sub.AddSubElement('FILE_REPARSE_FLAG_DFSR')
            elif reparse.type == REPARSE_TYPE_THIRD_PARTY:
                sub.AddAttribute('type', 'unknown')
            else:
                sub.AddAttribute('type', 'unknown')
            sub.AddSubElementWithText('Data1', reparse.reparseData1)
            sub.AddSubElementWithText('Data2', reparse.reparseData2)
            sub.AddSubElementWithText('Data3', reparse.reparseData3)
            sub.AddSubElementWithText('Data4', reparse.reparseData4)
    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)