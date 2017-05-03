# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: markupbase.py
"""Shared support for scanning document type declarations in HTML and XHTML.

This module is used as a foundation for the HTMLParser and sgmllib
modules (indirectly, for htmllib as well).  It has no documented
public API and should not be used directly.

"""
import re
_declname_match = re.compile('[a-zA-Z][-_.a-zA-Z0-9]*\\s*').match
_declstringlit_match = re.compile('(\\\'[^\\\']*\\\'|"[^"]*")\\s*').match
_commentclose = re.compile('--\\s*>')
_markedsectionclose = re.compile(']\\s*]\\s*>')
_msmarkedsectionclose = re.compile(']\\s*>')
del re

class ParserBase:
    """Parser base class which provides some common support methods used
    by the SGML/HTML and XHTML parsers."""

    def __init__(self):
        if self.__class__ is ParserBase:
            raise RuntimeError('markupbase.ParserBase must be subclassed')

    def error(self, message):
        raise NotImplementedError('subclasses of ParserBase must override error()')

    def reset(self):
        self.lineno = 1
        self.offset = 0

    def getpos(self):
        """Return current line number and offset."""
        return (
         self.lineno, self.offset)

    def updatepos(self, i, j):
        if i >= j:
            return j
        rawdata = self.rawdata
        nlines = rawdata.count('\n', i, j)
        if nlines:
            self.lineno = self.lineno + nlines
            pos = rawdata.rindex('\n', i, j)
            self.offset = j - (pos + 1)
        else:
            self.offset = self.offset + j - i
        return j

    _decl_otherchars = ''

    def parse_declaration(self, i):
        rawdata = self.rawdata
        j = i + 2
        if rawdata[j:j + 1] == '>':
            return j + 1
        if rawdata[j:j + 1] in ('-', ''):
            return -1
        n = len(rawdata)
        if rawdata[j:j + 2] == '--':
            return self.parse_comment(i)
        if rawdata[j] == '[':
            return self.parse_marked_section(i)
        decltype, j = self._scan_name(j, i)
        if j < 0:
            return j
        if decltype == 'doctype':
            self._decl_otherchars = ''
        while j < n:
            c = rawdata[j]
            if c == '>':
                data = rawdata[i + 2:j]
                if decltype == 'doctype':
                    self.handle_decl(data)
                else:
                    self.unknown_decl(data)
                return j + 1
            if c in '"\'':
                m = _declstringlit_match(rawdata, j)
                if not m:
                    return -1
                j = m.end()
            elif c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                name, j = self._scan_name(j, i)
            elif c in self._decl_otherchars:
                j = j + 1
            elif c == '[':
                if decltype == 'doctype':
                    j = self._parse_doctype_subset(j + 1, i)
                elif decltype in ('attlist', 'linktype', 'link', 'element'):
                    self.error("unsupported '[' char in %s declaration" % decltype)
                else:
                    self.error("unexpected '[' char in declaration")
            else:
                self.error('unexpected %r char in declaration' % rawdata[j])
            if j < 0:
                return j

        return -1

    def parse_marked_section(self, i, report=1):
        rawdata = self.rawdata
        sectName, j = self._scan_name(i + 3, i)
        if j < 0:
            return j
        if sectName in ('temp', 'cdata', 'ignore', 'include', 'rcdata'):
            match = _markedsectionclose.search(rawdata, i + 3)
        elif sectName in ('if', 'else', 'endif'):
            match = _msmarkedsectionclose.search(rawdata, i + 3)
        else:
            self.error('unknown status keyword %r in marked section' % rawdata[i + 3:j])
        if not match:
            return -1
        if report:
            j = match.start(0)
            self.unknown_decl(rawdata[i + 3:j])
        return match.end(0)

    def parse_comment(self, i, report=1):
        rawdata = self.rawdata
        if rawdata[i:i + 4] != '<!--':
            self.error('unexpected call to parse_comment()')
        match = _commentclose.search(rawdata, i + 4)
        if not match:
            return -1
        if report:
            j = match.start(0)
            self.handle_comment(rawdata[i + 4:j])
        return match.end(0)

    def _parse_doctype_subset--- This code section failed: ---

 180       0  LOAD_FAST             0  'self'
           3  LOAD_ATTR             0  'rawdata'
           6  STORE_FAST            3  'rawdata'

 181       9  LOAD_GLOBAL           1  'len'
          12  LOAD_FAST             3  'rawdata'
          15  CALL_FUNCTION_1       1 
          18  STORE_FAST            4  'n'

 182      21  LOAD_FAST             1  'i'
          24  STORE_FAST            5  'j'

 183      27  SETUP_LOOP          682  'to 712'
          30  LOAD_FAST             5  'j'
          33  LOAD_FAST             4  'n'
          36  COMPARE_OP            0  '<'
          39  POP_JUMP_IF_FALSE   711  'to 711'

 184      42  LOAD_FAST             3  'rawdata'
          45  LOAD_FAST             5  'j'
          48  BINARY_SUBSCR    
          49  STORE_FAST            6  'c'

 185      52  LOAD_FAST             6  'c'
          55  LOAD_CONST            1  '<'
          58  COMPARE_OP            2  '=='
          61  POP_JUMP_IF_FALSE   404  'to 404'

 186      64  LOAD_FAST             3  'rawdata'
          67  LOAD_FAST             5  'j'
          70  LOAD_FAST             5  'j'
          73  LOAD_CONST            2  2
          76  BINARY_ADD       
          77  SLICE+3          
          78  STORE_FAST            7  's'

 187      81  LOAD_FAST             7  's'
          84  LOAD_CONST            1  '<'
          87  COMPARE_OP            2  '=='
          90  POP_JUMP_IF_FALSE    97  'to 97'

 189      93  LOAD_CONST            3  -1
          96  RETURN_END_IF    
        97_0  COME_FROM                '90'

 190      97  LOAD_FAST             7  's'
         100  LOAD_CONST            4  '<!'
         103  COMPARE_OP            3  '!='
         106  POP_JUMP_IF_FALSE   149  'to 149'

 191     109  LOAD_FAST             0  'self'
         112  LOAD_ATTR             2  'updatepos'
         115  LOAD_FAST             2  'declstartpos'
         118  LOAD_FAST             5  'j'
         121  LOAD_CONST            5  1
         124  BINARY_ADD       
         125  CALL_FUNCTION_2       2 
         128  POP_TOP          

 192     129  LOAD_FAST             0  'self'
         132  LOAD_ATTR             3  'error'
         135  LOAD_CONST            6  'unexpected char in internal subset (in %r)'
         138  LOAD_FAST             7  's'
         141  BINARY_MODULO    
         142  CALL_FUNCTION_1       1 
         145  POP_TOP          
         146  JUMP_FORWARD          0  'to 149'
       149_0  COME_FROM                '146'

 193     149  LOAD_FAST             5  'j'
         152  LOAD_CONST            2  2
         155  BINARY_ADD       
         156  LOAD_FAST             4  'n'
         159  COMPARE_OP            2  '=='
         162  POP_JUMP_IF_FALSE   169  'to 169'

 195     165  LOAD_CONST            3  -1
         168  RETURN_END_IF    
       169_0  COME_FROM                '162'

 196     169  LOAD_FAST             5  'j'
         172  LOAD_CONST            7  4
         175  BINARY_ADD       
         176  LOAD_FAST             4  'n'
         179  COMPARE_OP            4  '>'
         182  POP_JUMP_IF_FALSE   189  'to 189'

 198     185  LOAD_CONST            3  -1
         188  RETURN_END_IF    
       189_0  COME_FROM                '182'

 199     189  LOAD_FAST             3  'rawdata'
         192  LOAD_FAST             5  'j'
         195  LOAD_FAST             5  'j'
         198  LOAD_CONST            7  4
         201  BINARY_ADD       
         202  SLICE+3          
         203  LOAD_CONST            8  '<!--'
         206  COMPARE_OP            2  '=='
         209  POP_JUMP_IF_FALSE   255  'to 255'

 200     212  LOAD_FAST             0  'self'
         215  LOAD_ATTR             4  'parse_comment'
         218  LOAD_FAST             5  'j'
         221  LOAD_CONST            9  'report'
         224  LOAD_CONST           10  ''
         227  CALL_FUNCTION_257   257 
         230  STORE_FAST            5  'j'

 201     233  LOAD_FAST             5  'j'
         236  LOAD_CONST           10  ''
         239  COMPARE_OP            0  '<'
         242  POP_JUMP_IF_FALSE    30  'to 30'

 202     245  LOAD_FAST             5  'j'
         248  RETURN_VALUE     

 203     249  JUMP_BACK            30  'to 30'
         252  JUMP_FORWARD          0  'to 255'
       255_0  COME_FROM                '252'

 204     255  LOAD_FAST             0  'self'
         258  LOAD_ATTR             5  '_scan_name'
         261  LOAD_FAST             5  'j'
         264  LOAD_CONST            2  2
         267  BINARY_ADD       
         268  LOAD_FAST             2  'declstartpos'
         271  CALL_FUNCTION_2       2 
         274  UNPACK_SEQUENCE_2     2 
         277  STORE_FAST            8  'name'
         280  STORE_FAST            5  'j'

 205     283  LOAD_FAST             5  'j'
         286  LOAD_CONST            3  -1
         289  COMPARE_OP            2  '=='
         292  POP_JUMP_IF_FALSE   299  'to 299'

 206     295  LOAD_CONST            3  -1
         298  RETURN_END_IF    
       299_0  COME_FROM                '292'

 207     299  LOAD_FAST             8  'name'
         302  LOAD_CONST           23  ('attlist', 'element', 'entity', 'notation')
         305  COMPARE_OP            7  'not in'
         308  POP_JUMP_IF_FALSE   351  'to 351'

 208     311  LOAD_FAST             0  'self'
         314  LOAD_ATTR             2  'updatepos'
         317  LOAD_FAST             2  'declstartpos'
         320  LOAD_FAST             5  'j'
         323  LOAD_CONST            2  2
         326  BINARY_ADD       
         327  CALL_FUNCTION_2       2 
         330  POP_TOP          

 209     331  LOAD_FAST             0  'self'
         334  LOAD_ATTR             3  'error'

 210     337  LOAD_CONST           15  'unknown declaration %r in internal subset'
         340  LOAD_FAST             8  'name'
         343  BINARY_MODULO    
         344  CALL_FUNCTION_1       1 
         347  POP_TOP          
         348  JUMP_FORWARD          0  'to 351'
       351_0  COME_FROM                '348'

 212     351  LOAD_GLOBAL           6  'getattr'
         354  LOAD_FAST             0  'self'
         357  LOAD_CONST           16  '_parse_doctype_'
         360  LOAD_FAST             8  'name'
         363  BINARY_ADD       
         364  CALL_FUNCTION_2       2 
         367  STORE_FAST            9  'meth'

 213     370  LOAD_FAST             9  'meth'
         373  LOAD_FAST             5  'j'
         376  LOAD_FAST             2  'declstartpos'
         379  CALL_FUNCTION_2       2 
         382  STORE_FAST            5  'j'

 214     385  LOAD_FAST             5  'j'
         388  LOAD_CONST           10  ''
         391  COMPARE_OP            0  '<'
         394  POP_JUMP_IF_FALSE   708  'to 708'

 215     397  LOAD_FAST             5  'j'
         400  RETURN_END_IF    
       401_0  COME_FROM                '394'
         401  JUMP_BACK            30  'to 30'

 216     404  LOAD_FAST             6  'c'
         407  LOAD_CONST           17  '%'
         410  COMPARE_OP            2  '=='
         413  POP_JUMP_IF_FALSE   512  'to 512'

 218     416  LOAD_FAST             5  'j'
         419  LOAD_CONST            5  1
         422  BINARY_ADD       
         423  LOAD_FAST             4  'n'
         426  COMPARE_OP            2  '=='
         429  POP_JUMP_IF_FALSE   436  'to 436'

 220     432  LOAD_CONST            3  -1
         435  RETURN_END_IF    
       436_0  COME_FROM                '429'

 221     436  LOAD_FAST             0  'self'
         439  LOAD_ATTR             5  '_scan_name'
         442  LOAD_FAST             5  'j'
         445  LOAD_CONST            5  1
         448  BINARY_ADD       
         449  LOAD_FAST             2  'declstartpos'
         452  CALL_FUNCTION_2       2 
         455  UNPACK_SEQUENCE_2     2 
         458  STORE_FAST            7  's'
         461  STORE_FAST            5  'j'

 222     464  LOAD_FAST             5  'j'
         467  LOAD_CONST           10  ''
         470  COMPARE_OP            0  '<'
         473  POP_JUMP_IF_FALSE   480  'to 480'

 223     476  LOAD_FAST             5  'j'
         479  RETURN_END_IF    
       480_0  COME_FROM                '473'

 224     480  LOAD_FAST             3  'rawdata'
         483  LOAD_FAST             5  'j'
         486  BINARY_SUBSCR    
         487  LOAD_CONST           18  ';'
         490  COMPARE_OP            2  '=='
         493  POP_JUMP_IF_FALSE   708  'to 708'

 225     496  LOAD_FAST             5  'j'
         499  LOAD_CONST            5  1
         502  BINARY_ADD       
         503  STORE_FAST            5  'j'
         506  JUMP_ABSOLUTE       708  'to 708'
         509  JUMP_BACK            30  'to 30'

 226     512  LOAD_FAST             6  'c'
         515  LOAD_CONST           19  ']'
         518  COMPARE_OP            2  '=='
         521  POP_JUMP_IF_FALSE   650  'to 650'

 227     524  LOAD_FAST             5  'j'
         527  LOAD_CONST            5  1
         530  BINARY_ADD       
         531  STORE_FAST            5  'j'

 228     534  SETUP_LOOP           42  'to 579'
         537  LOAD_FAST             5  'j'
         540  LOAD_FAST             4  'n'
         543  COMPARE_OP            0  '<'
         546  POP_JUMP_IF_FALSE   578  'to 578'
         549  LOAD_FAST             3  'rawdata'
         552  LOAD_FAST             5  'j'
         555  BINARY_SUBSCR    
         556  LOAD_ATTR             7  'isspace'
         559  CALL_FUNCTION_0       0 
       562_0  COME_FROM                '546'
         562  POP_JUMP_IF_FALSE   578  'to 578'

 229     565  LOAD_FAST             5  'j'
         568  LOAD_CONST            5  1
         571  BINARY_ADD       
         572  STORE_FAST            5  'j'
         575  JUMP_BACK           537  'to 537'
         578  POP_BLOCK        
       579_0  COME_FROM                '534'

 230     579  LOAD_FAST             5  'j'
         582  LOAD_FAST             4  'n'
         585  COMPARE_OP            0  '<'
         588  POP_JUMP_IF_FALSE   643  'to 643'

 231     591  LOAD_FAST             3  'rawdata'
         594  LOAD_FAST             5  'j'
         597  BINARY_SUBSCR    
         598  LOAD_CONST           20  '>'
         601  COMPARE_OP            2  '=='
         604  POP_JUMP_IF_FALSE   611  'to 611'

 232     607  LOAD_FAST             5  'j'
         610  RETURN_END_IF    
       611_0  COME_FROM                '604'

 233     611  LOAD_FAST             0  'self'
         614  LOAD_ATTR             2  'updatepos'
         617  LOAD_FAST             2  'declstartpos'
         620  LOAD_FAST             5  'j'
         623  CALL_FUNCTION_2       2 
         626  POP_TOP          

 234     627  LOAD_FAST             0  'self'
         630  LOAD_ATTR             3  'error'
         633  LOAD_CONST           21  'unexpected char after internal subset'
         636  CALL_FUNCTION_1       1 
         639  POP_TOP          
         640  JUMP_ABSOLUTE       708  'to 708'

 236     643  LOAD_CONST            3  -1
         646  RETURN_VALUE     
         647  JUMP_BACK            30  'to 30'

 237     650  LOAD_FAST             6  'c'
         653  LOAD_ATTR             7  'isspace'
         656  CALL_FUNCTION_0       0 
         659  POP_JUMP_IF_FALSE   675  'to 675'

 238     662  LOAD_FAST             5  'j'
         665  LOAD_CONST            5  1
         668  BINARY_ADD       
         669  STORE_FAST            5  'j'
         672  JUMP_BACK            30  'to 30'

 240     675  LOAD_FAST             0  'self'
         678  LOAD_ATTR             2  'updatepos'
         681  LOAD_FAST             2  'declstartpos'
         684  LOAD_FAST             5  'j'
         687  CALL_FUNCTION_2       2 
         690  POP_TOP          

 241     691  LOAD_FAST             0  'self'
         694  LOAD_ATTR             3  'error'
         697  LOAD_CONST           22  'unexpected char %r in internal subset'
         700  LOAD_FAST             6  'c'
         703  BINARY_MODULO    
         704  CALL_FUNCTION_1       1 
         707  POP_TOP          
         708  JUMP_BACK            30  'to 30'
         711  POP_BLOCK        
       712_0  COME_FROM                '27'

 243     712  LOAD_CONST            3  -1
         715  RETURN_VALUE     
          -1  RETURN_LAST      

