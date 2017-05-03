# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Dir_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.file.cmd.dir', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Dir', 'dir', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        if msg.GetCount() == 0:
            output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
            return True
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('Directories')
        while msg.GetNumRetrieved() < msg.GetCount():
            if mcl.CheckForStop():
                output.RecordXml(xml)
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            dirmsg = msg.FindMessage(MSG_KEY_DIRECTORY)
            path = dirmsg.FindString(MSG_KEY_DIRECTORY_PATH)
            if len(path) == 0:
                path = '.'
            sub = xml.AddSubElement('Directory')
            sub.AddAttribute('path', path)
            while dirmsg.GetNumRetrieved() < dirmsg.GetCount():
                if mcl.CheckForStop():
                    output.RecordXml(xml)
                    output.EndWithStatus(mcl.target.CALL_FAILED)
                    return False
                try:
                    filemsg = dirmsg.FindMessage(MSG_KEY_DIRECTORY_FILE)
                    item = FileItem()
                    item.Demarshal(filemsg)
                except:
                    output.RecordXml(xml)
                    output.RecordError('Returned data is invalid')
                    output.EndWithStatus(mcl.target.CALL_FAILED)
                    return False

                if item.typeFlags & FILE_ITEM_FLAG_TYPE_ACCESS_DENIED:
                    sub.AddAttribute('denied', 'true')
                else:
                    if len(item.name) == 0:
                        output.RecordXml(xml)
                        output.RecordError('Invalid filename(s) received')
                        output.EndWithStatus(mcl.target.CALL_FAILED)
                        return False
                    fileSub = sub.AddSubElement('File')
                    fileSub.AddAttribute('name', '%s' % item.name)
                    fileSub.AddAttribute('size', '%u' % item.size)
                    timeSub = fileSub.AddSubElement('FileTimes')
                    timeSub.AddTimeElement('Modified', item.modifiedTime)
                    timeSub.AddTimeElement('Created', item.createdTime)
                    timeSub.AddTimeElement('Accessed', item.accessedTime)
                    _handleAttributes(fileSub, item.attributes)
                    while filemsg.PeekByKey(MSG_KEY_FILE_HASH) != None:
                        hash = HashItem()
                        try:
                            hash.Demarshal(filemsg)
                        except:
                            output.RecordXml(xml)
                            output.RecordError('Returned data is invalid')
                            output.EndWithStatus(mcl.target.CALL_FAILED)
                            return False

                        hashSub = fileSub.AddSubElement('Hash')
                        hashSub.AddAttribute('size', '%u' % len(hash.hash))
                        if hash.type == HASH_ITEM_TYPE_SHA1:
                            hashSub.AddAttribute('type', 'SHA1')
                        elif hash.type == HASH_ITEM_TYPE_MD5:
                            hashSub.AddAttribute('type', 'MD5')
                        elif hash.type == HASH_ITEM_TYPE_SHA256:
                            hashSub.AddAttribute('type', 'SHA256')
                        elif hash.type == HASH_ITEM_TYPE_SHA512:
                            hashSub.AddAttribute('type', 'SHA512')
                        else:
                            hashSub.AddAttribute('type', 'unknown')
                        hashSub.SetTextAsData(hash.hash)

                    if item.typeFlags & FILE_ITEM_FLAG_TYPE_UNIX:
                        unixItem = FileItemUnix()
                        try:
                            unixItem.Demarshal(filemsg)
                        except:
                            output.RecordXml(xml)
                            output.RecordError('Returned data is invalid')
                            output.EndWithStatus(mcl.target.CALL_FAILED)
                            return False

                        _handleUnixItem(fileSub, unixItem)
                    if item.typeFlags & FILE_ITEM_FLAG_TYPE_WINDOWS:
                        windowsItem = FileItemWindows()
                        try:
                            windowsItem.Demarshal(filemsg)
                        except:
                            output.RecordXml(xml)
                            output.RecordError('Returned data is invalid')
                            output.EndWithStatus(mcl.target.CALL_FAILED)
                            return False

                        _handleWindowsItem(fileSub, windowsItem)

        output.RecordXml(xml)
        output.End()
        return True


