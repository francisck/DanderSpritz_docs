# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Drives_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.file.cmd.drives', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Drives', 'drives', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Drives')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.RecordXml(xml)
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        data = Result()
        data.Demarshal(msg)
        sub = xml.AddSubElement('Drive')
        sub.AddSubElementWithText('Path', data.location)
        sub.AddSubElementWithText('Type', _getDriveType(data.type))
        if len(data.source) > 0:
            sub.AddSubElementWithText('Source', data.source)
        if len(data.filesystem) > 0:
            sub.AddSubElementWithText('FileSystem', data.filesystem)
        if len(data.options) > 0:
            sub.AddSubElementWithText('Options', data.options)
        if data.maxComponentLength > 0:
            sub.AddSubElementWithText('MaximumComponentLength', '%u' % data.maxComponentLength)
        if data.volumeSerialNumber != 0:
            sub.AddSubElementWithText('SerialNumber', '%04x-%04x' % (data.volumeSerialNumber >> 16 & 65535, data.volumeSerialNumber & 65535))
        if data.flags != 0:
            _addFlags(sub, data.flags)

    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _addFlags(xml, flags):
    sub = xml.AddSubElement('Flags')
    sub.AddAttribute('value', '0x%08x' % flags)
    if flags & RESULT_FLAG_READ:
        sub.AddSubElement('DriveFlagReadPermission')
    if flags & RESULT_FLAG_WRITE:
        sub.AddSubElement('DriveFlagWritePermission')
    if flags & RESULT_FLAG_CASE_SENSITIVE_SEARCH:
        sub.AddSubElement('DriveFlagCaseSensitiveSearch')
    if flags & RESULT_FLAG_CASE_PRESERVED_NAMES:
        sub.AddSubElement('DriveFlagCasePreservedNames')
    if flags & RESULT_FLAG_UNICODE_ON_DISK:
        sub.AddSubElement('DriveFlagUnicodeOnDisk')
    if flags & RESULT_FLAG_PERSISTENT_ACLS:
        sub.AddSubElement('DriveFlagPersistentAcls')
    if flags & RESULT_FLAG_FILE_COMPRESSION:
        sub.AddSubElement('DriveFlagFileCompression')
    if flags & RESULT_FLAG_QUOTAS:
        sub.AddSubElement('DriveFlagQuotas')
    if flags & RESULT_FLAG_SUPPORTS_SPARSE_FILES:
        sub.AddSubElement('DriveFlagSupportsSparseFiles')
    if flags & RESULT_FLAG_SUPPORTS_REPARSE_POINTS:
        sub.AddSubElement('DriveFlagSupportsReparsePoints')
    if flags & RESULT_FLAG_SUPPORTS_REMOTE_STORAGE:
        sub.AddSubElement('DriveFlagSupportsRemoteStorage')
    if flags & RESULT_FLAG_IS_COMPRESSED:
        sub.AddSubElement('DriveFlagIsCompressed')
    if flags & RESULT_FLAG_SUPPORTS_OBJECT_IDS:
        sub.AddSubElement('DriveFlagSupportsObjectIds')
    if flags & RESULT_FLAG_SUPPORTS_ENCRYPTION:
        sub.AddSubElement('DriveFlagSupportsEncryption')
    if flags & RESULT_FLAG_SUPPORTS_NAMED_STREAMS:
        sub.AddSubElement('DriveFlagSupportsNameStreams')


def _getDriveType(driveType):
    if driveType == RESULT_DRIVE_TYPE_UNKNOWN:
        return 'Unknown'
    else:
        if driveType == RESULT_DRIVE_TYPE_REMOVABLE:
            return 'Removable'
        if driveType == RESULT_DRIVE_TYPE_FIXED:
            return 'Fixed'
        if driveType == RESULT_DRIVE_TYPE_NETWORK:
            return 'Network'
        if driveType == RESULT_DRIVE_TYPE_CDROM:
            return 'Cdrom'
        if driveType == RESULT_DRIVE_TYPE_RAMDISK:
            return 'Ramdisk'
        if driveType == RESULT_DRIVE_TYPE_SIMULATED:
            return 'Simulated'
        return 'UnhandledType'


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)