# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: conv.py
"""Convert graminit.[ch] spit out by pgen to Python code.

Pgen is the Python parser generator.  It is useful to quickly create a
parser from a grammar file in Python's grammar notation.  But I don't
want my parsers to be written in C (yet), so I'm translating the
parsing tables to Python data structures and writing a Python parse
engine.

Note that the token numbers are constants determined by the standard
Python tokenizer.  The standard token module defines these numbers and
their names (the names are not used much).  The token numbers are
hardcoded into the Python tokenizer and into pgen.  A Python
implementation of the Python tokenizer is also available, in the
standard tokenize module.

On the other hand, symbol numbers (representing the grammar's
non-terminals) are assigned by pgen based on the actual grammar
input.

Note: this module is pretty much obsolete; the pgen module generates
equivalent grammar tables directly from the Grammar.txt input file
without having to invoke the Python pgen C program.

"""
import re
from pgen2 import grammar, token

class Converter(grammar.Grammar):
    """Grammar subclass that reads classic pgen output files.
    
    The run() method reads the tables as produced by the pgen parser
    generator, typically contained in two C files, graminit.h and
    graminit.c.  The other methods are for internal use only.
    
    See the base class for more documentation.
    
    """

    def run(self, graminit_h, graminit_c):
        """Load the grammar tables from the text files written by pgen."""
        self.parse_graminit_h(graminit_h)
        self.parse_graminit_c(graminit_c)
        self.finish_off()

    def parse_graminit_h(self, filename):
        """Parse the .h file written by pgen.  (Internal)
        
        This file is a sequence of #define statements defining the
        nonterminals of the grammar as numbers.  We build two tables
        mapping the numbers to names and back.
        
        """
        try:
            f = open(filename)
        except IOError as err:
            print "Can't open %s: %s" % (filename, err)
            return False

        self.symbol2number = {}
        self.number2symbol = {}
        lineno = 0
        for line in f:
            lineno += 1
            mo = re.match('^#define\\s+(\\w+)\\s+(\\d+)$', line)
            if not mo and line.strip():
                print "%s(%s): can't parse %s" % (filename, lineno,
                 line.strip())
            else:
                symbol, number = mo.groups()
                number = int(number)
                self.symbol2number[symbol] = number
                self.number2symbol[number] = symbol

        return True

    def parse_graminit_c(self, filename):
        """Parse the .c file written by pgen.  (Internal)
        
        The file looks as follows.  The first two lines are always this:
        
        #include "pgenheaders.h"
        #include "grammar.h"
        
        After that come four blocks:
        
        1) one or more state definitions
        2) a table defining dfas
        3) a table defining labels
        4) a struct defining the grammar
        
        A state definition has the following form:
        - one or more arc arrays, each of the form:
          static arc arcs_<n>_<m>[<k>] = {
                  {<i>, <j>},
                  ...
          };
        - followed by a state array, of the form:
          static state states_<s>[<t>] = {
                  {<k>, arcs_<n>_<m>},
                  ...
          };
        
        """
        try:
            f = open(filename)
        except IOError as err:
            print "Can't open %s: %s" % (filename, err)
            return False

        lineno = 0
        lineno, line = lineno + 1, f.next()
        lineno, line = lineno + 1, f.next()
        lineno, line = lineno + 1, f.next()
        allarcs = {}
        states = []
        while line.startswith('static arc '):
            while line.startswith('static arc '):
                mo = re.match('static arc arcs_(\\d+)_(\\d+)\\[(\\d+)\\] = {$', line)
                n, m, k = map(int, mo.groups())
                arcs = []
                for _ in range(k):
                    lineno, line = lineno + 1, f.next()
                    mo = re.match('\\s+{(\\d+), (\\d+)},$', line)
                    i, j = map(int, mo.groups())
                    arcs.append((i, j))

                lineno, line = lineno + 1, f.next()
                allarcs[n, m] = arcs
                lineno, line = lineno + 1, f.next()

            mo = re.match('static state states_(\\d+)\\[(\\d+)\\] = {$', line)
            s, t = map(int, mo.groups())
            state = []
            for _ in range(t):
                lineno, line = lineno + 1, f.next()
                mo = re.match('\\s+{(\\d+), arcs_(\\d+)_(\\d+)},$', line)
                k, n, m = map(int, mo.groups())
                arcs = allarcs[n, m]
                state.append(arcs)

            states.append(state)
            lineno, line = lineno + 1, f.next()
            lineno, line = lineno + 1, f.next()

        self.states = states
        dfas = {}
        mo = re.match('static dfa dfas\\[(\\d+)\\] = {$', line)
        ndfas = int(mo.group(1))
        for i in range(ndfas):
            lineno, line = lineno + 1, f.next()
            mo = re.match('\\s+{(\\d+), "(\\w+)", (\\d+), (\\d+), states_(\\d+),$', line)
            symbol = mo.group(2)
            number, x, y, z = map(int, mo.group(1, 3, 4, 5))
            state = states[z]
            lineno, line = lineno + 1, f.next()
            mo = re.match('\\s+("(?:\\\\\\d\\d\\d)*")},$', line)
            first = {}
            rawbitset = eval(mo.group(1))
            for i, c in enumerate(rawbitset):
                byte = ord(c)
                for j in range(8):
                    if byte & 1 << j:
                        first[i * 8 + j] = 1

            dfas[number] = (
             state, first)

        lineno, line = lineno + 1, f.next()
        self.dfas = dfas
        labels = []
        lineno, line = lineno + 1, f.next()
        mo = re.match('static label labels\\[(\\d+)\\] = {$', line)
        nlabels = int(mo.group(1))
        for i in range(nlabels):
            lineno, line = lineno + 1, f.next()
            mo = re.match('\\s+{(\\d+), (0|"\\w+")},$', line)
            x, y = mo.groups()
            x = int(x)
            if y == '0':
                y = None
            else:
                y = eval(y)
            labels.append((x, y))

        lineno, line = lineno + 1, f.next()
        self.labels = labels
        lineno, line = lineno + 1, f.next()
        lineno, line = lineno + 1, f.next()
        mo = re.match('\\s+(\\d+),$', line)
        ndfas = int(mo.group(1))
        lineno, line = lineno + 1, f.next()
        lineno, line = lineno + 1, f.next()
        mo = re.match('\\s+{(\\d+), labels},$', line)
        nlabels = int(mo.group(1))
        lineno, line = lineno + 1, f.next()
        mo = re.match('\\s+(\\d+)$', line)
        start = int(mo.group(1))
        self.start = start
        lineno, line = lineno + 1, f.next()
        try:
            lineno, line = lineno + 1, f.next()
        except StopIteration:
            pass

        return

    def finish_off(self):
        """Create additional useful structures.  (Internal)."""
        self.keywords = {}
        self.tokens = {}
        for ilabel, (type, value) in enumerate(self.labels):
            if type == token.NAME and value is not None:
                self.keywords[value] = ilabel
            elif value is None:
                self.tokens[type] = ilabel

        return