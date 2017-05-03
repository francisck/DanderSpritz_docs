# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: PyParse.py
import re
import sys
C_NONE, C_BACKSLASH, C_STRING_FIRST_LINE, C_STRING_NEXT_LINES, C_BRACKET = range(5)
_synchre = re.compile('\n    ^\n    [ \\t]*\n    (?: while\n    |   else\n    |   def\n    |   return\n    |   assert\n    |   break\n    |   class\n    |   continue\n    |   elif\n    |   try\n    |   except\n    |   raise\n    |   import\n    |   yield\n    )\n    \\b\n', re.VERBOSE | re.MULTILINE).search
_junkre = re.compile('\n    [ \\t]*\n    (?: \\# \\S .* )?\n    \\n\n', re.VERBOSE).match
_match_stringre = re.compile('\n    \\""" [^"\\\\]* (?:\n                     (?: \\\\. | "(?!"") )\n                     [^"\\\\]*\n                 )*\n    (?: \\""" )?\n\n|   " [^"\\\\\\n]* (?: \\\\. [^"\\\\\\n]* )* "?\n\n|   \'\'\' [^\'\\\\]* (?:\n                   (?: \\\\. | \'(?!\'\') )\n                   [^\'\\\\]*\n                )*\n    (?: \'\'\' )?\n\n|   \' [^\'\\\\\\n]* (?: \\\\. [^\'\\\\\\n]* )* \'?\n', re.VERBOSE | re.DOTALL).match
_itemre = re.compile('\n    [ \\t]*\n    [^\\s#\\\\]    # if we match, m.end()-1 is the interesting char\n', re.VERBOSE).match
_closere = re.compile('\n    \\s*\n    (?: return\n    |   break\n    |   continue\n    |   raise\n    |   pass\n    )\n    \\b\n', re.VERBOSE).match
_chew_ordinaryre = re.compile('\n    [^[\\](){}#\'"\\\\]+\n', re.VERBOSE).match
_tran = [
 'x'] * 256
for ch in '({[':
    _tran[ord(ch)] = '('

for ch in ')}]':
    _tran[ord(ch)] = ')'

for ch in '"\'\\\n#':
    _tran[ord(ch)] = ch

_tran = ''.join(_tran)
del ch
try:
    UnicodeType = type(unicode(''))
except NameError:
    UnicodeType = None

