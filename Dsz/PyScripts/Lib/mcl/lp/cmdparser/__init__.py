# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py


def GetCommandUsage(command):
    usageStr = ''
    options = command.CopyOptions()
    arguments = command.CopyArguments()
    help = command.CopyHelp()
    usageStr = usageStr + 'Usage: %s' % command.GetCommandName()
    for arg in arguments:
        if arg.IsOptional():
            usageStr = usageStr + ' [%s]' % arg.GetName()
        else:
            usageStr = usageStr + ' <%s>' % arg.GetName()

    if len(options) > 0:
        usageStr = usageStr + ' _Options_'
    usageStr = usageStr + '\n'
    for helpStr in help:
        usageStr = usageStr + '   %s\n' % helpStr

    if len(arguments) > 0:
        usageStr = usageStr + '\nArguments:\n'
        for arg in arguments:
            argName = arg.GetName()
            if arg.HasValidValues():
                values = arg.GetValidValues()
                if len(values) > 0:
                    argName = ''
                    for value in values.keys():
                        if len(argName) > 0:
                            argName = argName + '|'
                        argName = argName + value

            groupString = ''
            if arg.HasGroup():
                groupString = ' (group=%s)' % arg.GetGroupName()
            usageStr = usageStr + '   '
            if arg.IsOptional():
                usageStr = usageStr + '[%s]' % argName
            else:
                usageStr = usageStr + '<%s>' % argName
            usageStr = usageStr + groupString + '\n'
            j = 0
            while j < arg.GetHelpSize():
                usageStr = usageStr + '   %s\n' % arg.GetHelp(j)
                j = j + 1

    if len(options) > 0:
        usageStr = usageStr + '\nOptions:\n'
        for option in options:
            argString = ''
            argHelp = ''
            if not option.IsArgumentsEmpty():
                for arg in option.GetArgumentsList():
                    argName = arg.GetName()
                    if arg.HasValidValues():
                        values = arg.GetValidValues()
                        if len(values) > 0:
                            argName = ''
                            for value in values.keys():
                                if len(argName) > 0:
                                    argName = argName + '|'
                                argName = argName + value

                    if arg.IsOptional():
                        argString = argString + ' [%s]' % argName
                    else:
                        argString = argString + ' <%s>' % argName
                    if arg.GetHelpSize() > 0:
                        argHelp = argHelp + '      %s\n' % argName
                        j = 0
                        while j < arg.GetHelpSize():
                            argHelp = argHelp + '         %s\n' % arg.GetHelp(j)
                            j = j + 1

            groupString = ''
            if option.HasGroup():
                groupString = ' (group=%s)' % option.GetGroupName()
            start = ''
            end = ''
            if option.IsOptional():
                start = '['
                end = ']'
            else:
                start = '<'
                end = '>'
            usageStr = usageStr + '   ' + start + command.GetOptionPrefix()
            usageStr = usageStr + option.GetName() + argString
            usageStr = usageStr + end + groupString + '\n'
            j = 0
            while j < option.GetHelpSize():
                usageStr = usageStr + '      %s\n' % option.GetHelp(j)
                j = j + 1

            if len(argHelp) > 0:
                usageStr = usageStr + '\n' + argHelp
            rejected = option.GetRejectedOptions()
            required = option.GetRequiredOptions()
            if len(rejected) > 0:
                usageStr = usageStr + '      REJECTED : '
                for rejStr in rejected:
                    usageStr = usageStr + command.GetOptionPrefix() + rejStr + ' '

                usageStr = usageStr + '\n'
            if len(required) > 0:
                usageStr = usageStr + '      REQUIRED : '
                for reqStr in required:
                    usageStr = usageStr + command.GetOptionPrefix() + reqStr + ' '

                usageStr = usageStr + '\n'

    return usageStr


def GetCommandsFromFile(xmlFile, xmlGrammar=None):
    from xml.dom.minidom import parse
    document = parse(xmlFile)
    return _parseDocument(document)


def GetCommandsFromXml(xmlText, xmlGrammar=None):
    from xml.dom.minidom import parseString
    document = parseString(xmlText)
    return _parseDocument(document)


