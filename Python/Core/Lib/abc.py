# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: abc.py
"""Abstract Base Classes (ABCs) according to PEP 3119."""
import types
from _weakrefset import WeakSet

class _C:
    pass


_InstanceType = type(_C())

def abstractmethod(funcobj):
    """A decorator indicating abstract methods.
    
    Requires that the metaclass is ABCMeta or derived from it.  A
    class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods are overridden.
    The abstract methods can be called using any of the normal
    'super' call mechanisms.
    
    Usage:
    
        class C:
            __metaclass__ = ABCMeta
            @abstractmethod
            def my_abstract_method(self, ...):
                ...
    """
    funcobj.__isabstractmethod__ = True
    return funcobj


class abstractproperty(property):
    """A decorator indicating abstract properties.
    
    Requires that the metaclass is ABCMeta or derived from it.  A
    class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract properties are overridden.
    The abstract properties can be called using any of the normal
    'super' call mechanisms.
    
    Usage:
    
        class C:
            __metaclass__ = ABCMeta
            @abstractproperty
            def my_abstract_property(self):
                ...
    
    This defines a read-only property; you can also define a read-write
    abstract property using the 'long' form of property declaration:
    
        class C:
            __metaclass__ = ABCMeta
            def getx(self): ...
            def setx(self, value): ...
            x = abstractproperty(getx, setx)
    """
    __isabstractmethod__ = True


class ABCMeta(type):
    """Metaclass for defining Abstract Base Classes (ABCs).
    
    Use this metaclass to create an ABC.  An ABC can be subclassed
    directly, and then acts as a mix-in class.  You can also register
    unrelated concrete classes (even built-in classes) and unrelated
    ABCs as 'virtual subclasses' -- these and their descendants will
    be considered subclasses of the registering ABC by the built-in
    issubclass() function, but the registering ABC won't show up in
    their MRO (Method Resolution Order) nor will method
    implementations defined by the registering ABC be callable (not
    even via super()).
    
    """
    _abc_invalidation_counter = 0

    def __new__(mcls, name, bases, namespace):
        cls = super(ABCMeta, mcls).__new__(mcls, name, bases, namespace)
        abstracts = set((name for name, value in namespace.items() if getattr(value, '__isabstractmethod__', False)))
        for base in bases:
            for name in getattr(base, '__abstractmethods__', set()):
                value = getattr(cls, name, None)
                if getattr(value, '__isabstractmethod__', False):
                    abstracts.add(name)

        cls.__abstractmethods__ = frozenset(abstracts)
        cls._abc_registry = WeakSet()
        cls._abc_cache = WeakSet()
        cls._abc_negative_cache = WeakSet()
        cls._abc_negative_cache_version = ABCMeta._abc_invalidation_counter
        return cls

    def register(cls, subclass):
        """Register a virtual subclass of an ABC."""
        if not isinstance(subclass, (type, types.ClassType)):
            raise TypeError('Can only register classes')
        if issubclass(subclass, cls):
            return
        if issubclass(cls, subclass):
            raise RuntimeError('Refusing to create an inheritance cycle')
        cls._abc_registry.add(subclass)
        ABCMeta._abc_invalidation_counter += 1

    def _dump_registry(cls, file=None):
        """Debug helper to print the ABC registry."""
        print >> file, 'Class: %s.%s' % (cls.__module__, cls.__name__)
        print >> file, 'Inv.counter: %s' % ABCMeta._abc_invalidation_counter
        for name in sorted(cls.__dict__.keys()):
            if name.startswith('_abc_'):
                value = getattr(cls, name)
                print >> file, '%s: %r' % (name, value)

    def __instancecheck__(cls, instance):
        """Override for isinstance(instance, cls)."""
        subclass = getattr(instance, '__class__', None)
        if subclass is not None and subclass in cls._abc_cache:
            return True
        else:
            subtype = type(instance)
            if subtype is _InstanceType:
                subtype = subclass
            if subtype is subclass or subclass is None:
                if cls._abc_negative_cache_version == ABCMeta._abc_invalidation_counter and subtype in cls._abc_negative_cache:
                    return False
                return cls.__subclasscheck__(subtype)
            return cls.__subclasscheck__(subclass) or cls.__subclasscheck__(subtype)

    def __subclasscheck__(cls, subclass):
        """Override for issubclass(subclass, cls)."""
        if subclass in cls._abc_cache:
            return True
        if cls._abc_negative_cache_version < ABCMeta._abc_invalidation_counter:
            cls._abc_negative_cache = WeakSet()
            cls._abc_negative_cache_version = ABCMeta._abc_invalidation_counter
        elif subclass in cls._abc_negative_cache:
            return False
        ok = cls.__subclasshook__(subclass)
        if ok is not NotImplemented:
            if ok:
                cls._abc_cache.add(subclass)
            else:
                cls._abc_negative_cache.add(subclass)
            return ok
        if cls in getattr(subclass, '__mro__', ()):
            cls._abc_cache.add(subclass)
            return True
        for rcls in cls._abc_registry:
            if issubclass(subclass, rcls):
                cls._abc_cache.add(subclass)
                return True

        for scls in cls.__subclasses__():
            if issubclass(subclass, scls):
                cls._abc_cache.add(subclass)
                return True

        cls._abc_negative_cache.add(subclass)
        return False