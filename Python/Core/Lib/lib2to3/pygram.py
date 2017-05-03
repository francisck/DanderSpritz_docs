# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: pygram.py
"""Export the Python grammar and symbols."""
import os
from .pgen2 import token
from .pgen2 import driver
from . import pytree
_GRAMMAR_FILE = os.path.join(os.path.dirname(__file__), 'Grammar.txt')
_PATTERN_GRAMMAR_FILE = os.path.join(os.path.dirname(__file__), 'PatternGrammar.txt')

class Symbols(object):

    def __init__(self, grammar):
        """Initializer.
        
        Creates an attribute for each grammar symbol (nonterminal),
        whose value is the symbol's type (an int >= 256).
        """
        for name, symbol in grammar.symbol2number.iteritems():
            setattr(self, name, symbol)


python_grammar = driver.load_grammar(_GRAMMAR_FILE)
python_symbols = Symbols(python_grammar)
python_grammar_no_print_statement = python_grammar.copy()
del python_grammar_no_print_statement.keywords['print']
pattern_grammar = driver.load_grammar(_PATTERN_GRAMMAR_FILE)
pattern_symbols = Symbols(pattern_grammar)