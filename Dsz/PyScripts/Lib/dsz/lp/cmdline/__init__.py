# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.path
import re

def DisplayHelp(filename=''):
    fullpath = _findCommandFile(filename)
    description = _parseCommandDescription(fullpath)
    return _displayHelp(dsz.script.Env['script_name'], description)


def ParseCommandLine(argv, filename='', stripQuotes=False):
    fullpath = _findCommandFile(filename)
    description = _parseCommandDescription(fullpath)
    if len(description) == 0 or len(argv) >= 2 and (argv[1] == '?' or argv[1] == '/?' or argv[1] == '-?' or argv[1] == '+?' or argv[1] == '/help' or argv[1] == '-help' or argv[1] == '+help'):
        _displayHelp(argv[0], description)
        return {}
    else:
        parameters = {}
        parameters['script'] = argv[0]
        option = ''
        i = 1
        while i < len(argv):
            arg = argv[i]
            i = i + 1
            matchObj = re.match('^[+-](.+)', arg)
            if matchObj != None:
                match = matchObj.group(1).lower()
                if len(option) > 0:
                    if not _fullOption(description, parameters, option):
                        _printError("Incomplete '%s'" % option, argv[0], description)
                        return {}
                    if not parameters.has_key(option):
                        parameters[option] = list()
                        parameters[option].append('true')
                if not _validOption(description, match):
                    _printError("Invalid option '%s'" % match, argv[0], description)
                    return {}
                if parameters.has_key(match):
                    _printError("Only one use of '%s' allowed" % arg, argv[0], description)
                    return {}
                option = match
            else:
                if len(option) == 0:
                    _printError('Missing required option', argv[0], description)
                    return {}
                paramOptionLen = 0
                if parameters.has_key(option):
                    paramOptionLen = len(parameters[option])
                if stripQuotes:
                    arg = re.sub('"(.*)"', '\\1', arg)
                if not _validArgument(description, option, paramOptionLen, arg):
                    _printError("Invalid argument '%s'" % arg, argv[0], description)
                    return {}
                if not parameters.has_key(option):
                    parameters[option] = list()
                parameters[option].append(arg)

        if len(option) > 0 and not _fullOption(description, parameters, option):
            _printError("Incomplete '%s'" % option, argv[0], description)
            return {}
        if len(option) > 0 and not parameters.has_key(option):
            l = list()
            l.append('true')
            parameters[option] = l
        if not _allRequiredOptionsUsed(description, parameters):
            return {}
        return parameters
        return


def _findCommandFile(filename):
    if len(filename) == 0:
        matchObj = re.match('([^\\\\/]*)\\.py', dsz.script.Env['script_name'])
        if matchObj == None:
            raise RuntimeError, 'Failed to determine command .txt name'
        filename = '%s.txt' % matchObj.group(1)
    if dsz.path.IsFullPath(filename):
        return filename
    else:
        return '%s/%s' % (dsz.script.Env['script_path'], filename)
        return


def _parseCommandDescription(filename):
    lines = list()
    try:
        f = open(filename, 'r')
        try:
            lines = f.readlines()
        finally:
            f.close()

    except:
        dsz.ui.Echo('Unable to open %s' % filename, dsz.ERROR)
        return {}

    optionKey, argumentKey, helpKey, required, name, value = _getKeys()
    parameters = {}
    option = -1
    for line in lines:
        line = re.sub('\r', '', line)
        line = re.sub('\n', '', line)
        if re.match('^[\t ]*(#.*){0,1}$', line) != None:
            continue
        else:
            matchObj = re.match('^[\t ]+([^\t ].*)$', line)
            if matchObj != None:
                if option == -1:
                    dsz.ui.Echo('Invalid file format', dsz.ERROR)
                    return {}
                key = '%s%u%s' % (optionKey, option, helpKey)
                parameters[key] = matchObj.group(1)
            else:
                matchObj = re.match('^([\\[<])-([^\t ]+) *(.*)([\\]>])[\t ]*$', line)
                if matchObj != None:
                    option = option + 1
                    key = '%s%u%s' % (optionKey, option, required)
                    if matchObj.group(1) == '[' and matchObj.group(4) == ']':
                        parameters[key] = 'false'
                    elif matchObj.group(1) == '<' and matchObj.group(4) == '>':
                        parameters[key] = 'true'
                    else:
                        dsz.ui.Echo('Invalid file format', dsz.ERROR)
                        return {}
                    key = '%s%u%s' % (optionKey, option, name)
                    if parameters.has_key(key):
                        dsz.ui.Echo("Option '%s' defined twice" % matchObj.group(2), dsz.ERROR)
                        return {}
                    parameters[key] = matchObj.group(2)
                    argument = 0
                    args = matchObj.group(3)
                    mustBeOptional = False
                    while args != '':
                        matchObj = re.match('^[\t ]*([\\[<])([^\t ]+)([\\]>])[\t ]*(.*)$', args)
                        if matchObj != None:
                            key = '%s%u%s%u%s' % (optionKey, option, argumentKey, argument, required)
                            if matchObj.group(1) == '[' and matchObj.group(3) == ']':
                                parameters[key] = 'false'
                                mustBeOptional = True
                            elif matchObj.group(1) == '<' and matchObj.group(3) == '>' and not mustBeOptional:
                                parameters[key] = 'true'
                            else:
                                dsz.ui.Echo('Invalid file format: Mismatched argument tags', dsz.ERROR)
                                return {}
                            key = '%s%u%s%u%s' % (optionKey, option, argumentKey, argument, name)
                            parameters[key] = matchObj.group(2).lower()
                            args = matchObj.group(4)
                            argument = argument + 1
                        elif re.match('^[\t ]*$', args) != None:
                            break
                        else:
                            dsz.ui.Echo("Invalid file format: Couldn't parse '%s'" % args, dsz.ERROR)
                            return {}

                else:
                    dsz.ui.Echo('Invalid line', dsz.ERROR)
                    return {}

    return parameters