def ParseCommandByObject--- This code section failed: ---

 176       0  BUILD_MAP_4           4 

 177       3  LOAD_CONST            1  ''
           6  LOAD_CONST            2  'displayFile'
           9  STORE_MAP        

 178      10  BUILD_MAP_0           0 
          13  LOAD_CONST            3  'displayParams'
          16  STORE_MAP        

 179      17  BUILD_MAP_0           0 
          20  LOAD_CONST            4  'parameters'
          23  STORE_MAP        

 180      24  BUILD_LIST_0          0 
          27  LOAD_CONST            5  'usedArgs'
          30  STORE_MAP        
          31  STORE_FAST            2  'result'

 183      34  LOAD_GLOBAL           0  'len'
          37  LOAD_FAST             1  'args'
          40  CALL_FUNCTION_1       1 
          43  LOAD_CONST            6  ''
          46  COMPARE_OP            2  '=='
          49  POP_JUMP_IF_FALSE    65  'to 65'

 184      52  LOAD_GLOBAL           1  'False'
          55  LOAD_CONST            7  '* Invalid arguments'
          58  LOAD_FAST             2  'result'
          61  BUILD_TUPLE_3         3 
          64  RETURN_END_IF    
        65_0  COME_FROM                '49'

 187      65  LOAD_FAST             0  'command'
          68  LOAD_ATTR             2  'GetDefaultDisplay'
          71  CALL_FUNCTION_0       0 
          74  LOAD_ATTR             3  'encode'
          77  LOAD_CONST            8  'utf_8'
          80  CALL_FUNCTION_1       1 
          83  LOAD_FAST             2  'result'
          86  LOAD_CONST            2  'displayFile'
          89  STORE_SUBSCR     

 188      90  LOAD_FAST             0  'command'
          93  LOAD_ATTR             4  'CopyDefaultDisplayParameters'
          96  CALL_FUNCTION_0       0 
          99  LOAD_FAST             2  'result'
         102  LOAD_CONST            3  'displayParams'
         105  STORE_SUBSCR     

 191     106  LOAD_FAST             0  'command'
         109  LOAD_ATTR             5  'CopyOptions'
         112  CALL_FUNCTION_0       0 
         115  STORE_FAST            3  'cmdOptions'

 192     118  LOAD_FAST             0  'command'
         121  LOAD_ATTR             6  'CopyArguments'
         124  CALL_FUNCTION_0       0 
         127  STORE_FAST            4  'cmdArguments'

 193     130  LOAD_FAST             0  'command'
         133  LOAD_ATTR             7  'CopyData'
         136  CALL_FUNCTION_0       0 
         139  STORE_FAST            5  'cmdData'

 195     142  LOAD_CONST            9  1
         145  STORE_FAST            6  'numUsedArgs'

 196     148  SETUP_LOOP           31  'to 182'
         151  LOAD_FAST             1  'args'
         154  GET_ITER         
         155  FOR_ITER             23  'to 181'
         158  STORE_FAST            7  'cmdArg'

 197     161  LOAD_FAST             2  'result'
         164  LOAD_CONST            5  'usedArgs'
         167  BINARY_SUBSCR    
         168  LOAD_ATTR             8  'append'
         171  LOAD_GLOBAL           1  'False'
         174  CALL_FUNCTION_1       1 
         177  POP_TOP          
         178  JUMP_BACK           155  'to 155'
         181  POP_BLOCK        
       182_0  COME_FROM                '148'

 198     182  LOAD_GLOBAL           9  'True'
         185  LOAD_FAST             2  'result'
         188  LOAD_CONST            5  'usedArgs'
         191  BINARY_SUBSCR    
         192  LOAD_CONST            6  ''
         195  STORE_SUBSCR     

 201     196  BUILD_MAP_0           0 
         199  STORE_FAST            8  'groups'

 202     202  LOAD_GLOBAL           0  'len'
         205  LOAD_FAST             4  'cmdArguments'
         208  CALL_FUNCTION_1       1 
         211  LOAD_CONST            6  ''
         214  COMPARE_OP            4  '>'
         217  POP_JUMP_IF_FALSE   485  'to 485'

 203     220  LOAD_FAST             6  'numUsedArgs'
         223  STORE_FAST            9  'origArgs'

 204     226  LOAD_GLOBAL          10  '_parseArguments'
         229  LOAD_FAST             5  'cmdData'

 205     232  LOAD_FAST             4  'cmdArguments'

 206     235  LOAD_FAST             1  'args'
         238  LOAD_FAST             6  'numUsedArgs'
         241  SLICE+1          

 207     242  LOAD_GLOBAL           0  'len'
         245  LOAD_FAST             3  'cmdOptions'
         248  CALL_FUNCTION_1       1 
         251  LOAD_CONST            6  ''
         254  COMPARE_OP            2  '=='

 208     257  LOAD_FAST             0  'command'
         260  LOAD_ATTR            11  'GetOptionPrefix'
         263  CALL_FUNCTION_0       0 

 209     266  LOAD_FAST             2  'result'
         269  CALL_FUNCTION_6       6 
         272  UNPACK_SEQUENCE_3     3 
         275  STORE_FAST           10  'success'
         278  STORE_FAST           11  'parsedArgs'
         281  STORE_FAST           12  'outputStr'

 210     284  LOAD_FAST            10  'success'
         287  POP_JUMP_IF_TRUE    303  'to 303'

 211     290  LOAD_GLOBAL           1  'False'
         293  LOAD_FAST            12  'outputStr'
         296  LOAD_FAST             2  'result'
         299  BUILD_TUPLE_3         3 
         302  RETURN_END_IF    
       303_0  COME_FROM                '287'

 213     303  LOAD_FAST             6  'numUsedArgs'
         306  LOAD_FAST            11  'parsedArgs'
         309  BINARY_ADD       
         310  STORE_FAST            6  'numUsedArgs'

 215     313  LOAD_FAST             9  'origArgs'
         316  LOAD_FAST             6  'numUsedArgs'
         319  COMPARE_OP            3  '!='
         322  POP_JUMP_IF_FALSE   485  'to 485'

 217     325  SETUP_LOOP          154  'to 482'
         328  LOAD_FAST             4  'cmdArguments'
         331  GET_ITER         
         332  FOR_ITER            143  'to 478'
         335  STORE_FAST            7  'cmdArg'

 218     338  LOAD_FAST             9  'origArgs'
         341  LOAD_FAST             6  'numUsedArgs'
         344  COMPARE_OP            2  '=='
         347  POP_JUMP_IF_FALSE   354  'to 354'

 220     350  BREAK_LOOP       
         351  JUMP_FORWARD          0  'to 354'
       354_0  COME_FROM                '351'

 223     354  LOAD_GLOBAL           9  'True'
         357  LOAD_FAST             2  'result'
         360  LOAD_CONST            5  'usedArgs'
         363  BINARY_SUBSCR    
         364  LOAD_FAST             9  'origArgs'
         367  STORE_SUBSCR     

 225     368  LOAD_FAST             7  'cmdArg'
         371  LOAD_ATTR            12  'HasGroup'
         374  CALL_FUNCTION_0       0 
         377  POP_JUMP_IF_FALSE   465  'to 465'

 226     380  LOAD_FAST             8  'groups'
         383  LOAD_ATTR            13  'has_key'
         386  LOAD_FAST             7  'cmdArg'
         389  LOAD_ATTR            14  'GetGroupName'
         392  CALL_FUNCTION_0       0 
         395  CALL_FUNCTION_1       1 
         398  POP_JUMP_IF_FALSE   440  'to 440'

 227     401  LOAD_GLOBAL           1  'False'

 228     404  LOAD_CONST           10  "* Argument '%s' and '%s' are mutually exclusive"
         407  LOAD_FAST             7  'cmdArg'
         410  LOAD_ATTR            15  'GetName'
         413  CALL_FUNCTION_0       0 
         416  LOAD_FAST             8  'groups'
         419  LOAD_FAST             7  'cmdArg'
         422  LOAD_ATTR            14  'GetGroupName'
         425  CALL_FUNCTION_0       0 
         428  BINARY_SUBSCR    
         429  BUILD_TUPLE_2         2 
         432  BINARY_MODULO    

 229     433  LOAD_FAST             2  'result'
         436  BUILD_TUPLE_3         3 
         439  RETURN_END_IF    
       440_0  COME_FROM                '398'

 232     440  LOAD_FAST             7  'cmdArg'
         443  LOAD_ATTR            15  'GetName'
         446  CALL_FUNCTION_0       0 
         449  LOAD_FAST             8  'groups'
         452  LOAD_FAST             7  'cmdArg'
         455  LOAD_ATTR            14  'GetGroupName'
         458  CALL_FUNCTION_0       0 
         461  STORE_SUBSCR     
         462  JUMP_FORWARD          0  'to 465'
       465_0  COME_FROM                '462'

 234     465  LOAD_FAST             9  'origArgs'
         468  LOAD_CONST            9  1
         471  BINARY_ADD       
         472  STORE_FAST            9  'origArgs'
         475  JUMP_BACK           332  'to 332'
         478  POP_BLOCK        
       479_0  COME_FROM                '325'
         479  JUMP_ABSOLUTE       485  'to 485'
         482  JUMP_FORWARD          0  'to 485'
       485_0  COME_FROM                '482'

 237     485  SETUP_LOOP          225  'to 713'
         488  LOAD_FAST             3  'cmdOptions'
         491  GET_ITER         
         492  FOR_ITER            217  'to 712'
         495  STORE_FAST           13  'cmdOption'

 238     498  LOAD_FAST             6  'numUsedArgs'
         501  STORE_FAST            9  'origArgs'

 239     504  LOAD_GLOBAL          16  '_parseOption'
         507  LOAD_FAST             5  'cmdData'

 240     510  LOAD_FAST            13  'cmdOption'

 241     513  LOAD_FAST             1  'args'

 242     516  LOAD_FAST             0  'command'
         519  LOAD_ATTR            11  'GetOptionPrefix'
         522  CALL_FUNCTION_0       0 

 243     525  LOAD_FAST             2  'result'
         528  CALL_FUNCTION_5       5 
         531  UNPACK_SEQUENCE_3     3 
         534  STORE_FAST           10  'success'
         537  STORE_FAST           11  'parsedArgs'
         540  STORE_FAST           12  'outputStr'

 244     543  LOAD_FAST            10  'success'
         546  POP_JUMP_IF_TRUE    562  'to 562'

 245     549  LOAD_GLOBAL           1  'False'
         552  LOAD_FAST            12  'outputStr'
         555  LOAD_FAST             2  'result'
         558  BUILD_TUPLE_3         3 
         561  RETURN_END_IF    
       562_0  COME_FROM                '546'

 248     562  LOAD_FAST             6  'numUsedArgs'
         565  LOAD_FAST            11  'parsedArgs'
         568  BINARY_ADD       
         569  STORE_FAST            6  'numUsedArgs'

 250     572  LOAD_FAST             9  'origArgs'
         575  LOAD_FAST             6  'numUsedArgs'
         578  COMPARE_OP            3  '!='
         581  POP_JUMP_IF_FALSE   492  'to 492'

 252     584  LOAD_FAST            13  'cmdOption'
         587  LOAD_ATTR            12  'HasGroup'
         590  CALL_FUNCTION_0       0 
         593  POP_JUMP_IF_FALSE   709  'to 709'

 253     596  LOAD_FAST             8  'groups'
         599  LOAD_ATTR            13  'has_key'
         602  LOAD_FAST            13  'cmdOption'
         605  LOAD_ATTR            14  'GetGroupName'
         608  CALL_FUNCTION_0       0 
         611  CALL_FUNCTION_1       1 
         614  POP_JUMP_IF_FALSE   665  'to 665'

 254     617  LOAD_GLOBAL           1  'False'

 255     620  LOAD_CONST           11  "* Option '%s%s' and '%s' are mutually exclusive"
         623  LOAD_FAST             0  'command'
         626  LOAD_ATTR            11  'GetOptionPrefix'
         629  CALL_FUNCTION_0       0 
         632  LOAD_FAST            13  'cmdOption'
         635  LOAD_ATTR            15  'GetName'
         638  CALL_FUNCTION_0       0 
         641  LOAD_FAST             8  'groups'
         644  LOAD_FAST            13  'cmdOption'
         647  LOAD_ATTR            14  'GetGroupName'
         650  CALL_FUNCTION_0       0 
         653  BINARY_SUBSCR    
         654  BUILD_TUPLE_3         3 
         657  BINARY_MODULO    

 256     658  LOAD_FAST             2  'result'
         661  BUILD_TUPLE_3         3 
         664  RETURN_END_IF    
       665_0  COME_FROM                '614'

 259     665  LOAD_CONST           12  '%s%s'
         668  LOAD_FAST             0  'command'
         671  LOAD_ATTR            11  'GetOptionPrefix'
         674  CALL_FUNCTION_0       0 
         677  LOAD_FAST            13  'cmdOption'
         680  LOAD_ATTR            15  'GetName'
         683  CALL_FUNCTION_0       0 
         686  BUILD_TUPLE_2         2 
         689  BINARY_MODULO    
         690  LOAD_FAST             8  'groups'
         693  LOAD_FAST            13  'cmdOption'
         696  LOAD_ATTR            14  'GetGroupName'
         699  CALL_FUNCTION_0       0 
         702  STORE_SUBSCR     
         703  JUMP_ABSOLUTE       709  'to 709'
         706  JUMP_BACK           492  'to 492'
         709  JUMP_BACK           492  'to 492'
         712  POP_BLOCK        
       713_0  COME_FROM                '485'

 262     713  SETUP_LOOP          169  'to 885'
         716  LOAD_FAST             3  'cmdOptions'
         719  GET_ITER         
         720  FOR_ITER            161  'to 884'
         723  STORE_FAST           13  'cmdOption'

 263     726  LOAD_FAST            13  'cmdOption'
         729  LOAD_ATTR            17  'WasFound'
         732  CALL_FUNCTION_0       0 
         735  POP_JUMP_IF_FALSE   720  'to 720'

 264     738  LOAD_FAST            13  'cmdOption'
         741  LOAD_ATTR            18  'GetRequiredOptions'
         744  CALL_FUNCTION_0       0 
         747  STORE_FAST           14  'requiredList'

 265     750  SETUP_LOOP          128  'to 881'
         753  LOAD_FAST            14  'requiredList'
         756  GET_ITER         
         757  FOR_ITER            117  'to 877'
         760  STORE_FAST           15  'reqOpt'

 266     763  LOAD_GLOBAL           1  'False'
         766  STORE_FAST           16  'foundOption'

 267     769  SETUP_LOOP           67  'to 839'
         772  LOAD_FAST             3  'cmdOptions'
         775  GET_ITER         
         776  FOR_ITER             59  'to 838'
         779  STORE_FAST           17  'optionToChange'

 268     782  LOAD_FAST            15  'reqOpt'
         785  LOAD_ATTR            19  'lower'
         788  CALL_FUNCTION_0       0 
         791  LOAD_FAST            17  'optionToChange'
         794  LOAD_ATTR            15  'GetName'
         797  CALL_FUNCTION_0       0 
         800  LOAD_ATTR            19  'lower'
         803  CALL_FUNCTION_0       0 
         806  COMPARE_OP            2  '=='
         809  POP_JUMP_IF_FALSE   776  'to 776'

 270     812  LOAD_GLOBAL           9  'True'
         815  STORE_FAST           16  'foundOption'

 271     818  LOAD_FAST            17  'optionToChange'
         821  LOAD_ATTR            20  'SetOptional'
         824  LOAD_GLOBAL           1  'False'
         827  CALL_FUNCTION_1       1 
         830  POP_TOP          

 272     831  BREAK_LOOP       
         832  JUMP_BACK           776  'to 776'
         835  JUMP_BACK           776  'to 776'
         838  POP_BLOCK        
       839_0  COME_FROM                '769'

 274     839  LOAD_FAST            16  'foundOption'
         842  POP_JUMP_IF_TRUE    757  'to 757'

 275     845  LOAD_GLOBAL           1  'False'

 276     848  LOAD_CONST           13  "* Option '%s%s' not found"
         851  LOAD_FAST             0  'command'
         854  LOAD_ATTR            11  'GetOptionPrefix'
         857  CALL_FUNCTION_0       0 
         860  LOAD_FAST            15  'reqOpt'
         863  BUILD_TUPLE_2         2 
         866  BINARY_MODULO    

 277     867  LOAD_FAST             2  'result'
         870  BUILD_TUPLE_3         3 
         873  RETURN_END_IF    
       874_0  COME_FROM                '842'
         874  JUMP_BACK           757  'to 757'
         877  POP_BLOCK        
       878_0  COME_FROM                '750'
         878  JUMP_BACK           720  'to 720'
         881  JUMP_BACK           720  'to 720'
         884  POP_BLOCK        
       885_0  COME_FROM                '713'

 280     885  SETUP_LOOP          177  'to 1065'
         888  LOAD_FAST             3  'cmdOptions'
         891  GET_ITER         
         892  FOR_ITER            169  'to 1064'
         895  STORE_FAST           13  'cmdOption'

 281     898  LOAD_FAST            13  'cmdOption'
         901  LOAD_ATTR            17  'WasFound'
         904  CALL_FUNCTION_0       0 
         907  POP_JUMP_IF_TRUE    892  'to 892'

 283     910  LOAD_FAST            13  'cmdOption'
         913  LOAD_ATTR            21  'IsOptional'
         916  CALL_FUNCTION_0       0 
         919  POP_JUMP_IF_TRUE   1061  'to 1061'

 285     922  LOAD_FAST            13  'cmdOption'
         925  LOAD_ATTR            12  'HasGroup'
         928  CALL_FUNCTION_0       0 
         931  POP_JUMP_IF_FALSE   964  'to 964'

 287     934  LOAD_FAST             8  'groups'
         937  LOAD_ATTR            13  'has_key'
         940  LOAD_FAST            13  'cmdOption'
         943  LOAD_ATTR            14  'GetGroupName'
         946  CALL_FUNCTION_0       0 
         949  CALL_FUNCTION_1       1 
       952_0  COME_FROM                '919'
       952_1  COME_FROM                '907'
         952  POP_JUMP_IF_FALSE   964  'to 964'

 289     955  CONTINUE            892  'to 892'
         958  JUMP_ABSOLUTE       964  'to 964'
         961  JUMP_FORWARD          0  'to 964'
       964_0  COME_FROM                '961'

 293     964  LOAD_FAST            13  'cmdOption'
         967  LOAD_ATTR            12  'HasGroup'
         970  CALL_FUNCTION_0       0 
         973  POP_JUMP_IF_FALSE  1020  'to 1020'

 294     976  LOAD_GLOBAL           1  'False'

 295     979  LOAD_CONST           14  "* Option '%s%s' (or another from the '%s' group) must be specified"
         982  LOAD_FAST             0  'command'
         985  LOAD_ATTR            11  'GetOptionPrefix'
         988  CALL_FUNCTION_0       0 
         991  LOAD_FAST            13  'cmdOption'
         994  LOAD_ATTR            15  'GetName'
         997  CALL_FUNCTION_0       0 
        1000  LOAD_FAST            13  'cmdOption'
        1003  LOAD_ATTR            14  'GetGroupName'
        1006  CALL_FUNCTION_0       0 
        1009  BUILD_TUPLE_3         3 
        1012  BINARY_MODULO    

 296    1013  LOAD_FAST             2  'result'
        1016  BUILD_TUPLE_3         3 
        1019  RETURN_END_IF    
      1020_0  COME_FROM                '973'

 298    1020  LOAD_GLOBAL           1  'False'

 299    1023  LOAD_CONST           15  "* Option '%s%s' must be specified"
        1026  LOAD_FAST             0  'command'
        1029  LOAD_ATTR            11  'GetOptionPrefix'
        1032  CALL_FUNCTION_0       0 
        1035  LOAD_FAST            13  'cmdOption'
        1038  LOAD_ATTR            15  'GetName'
        1041  CALL_FUNCTION_0       0 
        1044  BUILD_TUPLE_2         2 
        1047  BINARY_MODULO    

 300    1048  LOAD_FAST             2  'result'
        1051  BUILD_TUPLE_3         3 
        1054  RETURN_VALUE     
        1055  JUMP_ABSOLUTE      1061  'to 1061'
        1058  JUMP_BACK           892  'to 892'
        1061  JUMP_BACK           892  'to 892'
        1064  POP_BLOCK        
      1065_0  COME_FROM                '885'

 303    1065  SETUP_LOOP          215  'to 1283'
        1068  LOAD_FAST             3  'cmdOptions'
        1071  GET_ITER         
        1072  FOR_ITER            207  'to 1282'
        1075  STORE_FAST           13  'cmdOption'

 304    1078  LOAD_FAST            13  'cmdOption'
        1081  LOAD_ATTR            17  'WasFound'
        1084  CALL_FUNCTION_0       0 
        1087  POP_JUMP_IF_FALSE  1072  'to 1072'

 305    1090  LOAD_FAST            13  'cmdOption'
        1093  LOAD_ATTR            22  'GetRejectedOptions'
        1096  CALL_FUNCTION_0       0 
        1099  STORE_FAST           18  'rejectedList'

 306    1102  SETUP_LOOP          174  'to 1279'
        1105  LOAD_FAST            18  'rejectedList'
        1108  GET_ITER         
        1109  FOR_ITER            163  'to 1275'
        1112  STORE_FAST           19  'rejOpt'

 307    1115  LOAD_GLOBAL           1  'False'
        1118  STORE_FAST           16  'foundOption'

 308    1121  SETUP_LOOP          113  'to 1237'
        1124  LOAD_FAST             3  'cmdOptions'
        1127  GET_ITER         
        1128  FOR_ITER            105  'to 1236'
        1131  STORE_FAST           17  'optionToChange'

 309    1134  LOAD_FAST            19  'rejOpt'
        1137  LOAD_ATTR            19  'lower'
        1140  CALL_FUNCTION_0       0 
        1143  LOAD_FAST            17  'optionToChange'
        1146  LOAD_ATTR            15  'GetName'
        1149  CALL_FUNCTION_0       0 
        1152  LOAD_ATTR            19  'lower'
        1155  CALL_FUNCTION_0       0 
        1158  COMPARE_OP            2  '=='
        1161  POP_JUMP_IF_FALSE  1128  'to 1128'

 311    1164  LOAD_GLOBAL           9  'True'
        1167  STORE_FAST           16  'foundOption'

 312    1170  LOAD_FAST            17  'optionToChange'
        1173  LOAD_ATTR            17  'WasFound'
        1176  CALL_FUNCTION_0       0 
        1179  POP_JUMP_IF_FALSE  1229  'to 1229'

 313    1182  LOAD_GLOBAL           1  'False'

 314    1185  LOAD_CONST           16  "* Option '%s%s' may not be specified when using option '%s%s'"
        1188  LOAD_FAST             0  'command'
        1191  LOAD_ATTR            11  'GetOptionPrefix'
        1194  CALL_FUNCTION_0       0 
        1197  LOAD_FAST            19  'rejOpt'
        1200  LOAD_FAST             0  'command'
        1203  LOAD_ATTR            11  'GetOptionPrefix'
        1206  CALL_FUNCTION_0       0 
        1209  LOAD_FAST            13  'cmdOption'
        1212  LOAD_ATTR            15  'GetName'
        1215  CALL_FUNCTION_0       0 
        1218  BUILD_TUPLE_4         4 
        1221  BINARY_MODULO    

 315    1222  LOAD_FAST             2  'result'
        1225  BUILD_TUPLE_3         3 
        1228  RETURN_END_IF    
      1229_0  COME_FROM                '1179'

 316    1229  BREAK_LOOP       
        1230  JUMP_BACK          1128  'to 1128'
        1233  JUMP_BACK          1128  'to 1128'
        1236  POP_BLOCK        
      1237_0  COME_FROM                '1121'

 318    1237  LOAD_FAST            16  'foundOption'
        1240  POP_JUMP_IF_TRUE   1109  'to 1109'

 319    1243  LOAD_GLOBAL           1  'False'

 320    1246  LOAD_CONST           13  "* Option '%s%s' not found"
        1249  LOAD_FAST             0  'command'
        1252  LOAD_ATTR            11  'GetOptionPrefix'
        1255  CALL_FUNCTION_0       0 
        1258  LOAD_FAST            19  'rejOpt'
        1261  BUILD_TUPLE_2         2 
        1264  BINARY_MODULO    

 321    1265  LOAD_FAST             2  'result'
        1268  BUILD_TUPLE_3         3 
        1271  RETURN_END_IF    
      1272_0  COME_FROM                '1240'
        1272  JUMP_BACK          1109  'to 1109'
        1275  POP_BLOCK        
      1276_0  COME_FROM                '1102'
        1276  JUMP_BACK          1072  'to 1072'
        1279  JUMP_BACK          1072  'to 1072'
        1282  POP_BLOCK        
      1283_0  COME_FROM                '1065'

 323    1283  LOAD_FAST             6  'numUsedArgs'
        1286  LOAD_GLOBAL           0  'len'
        1289  LOAD_FAST             1  'args'
        1292  CALL_FUNCTION_1       1 
        1295  COMPARE_OP            3  '!='
        1298  POP_JUMP_IF_FALSE  1416  'to 1416'

 325    1301  LOAD_CONST            1  ''
        1304  STORE_FAST           20  'extraArg'

 326    1307  LOAD_CONST            6  ''
        1310  STORE_FAST           21  'i'

 327    1313  SETUP_LOOP           68  'to 1384'
        1316  LOAD_FAST            21  'i'
        1319  LOAD_GLOBAL           0  'len'
        1322  LOAD_FAST             2  'result'
        1325  LOAD_CONST            5  'usedArgs'
        1328  BINARY_SUBSCR    
        1329  CALL_FUNCTION_1       1 
        1332  COMPARE_OP            0  '<'
        1335  POP_JUMP_IF_FALSE  1383  'to 1383'

 328    1338  LOAD_FAST             2  'result'
        1341  LOAD_CONST            5  'usedArgs'
        1344  BINARY_SUBSCR    
        1345  LOAD_FAST            21  'i'
        1348  BINARY_SUBSCR    
        1349  POP_JUMP_IF_TRUE   1370  'to 1370'

 329    1352  LOAD_FAST             1  'args'
        1355  LOAD_FAST            21  'i'
        1358  BINARY_SUBSCR    
        1359  LOAD_CONST           17  'value'
        1362  BINARY_SUBSCR    
        1363  STORE_FAST           20  'extraArg'

 330    1366  BREAK_LOOP       
        1367  JUMP_FORWARD          0  'to 1370'
      1370_0  COME_FROM                '1367'

 331    1370  LOAD_FAST            21  'i'
        1373  LOAD_CONST            9  1
        1376  BINARY_ADD       
        1377  STORE_FAST           21  'i'
        1380  JUMP_BACK          1316  'to 1316'
        1383  POP_BLOCK        
      1384_0  COME_FROM                '1313'

 333    1384  LOAD_GLOBAL           1  'False'
        1387  LOAD_CONST           18  '* Invalid option/argument (%s) or too many parameters (used %u args of total %u)'
        1390  LOAD_FAST            20  'extraArg'
        1393  LOAD_FAST             6  'numUsedArgs'
        1396  LOAD_GLOBAL           0  'len'
        1399  LOAD_FAST             1  'args'
        1402  CALL_FUNCTION_1       1 
        1405  BUILD_TUPLE_3         3 
        1408  BINARY_MODULO    
        1409  LOAD_FAST             2  'result'
        1412  BUILD_TUPLE_3         3 
        1415  RETURN_END_IF    
      1416_0  COME_FROM                '1298'

 336    1416  SETUP_LOOP           49  'to 1468'
        1419  LOAD_FAST             5  'cmdData'
        1422  GET_ITER         
        1423  FOR_ITER             41  'to 1467'
        1426  STORE_FAST           22  'data'

 337    1429  LOAD_FAST            22  'data'
        1432  LOAD_ATTR            23  'GetValue'
        1435  CALL_FUNCTION_0       0 
        1438  LOAD_FAST             2  'result'
        1441  LOAD_CONST            4  'parameters'
        1444  BINARY_SUBSCR    
        1445  LOAD_FAST            22  'data'
        1448  LOAD_ATTR            15  'GetName'
        1451  CALL_FUNCTION_0       0 
        1454  LOAD_ATTR             3  'encode'
        1457  LOAD_CONST            8  'utf_8'
        1460  CALL_FUNCTION_1       1 
        1463  STORE_SUBSCR     
        1464  JUMP_BACK          1423  'to 1423'
        1467  POP_BLOCK        
      1468_0  COME_FROM                '1416'

 339    1468  LOAD_GLOBAL           9  'True'
        1471  LOAD_CONST            1  ''
        1474  LOAD_FAST             2  'result'
        1477  BUILD_TUPLE_3         3 
        1480  RETURN_VALUE     
          -1  RETURN_LAST      

