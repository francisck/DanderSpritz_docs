# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: collections.py
__all__ = ['Counter', 'deque', 'defaultdict', 'namedtuple', 'OrderedDict']
from _abcoll import *
import _abcoll
__all__ += _abcoll.__all__
from _collections import deque, defaultdict
from operator import itemgetter as _itemgetter
from keyword import iskeyword as _iskeyword
import sys as _sys
import heapq as _heapq
from itertools import repeat as _repeat, chain as _chain, starmap as _starmap
try:
    from thread import get_ident as _get_ident
except ImportError:
    from dummy_thread import get_ident as _get_ident

class OrderedDict(dict):
    """Dictionary that remembers insertion order"""

    def __init__(self, *args, **kwds):
        """Initialize an ordered dictionary.  The signature is the same as
        regular dictionaries, but keyword arguments are not recommended because
        their insertion order is arbitrary.
        
        """
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))
        try:
            self.__root
        except AttributeError:
            self.__root = root = []
            root[:] = [
             root, root, None]
            self.__map = {}

        self.__update(*args, **kwds)
        return

    def __setitem__(self, key, value, PREV=0, NEXT=1, dict_setitem=dict.__setitem__):
        """od.__setitem__(i, y) <==> od[i]=y"""
        if key not in self:
            root = self.__root
            last = root[PREV]
            last[NEXT] = root[PREV] = self.__map[key] = [last, root, key]
        dict_setitem(self, key, value)

    def __delitem__(self, key, PREV=0, NEXT=1, dict_delitem=dict.__delitem__):
        """od.__delitem__(y) <==> del od[y]"""
        dict_delitem(self, key)
        link_prev, link_next, key = self.__map.pop(key)
        link_prev[NEXT] = link_next
        link_next[PREV] = link_prev

    def __iter__(self):
        """od.__iter__() <==> iter(od)"""
        NEXT, KEY = (1, 2)
        root = self.__root
        curr = root[NEXT]
        while curr is not root:
            yield curr[KEY]
            curr = curr[NEXT]

    def __reversed__(self):
        """od.__reversed__() <==> reversed(od)"""
        PREV, KEY = (0, 2)
        root = self.__root
        curr = root[PREV]
        while curr is not root:
            yield curr[KEY]
            curr = curr[PREV]

    def clear(self):
        """od.clear() -> None.  Remove all items from od."""
        for node in self.__map.itervalues():
            del node[:]

        root = self.__root
        root[:] = [root, root, None]
        self.__map.clear()
        dict.clear(self)
        return

    def keys(self):
        """od.keys() -> list of keys in od"""
        return list(self)

    def values(self):
        """od.values() -> list of values in od"""
        return [ self[key] for key in self ]

    def items(self):
        """od.items() -> list of (key, value) pairs in od"""
        return [ (key, self[key]) for key in self ]

    def iterkeys(self):
        """od.iterkeys() -> an iterator over the keys in od"""
        return iter(self)

    def itervalues(self):
        """od.itervalues -> an iterator over the values in od"""
        for k in self:
            yield self[k]

    def iteritems(self):
        """od.iteritems -> an iterator over the (key, value) pairs in od"""
        for k in self:
            yield (k, self[k])

    update = MutableMapping.update
    __update = update
    __marker = object()

    def pop(self, key, default=__marker):
        """od.pop(k[,d]) -> v, remove specified key and return the corresponding
        value.  If key is not found, d is returned if given, otherwise KeyError
        is raised.
        
        """
        if key in self:
            result = self[key]
            del self[key]
            return result
        if default is self.__marker:
            raise KeyError(key)
        return default

    def setdefault(self, key, default=None):
        """od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od"""
        if key in self:
            return self[key]
        self[key] = default
        return default

    def popitem(self, last=True):
        """od.popitem() -> (k, v), return and remove a (key, value) pair.
        Pairs are returned in LIFO order if last is true or FIFO order if false.
        
        """
        if not self:
            raise KeyError('dictionary is empty')
        key = next(reversed(self) if last else iter(self))
        value = self.pop(key)
        return (
         key, value)

    def __repr__(self, _repr_running={}):
        """od.__repr__() <==> repr(od)"""
        call_key = (
         id(self), _get_ident())
        if call_key in _repr_running:
            return '...'
        _repr_running[call_key] = 1
        try:
            if not self:
                return '%s()' % (self.__class__.__name__,)
            return '%s(%r)' % (self.__class__.__name__, self.items())
        finally:
            del _repr_running[call_key]

    def __reduce__(self):
        """Return state information for pickling"""
        items = [ [k, self[k]] for k in self ]
        inst_dict = vars(self).copy()
        for k in vars(OrderedDict()):
            inst_dict.pop(k, None)

        if inst_dict:
            return (self.__class__, (items,), inst_dict)
        else:
            return (
             self.__class__, (items,))

    def copy(self):
        """od.copy() -> a shallow copy of od"""
        return self.__class__(self)

    @classmethod
    def fromkeys(cls, iterable, value=None):
        """OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S.
        If not specified, the value defaults to None.
        
        """
        self = cls()
        for key in iterable:
            self[key] = value

        return self

    def __eq__(self, other):
        """od.__eq__(y) <==> od==y.  Comparison to another OD is order-sensitive
        while comparison to a regular mapping is order-insensitive.
        
        """
        if isinstance(other, OrderedDict):
            return len(self) == len(other) and self.items() == other.items()
        return dict.__eq__(self, other)

    def __ne__(self, other):
        """od.__ne__(y) <==> od!=y"""
        return not self == other

    def viewkeys(self):
        """od.viewkeys() -> a set-like object providing a view on od's keys"""
        return KeysView(self)

    def viewvalues(self):
        """od.viewvalues() -> an object providing a view on od's values"""
        return ValuesView(self)

    def viewitems(self):
        """od.viewitems() -> a set-like object providing a view on od's items"""
        return ItemsView(self)


