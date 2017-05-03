# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: _ModuleToggle.py
import dsz
import dsz.lp
import dsz.user
import dsz.script
import dsz.data
import sys
import xml.dom.minidom
import re
import os
Action = 'action'
SystemName = 'systemName'
Implementation = 'impl'
Silent = 'silent'
Load = 'load'
Free = 'free'
List = 1
Set = 2
Register = 3
bShowOutput = True
matchSystemName = re.compile('_PROV_(MCL_[^_]+)')
matchTargetName = re.compile('_PROV_(.+_TARGET)')
matchSystemImplementation = re.compile('_PROV_(MCL_[^_]*)_(.*)')
matchTargetImplementation = re.compile('_PROV_(.+_TARGET)_(.*)')
matchSystemSubstitution = re.compile('_SUB_(MCL_.+)')
matchTargetSubstitution = re.compile('_SUB_(.+_TARGET)')
bLoad = True
bFree = True

class ModuleInfo:

    def __init__(self, name):
        self.Name = name
        if name.startswith('MCL'):
            self.Implementations = [
             'FAIL']
            self.Selected = 'FAIL'
        else:
            self.Implementations = [
             'DEFAULT']
            self.Selected = 'DEFAULT'


def TaskingMain(namespace):
    global bFree
    global bShowOutput
    global bLoad
    import mcl.target
    import mcl.tasking
    dsz.control.echo.Off()
    params = mcl.tasking.GetParameters()
    bLoad = params[Load]
    bFree = params[Free]
    if params[Silent]:
        bShowOutput = False
    if params[Action] == List:
        retVal = _DoList(params[SystemName])
    elif params[Action] == Set:
        retVal = _DoSet(params[SystemName], params[Implementation])
    elif params[Action] == Register:
        retVal = _DoRegister(params[SystemName])
    else:
        dsz.ui.Echo('Unknown action')
        retVal = False
    if retVal:
        mcl.tasking.TaskSetStatus(mcl.target.CALL_SUCCEEDED)
    else:
        mcl.tasking.TaskSetStatus(mcl.target.CALL_FAILED)
    return True


def _DoList(systemDesired, bDisplay=True):
    if bDisplay:
        _PrintTask('Retrieving List')
    lpEnv = dsz.data.CreateCommand('lpgetenv', 'lpgetenv')
    if lpEnv == None:
        if bDisplay:
            _PrintFailure('lpgetenv failed')
        return False
    else:
        if bDisplay:
            _PrintSuccess()
        listOfSystems = dict()

        def matchName(systemList, option, value):
            for pattern in [matchSystemName, matchTargetName]:
                match = pattern.match(option)
                if match == None:
                    continue
                if match.group(1).upper() not in systemList:
                    systemList[match.group(1).upper()] = ModuleInfo(match.group(1))

            return

        def matchImpl(systemList, option, value):
            for pattern in [matchSystemImplementation, matchTargetImplementation]:
                match = pattern.match(option)
                if match == None:
                    continue
                if match.group(1).upper() not in systemList:
                    systemList[match.group(1).upper()] = ModuleInfo(match.group(1))
                systemList[match.group(1).upper()].Implementations.append(match.group(2))

            return

        def matchSub(systemList, option, value):
            for pattern in [matchSystemSubstitution, matchTargetSubstitution]:
                match = pattern.match(option)
                if match == None:
                    continue
                if match.group(1).upper() not in systemList:
                    systemList[match.group(1).upper()] = ModuleInfo(match.group(1))
                for pattern2 in ['MCL_[^_]+_(.+)', '%s_(.+)' % match.group(1).upper()]:
                    valueMatch = re.match(pattern2, value.upper())
                    if valueMatch:
                        if valueMatch.group(1) == 'DEFAULT':
                            return
                        systemList[match.group(1).upper()].Selected = valueMatch.group(1)

            return

        for envItem in lpEnv.EnvItem:
            matchName(listOfSystems, envItem.option, envItem.Value)
            matchImpl(listOfSystems, envItem.option, envItem.Value)
            matchSub(listOfSystems, envItem.option, envItem.Value)

        dsz.script.data.Start('ModuleToggle')
        try:
            if systemDesired:
                if systemDesired.upper() in listOfSystems.keys():
                    if bDisplay:
                        _DisplaySystemOptions(systemDesired, listOfSystems[systemDesired.upper()])
                        _PrintSuccess()
                    _StoreSystem(systemDesired, listOfSystems[systemDesired.upper()])
                    return listOfSystems[systemDesired.upper()]
                else:
                    if bDisplay:
                        _PrintFailure('System %s not found' % systemDesired)
                    return

            else:
                if bDisplay:
                    for sys in sorted(listOfSystems.keys()):
                        _DisplaySystemOptions(sys, listOfSystems[sys])

                    _PrintSuccess()
                for sys in listOfSystems.keys():
                    _StoreSystem(sys, listOfSystems[sys])

                return listOfSystems
        finally:
            dsz.script.data.Store()

        return