class Parser:

    def __init__(self, indentwidth, tabwidth):
        self.indentwidth = indentwidth
        self.tabwidth = tabwidth

    def set_str(self, str):
        if type(str) is UnicodeType:
            uniphooey = str
            str = []
            push = str.append
            for raw in map(ord, uniphooey):
                push(raw < 127 and chr(raw) or 'x')

            str = ''.join(str)
        self.str = str
        self.study_level = 0

    def find_good_parse_start(self, is_char_in_string=None, _synchre=_synchre):
        str, pos = self.str, None
        if not is_char_in_string:
            return
        else:
            limit = len(str)
            for tries in range(5):
                i = str.rfind(':\n', 0, limit)
                if i < 0:
                    break
                i = str.rfind('\n', 0, i) + 1
                m = _synchre(str, i, limit)
                if m and not is_char_in_string(m.start()):
                    pos = m.start()
                    break
                limit = i

            if pos is None:
                m = _synchre(str)
                if m and not is_char_in_string(m.start()):
                    pos = m.start()
                return pos
            i = pos + 1
            while 1:
                m = _synchre(str, i)
                if m:
                    s, i = m.span()
                    if not is_char_in_string(s):
                        pos = s
                else:
                    break

            return pos

    def set_lo(self, lo):
        if lo > 0:
            self.str = self.str[lo:]

    def _study1--- This code section failed: ---

 209       0  LOAD_FAST             0  'self'
           3  LOAD_ATTR             0  'study_level'
           6  LOAD_CONST            1  1
           9  COMPARE_OP            5  '>='
          12  POP_JUMP_IF_FALSE    19  'to 19'

 210      15  LOAD_CONST            0  ''
          18  RETURN_END_IF    
        19_0  COME_FROM                '12'

 211      19  LOAD_CONST            1  1
          22  LOAD_FAST             0  'self'
          25  STORE_ATTR            0  'study_level'

 217      28  LOAD_FAST             0  'self'
          31  LOAD_ATTR             1  'str'
          34  STORE_FAST            1  'str'

 218      37  LOAD_FAST             1  'str'
          40  LOAD_ATTR             2  'translate'
          43  LOAD_GLOBAL           3  '_tran'
          46  CALL_FUNCTION_1       1 
          49  STORE_FAST            1  'str'

 219      52  LOAD_FAST             1  'str'
          55  LOAD_ATTR             4  'replace'
          58  LOAD_CONST            2  'xxxxxxxx'
          61  LOAD_CONST            3  'x'
          64  CALL_FUNCTION_2       2 
          67  STORE_FAST            1  'str'

 220      70  LOAD_FAST             1  'str'
          73  LOAD_ATTR             4  'replace'
          76  LOAD_CONST            4  'xxxx'
          79  LOAD_CONST            3  'x'
          82  CALL_FUNCTION_2       2 
          85  STORE_FAST            1  'str'

 221      88  LOAD_FAST             1  'str'
          91  LOAD_ATTR             4  'replace'
          94  LOAD_CONST            5  'xx'
          97  LOAD_CONST            3  'x'
         100  CALL_FUNCTION_2       2 
         103  STORE_FAST            1  'str'

 222     106  LOAD_FAST             1  'str'
         109  LOAD_ATTR             4  'replace'
         112  LOAD_CONST            5  'xx'
         115  LOAD_CONST            3  'x'
         118  CALL_FUNCTION_2       2 
         121  STORE_FAST            1  'str'

 223     124  LOAD_FAST             1  'str'
         127  LOAD_ATTR             4  'replace'
         130  LOAD_CONST            6  '\nx'
         133  LOAD_CONST            7  '\n'
         136  CALL_FUNCTION_2       2 
         139  STORE_FAST            1  'str'

 230     142  LOAD_GLOBAL           5  'C_NONE'
         145  STORE_FAST            2  'continuation'

 231     148  LOAD_CONST            8  ''
         151  DUP_TOP          
         152  STORE_FAST            3  'level'
         155  STORE_FAST            4  'lno'

 232     158  LOAD_CONST            8  ''
         161  BUILD_LIST_1          1 
         164  DUP_TOP          
         165  LOAD_FAST             0  'self'
         168  STORE_ATTR            6  'goodlines'
         171  STORE_FAST            5  'goodlines'

 233     174  LOAD_FAST             5  'goodlines'
         177  LOAD_ATTR             7  'append'
         180  STORE_FAST            6  'push_good'

 234     183  LOAD_CONST            8  ''
         186  LOAD_GLOBAL           8  'len'
         189  LOAD_FAST             1  'str'
         192  CALL_FUNCTION_1       1 
         195  ROT_TWO          
         196  STORE_FAST            7  'i'
         199  STORE_FAST            8  'n'

 235     202  SETUP_LOOP          639  'to 844'
         205  LOAD_FAST             7  'i'
         208  LOAD_FAST             8  'n'
         211  COMPARE_OP            0  '<'
         214  POP_JUMP_IF_FALSE   843  'to 843'

 236     217  LOAD_FAST             1  'str'
         220  LOAD_FAST             7  'i'
         223  BINARY_SUBSCR    
         224  STORE_FAST            9  'ch'

 237     227  LOAD_FAST             7  'i'
         230  LOAD_CONST            1  1
         233  BINARY_ADD       
         234  STORE_FAST            7  'i'

 240     237  LOAD_FAST             9  'ch'
         240  LOAD_CONST            3  'x'
         243  COMPARE_OP            2  '=='
         246  POP_JUMP_IF_FALSE   255  'to 255'

 241     249  CONTINUE            205  'to 205'
         252  JUMP_FORWARD          0  'to 255'
       255_0  COME_FROM                '252'

 243     255  LOAD_FAST             9  'ch'
         258  LOAD_CONST            7  '\n'
         261  COMPARE_OP            2  '=='
         264  POP_JUMP_IF_FALSE   308  'to 308'

 244     267  LOAD_FAST             4  'lno'
         270  LOAD_CONST            1  1
         273  BINARY_ADD       
         274  STORE_FAST            4  'lno'

 245     277  LOAD_FAST             3  'level'
         280  LOAD_CONST            8  ''
         283  COMPARE_OP            2  '=='
         286  POP_JUMP_IF_FALSE   205  'to 205'

 246     289  LOAD_FAST             6  'push_good'
         292  LOAD_FAST             4  'lno'
         295  CALL_FUNCTION_1       1 
         298  POP_TOP          
         299  JUMP_BACK           205  'to 205'

 248     302  CONTINUE            205  'to 205'
         305  JUMP_FORWARD          0  'to 308'
       308_0  COME_FROM                '305'

 250     308  LOAD_FAST             9  'ch'
         311  LOAD_CONST            9  '('
         314  COMPARE_OP            2  '=='
         317  POP_JUMP_IF_FALSE   336  'to 336'

 251     320  LOAD_FAST             3  'level'
         323  LOAD_CONST            1  1
         326  BINARY_ADD       
         327  STORE_FAST            3  'level'

 252     330  CONTINUE            205  'to 205'
         333  JUMP_FORWARD          0  'to 336'
       336_0  COME_FROM                '333'

 254     336  LOAD_FAST             9  'ch'
         339  LOAD_CONST           10  ')'
         342  COMPARE_OP            2  '=='
         345  POP_JUMP_IF_FALSE   373  'to 373'

 255     348  LOAD_FAST             3  'level'
         351  POP_JUMP_IF_FALSE   205  'to 205'

 256     354  LOAD_FAST             3  'level'
         357  LOAD_CONST            1  1
         360  BINARY_SUBTRACT  
         361  STORE_FAST            3  'level'
         364  JUMP_BACK           205  'to 205'

 258     367  CONTINUE            205  'to 205'
         370  JUMP_FORWARD          0  'to 373'
       373_0  COME_FROM                '370'

 260     373  LOAD_FAST             9  'ch'
         376  LOAD_CONST           11  '"'
         379  COMPARE_OP            2  '=='
         382  POP_JUMP_IF_TRUE    397  'to 397'
         385  LOAD_FAST             9  'ch'
         388  LOAD_CONST           12  "'"
         391  COMPARE_OP            2  '=='
       394_0  COME_FROM                '382'
         394  POP_JUMP_IF_FALSE   740  'to 740'

 262     397  LOAD_FAST             9  'ch'
         400  STORE_FAST           10  'quote'

 263     403  LOAD_FAST             1  'str'
         406  LOAD_FAST             7  'i'
         409  LOAD_CONST            1  1
         412  BINARY_SUBTRACT  
         413  LOAD_FAST             7  'i'
         416  LOAD_CONST           13  2
         419  BINARY_ADD       
         420  SLICE+3          
         421  LOAD_FAST            10  'quote'
         424  LOAD_CONST           14  3
         427  BINARY_MULTIPLY  
         428  COMPARE_OP            2  '=='
         431  POP_JUMP_IF_FALSE   447  'to 447'

 264     434  LOAD_FAST            10  'quote'
         437  LOAD_CONST           14  3
         440  BINARY_MULTIPLY  
         441  STORE_FAST           10  'quote'
         444  JUMP_FORWARD          0  'to 447'
       447_0  COME_FROM                '444'

 265     447  LOAD_FAST             4  'lno'
         450  STORE_FAST           11  'firstlno'

 266     453  LOAD_GLOBAL           8  'len'
         456  LOAD_FAST            10  'quote'
         459  CALL_FUNCTION_1       1 
         462  LOAD_CONST            1  1
         465  BINARY_SUBTRACT  
         466  STORE_FAST           12  'w'

 267     469  LOAD_FAST             7  'i'
         472  LOAD_FAST            12  'w'
         475  BINARY_ADD       
         476  STORE_FAST            7  'i'

 268     479  SETUP_LOOP          252  'to 734'
         482  LOAD_FAST             7  'i'
         485  LOAD_FAST             8  'n'
         488  COMPARE_OP            0  '<'
         491  POP_JUMP_IF_FALSE   702  'to 702'

 269     494  LOAD_FAST             1  'str'
         497  LOAD_FAST             7  'i'
         500  BINARY_SUBSCR    
         501  STORE_FAST            9  'ch'

 270     504  LOAD_FAST             7  'i'
         507  LOAD_CONST            1  1
         510  BINARY_ADD       
         511  STORE_FAST            7  'i'

 272     514  LOAD_FAST             9  'ch'
         517  LOAD_CONST            3  'x'
         520  COMPARE_OP            2  '=='
         523  POP_JUMP_IF_FALSE   532  'to 532'

 273     526  CONTINUE            482  'to 482'
         529  JUMP_FORWARD          0  'to 532'
       532_0  COME_FROM                '529'

 275     532  LOAD_FAST             1  'str'
         535  LOAD_FAST             7  'i'
         538  LOAD_CONST            1  1
         541  BINARY_SUBTRACT  
         542  LOAD_FAST             7  'i'
         545  LOAD_FAST            12  'w'
         548  BINARY_ADD       
         549  SLICE+3          
         550  LOAD_FAST            10  'quote'
         553  COMPARE_OP            2  '=='
         556  POP_JUMP_IF_FALSE   573  'to 573'

 276     559  LOAD_FAST             7  'i'
         562  LOAD_FAST            12  'w'
         565  BINARY_ADD       
         566  STORE_FAST            7  'i'

 277     569  BREAK_LOOP       
         570  JUMP_FORWARD          0  'to 573'
       573_0  COME_FROM                '570'

 279     573  LOAD_FAST             9  'ch'
         576  LOAD_CONST            7  '\n'
         579  COMPARE_OP            2  '=='
         582  POP_JUMP_IF_FALSE   642  'to 642'

 280     585  LOAD_FAST             4  'lno'
         588  LOAD_CONST            1  1
         591  BINARY_ADD       
         592  STORE_FAST            4  'lno'

 281     595  LOAD_FAST            12  'w'
         598  LOAD_CONST            8  ''
         601  COMPARE_OP            2  '=='
         604  POP_JUMP_IF_FALSE   482  'to 482'

 283     607  LOAD_FAST             3  'level'
         610  LOAD_CONST            8  ''
         613  COMPARE_OP            2  '=='
         616  POP_JUMP_IF_FALSE   632  'to 632'

 284     619  LOAD_FAST             6  'push_good'
         622  LOAD_FAST             4  'lno'
         625  CALL_FUNCTION_1       1 
         628  POP_TOP          
         629  JUMP_FORWARD          0  'to 632'
       632_0  COME_FROM                '629'

 285     632  BREAK_LOOP       
         633  JUMP_BACK           482  'to 482'

 286     636  CONTINUE            482  'to 482'
         639  JUMP_FORWARD          0  'to 642'
       642_0  COME_FROM                '639'

 288     642  LOAD_FAST             9  'ch'
         645  LOAD_CONST           15  '\\'
         648  COMPARE_OP            2  '=='
         651  POP_JUMP_IF_FALSE   482  'to 482'

 290     654  LOAD_FAST             1  'str'
         657  LOAD_FAST             7  'i'
         660  BINARY_SUBSCR    
         661  LOAD_CONST            7  '\n'
         664  COMPARE_OP            2  '=='
         667  POP_JUMP_IF_FALSE   683  'to 683'

 291     670  LOAD_FAST             4  'lno'
         673  LOAD_CONST            1  1
         676  BINARY_ADD       
         677  STORE_FAST            4  'lno'
         680  JUMP_FORWARD          0  'to 683'
       683_0  COME_FROM                '680'

 292     683  LOAD_FAST             7  'i'
         686  LOAD_CONST            1  1
         689  BINARY_ADD       
         690  STORE_FAST            7  'i'

 293     693  CONTINUE            482  'to 482'
         696  JUMP_BACK           482  'to 482'
         699  JUMP_BACK           482  'to 482'
         702  POP_BLOCK        

 300     703  LOAD_FAST             4  'lno'
         706  LOAD_CONST            1  1
         709  BINARY_SUBTRACT  
         710  LOAD_FAST            11  'firstlno'
         713  COMPARE_OP            2  '=='
         716  POP_JUMP_IF_FALSE   728  'to 728'

 303     719  LOAD_GLOBAL           9  'C_STRING_FIRST_LINE'
         722  STORE_FAST            2  'continuation'
         725  JUMP_BACK           205  'to 205'

 305     728  LOAD_GLOBAL          10  'C_STRING_NEXT_LINES'
         731  STORE_FAST            2  'continuation'
       734_0  COME_FROM                '479'

 306     734  CONTINUE            205  'to 205'
         737  JUMP_FORWARD          0  'to 740'
       740_0  COME_FROM                '737'

 308     740  LOAD_FAST             9  'ch'
         743  LOAD_CONST           16  '#'
         746  COMPARE_OP            2  '=='
         749  POP_JUMP_IF_FALSE   776  'to 776'

 310     752  LOAD_FAST             1  'str'
         755  LOAD_ATTR            11  'find'
         758  LOAD_CONST            7  '\n'
         761  LOAD_FAST             7  'i'
         764  CALL_FUNCTION_2       2 
         767  STORE_FAST            7  'i'

 312     770  CONTINUE            205  'to 205'
         773  JUMP_FORWARD          0  'to 776'
       776_0  COME_FROM                '773'

 316     776  LOAD_FAST             1  'str'
         779  LOAD_FAST             7  'i'
         782  BINARY_SUBSCR    
         783  LOAD_CONST            7  '\n'
         786  COMPARE_OP            2  '=='
         789  POP_JUMP_IF_FALSE   830  'to 830'

 317     792  LOAD_FAST             4  'lno'
         795  LOAD_CONST            1  1
         798  BINARY_ADD       
         799  STORE_FAST            4  'lno'

 318     802  LOAD_FAST             7  'i'
         805  LOAD_CONST            1  1
         808  BINARY_ADD       
         809  LOAD_FAST             8  'n'
         812  COMPARE_OP            2  '=='
         815  POP_JUMP_IF_FALSE   830  'to 830'

 319     818  LOAD_GLOBAL          12  'C_BACKSLASH'
         821  STORE_FAST            2  'continuation'
         824  JUMP_ABSOLUTE       830  'to 830'
         827  JUMP_FORWARD          0  'to 830'
       830_0  COME_FROM                '827'

 320     830  LOAD_FAST             7  'i'
         833  LOAD_CONST            1  1
         836  BINARY_ADD       
         837  STORE_FAST            7  'i'
         840  JUMP_BACK           205  'to 205'
         843  POP_BLOCK        
       844_0  COME_FROM                '202'

 325     844  LOAD_FAST             2  'continuation'
         847  LOAD_GLOBAL           9  'C_STRING_FIRST_LINE'
         850  COMPARE_OP            3  '!='
         853  POP_JUMP_IF_FALSE   889  'to 889'

 326     856  LOAD_FAST             2  'continuation'
         859  LOAD_GLOBAL          10  'C_STRING_NEXT_LINES'
         862  COMPARE_OP            3  '!='
         865  POP_JUMP_IF_FALSE   889  'to 889'
         868  LOAD_FAST             3  'level'
         871  LOAD_CONST            8  ''
         874  COMPARE_OP            4  '>'
       877_0  COME_FROM                '865'
       877_1  COME_FROM                '853'
         877  POP_JUMP_IF_FALSE   889  'to 889'

 327     880  LOAD_GLOBAL          13  'C_BRACKET'
         883  STORE_FAST            2  'continuation'
         886  JUMP_FORWARD          0  'to 889'
       889_0  COME_FROM                '886'

 328     889  LOAD_FAST             2  'continuation'
         892  LOAD_FAST             0  'self'
         895  STORE_ATTR           14  'continuation'

 333     898  LOAD_FAST             5  'goodlines'
         901  LOAD_CONST           17  -1
         904  BINARY_SUBSCR    
         905  LOAD_FAST             4  'lno'
         908  COMPARE_OP            3  '!='
         911  POP_JUMP_IF_FALSE   927  'to 927'

 334     914  LOAD_FAST             6  'push_good'
         917  LOAD_FAST             4  'lno'
         920  CALL_FUNCTION_1       1 
         923  POP_TOP          
         924  JUMP_FORWARD          0  'to 927'
       927_0  COME_FROM                '924'

