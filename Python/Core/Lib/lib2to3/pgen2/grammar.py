# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: grammar.py
"""This module defines the data structures used to represent a grammar.

These are a bit arcane because they are derived from the data
structures used by Python's 'pgen' parser generator.

There's also a table here mapping operators to their names in the
token module; the Python tokenize module reports all operators as the
fallback token code OP, but the parser needs the actual token code.

"""
import pickle
from . import token, tokenize

class Grammar(object):
    """Pgen parsing tables tables conversion class.
    
    Once initialized, this class supplies the grammar tables for the
    parsing engine implemented by parse.py.  The parsing engine
    accesses the instance variables directly.  The class here does not
    provide initialization of the tables; several subclasses exist to
    do this (see the conv and pgen modules).
    
    The load() method reads the tables from a pickle file, which is
    much faster than the other ways offered by subclasses.  The pickle
    file is written by calling dump() (after loading the grammar
    tables using a subclass).  The report() method prints a readable
    representation of the tables to stdout, for debugging.
    
    The instance variables are as follows:
    
    symbol2number -- a dict mapping symbol names to numbers.  Symbol
                     numbers are always 256 or higher, to distinguish
                     them from token numbers, which are between 0 and
                     255 (inclusive).
    
    number2symbol -- a dict mapping numbers to symbol names;
                     these two are each other's inverse.
    
    states        -- a list of DFAs, where each DFA is a list of
                     states, each state is is a list of arcs, and each
                     arc is a (i, j) pair where i is a label and j is
                     a state number.  The DFA number is the index into
                     this list.  (This name is slightly confusing.)
                     Final states are represented by a special arc of
                     the form (0, j) where j is its own state number.
    
    dfas          -- a dict mapping symbol numbers to (DFA, first)
                     pairs, where DFA is an item from the states list
                     above, and first is a set of tokens that can
                     begin this grammar rule (represented by a dict
                     whose values are always 1).
    
    labels        -- a list of (x, y) pairs where x is either a token
                     number or a symbol number, and y is either None
                     or a string; the strings are keywords.  The label
                     number is the index in this list; label numbers
                     are used to mark state transitions (arcs) in the
                     DFAs.
    
    start         -- the number of the grammar's start symbol.
    
    keywords      -- a dict mapping keyword strings to arc labels.
    
    tokens        -- a dict mapping token numbers to arc labels.
    
    """

    def __init__(self):
        self.symbol2number = {}
        self.number2symbol = {}
        self.states = []
        self.dfas = {}
        self.labels = [
         (0, 'EMPTY')]
        self.keywords = {}
        self.tokens = {}
        self.symbol2label = {}
        self.start = 256

    def dump(self, filename):
        """Dump the grammar tables to a pickle file."""
        f = open(filename, 'wb')
        pickle.dump(self.__dict__, f, 2)
        f.close()

    def load(self, filename):
        """Load the grammar tables from a pickle file."""
        f = open(filename, 'rb')
        d = pickle.load(f)
        f.close()
        self.__dict__.update(d)

    def copy(self):
        """
        Copy the grammar.
        """
        new = self.__class__()
        for dict_attr in ('symbol2number', 'number2symbol', 'dfas', 'keywords', 'tokens',
                          'symbol2label'):
            setattr(new, dict_attr, getattr(self, dict_attr).copy())

        new.labels = self.labels[:]
        new.states = self.states[:]
        new.start = self.start
        return new

    def report(self):
        """Dump the grammar tables to standard output, for debugging."""
        from pprint import pprint
        print 's2n'
        pprint(self.symbol2number)
        print 'n2s'
        pprint(self.number2symbol)
        print 'states'
        pprint(self.states)
        print 'dfas'
        pprint(self.dfas)
        print 'labels'
        pprint(self.labels)
        print 'start', self.start


opmap_raw = '\n( LPAR\n) RPAR\n[ LSQB\n] RSQB\n: COLON\n, COMMA\n; SEMI\n+ PLUS\n- MINUS\n* STAR\n/ SLASH\n| VBAR\n& AMPER\n< LESS\n> GREATER\n= EQUAL\n. DOT\n% PERCENT\n` BACKQUOTE\n{ LBRACE\n} RBRACE\n@ AT\n== EQEQUAL\n!= NOTEQUAL\n<> NOTEQUAL\n<= LESSEQUAL\n>= GREATEREQUAL\n~ TILDE\n^ CIRCUMFLEX\n<< LEFTSHIFT\n>> RIGHTSHIFT\n** DOUBLESTAR\n+= PLUSEQUAL\n-= MINEQUAL\n*= STAREQUAL\n/= SLASHEQUAL\n%= PERCENTEQUAL\n&= AMPEREQUAL\n|= VBAREQUAL\n^= CIRCUMFLEXEQUAL\n<<= LEFTSHIFTEQUAL\n>>= RIGHTSHIFTEQUAL\n**= DOUBLESTAREQUAL\n// DOUBLESLASH\n//= DOUBLESLASHEQUAL\n-> RARROW\n'
opmap = {}
for line in opmap_raw.splitlines():
    if line:
        op, name = line.split()
        opmap[op] = getattr(token, name)