def _StoreSystem(system, data):
    dsz.script.data.Start('System')
    dsz.script.data.Add('Name', system, dsz.TYPE_STRING)
    if data.Selected:
        dsz.script.data.Add('Selected', data.Selected, dsz.TYPE_STRING)
    for item in data.Implementations:
        dsz.script.data.Add('Implementation', item, dsz.TYPE_STRING)

    dsz.script.data.End()


def _DisplaySystemOptions(name, options):
    dsz.ui.Echo('Implementations for %s (%s)' % (name, options.Selected))
    dsz.ui.Echo('----------------------------')
    for impl in options.Implementations:
        type = dsz.DEFAULT
        if impl == 'FAIL' and impl == options.Selected:
            type = dsz.WARNING
            suffix = '(selected)'
        elif impl == 'FAIL':
            type = dsz.ERROR
            suffix = ''
        elif impl == options.Selected:
            type = dsz.GOOD
            suffix = '(selected)'
        else:
            suffix = ''
        dsz.ui.Echo('%s %s' % (impl, suffix), type)

    dsz.ui.Echo('----------------------------')
    dsz.ui.Echo('')


def _DoSet(system, impl):
    if bFree:
        plugins = dsz.data.CreateCommand('plugins', 'plugins')
    else:
        plugins = None
    _PrintTask('Preparing to set %s to %s' % (system, impl))
    if system == None or impl == None:
        _PrintFailure('Invalid parameters')
        return False
    else:
        provVar = '_PROV_%s' % system.upper()
        subVar = '_SUB_%s' % system.upper()
        if impl.upper() == 'FAIL':
            subVal = '%s' % system.upper()
        else:
            subVal = '%s_%s' % (system.upper(), impl.upper())
        if not dsz.env.Check(provVar):
            _PrintFailure('System (%s) is not found' % system)
            return False
        if impl.upper() == 'DEFAULT':
            dsz.env.Delete(subVar)
            _PrintSuccess()
            if _DoFree(plugins, system):
                return _DoLoad(system, impl)
            else:
                return True

        if dsz.env.Check(subVar) and dsz.env.Get(subVar) == subVal:
            pass
        options = _DoList(system, False)
        if options == None:
            _PrintFailure('System (%s) implementations cannot be enumerated' % system)
            return False
        if impl.upper() not in options.Implementations:
            _PrintFailure('%s not a valid implementation: %s' % (impl, options.Implementations))
            return False
        _PrintSuccess()
        rtn = True
        if _DoFree(plugins, system):
            if not _DoLoad(system, impl):
                rtn = False
        else:
            rtn = False
        _PrintTask('Setting environment variable')
        if not dsz.env.Set(subVar, subVal):
            _PrintFailure()
            return False
        if rtn:
            _PrintSuccess()
        else:
            _PrintFailure()
        return rtn


def _DoRegister(system):
    if system:
        _PrintTask('Registering implementations of %s' % system)
    else:
        _PrintTask('Registering all implementations')
    retVal = True
    try:
        LegalTechniques = _GetAvailableModuleTechniquesByName(system)
        for tech in LegalTechniques:
            try:
                dsz.env.Set('_PROV_%s' % tech['name'].upper(), '%d' % tech['implementation'])
            except:
                retVal = False

    finally:
        _PrintOutcome(retVal)

    return retVal


def _DoFree(plugins, system):
    if bFree == False:
        return True
    else:
        if system == None:
            _PrintTask('Freeing items')
            _PrintFailure('System must be specified')
            return False
        if not bFree:
            return True
        localSystem = '%s' % system
        if not __FreeDependantPlugins(plugins, localSystem):
            return False
        if not __Free(plugins, localSystem):
            return False
        return True


def _DoLoad(system, name):
    if not bLoad:
        return True
    else:
        if system == None:
            _PrintTask('Loading implementation')
            _PrintFailure('System must be specified')
            return False
        if name == None:
            _PrintTask('Loading implementation')
            _PrintFailure('Implementation must be specified')
            return False
        potentialItems = _GetAvailableModuleTechniquesByName(system)
        for item in potentialItems:
            if item['name'].lower().endswith(name.lower()) or name.lower() == 'fail' and item['name'].lower() == system.lower() or name.lower() == 'default' and item['name'].lower() == system.lower():
                _PrintTask('Loading %s (%d)' % (item['name'], item['id']))
                if dsz.cmd.Run('load -id %d' % item['id']):
                    _PrintSuccess()
                    return True
                else:
                    _PrintFailure()
                    return False

        _PrintTask('Loading %s' % system)
        _PrintFailure('Cannot find implementation id')
        return False


def __GetAppropriatePluginSet(plugins):
    if dsz.script.IsLocal():
        return plugins.Local.Plugin
    return plugins.Remote.Plugin


def __Free(plugins, name):
    if name.strip() == '':
        return True
    for plugin in __GetAppropriatePluginSet(plugins):
        if name.upper() in plugin.Name.upper():
            _PrintTask('Free %s (%d)' % (plugin.Name, plugin.Id))
            cmd = 'free -id %d -force -depends 0' % plugin.Id
            if dsz.cmd.Run(cmd):
                _PrintSuccess()
            else:
                _PrintFailure()
                return False

    return True