def namedtuple(typename, field_names, verbose=False, rename=False):
    """Returns a new subclass of tuple with named fields.
    
    >>> Point = namedtuple('Point', 'x y')
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessable by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)
    
    """
    if isinstance(field_names, basestring):
        field_names = field_names.replace(',', ' ').split()
    field_names = tuple(map(str, field_names))
    if rename:
        names = list(field_names)
        seen = set()
        for i, name in enumerate(names):
            if not all((c.isalnum() or c == '_' for c in name)) or _iskeyword(name) or not name or name[0].isdigit() or name.startswith('_') or name in seen:
                names[i] = '_%d' % i
            seen.add(name)

        field_names = tuple(names)
    for name in (typename,) + field_names:
        if not all((c.isalnum() or c == '_' for c in name)):
            raise ValueError('Type names and field names can only contain alphanumeric characters and underscores: %r' % name)
        if _iskeyword(name):
            raise ValueError('Type names and field names cannot be a keyword: %r' % name)
        if name[0].isdigit():
            raise ValueError('Type names and field names cannot start with a number: %r' % name)

    seen_names = set()
    for name in field_names:
        if name.startswith('_') and not rename:
            raise ValueError('Field names cannot start with an underscore: %r' % name)
        if name in seen_names:
            raise ValueError('Encountered duplicate field name: %r' % name)
        seen_names.add(name)

    numfields = len(field_names)
    argtxt = repr(field_names).replace("'", '')[1:-1]
    reprtxt = ', '.join(('%s=%%r' % name for name in field_names))
    template = "class %(typename)s(tuple):\n        '%(typename)s(%(argtxt)s)' \n\n        __slots__ = () \n\n        _fields = %(field_names)r \n\n        def __new__(_cls, %(argtxt)s):\n            'Create new instance of %(typename)s(%(argtxt)s)'\n            return _tuple.__new__(_cls, (%(argtxt)s)) \n\n        @classmethod\n        def _make(cls, iterable, new=tuple.__new__, len=len):\n            'Make a new %(typename)s object from a sequence or iterable'\n            result = new(cls, iterable)\n            if len(result) != %(numfields)d:\n                raise TypeError('Expected %(numfields)d arguments, got %%d' %% len(result))\n            return result \n\n        def __repr__(self):\n            'Return a nicely formatted representation string'\n            return '%(typename)s(%(reprtxt)s)' %% self \n\n        def _asdict(self):\n            'Return a new OrderedDict which maps field names to their values'\n            return OrderedDict(zip(self._fields, self)) \n\n        def _replace(_self, **kwds):\n            'Return a new %(typename)s object replacing specified fields with new values'\n            result = _self._make(map(kwds.pop, %(field_names)r, _self))\n            if kwds:\n                raise ValueError('Got unexpected field names: %%r' %% kwds.keys())\n            return result \n\n        def __getnewargs__(self):\n            'Return self as a plain tuple.  Used by copy and pickle.'\n            return tuple(self) \n\n" % locals()
    for i, name in enumerate(field_names):
        template += "        %s = _property(_itemgetter(%d), doc='Alias for field number %d')\n" % (name, i, i)

    if verbose:
        print template
    namespace = dict(_itemgetter=_itemgetter, __name__='namedtuple_%s' % typename, OrderedDict=OrderedDict, _property=property, _tuple=tuple)
    try:
        exec template in namespace
    except SyntaxError as e:
        raise SyntaxError(e.message + ':\n' + template)

    result = namespace[typename]
    try:
        result.__module__ = _sys._getframe(1).f_globals.get('__name__', '__main__')
    except (AttributeError, ValueError):
        pass

    return result


