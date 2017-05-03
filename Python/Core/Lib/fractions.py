# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fractions.py
"""Rational, infinite-precision, real numbers."""
from __future__ import division
from decimal import Decimal
import math
import numbers
import operator
import re
__all__ = [
 'Fraction', 'gcd']
Rational = numbers.Rational

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.
    
    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b

    return a


_RATIONAL_FORMAT = re.compile('\n    \\A\\s*                      # optional whitespace at the start, then\n    (?P<sign>[-+]?)            # an optional sign, then\n    (?=\\d|\\.\\d)                # lookahead for digit or .digit\n    (?P<num>\\d*)               # numerator (possibly empty)\n    (?:                        # followed by\n       (?:/(?P<denom>\\d+))?    # an optional denominator\n    |                          # or\n       (?:\\.(?P<decimal>\\d*))? # an optional fractional part\n       (?:E(?P<exp>[-+]?\\d+))? # and optional exponent\n    )\n    \\s*\\Z                      # and optional whitespace to finish\n', re.VERBOSE | re.IGNORECASE)

class Fraction(Rational):
    """This class implements rational numbers.
    
    In the two-argument form of the constructor, Fraction(8, 6) will
    produce a rational number equivalent to 4/3. Both arguments must
    be Rational. The numerator defaults to 0 and the denominator
    defaults to 1 so that Fraction(3) == 3 and Fraction() == 0.
    
    Fractions can also be constructed from:
    
      - numeric strings similar to those accepted by the
        float constructor (for example, '-2.3' or '1e10')
    
      - strings of the form '123/456'
    
      - float and Decimal instances
    
      - other Rational instances (including integers)
    
    """
    __slots__ = ('_numerator', '_denominator')

    def __new__(cls, numerator=0, denominator=None):
        """Constructs a Fraction.
        
        Takes a string like '3/2' or '1.5', another Rational instance, a
        numerator/denominator pair, or a float.
        
        Examples
        --------
        
        >>> Fraction(10, -8)
        Fraction(-5, 4)
        >>> Fraction(Fraction(1, 7), 5)
        Fraction(1, 35)
        >>> Fraction(Fraction(1, 7), Fraction(2, 3))
        Fraction(3, 14)
        >>> Fraction('314')
        Fraction(314, 1)
        >>> Fraction('-35/4')
        Fraction(-35, 4)
        >>> Fraction('3.1415') # conversion from numeric string
        Fraction(6283, 2000)
        >>> Fraction('-47e-2') # string may include a decimal exponent
        Fraction(-47, 100)
        >>> Fraction(1.47)  # direct construction from float (exact conversion)
        Fraction(6620291452234629, 4503599627370496)
        >>> Fraction(2.25)
        Fraction(9, 4)
        >>> Fraction(Decimal('1.47'))
        Fraction(147, 100)
        
        """
        self = super(Fraction, cls).__new__(cls)
        if denominator is None:
            if isinstance(numerator, Rational):
                self._numerator = numerator.numerator
                self._denominator = numerator.denominator
                return self
            if isinstance(numerator, float):
                value = Fraction.from_float(numerator)
                self._numerator = value._numerator
                self._denominator = value._denominator
                return self
            if isinstance(numerator, Decimal):
                value = Fraction.from_decimal(numerator)
                self._numerator = value._numerator
                self._denominator = value._denominator
                return self
            if isinstance(numerator, basestring):
                m = _RATIONAL_FORMAT.match(numerator)
                if m is None:
                    raise ValueError('Invalid literal for Fraction: %r' % numerator)
                numerator = int(m.group('num') or '0')
                denom = m.group('denom')
                if denom:
                    denominator = int(denom)
                else:
                    denominator = 1
                    decimal = m.group('decimal')
                    if decimal:
                        scale = 10 ** len(decimal)
                        numerator = numerator * scale + int(decimal)
                        denominator *= scale
                    exp = m.group('exp')
                    if exp:
                        exp = int(exp)
                        if exp >= 0:
                            numerator *= 10 ** exp
                        else:
                            denominator *= 10 ** (-exp)
                if m.group('sign') == '-':
                    numerator = -numerator
            else:
                raise TypeError('argument should be a string or a Rational instance')
        elif isinstance(numerator, Rational) and isinstance(denominator, Rational):
            numerator, denominator = numerator.numerator * denominator.denominator, denominator.numerator * numerator.denominator
        else:
            raise TypeError('both arguments should be Rational instances')
        if denominator == 0:
            raise ZeroDivisionError('Fraction(%s, 0)' % numerator)
        g = gcd(numerator, denominator)
        self._numerator = numerator // g
        self._denominator = denominator // g
        return self

    @classmethod
    def from_float(cls, f):
        """Converts a finite float to a rational number, exactly.
        
        Beware that Fraction.from_float(0.3) != Fraction(3, 10).
        
        """
        if isinstance(f, numbers.Integral):
            return cls(f)
        if not isinstance(f, float):
            raise TypeError('%s.from_float() only takes floats, not %r (%s)' % (
             cls.__name__, f, type(f).__name__))
        if math.isnan(f) or math.isinf(f):
            raise TypeError('Cannot convert %r to %s.' % (f, cls.__name__))
        return cls(*f.as_integer_ratio())

    @classmethod
    def from_decimal(cls, dec):
        """Converts a finite Decimal instance to a rational number, exactly."""
        from decimal import Decimal
        if isinstance(dec, numbers.Integral):
            dec = Decimal(int(dec))
        elif not isinstance(dec, Decimal):
            raise TypeError('%s.from_decimal() only takes Decimals, not %r (%s)' % (
             cls.__name__, dec, type(dec).__name__))
        if not dec.is_finite():
            raise TypeError('Cannot convert %s to %s.' % (dec, cls.__name__))
        sign, digits, exp = dec.as_tuple()
        digits = int(''.join(map(str, digits)))
        if sign:
            digits = -digits
        if exp >= 0:
            return cls(digits * 10 ** exp)
        else:
            return cls(digits, 10 ** (-exp))

    def limit_denominator(self, max_denominator=1000000):
        """Closest Fraction to self with denominator at most max_denominator.
        
        >>> Fraction('3.141592653589793').limit_denominator(10)
        Fraction(22, 7)
        >>> Fraction('3.141592653589793').limit_denominator(100)
        Fraction(311, 99)
        >>> Fraction(4321, 8765).limit_denominator(10000)
        Fraction(4321, 8765)
        
        """
        if max_denominator < 1:
            raise ValueError('max_denominator should be at least 1')
        if self._denominator <= max_denominator:
            return Fraction(self)
        else:
            p0, q0, p1, q1 = (0, 1, 1, 0)
            n, d = self._numerator, self._denominator
            while True:
                a = n // d
                q2 = q0 + a * q1
                if q2 > max_denominator:
                    break
                p0, q0, p1, q1 = (
                 p1, q1, p0 + a * p1, q2)
                n, d = d, n - a * d

            k = (max_denominator - q0) // q1
            bound1 = Fraction(p0 + k * p1, q0 + k * q1)
            bound2 = Fraction(p1, q1)
            if abs(bound2 - self) <= abs(bound1 - self):
                return bound2
            return bound1

    @property
    def numerator(a):
        return a._numerator

    @property
    def denominator(a):
        return a._denominator

    def __repr__(self):
        """repr(self)"""
        return 'Fraction(%s, %s)' % (self._numerator, self._denominator)

    def __str__(self):
        """str(self)"""
        if self._denominator == 1:
            return str(self._numerator)
        else:
            return '%s/%s' % (self._numerator, self._denominator)

    def _operator_fallbacks(monomorphic_operator, fallback_operator):
        """Generates forward and reverse operators given a purely-rational
        operator and a function from the operator module.
        
        Use this like:
        __op__, __rop__ = _operator_fallbacks(just_rational_op, operator.op)
        
        In general, we want to implement the arithmetic operations so
        that mixed-mode operations either call an implementation whose
        author knew about the types of both arguments, or convert both
        to the nearest built in type and do the operation there. In
        Fraction, that means that we define __add__ and __radd__ as:
        
            def __add__(self, other):
                # Both types have numerators/denominator attributes,
                # so do the operation directly
                if isinstance(other, (int, long, Fraction)):
                    return Fraction(self.numerator * other.denominator +
                                    other.numerator * self.denominator,
                                    self.denominator * other.denominator)
                # float and complex don't have those operations, but we
                # know about those types, so special case them.
                elif isinstance(other, float):
                    return float(self) + other
                elif isinstance(other, complex):
                    return complex(self) + other
                # Let the other type take over.
                return NotImplemented
        
            def __radd__(self, other):
                # radd handles more types than add because there's
                # nothing left to fall back to.
                if isinstance(other, Rational):
                    return Fraction(self.numerator * other.denominator +
                                    other.numerator * self.denominator,
                                    self.denominator * other.denominator)
                elif isinstance(other, Real):
                    return float(other) + float(self)
                elif isinstance(other, Complex):
                    return complex(other) + complex(self)
                return NotImplemented
        
        
        There are 5 different cases for a mixed-type addition on
        Fraction. I'll refer to all of the above code that doesn't
        refer to Fraction, float, or complex as "boilerplate". 'r'
        will be an instance of Fraction, which is a subtype of
        Rational (r : Fraction <: Rational), and b : B <:
        Complex. The first three involve 'r + b':
        
            1. If B <: Fraction, int, float, or complex, we handle
               that specially, and all is well.
            2. If Fraction falls back to the boilerplate code, and it
               were to return a value from __add__, we'd miss the
               possibility that B defines a more intelligent __radd__,
               so the boilerplate should return NotImplemented from
               __add__. In particular, we don't handle Rational
               here, even though we could get an exact answer, in case
               the other type wants to do something special.
            3. If B <: Fraction, Python tries B.__radd__ before
               Fraction.__add__. This is ok, because it was
               implemented with knowledge of Fraction, so it can
               handle those instances before delegating to Real or
               Complex.
        
        The next two situations describe 'b + r'. We assume that b
        didn't know about Fraction in its implementation, and that it
        uses similar boilerplate code:
        
            4. If B <: Rational, then __radd_ converts both to the
               builtin rational type (hey look, that's us) and
               proceeds.
            5. Otherwise, __radd__ tries to find the nearest common
               base ABC, and fall back to its builtin type. Since this
               class doesn't subclass a concrete type, there's no
               implementation to fall back to, so we need to try as
               hard as possible to return an actual value, or the user
               will get a TypeError.
        
        """

        def forward(a, b):
            if isinstance(b, (int, long, Fraction)):
                return monomorphic_operator(a, b)
            else:
                if isinstance(b, float):
                    return fallback_operator(float(a), b)
                if isinstance(b, complex):
                    return fallback_operator(complex(a), b)
                return NotImplemented

        forward.__name__ = '__' + fallback_operator.__name__ + '__'
        forward.__doc__ = monomorphic_operator.__doc__

        def reverse(b, a):
            if isinstance(a, Rational):
                return monomorphic_operator(a, b)
            else:
                if isinstance(a, numbers.Real):
                    return fallback_operator(float(a), float(b))
                if isinstance(a, numbers.Complex):
                    return fallback_operator(complex(a), complex(b))
                return NotImplemented

        reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
        reverse.__doc__ = monomorphic_operator.__doc__
        return (
         forward, reverse)

    def _add(a, b):
        """a + b"""
        return Fraction(a.numerator * b.denominator + b.numerator * a.denominator, a.denominator * b.denominator)

    __add__, __radd__ = _operator_fallbacks(_add, operator.add)

    def _sub(a, b):
        """a - b"""
        return Fraction(a.numerator * b.denominator - b.numerator * a.denominator, a.denominator * b.denominator)

    __sub__, __rsub__ = _operator_fallbacks(_sub, operator.sub)

    def _mul(a, b):
        """a * b"""
        return Fraction(a.numerator * b.numerator, a.denominator * b.denominator)

    __mul__, __rmul__ = _operator_fallbacks(_mul, operator.mul)

    def _div(a, b):
        """a / b"""
        return Fraction(a.numerator * b.denominator, a.denominator * b.numerator)

    __truediv__, __rtruediv__ = _operator_fallbacks(_div, operator.truediv)
    __div__, __rdiv__ = _operator_fallbacks(_div, operator.div)

    def __floordiv__(a, b):
        """a // b"""
        div = a / b
        if isinstance(div, Rational):
            return div.numerator // div.denominator
        else:
            return math.floor(div)

    def __rfloordiv__(b, a):
        """a // b"""
        div = a / b
        if isinstance(div, Rational):
            return div.numerator // div.denominator
        else:
            return math.floor(div)

    def __mod__(a, b):
        """a % b"""
        div = a // b
        return a - b * div

    def __rmod__(b, a):
        """a % b"""
        div = a // b
        return a - b * div

    def __pow__(a, b):
        """a ** b
        
        If b is not an integer, the result will be a float or complex
        since roots are generally irrational. If b is an integer, the
        result will be rational.
        
        """
        if isinstance(b, Rational):
            if b.denominator == 1:
                power = b.numerator
                if power >= 0:
                    return Fraction(a._numerator ** power, a._denominator ** power)
                else:
                    return Fraction(a._denominator ** (-power), a._numerator ** (-power))

            else:
                return float(a) ** float(b)
        else:
            return float(a) ** b

    def __rpow__(b, a):
        """a ** b"""
        if b._denominator == 1 and b._numerator >= 0:
            return a ** b._numerator
        if isinstance(a, Rational):
            return Fraction(a.numerator, a.denominator) ** b
        if b._denominator == 1:
            return a ** b._numerator
        return a ** float(b)

    def __pos__(a):
        """+a: Coerces a subclass instance to Fraction"""
        return Fraction(a._numerator, a._denominator)

    def __neg__(a):
        """-a"""
        return Fraction(-a._numerator, a._denominator)

    def __abs__(a):
        """abs(a)"""
        return Fraction(abs(a._numerator), a._denominator)

    def __trunc__(a):
        """trunc(a)"""
        if a._numerator < 0:
            return -(-a._numerator // a._denominator)
        else:
            return a._numerator // a._denominator

    def __hash__(self):
        """hash(self)
        
        Tricky because values that are exactly representable as a
        float must have the same hash as that float.
        
        """
        if self._denominator == 1:
            return hash(self._numerator)
        else:
            if self == float(self):
                return hash(float(self))
            return hash((self._numerator, self._denominator))

    def __eq__(a, b):
        """a == b"""
        if isinstance(b, Rational):
            return a._numerator == b.numerator and a._denominator == b.denominator
        if isinstance(b, numbers.Complex) and b.imag == 0:
            b = b.real
        if isinstance(b, float):
            if math.isnan(b) or math.isinf(b):
                return 0.0 == b
            else:
                return a == a.from_float(b)

        else:
            return NotImplemented

    def _richcmp(self, other, op):
        """Helper for comparison operators, for internal use only.
        
        Implement comparison between a Rational instance `self`, and
        either another Rational instance or a float `other`.  If
        `other` is not a Rational instance or a float, return
        NotImplemented. `op` should be one of the six standard
        comparison operators.
        
        """
        if isinstance(other, Rational):
            return op(self._numerator * other.denominator, self._denominator * other.numerator)
        if isinstance(other, complex):
            raise TypeError('no ordering relation is defined for complex numbers')
        if isinstance(other, float):
            if math.isnan(other) or math.isinf(other):
                return op(0.0, other)
            else:
                return op(self, self.from_float(other))

        else:
            return NotImplemented

    def __lt__(a, b):
        """a < b"""
        return a._richcmp(b, operator.lt)

    def __gt__(a, b):
        """a > b"""
        return a._richcmp(b, operator.gt)

    def __le__(a, b):
        """a <= b"""
        return a._richcmp(b, operator.le)

    def __ge__(a, b):
        """a >= b"""
        return a._richcmp(b, operator.ge)

    def __nonzero__(a):
        """a != 0"""
        return a._numerator != 0

    def __reduce__(self):
        return (
         self.__class__, (str(self),))

    def __copy__(self):
        if type(self) == Fraction:
            return self
        return self.__class__(self._numerator, self._denominator)

    def __deepcopy__(self, memo):
        if type(self) == Fraction:
            return self
        return self.__class__(self._numerator, self._denominator)