def _handleAttributes(sub, attributes):
    if attributes & FILE_ITEM_FLAG_ATTRIBS_DIR:
        sub.AddSubElement('FileAttributeDirectory')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_LINK:
        sub.AddSubElement('FileAttributeLink')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_SOCKET:
        sub.AddSubElement('FileAttributeAFUnixFamilySocket')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_BLOCK_DEV:
        sub.AddSubElement('FileAttributeBlockSpecialFile')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_CHAR_DEV:
        sub.AddSubElement('FileAttributeCharacterSpecialFile')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_NAMED_PIPE:
        sub.AddSubElement('FileAttributeNamedPipeFile')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_ARCHIVE:
        sub.AddSubElement('FileAttributeArchive')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_COMPRESSED:
        sub.AddSubElement('FileAttributeCompressed')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_ENCRYPTED:
        sub.AddSubElement('FileAttributeEncrypted')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_HIDDEN:
        sub.AddSubElement('FileAttributeHidden')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_OFFLINE:
        sub.AddSubElement('FileAttributeOffline')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_READONLY:
        sub.AddSubElement('FileAttributeReadonly')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_SYSTEM:
        sub.AddSubElement('FileAttributeSystem')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_TEMPORARY:
        sub.AddSubElement('FileAttributeTemporary')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_SPARSE_FILE:
        sub.AddSubElement('FileAttributeSparseFile')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_VIRTUAL:
        sub.AddSubElement('FileAttributeVirtual')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_NOT_INDEXED:
        sub.AddSubElement('FileAttributeNotIndexed')
    if attributes & FILE_ITEM_FLAG_ATTRIBS_DEVICE:
        sub.AddSubElement('FileAttributeDevice')


def _handleUnixItem(sub, unixInfo):
    sub.AddAttribute('inode', '%u' % unixInfo.inode)
    sub.AddAttribute('hardLinks', '%u' % unixInfo.numHardLinks)
    sub.AddAttribute('owner', unixInfo.owner)
    sub.AddAttribute('ownerId', '%u' % unixInfo.ownerId)
    sub.AddAttribute('group', unixInfo.group)
    sub.AddAttribute('groupId', '%u' % unixInfo.groupId)
    perms = sub.AddSubElement('Permissions')
    if unixInfo.permissions & FILE_ITEM_UNIX_FLAG_PERM_SET_UID:
        perms.AddSubElement('FilePermissionSetUid')
    if unixInfo.permissions & FILE_ITEM_UNIX_FLAG_PERM_SET_GID:
        perms.AddSubElement('FilePermissionSetGid')
    if unixInfo.permissions & FILE_ITEM_UNIX_FLAG_PERM_STICKY:
        perms.AddSubElement('FilePermissionSticky')
    if unixInfo.permissions & FILE_ITEM_UNIX_FLAG_PERM_OWNER_READ:
        perms.AddSubElement('FilePermissionOwnerRead')
    if unixInfo.permissions & FILE_ITEM_UNIX_FLAG_PERM_OWNER_WRITE:
        perms.AddSubElement('FilePermissionOwnerWrite')
    if unixInfo.permissions & FILE_ITEM_UNIX_FLAG_PERM_OWNER_EXEC:
        perms.AddSubElement('FilePermissionOwnerExecute')
    if unixInfo.permissions & FILE_ITEM_UNIX_FLAG_PERM_GROUP_READ:
        perms.AddSubElement('FilePermissionGroupRead')
    if unixInfo.permissions & FILE_ITEM_UNIX_FLAG_PERM_GROUP_WRITE:
        perms.AddSubElement('FilePermissionGroupWrite')
    if unixInfo.permissions & FILE_ITEM_UNIX_FLAG_PERM_GROUP_EXEC:
        perms.AddSubElement('FilePermissionGroupExecute')
    if unixInfo.permissions & FILE_ITEM_UNIX_FLAG_PERM_WORLD_READ:
        perms.AddSubElement('FilePermissionWorldRead')
    if unixInfo.permissions & FILE_ITEM_UNIX_FLAG_PERM_WORLD_WRITE:
        perms.AddSubElement('FilePermissionWorldWrite')
    if unixInfo.permissions & FILE_ITEM_UNIX_FLAG_PERM_WORLD_EXEC:
        perms.AddSubElement('FilePermissionWorldExecute')


def _handleWindowsItem(sub, windowsInfo):
    sub.AddAttribute('shortName', windowsInfo.shortName)


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)