Parse error at or near `COME_FROM' instruction at offset 255_0

    def _parse_doctype_element(self, i, declstartpos):
        name, j = self._scan_name(i, declstartpos)
        if j == -1:
            return -1
        rawdata = self.rawdata
        if '>' in rawdata[j:]:
            return rawdata.find('>', j) + 1
        return -1

    def _parse_doctype_attlist(self, i, declstartpos):
        rawdata = self.rawdata
        name, j = self._scan_name(i, declstartpos)
        c = rawdata[j:j + 1]
        if c == '':
            return -1
        if c == '>':
            return j + 1
        while 1:
            name, j = self._scan_name(j, declstartpos)
            if j < 0:
                return j
            c = rawdata[j:j + 1]
            if c == '':
                return -1
            if c == '(':
                if ')' in rawdata[j:]:
                    j = rawdata.find(')', j) + 1
                else:
                    return -1
                while rawdata[j:j + 1].isspace():
                    j = j + 1

                if not rawdata[j:]:
                    return -1
            else:
                name, j = self._scan_name(j, declstartpos)
            c = rawdata[j:j + 1]
            if not c:
                return -1
            if c in '\'"':
                m = _declstringlit_match(rawdata, j)
                if m:
                    j = m.end()
                else:
                    return -1
                c = rawdata[j:j + 1]
                if not c:
                    return -1
            if c == '#':
                if rawdata[j:] == '#':
                    return -1
                name, j = self._scan_name(j + 1, declstartpos)
                if j < 0:
                    return j
                c = rawdata[j:j + 1]
                if not c:
                    return -1
            if c == '>':
                return j + 1

    def _parse_doctype_notation(self, i, declstartpos):
        name, j = self._scan_name(i, declstartpos)
        if j < 0:
            return j
        rawdata = self.rawdata
        while 1:
            c = rawdata[j:j + 1]
            if not c:
                return -1
            if c == '>':
                return j + 1
            if c in '\'"':
                m = _declstringlit_match(rawdata, j)
                if not m:
                    return -1
                j = m.end()
            else:
                name, j = self._scan_name(j, declstartpos)
                if j < 0:
                    return j

    def _parse_doctype_entity(self, i, declstartpos):
        rawdata = self.rawdata
        if rawdata[i:i + 1] == '%':
            j = i + 1
            while 1:
                c = rawdata[j:j + 1]
                if not c:
                    return -1
                if c.isspace():
                    j = j + 1
                else:
                    break

        else:
            j = i
        name, j = self._scan_name(j, declstartpos)
        if j < 0:
            return j
        while 1:
            c = self.rawdata[j:j + 1]
            if not c:
                return -1
            if c in '\'"':
                m = _declstringlit_match(rawdata, j)
                if m:
                    j = m.end()
                else:
                    return -1
            else:
                if c == '>':
                    return j + 1
                name, j = self._scan_name(j, declstartpos)
                if j < 0:
                    return j

    def _scan_name(self, i, declstartpos):
        rawdata = self.rawdata
        n = len(rawdata)
        if i == n:
            return (None, -1)
        else:
            m = _declname_match(rawdata, i)
            if m:
                s = m.group()
                name = s.strip()
                if i + len(s) == n:
                    return (None, -1)
                return (name.lower(), m.end())
            self.updatepos(declstartpos, i)
            self.error('expected name token at %r' % rawdata[declstartpos:declstartpos + 20])
            return None

    def unknown_decl(self, data):
        pass