def __FreeDependantPlugins(plugins, key, cntDown=10):
    if key.strip() == '':
        return True
    if cntDown == 0:
        _PrintTask('Free Dependant Plugins')
        _PrintFailure('Excessive recursion')
        return False
    for plugin in __GetAppropriatePluginSet(plugins):
        for acquiredApi in plugin.AcquiredApis:
            if acquiredApi.ProvidedBy.upper() == key.upper():
                if not __FreeDependantPlugins(plugins, plugin.Name, cntDown - 1):
                    return False
                if not __Free(plugins, plugin.Name):
                    return False

    return True


def _FreeItem(plugins, system):
    _PrintTask('Freeing %s' % system)
    retVal = True
    try:
        pluginSet = plugins.Remote
        if dsz.script.IsLocal():
            pluginSet = plugins.Local
        for plugin in pluginSet.Plugin:
            if system in plugin.Name:
                if not dsz.cmd.Run('free -id %d -force' % plugin.id):
                    retVal = False

    finally:
        _PrintOutcome(retVal)

    return retVal


def _GetAvailableModuleTechniquesByName(Module):
    retVal = list()
    AllModules = _GetTechniqueFiles()
    for file in AllModules:
        try:
            xmlFile = xml.dom.minidom.parse(file)
            name = xmlFile.getElementsByTagName('Technique')[0].getAttribute('name')
            id = int(xmlFile.getElementsByTagName('Technique')[0].getAttribute('id'), 10)
            if Module != None and Module.lower() not in name.lower():
                continue
            if _DoesModuleMatch(xmlFile):
                for implementation in xmlFile.getElementsByTagName('Implementation'):
                    value = int(implementation.getAttribute('value'), 10)
                    retVal.append({'name': name,'filename': file,'implementation': value,'id': id})

        except Exception as E:
            pass

    return retVal


def _GetTechniqueFiles():
    retVal = list()
    resDir = dsz.env.Get('_LPDIR_RESOURCES')
    resDirs = dsz.env.Get('_RES_DIRS')
    osStr = dsz.env.Get('_OS')
    if osStr == 'winnt':
        osStr = 'windows'
    for res in resDirs.split(';'):
        path = os.path.normpath('%s/%s/Modules/Techniques/%s/' % (resDir, res, osStr))
        if not os.path.exists(path):
            continue
        for file in os.listdir(path):
            filename = '%s/%s' % (path, file)
            if os.path.isdir(filename):
                continue
            retVal.append(filename)

    return retVal


def _DoesModuleMatch(xmlFile):
    for arch in xmlFile.getElementsByTagName('Architecture'):
        if not _DoesArchMatch(arch.getAttribute('type')):
            continue
        for platform in arch.childNodes:
            if not platform.nodeType == xml.dom.Node.ELEMENT_NODE:
                continue
            if not _DoesPlatformMatch(platform.getAttribute('family')):
                continue
            for version in platform.childNodes:
                if not version.nodeType == xml.dom.Node.ELEMENT_NODE:
                    continue
                if _DoesVersionMatch(version.getAttribute('major'), version.getAttribute('minor'), version.getAttribute('other')):
                    return True

    return False


def _DoesArchMatch(moduleArch):
    arch = dsz.env.Get('_ARCH')
    compArch = dsz.env.Get('_COMPILED_ARCH')
    return compArch == moduleArch


def _DoesPlatformMatch(modulePlatform):
    osStr = dsz.env.Get('_OS')
    if osStr == 'winnt':
        return modulePlatform == 'windows_nt' or modulePlatform == 'winnt'
    return False


def _DoesVersionMatch(major, minor, other):
    return _DoesVersionElementMatch(major, dsz.env.Get('_OS_VERSION_MAJOR')) and _DoesVersionElementMatch(minor, dsz.env.Get('_OS_VERSION_MINOR')) and _DoesVersionElementMatch(other, dsz.env.Get('_OS_VERSION_OTHER'))


def _DoesVersionElementMatch(fileVer, envVer):
    if fileVer == '*':
        return True
    bGreater = False
    if '+' in fileVer:
        bGreater = True
        fileVer = fileVer[:fileVer.index('+')]
    fileVer = int(fileVer)
    envVer = int(envVer)
    if fileVer == envVer:
        return True
    if bGreater and fileVer < envVer:
        return True
    return False


def _PrintTask(task):
    if bShowOutput:
        dsz.ui.Echo(task)


def _PrintOutcome(bState, msg=None):
    if bState:
        _PrintSuccess(msg)
    else:
        _PrintFailure(msg)


def _PrintSuccess(msg=None):
    __PrintImpl('PASSED', msg, dsz.GOOD)


def _PrintFailure(msg=None):
    __PrintImpl('FAILED', msg, dsz.ERROR)


def __PrintImpl(msg, detail, type):
    if not bShowOutput:
        return
    else:
        if detail != None:
            dsz.ui.Echo('    %s (%s)' % (msg, detail), type)
        else:
            dsz.ui.Echo('    %s' % msg, type)
        return


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)