Parse error at or near `JUMP_BACK' instruction at offset 1058


def ParseCommandByXml(cmdXml, cmdId, args):
    cmds = GetCommandsFromXml(cmdXml)
    for cmd in cmds:
        if cmd.GetCommandId() == cmdId:
            return ParseCommandByObject(cmd, args)

    raise RuntimeError('Failed to find command %u in XML' % cmdId)


def _findOption(args, optionPrefix, option, result):
    if len(args) == 0:
        return (
         True, [])
    argsFound = []
    if not option.startswith(optionPrefix):
        raise RuntimeError("* Given option (%s) didn't start with '%s'" % (option, optionPrefix))
    optionIndex = 0
    while optionIndex < len(args):
        if not args[optionIndex]['quoted'] and args[optionIndex]['value'] == option:
            break
        optionIndex = optionIndex + 1

    if optionIndex >= len(args):
        return (
         False, argsFound)
    endIndex = optionIndex
    while endIndex + 1 < len(args):
        if not args[endIndex + 1]['quoted'] and args[endIndex + 1]['value'].startswith(optionPrefix):
            break
        endIndex = endIndex + 1

    result['usedArgs'][optionIndex] = True
    i = optionIndex + 1
    while i <= endIndex:
        result['usedArgs'][i] = True
        argsFound.append(args[i])
        i = i + 1

    return (
     True, argsFound)


def _parseArguments(cmdData, cmdArgs, args, ignoreOptions, optionPrefix, result):
    onArg = 0
    for cmdArg in cmdArgs:
        if onArg >= len(args) or not ignoreOptions and not args[onArg]['quoted'] and args[onArg]['value'].startswith(optionPrefix):
            if not cmdArg.IsOptional():
                if not cmdArg.HasGroup():
                    return (
                     False, 0, "* Argument '%s' must be specified" % cmdArgs.GetName())
        else:
            cmdArg.AppendParameters(result['displayParams'])
            if cmdArg.HasValidValues():
                validValue = False
                values = cmdArg.GetValidValues()
                for value in values.keys():
                    if value.lower() == args[onArg]['value'].lower():
                        validValue = True
                        for paramName in values[value][0].keys():
                            result['displayParams'][paramName.encode('utf_8')] = values[value][0][paramName].encode('utf_8')

                        for dataName in values[value][1].keys():
                            if dataName.lower() == 'display':
                                result['displayFile'] = values[value][1][dataName].encode('utf_8')
                            else:
                                dataFound = False
                                for cmdDataItem in cmdData:
                                    if cmdDataItem.GetName() == dataName:
                                        try:
                                            cmdDataItem.SetValue(values[value][1][dataName])
                                        except RuntimeError as e:
                                            return (
                                             False, 0, str(e))

                                        dataFound = True
                                        break

                                if not dataFound:
                                    return (False, 0, "* Invalid command definition -- data '%s' not found" % dataName)

                if not validValue:
                    return (False, 0, "* Invalid value ('%s') for argument '%s'" % (args[onArg]['value'], cmdArg.GetName()))
            elif len(cmdArg.GetDataName()) > 0:
                dataFound = False
                for cmdDataItem in cmdData:
                    if cmdArg.GetDataName() == cmdDataItem.GetName():
                        try:
                            cmdDataItem.SetValue(args[onArg]['value'])
                        except RuntimeError as e:
                            return (
                             False, 0, str(e))

                        dataFound = True
                        break

                if not dataFound:
                    return (False, 0, "* Invalid command definition -- data '%s' not found" % cmdArg.GetDataName())
            onArg = onArg + 1

    return (True, onArg, '')


def _parseDocument(document):
    commands = []
    pluginList = document.getElementsByTagName('Plugin')
    if len(pluginList) == 0:
        raise RuntimeError('No plugin element found')
    pluginNode = pluginList[0]
    providerName = pluginNode.getAttribute('providerName')
    providerType = pluginNode.getAttribute('providerType')
    if providerType.lower() != 'script':
        raise RuntimeError("A 'providerType' of 'script' must be specified")
    if len(providerName) == 0:
        raise RuntimeError("A 'providerName' must be specified")
    commandNodeList = document.getElementsByTagName('Command')
    if len(commandNodeList) == 0:
        raise RuntimeError("No 'Command' elements found")
    for cmdNode in commandNodeList:
        from XmlCommand import XmlCommand
        cmd = XmlCommand()
        cmd.Initialize(cmdNode)
        cmd.SetCommandScript(providerName)
        commands.append(cmd)

    return commands


def _parseOption(cmdData, cmdOption, args, optionPrefix, result):
    optStr = '%s%s' % (optionPrefix, cmdOption.GetName())
    usedWords = 0
    optionFound, argsFound = _findOption(args, optionPrefix, optStr, result)
    if optionFound:
        cmdOption.SetFound()
        if len(argsFound) < cmdOption.GetMinimumNumArguments() or len(argsFound) > cmdOption.GetMaximumNumArguments():
            if cmdOption.GetMinimumNumArguments() == cmdOption.GetMaximumNumArguments():
                return (False, 0, "* Option '%s' takes %u argument(s)" % (optStr, cmdOption.GetMinimumNumArguments()))
            else:
                return (
                 False, 0, "* Option '%s' takes between %u and %u argument(s)" % (optStr, cmdOption.GetMinimumNumArguments(), cmdOption.GetMaximumNumArguments()))

        cmdOption.AppendParameters(result['displayParams'])
        dataMap = cmdOption.GetSetDataMap()
        for dataName in dataMap.keys():
            if dataName == 'display':
                result['displayFile'] = dataMap[dataName].encode('utf_8')
            else:
                dataFound = False
                for cmdDataItem in cmdData:
                    if dataName == cmdDataItem.GetName():
                        try:
                            cmdDataItem.SetValue(dataMap[dataName])
                        except RuntimeError as e:
                            return (
                             False, 0, str(e))

                        dataFound = True
                        break

                if not dataFound:
                    return (False, 0, "* Invalid command definition -- data '%s' not found" % dataName)

        if not cmdOption.IsArgumentsEmpty():
            success, parsedArgs, outputStr = _parseArguments(cmdData, cmdOption.GetArgumentsList(), argsFound, False, optionPrefix, result)
            if not success:
                return (False, 0, outputStr)
            usedWords = usedWords + parsedArgs
        usedWords = usedWords + 1
    return (
     True, usedWords, '')