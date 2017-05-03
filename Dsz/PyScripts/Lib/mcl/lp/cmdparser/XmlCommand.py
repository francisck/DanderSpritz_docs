# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: XmlCommand.py


class XmlCommand():

    def __init__(self):
        self.m_help = []
        self.m_commandName = ''
        self.m_requiredArgs = 0
        self.m_commandId = 0
        self.m_commandScript = ''
        self.m_arguments = []
        self.m_data = []
        self.m_options = []
        self.m_optionPrefix = '-'
        self.m_defaultDisplay = ''
        self.m_defaultDisplayParameters = {}

    def CopyArguments(self):
        import copy
        return copy.deepcopy(self.m_arguments)

    def CopyData(self):
        import copy
        return copy.deepcopy(self.m_data)

    def CopyDefaultDisplayParameters(self):
        return self.m_defaultDisplayParameters.copy()

    def CopyHelp(self):
        import copy
        return copy.deepcopy(self.m_help)

    def CopyOptions(self):
        import copy
        return copy.deepcopy(self.m_options)

    def GetOptionPrefix(self):
        return self.m_optionPrefix

    def GetCommandId(self):
        return self.m_commandId

    def GetCommandName(self):
        return self.m_commandName.encode('utf_8')

    def GetCommandScript(self):
        return self.m_commandScript.encode('utf_8')

    def GetDefaultDisplay(self):
        return self.m_defaultDisplay.encode('utf_8')

    def GetNumRequiredArgs(self):
        return self.m_requiredArgs

    def Initialize(self, CommandNode):
        idStr = CommandNode.getAttribute('id')
        if len(idStr) == 0:
            raise RuntimeError("No 'id' attribute for command element")
        self.m_commandId = int(idStr, 0)
        cmdName = CommandNode.getAttribute('name')
        if len(cmdName) == 0:
            raise RuntimeError("No 'name' attribute for command element")
        self.m_commandName = cmdName.lower()
        self.m_help = _getTextFromMultipleElements(CommandNode, 'Help')
        self._ParseDefault(CommandNode, CommandNode.getElementsByTagName('Default'))
        self._ParseInput(CommandNode, CommandNode.getElementsByTagName('Input'))
        self._ParseOutput(CommandNode, CommandNode.getElementsByTagName('Output'))

    def SetCommandScript(self, script):
        self.m_commandScript = script

    def _GetArgument(self, ArgNode):
        from XmlCommandArgument import XmlCommandArgument
        arg = XmlCommandArgument()
        name = ArgNode.getAttribute('name')
        if len(name) == 0:
            raise RuntimeError("No 'name' attribute for argument node")
        arg.SetName(name)
        optional = ArgNode.getAttribute('optional')
        if optional.lower() == 'true':
            arg.SetOptional(True)
        elif optional.lower() == 'false':
            arg.SetOptional(False)
        group = ArgNode.getAttribute('group')
        if len(group) > 0:
            arg.SetGroupName(group)
        data = ArgNode.getAttribute('data')
        if len(data) > 0:
            arg.SetDataName(data)
        help = _getTextFromMultipleElements(ArgNode, 'Help')
        if len(help) > 0:
            arg.SetHelp(help)
        if ArgNode.nodeType == ArgNode.ELEMENT_NODE:
            for node in ArgNode.getElementsByTagName('Value'):
                if node.nodeType == node.ELEMENT_NODE:
                    valueName = node.getAttribute('string')
                    if len(valueName) == 0:
                        raise RuntimeError("No 'string' attribute for value node")
                    for setNode in node.getElementsByTagName('Set'):
                        dataName = setNode.getAttribute('data')
                        if len(dataName) > 0:
                            value = setNode.getAttribute('value')
                            if len(value) == 0:
                                raise RuntimeError('Invalid <Set data=...> node')
                            arg.AddValidValueData(valueName, dataName, value)
                        else:
                            paramName = setNode.getAttribute('param')
                            value = setNode.getAttribute('value')
                            if len(paramName) == 0 or len(value) == 0:
                                raise RuntimeError('Invalid <Set param=...> node')
                            arg.AddValidValueParam(valueName, paramName, value)

        return arg

    def _GetData(self, DataNode):
        from XmlCommandData import XmlCommandData
        data = XmlCommandData()
        dataName = DataNode.getAttribute('name')
        if len(dataName) == 0:
            raise RuntimeError("No 'name' attribute for data node")
        data.SetName(dataName)
        type = DataNode.getAttribute('type')
        if len(type) == 0:
            raise RuntimeError("No 'type' attribute for data node")
        data.SetType(type)
        default = DataNode.getAttribute('default')
        if len(default) > 0:
            data.SetDefaultValue(default)
        return data

    def _GetOption(self, OptionNode):
        from XmlCommandOption import XmlCommandOption
        option = XmlCommandOption()
        optionName = OptionNode.getAttribute('name')
        if len(optionName) == 0:
            raise RuntimeError("No 'name' attribute for option node")
        option.SetName(optionName.lower())
        optional = OptionNode.getAttribute('optional')
        if optional.lower() == 'true':
            option.SetOptional(True)
        elif optional.lower() == 'false':
            option.SetOptional(False)
        groupName = OptionNode.getAttribute('group')
        if len(groupName) > 0:
            option.SetGroupName(groupName)
        help = _getTextFromMultipleElements(OptionNode, 'Help')
        if len(help) > 0:
            option.SetHelp(help)
        optNames = _getTextFromMultipleElements(OptionNode, 'Require')
        for optName in optNames:
            option.AddRequiredOption(optName)

        optNames = _getTextFromMultipleElements(OptionNode, 'Reject')
        for optName in optNames:
            option.AddRejectedOption(optName)

        for child in OptionNode.childNodes:
            if child.nodeType == child.ELEMENT_NODE:
                if child.nodeName == 'Argument':
                    newArgument = self._GetArgument(child)
                    option.AddArgument(newArgument)
                elif child.nodeName == 'Set':
                    dataName = child.getAttribute('data')
                    if len(dataName) > 0:
                        value = child.getAttribute('value')
                        if len(value) > 0:
                            option.AddSetData(dataName, value)
                    else:
                        paramName = child.getAttribute('param')
                        if len(paramName) > 0:
                            value = child.getAttribute('value')
                            if len(value) > 0:
                                option.AddSetParameter(paramName, value)

        return option

    def _ParseDefault(self, Parent, DataList):
        if DataList == None:
            return
        else:
            displayNotSet = True
            for DefaultElement in DataList:
                if not Parent.isSameNode(DefaultElement.parentNode):
                    continue
                DefaultList = DefaultElement.childNodes
                if DefaultList == None:
                    return
                for Element in DefaultList:
                    if Element.nodeType != Element.ELEMENT_NODE:
                        continue
                    if Element.nodeName == 'Display':
                        display = _getTextFromSingleElement(Element)
                        if len(display) > 0:
                            self.m_defaultDisplay = display
                            displayNotSet = False
                    elif Element.nodeName == 'Parameter':
                        name = Element.getAttribute('name')
                        value = Element.getAttribute('value')
                        if len(name) > 0:
                            self.m_defaultDisplayParameters[pName] = value

            if displayNotSet:
                self.m_defaultDisplay = self.m_commandName.lower() + '_display.xsl'
            return

    def _ParseInput(self, Parent, DataList):
        if DataList == None:
            return
        else:
            for InputElement in DataList:
                if not Parent.isSameNode(InputElement.parentNode):
                    continue
                optionprefix = InputElement.getAttribute('optionprefix')
                if len(optionprefix) > 0:
                    if len(optionprefix) != 1:
                        raise RuntimeError("Invalid value for 'Input' attribute 'optionprefix' (must be a single character)")
                    self.m_optionPrefix = optionprefix
                InputList = InputElement.childNodes
                if InputList == None:
                    return
                for Element in InputList:
                    if Element.nodeType != Element.ELEMENT_NODE:
                        continue
                    if Element.nodeName == 'Option':
                        newOption = self._GetOption(Element)
                        self.m_options.append(newOption)
                    elif Element.nodeName == 'Argument':
                        newArgument = self._GetArgument(Element)
                        self.m_arguments.append(newArgument)

                for arg in self.m_arguments:
                    if arg.IsOptional() == False:
                        self.m_requiredArgs = self.m_requiredArgs + 1

                for opt in self.m_options:
                    if opt.IsOptional() == False:
                        self.m_requiredArgs = self.m_requiredArgs + 1

            return

    def _ParseOutput(self, Parent, DataList):
        if DataList == None:
            return true
        else:
            for OutputElement in DataList:
                if not Parent.isSameNode(OutputElement.parentNode):
                    continue
                OutputList = OutputElement.childNodes
                if OutputList == None:
                    return
                for Element in OutputList:
                    if Element.nodeType == Element.TEXT_NODE or Element.nodeType == Element.COMMENT_NODE:
                        continue
                    elif Element.nodeType != Element.ELEMENT_NODE:
                        raise RuntimeError('Invalid data in <Output> element (nodeType=%d)' % Element.nodeType)
                    if Element.nodeName == 'Data':
                        newData = self._GetData(Element)
                        for dataObject in self.m_data:
                            if dataObject.GetName() == newData.GetName():
                                raise RuntimeError("Data element '%s' already defined" % newData.GetName())

                        self.m_data.append(newData)

            return


def _getTextFromSingleElement(element):
    txt = ''
    for node in element.childNodes:
        if node.nodeType == node.TEXT_NODE:
            txt = txt + node.data

    return txt


def _getTextFromMultipleElements(root, elementName):
    textList = list()
    for node in root.getElementsByTagName(elementName):
        if root.isSameNode(node.parentNode):
            nodeText = _getTextFromSingleElement(node)
            if len(nodeText) > 0:
                textList.append(nodeText)

    return textList