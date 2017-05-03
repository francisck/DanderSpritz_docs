# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: pgen.py
from . import grammar, token, tokenize

class PgenGrammar(grammar.Grammar):
    pass


class ParserGenerator(object):

    def __init__(self, filename, stream=None):
        close_stream = None
        if stream is None:
            stream = open(filename)
            close_stream = stream.close
        self.filename = filename
        self.stream = stream
        self.generator = tokenize.generate_tokens(stream.readline)
        self.gettoken()
        self.dfas, self.startsymbol = self.parse()
        if close_stream is not None:
            close_stream()
        self.first = {}
        self.addfirstsets()
        return

    def make_grammar(self):
        c = PgenGrammar()
        names = self.dfas.keys()
        names.sort()
        names.remove(self.startsymbol)
        names.insert(0, self.startsymbol)
        for name in names:
            i = 256 + len(c.symbol2number)
            c.symbol2number[name] = i
            c.number2symbol[i] = name

        for name in names:
            dfa = self.dfas[name]
            states = []
            for state in dfa:
                arcs = []
                for label, next in state.arcs.iteritems():
                    arcs.append((self.make_label(c, label), dfa.index(next)))

                if state.isfinal:
                    arcs.append((0, dfa.index(state)))
                states.append(arcs)

            c.states.append(states)
            c.dfas[c.symbol2number[name]] = (states, self.make_first(c, name))

        c.start = c.symbol2number[self.startsymbol]
        return c

    def make_first(self, c, name):
        rawfirst = self.first[name]
        first = {}
        for label in rawfirst:
            ilabel = self.make_label(c, label)
            first[ilabel] = 1

        return first

    def make_label(self, c, label):
        ilabel = len(c.labels)
        if label[0].isalpha():
            if label in c.symbol2number:
                if label in c.symbol2label:
                    return c.symbol2label[label]
                else:
                    c.labels.append((c.symbol2number[label], None))
                    c.symbol2label[label] = ilabel
                    return ilabel

            else:
                itoken = getattr(token, label, None)
                if itoken in c.tokens:
                    return c.tokens[itoken]
                else:
                    c.labels.append((itoken, None))
                    c.tokens[itoken] = ilabel
                    return ilabel

        else:
            value = eval(label)
            if value[0].isalpha():
                if value in c.keywords:
                    return c.keywords[value]
                else:
                    c.labels.append((token.NAME, value))
                    c.keywords[value] = ilabel
                    return ilabel

            else:
                itoken = grammar.opmap[value]
                if itoken in c.tokens:
                    return c.tokens[itoken]
                c.labels.append((itoken, None))
                c.tokens[itoken] = ilabel
                return ilabel
        return

    def addfirstsets(self):
        names = self.dfas.keys()
        names.sort()
        for name in names:
            if name not in self.first:
                self.calcfirst(name)

    def calcfirst(self, name):
        dfa = self.dfas[name]
        self.first[name] = None
        state = dfa[0]
        totalset = {}
        overlapcheck = {}
        for label, next in state.arcs.iteritems():
            if label in self.dfas:
                if label in self.first:
                    fset = self.first[label]
                    if fset is None:
                        raise ValueError('recursion for rule %r' % name)
                else:
                    self.calcfirst(label)
                    fset = self.first[label]
                totalset.update(fset)
                overlapcheck[label] = fset
            else:
                totalset[label] = 1
                overlapcheck[label] = {label: 1}

        inverse = {}
        for label, itsfirst in overlapcheck.iteritems():
            for symbol in itsfirst:
                if symbol in inverse:
                    raise ValueError('rule %s is ambiguous; %s is in the first sets of %s as well as %s' % (
                     name, symbol, label, inverse[symbol]))
                inverse[symbol] = label

        self.first[name] = totalset
        return

    def parse(self):
        dfas = {}
        startsymbol = None
        while self.type != token.ENDMARKER:
            while self.type == token.NEWLINE:
                self.gettoken()

            name = self.expect(token.NAME)
            self.expect(token.OP, ':')
            a, z = self.parse_rhs()
            self.expect(token.NEWLINE)
            dfa = self.make_dfa(a, z)
            oldlen = len(dfa)
            self.simplify_dfa(dfa)
            newlen = len(dfa)
            dfas[name] = dfa
            if startsymbol is None:
                startsymbol = name

        return (
         dfas, startsymbol)

    def make_dfa(self, start, finish):

        def closure(state):
            base = {}
            addclosure(state, base)
            return base

        def addclosure(state, base):
            if state in base:
                return
            else:
                base[state] = 1
                for label, next in state.arcs:
                    if label is None:
                        addclosure(next, base)

                return

        states = [
         DFAState(closure(start), finish)]
        for state in states:
            arcs = {}
            for nfastate in state.nfaset:
                for label, next in nfastate.arcs:
                    if label is not None:
                        addclosure(next, arcs.setdefault(label, {}))

            for label, nfaset in arcs.iteritems():
                for st in states:
                    if st.nfaset == nfaset:
                        break
                else:
                    st = DFAState(nfaset, finish)
                    states.append(st)

                state.addarc(st, label)

        return states

    def dump_nfa(self, name, start, finish):
        print 'Dump of NFA for', name
        todo = [start]
        for i, state in enumerate(todo):
            print '  State', i, state is finish and '(final)' or ''
            for label, next in state.arcs:
                if next in todo:
                    j = todo.index(next)
                else:
                    j = len(todo)
                    todo.append(next)
                if label is None:
                    print '    -> %d' % j
                else:
                    print '    %s -> %d' % (label, j)

        return

    def dump_dfa(self, name, dfa):
        print 'Dump of DFA for', name
        for i, state in enumerate(dfa):
            print '  State', i, state.isfinal and '(final)' or ''
            for label, next in state.arcs.iteritems():
                print '    %s -> %d' % (label, dfa.index(next))

    def simplify_dfa(self, dfa):
        changes = True
        while changes:
            changes = False
            for i, state_i in enumerate(dfa):
                for j in range(i + 1, len(dfa)):
                    state_j = dfa[j]
                    if state_i == state_j:
                        del dfa[j]
                        for state in dfa:
                            state.unifystate(state_j, state_i)

                        changes = True
                        break

    def parse_rhs(self):
        a, z = self.parse_alt()
        if self.value != '|':
            return (a, z)
        else:
            aa = NFAState()
            zz = NFAState()
            aa.addarc(a)
            z.addarc(zz)
            while self.value == '|':
                self.gettoken()
                a, z = self.parse_alt()
                aa.addarc(a)
                z.addarc(zz)

            return (aa, zz)

    def parse_alt(self):
        a, b = self.parse_item()
        while self.value in ('(', '[') or self.type in (token.NAME, token.STRING):
            c, d = self.parse_item()
            b.addarc(c)
            b = d

        return (a, b)

    def parse_item(self):
        if self.value == '[':
            self.gettoken()
            a, z = self.parse_rhs()
            self.expect(token.OP, ']')
            a.addarc(z)
            return (
             a, z)
        else:
            a, z = self.parse_atom()
            value = self.value
            if value not in ('+', '*'):
                return (a, z)
            self.gettoken()
            z.addarc(a)
            if value == '+':
                return (a, z)
            return (
             a, a)

    def parse_atom(self):
        if self.value == '(':
            self.gettoken()
            a, z = self.parse_rhs()
            self.expect(token.OP, ')')
            return (
             a, z)
        if self.type in (token.NAME, token.STRING):
            a = NFAState()
            z = NFAState()
            a.addarc(z, self.value)
            self.gettoken()
            return (
             a, z)
        self.raise_error('expected (...) or NAME or STRING, got %s/%s', self.type, self.value)

    def expect(self, type, value=None):
        if self.type != type or value is not None and self.value != value:
            self.raise_error('expected %s/%s, got %s/%s', type, value, self.type, self.value)
        value = self.value
        self.gettoken()
        return value

    def gettoken(self):
        tup = self.generator.next()
        while tup[0] in (tokenize.COMMENT, tokenize.NL):
            tup = self.generator.next()

        self.type, self.value, self.begin, self.end, self.line = tup

    def raise_error(self, msg, *args):
        if args:
            try:
                msg = msg % args
            except:
                msg = ' '.join([msg] + map(str, args))

        raise SyntaxError(msg, (self.filename, self.end[0],
         self.end[1], self.line))


class NFAState(object):

    def __init__(self):
        self.arcs = []

    def addarc(self, next, label=None):
        self.arcs.append((label, next))


class DFAState(object):

    def __init__(self, nfaset, final):
        self.nfaset = nfaset
        self.isfinal = final in nfaset
        self.arcs = {}

    def addarc(self, next, label):
        self.arcs[label] = next

    def unifystate(self, old, new):
        for label, next in self.arcs.iteritems():
            if next is old:
                self.arcs[label] = new

    def __eq__(self, other):
        if self.isfinal != other.isfinal:
            return False
        if len(self.arcs) != len(other.arcs):
            return False
        for label, next in self.arcs.iteritems():
            if next is not other.arcs.get(label):
                return False

        return True

    __hash__ = None


def generate_grammar(filename='Grammar.txt'):
    p = ParserGenerator(filename)
    return p.make_grammar()