Parse error at or near `COME_FROM' instruction at offset 740_0

    def get_continuation_type(self):
        self._study1()
        return self.continuation

    def _study2(self):
        if self.study_level >= 2:
            return
        self._study1()
        self.study_level = 2
        str, goodlines = self.str, self.goodlines
        i = len(goodlines) - 1
        p = len(str)
        while i:
            q = p
            for nothing in range(goodlines[i - 1], goodlines[i]):
                p = str.rfind('\n', 0, p - 1) + 1

            if _junkre(str, p):
                i = i - 1
            else:
                break

        if i == 0:
            q = p
        self.stmt_start, self.stmt_end = p, q
        lastch = ''
        stack = []
        push_stack = stack.append
        bracketing = [(p, 0)]
        while p < q:
            m = _chew_ordinaryre(str, p, q)
            if m:
                newp = m.end()
                i = newp - 1
                while i >= p and str[i] in ' \t\n':
                    i = i - 1

                if i >= p:
                    lastch = str[i]
                p = newp
                if p >= q:
                    break
            ch = str[p]
            if ch in '([{':
                push_stack(p)
                bracketing.append((p, len(stack)))
                lastch = ch
                p = p + 1
                continue
            if ch in ')]}':
                if stack:
                    del stack[-1]
                lastch = ch
                p = p + 1
                bracketing.append((p, len(stack)))
                continue
            if ch == '"' or ch == "'":
                bracketing.append((p, len(stack) + 1))
                lastch = ch
                p = _match_stringre(str, p, q).end()
                bracketing.append((p, len(stack)))
                continue
            if ch == '#':
                bracketing.append((p, len(stack) + 1))
                p = str.find('\n', p, q) + 1
                bracketing.append((p, len(stack)))
                continue
            p = p + 1
            if str[p] != '\n':
                lastch = ch + str[p]
            p = p + 1

        self.lastch = lastch
        if stack:
            self.lastopenbracketpos = stack[-1]
        self.stmt_bracketing = tuple(bracketing)

    def compute_bracket_indent(self):
        self._study2()
        j = self.lastopenbracketpos
        str = self.str
        n = len(str)
        origi = i = str.rfind('\n', 0, j) + 1
        j = j + 1
        while j < n:
            m = _itemre(str, j)
            if m:
                j = m.end() - 1
                extra = 0
                break
            else:
                i = j = str.find('\n', j) + 1
        else:
            j = i = origi
            while str[j] in ' \t':
                j = j + 1

            extra = self.indentwidth

        return len(str[i:j].expandtabs(self.tabwidth)) + extra

    def get_num_lines_in_stmt(self):
        self._study1()
        goodlines = self.goodlines
        return goodlines[-1] - goodlines[-2]

    def compute_backslash_indent(self):
        self._study2()
        str = self.str
        i = self.stmt_start
        while str[i] in ' \t':
            i = i + 1

        startpos = i
        endpos = str.find('\n', startpos) + 1
        found = level = 0
        while i < endpos:
            ch = str[i]
            if ch in '([{':
                level = level + 1
                i = i + 1
            elif ch in ')]}':
                if level:
                    level = level - 1
                i = i + 1
            elif ch == '"' or ch == "'":
                i = _match_stringre(str, i, endpos).end()
            elif ch == '#':
                break
            elif level == 0 and ch == '=' and (i == 0 or str[i - 1] not in '=<>!') and str[i + 1] != '=':
                found = 1
                break
            else:
                i = i + 1

        if found:
            i = i + 1
            found = re.match('\\s*\\\\', str[i:endpos]) is None
        if not found:
            i = startpos
            while str[i] not in ' \t\n':
                i = i + 1

        return len(str[self.stmt_start:i].expandtabs(self.tabwidth)) + 1

    def get_base_indent_string(self):
        self._study2()
        i, n = self.stmt_start, self.stmt_end
        j = i
        str = self.str
        while j < n and str[j] in ' \t':
            j = j + 1

        return str[i:j]

    def is_block_opener(self):
        self._study2()
        return self.lastch == ':'

    def is_block_closer(self):
        self._study2()
        return _closere(self.str, self.stmt_start) is not None

    lastopenbracketpos = None

    def get_last_open_bracket_pos(self):
        self._study2()
        return self.lastopenbracketpos

    stmt_bracketing = None

    def get_last_stmt_bracketing(self):
        self._study2()
        return self.stmt_bracketing