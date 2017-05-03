# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
Name = 'Name'
Function = 'Function'
Parameter = 'Parameter'
Tags = 'Tags'
RecordData = 'RecordData'

def ExecuteSimpleMenu(comment, menuItems):
    dsz.ui.Echo(comment)
    dsz.ui.Echo('  0) Exit')
    i = 0
    while i < len(menuItems):
        item = menuItems[i]
        if isinstance(item, dict):
            dsz.ui.Echo(' %2u) %s' % (i + 1, item[Name]))
        else:
            dsz.ui.Echo(' %2u) %s' % (i + 1, item))
        i = i + 1

    while True:
        choice = dsz.ui.GetInt('Enter the desired option')
        if choice < 0:
            continue
        if choice == 0:
            return ('', -1)
        if choice > len(menuItems):
            continue
        select = menuItems[choice - 1]
        if isinstance(select, dict):
            if select.has_key(Parameter):
                return (select[Function](select[Parameter]), choice - 1)
            else:
                return (
                 select[Function](None), choice - 1)

        else:
            return (
             select, choice - 1)

    return ('', 0)


def FilterList(origList, filterList):
    newList = list(origList)
    for item in filterList:
        i = 0
        while i < len(newList):
            dsz.script.CheckStop()
            tagPresent = False
            for tag in newList[i][Tags]:
                if tag.lower() == item.lower() or '-%s' % tag.lower() == item.lower():
                    tagPresent = True
                    break

            if not tagPresent:
                del newList[i]
            else:
                i = i + 1

    return newList