def _displayHelp(script, description):
    if len(description) == 0:
        dsz.ui.Echo('python "%s" -args "[options]"' % script)
        return
    dsz.ui.Echo('python "%s" -args "..."' % script)
    optionKey, argumentKey, helpKey, required, name, value = _getKeys()
    index = 0
    while description.has_key('%s%u%s' % (optionKey, index, name)):
        arguments = ''
        arg = 0
        while description.has_key('%s%u%s%u%s' % (optionKey, index, argumentKey, arg, name)):
            if description['%s%u%s%u%s' % (optionKey, index, argumentKey, arg, required)] == 'true':
                arguments = arguments + ' <%s>' % description['%s%u%s%u%s' % (optionKey, index, argumentKey, arg, name)]
            else:
                arguments = arguments + ' [%s]' % description['%s%u%s%u%s' % (optionKey, index, argumentKey, arg, name)]
            arg = arg + 1

        if description['%s%u%s' % (optionKey, index, required)] == 'true':
            dsz.ui.Echo('    <-%s%s>' % (description['%s%u%s' % (optionKey, index, name)], arguments))
        else:
            dsz.ui.Echo('    [-%s%s]' % (description['%s%u%s' % (optionKey, index, name)], arguments))
        key = '%s%u%s' % (optionKey, index, helpKey)
        if description.has_key(key):
            dsz.ui.Echo('        %s' % description[key])
        index = index + 1


def _validOption(description, option):
    optionKey, argumentKey, helpKey, required, name, value = _getKeys()
    num = 0
    while description.has_key('%s%u%s' % (optionKey, num, name)):
        if description['%s%u%s' % (optionKey, num, name)].lower() == option.lower():
            return True
        num = num + 1

    return False


def _validArgument(description, option, index, argument):
    optionKey, argumentKey, helpKey, required, name, value = _getKeys()
    num = 0
    while description.has_key('%s%u%s' % (optionKey, num, name)):
        if description['%s%u%s' % (optionKey, num, name)].lower() == option.lower():
            key = '%s%u%s%u%s' % (optionKey, num, argumentKey, index, name)
            if not description.has_key(key):
                return False
            else:
                str = description[key].lower()
                if re.search('[^\\|]+\\|[^\\|].+', str) != None:
                    while len(str) > 0:
                        matchObj = re.search('[\t ]*([^\\|]+)[\t ]*\\|[\t ]*([^\\|].*)', str)
                        if matchObj == None:
                            return str.lower() == argument.lower()
                        str = matchObj.group(2).lower()
                        if argument.lower() == matchObj.group(1).lower():
                            return True

                    return False
                return True

        num = num + 1

    return True


def _fullOption(description, parameters, option):
    optionKey, argumentKey, helpKey, required, name, value = _getKeys()
    num = 0
    while 1:
        if description.has_key('%s%u%s' % (optionKey, num, name)):
            if description['%s%u%s' % (optionKey, num, name)].lower() != option.lower():
                num = num + 1
                continue
            num2 = 0
            min = 0
            max = 0
            while description.has_key('%s%u%s%u%s' % (optionKey, num, argumentKey, num2, name)):
                max = max + 1
                if description['%s%u%s%u%s' % (optionKey, num, argumentKey, num2, required)] == 'true':
                    min = min + 1
                num2 = num2 + 1

            paramOptionLen = 0
            paramOptionLen = parameters.has_key(option) and len(parameters[option])
        return paramOptionLen >= min and paramOptionLen <= max

    return True


def _allRequiredOptionsUsed(description, parameters):
    optionKey, argumentKey, helpKey, required, name, value = _getKeys()
    num = 0
    while description.has_key('%s%u%s' % (optionKey, num, name)):
        if description['%s%u%s' % (optionKey, num, required)] == 'true':
            key = '%s%u%s' % (optionKey, num, name)
            if not parameters.has_key(description[key]) or len(parameters[description[key]]) == 0:
                dsz.ui.Echo("Missing option '%s'" % description[key], dsz.ERROR)
                return False
        num = num + 1

    return True


def _printError(error, cmd='', description={}):
    dsz.ui.Echo('', dsz.ERROR)
    dsz.ui.Echo('* ', dsz.ERROR)
    dsz.ui.Echo('* %s' % error, dsz.ERROR)
    dsz.ui.Echo('* ', dsz.ERROR)
    dsz.ui.Echo('', dsz.ERROR)
    if len(cmd) > 0:
        _displayHelp(cmd, description)


def _getKeys():
    return ('opt_', 'arg_', 'help_', 'req_', 'name_', 'value_')