class Counter(dict):
    """Dict subclass for counting hashable items.  Sometimes called a bag
    or multiset.  Elements are stored as dictionary keys and their counts
    are stored as dictionary values.
    
    >>> c = Counter('abcdeabcdabcaba')  # count elements from a string
    
    >>> c.most_common(3)                # three most common elements
    [('a', 5), ('b', 4), ('c', 3)]
    >>> sorted(c)                       # list all unique elements
    ['a', 'b', 'c', 'd', 'e']
    >>> ''.join(sorted(c.elements()))   # list elements with repetitions
    'aaaaabbbbcccdde'
    >>> sum(c.values())                 # total of all counts
    15
    
    >>> c['a']                          # count of letter 'a'
    5
    >>> for elem in 'shazam':           # update counts from an iterable
    ...     c[elem] += 1                # by adding 1 to each element's count
    >>> c['a']                          # now there are seven 'a'
    7
    >>> del c['b']                      # remove all 'b'
    >>> c['b']                          # now there are zero 'b'
    0
    
    >>> d = Counter('simsalabim')       # make another counter
    >>> c.update(d)                     # add in the second counter
    >>> c['a']                          # now there are nine 'a'
    9
    
    >>> c.clear()                       # empty the counter
    >>> c
    Counter()
    
    Note:  If a count is set to zero or reduced to zero, it will remain
    in the counter until the entry is deleted or the counter is cleared:
    
    >>> c = Counter('aaabbc')
    >>> c['b'] -= 2                     # reduce the count of 'b' by two
    >>> c.most_common()                 # 'b' is still in, but its count is zero
    [('a', 3), ('c', 1), ('b', 0)]
    
    """

    def __init__(self, iterable=None, **kwds):
        """Create a new, empty Counter object.  And if given, count elements
        from an input iterable.  Or, initialize the count from another mapping
        of elements to their counts.
        
        >>> c = Counter()                           # a new, empty counter
        >>> c = Counter('gallahad')                 # a new counter from an iterable
        >>> c = Counter({'a': 4, 'b': 2})           # a new counter from a mapping
        >>> c = Counter(a=4, b=2)                   # a new counter from keyword args
        
        """
        super(Counter, self).__init__()
        self.update(iterable, **kwds)

    def __missing__(self, key):
        """The count of elements not in the Counter is zero."""
        return 0

    def most_common(self, n=None):
        """List the n most common elements and their counts from the most
        common to the least.  If n is None, then list all element counts.
        
        >>> Counter('abcdeabcdabcaba').most_common(3)
        [('a', 5), ('b', 4), ('c', 3)]
        
        """
        if n is None:
            return sorted(self.iteritems(), key=_itemgetter(1), reverse=True)
        else:
            return _heapq.nlargest(n, self.iteritems(), key=_itemgetter(1))

    def elements(self):
        """Iterator over elements repeating each as many times as its count.
        
        >>> c = Counter('ABCABC')
        >>> sorted(c.elements())
        ['A', 'A', 'B', 'B', 'C', 'C']
        
        # Knuth's example for prime factors of 1836:  2**2 * 3**3 * 17**1
        >>> prime_factors = Counter({2: 2, 3: 3, 17: 1})
        >>> product = 1
        >>> for factor in prime_factors.elements():     # loop over factors
        ...     product *= factor                       # and multiply them
        >>> product
        1836
        
        Note, if an element's count has been set to zero or is a negative
        number, elements() will ignore it.
        
        """
        return _chain.from_iterable(_starmap(_repeat, self.iteritems()))

    @classmethod
    def fromkeys(cls, iterable, v=None):
        raise NotImplementedError('Counter.fromkeys() is undefined.  Use Counter(iterable) instead.')

    def update(self, iterable=None, **kwds):
        """Like dict.update() but add counts instead of replacing them.
        
        Source can be an iterable, a dictionary, or another Counter instance.
        
        >>> c = Counter('which')
        >>> c.update('witch')           # add elements from another iterable
        >>> d = Counter('watch')
        >>> c.update(d)                 # add elements from another counter
        >>> c['h']                      # four 'h' in which, witch, and watch
        4
        
        """
        if iterable is not None:
            if isinstance(iterable, Mapping):
                if self:
                    self_get = self.get
                    for elem, count in iterable.iteritems():
                        self[elem] = self_get(elem, 0) + count

                else:
                    super(Counter, self).update(iterable)
            else:
                self_get = self.get
                for elem in iterable:
                    self[elem] = self_get(elem, 0) + 1

        if kwds:
            self.update(kwds)
        return

    def subtract(self, iterable=None, **kwds):
        """Like dict.update() but subtracts counts instead of replacing them.
        Counts can be reduced below zero.  Both the inputs and outputs are
        allowed to contain zero and negative counts.
        
        Source can be an iterable, a dictionary, or another Counter instance.
        
        >>> c = Counter('which')
        >>> c.subtract('witch')             # subtract elements from another iterable
        >>> c.subtract(Counter('watch'))    # subtract elements from another counter
        >>> c['h']                          # 2 in which, minus 1 in witch, minus 1 in watch
        0
        >>> c['w']                          # 1 in which, minus 1 in witch, minus 1 in watch
        -1
        
        """
        if iterable is not None:
            self_get = self.get
            if isinstance(iterable, Mapping):
                for elem, count in iterable.items():
                    self[elem] = self_get(elem, 0) - count

            else:
                for elem in iterable:
                    self[elem] = self_get(elem, 0) - 1

        if kwds:
            self.subtract(kwds)
        return

    def copy(self):
        """Return a shallow copy."""
        return self.__class__(self)

    def __reduce__(self):
        return (
         self.__class__, (dict(self),))

    def __delitem__(self, elem):
        """Like dict.__delitem__() but does not raise KeyError for missing values."""
        if elem in self:
            super(Counter, self).__delitem__(elem)

    def __repr__(self):
        if not self:
            return '%s()' % self.__class__.__name__
        items = ', '.join(map('%r: %r'.__mod__, self.most_common()))
        return '%s({%s})' % (self.__class__.__name__, items)

    def __add__(self, other):
        """Add counts from two counters.
        
        >>> Counter('abbb') + Counter('bcc')
        Counter({'b': 4, 'c': 2, 'a': 1})
        
        """
        if not isinstance(other, Counter):
            return NotImplemented
        result = Counter()
        for elem, count in self.items():
            newcount = count + other[elem]
            if newcount > 0:
                result[elem] = newcount

        for elem, count in other.items():
            if elem not in self and count > 0:
                result[elem] = count

        return result

    def __sub__(self, other):
        """ Subtract count, but keep only results with positive counts.
        
        >>> Counter('abbbc') - Counter('bccd')
        Counter({'b': 2, 'a': 1})
        
        """
        if not isinstance(other, Counter):
            return NotImplemented
        result = Counter()
        for elem, count in self.items():
            newcount = count - other[elem]
            if newcount > 0:
                result[elem] = newcount

        for elem, count in other.items():
            if elem not in self and count < 0:
                result[elem] = 0 - count

        return result

    def __or__(self, other):
        """Union is the maximum of value in either of the input counters.
        
        >>> Counter('abbb') | Counter('bcc')
        Counter({'b': 3, 'c': 2, 'a': 1})
        
        """
        if not isinstance(other, Counter):
            return NotImplemented
        result = Counter()
        for elem, count in self.items():
            other_count = other[elem]
            newcount = other_count if count < other_count else count
            if newcount > 0:
                result[elem] = newcount

        for elem, count in other.items():
            if elem not in self and count > 0:
                result[elem] = count

        return result

    def __and__(self, other):
        """ Intersection is the minimum of corresponding counts.
        
        >>> Counter('abbb') & Counter('bcc')
        Counter({'b': 1})
        
        """
        if not isinstance(other, Counter):
            return NotImplemented
        result = Counter()
        for elem, count in self.items():
            other_count = other[elem]
            newcount = count if count < other_count else other_count
            if newcount > 0:
                result[elem] = newcount

        return result


if __name__ == '__main__':
    from cPickle import loads, dumps
    Point = namedtuple('Point', 'x, y', True)
    p = Point(x=10, y=20)

    class Point(namedtuple('Point', 'x y')):
        __slots__ = ()

        @property
        def hypot(self):
            return (self.x ** 2 + self.y ** 2) ** 0.5

        def __str__(self):
            return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)


    for p in (Point(3, 4), Point(14, 5 / 7.0)):
        print p

    class Point(namedtuple('Point', 'x y')):
        """Point class with optimized _make() and _replace() without error-checking"""
        __slots__ = ()
        _make = classmethod(tuple.__new__)

        def _replace(self, _map=map, **kwds):
            return self._make(_map(kwds.get, ('x', 'y'), self))


    print Point(11, 22)._replace(x=100)
    Point3D = namedtuple('Point3D', Point._fields + ('z',))
    print Point3D.__doc__
    import doctest
    TestResults = namedtuple('TestResults', 'failed attempted')
    print TestResults(*doctest.testmod())