# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: hmac.py
"""HMAC (Keyed-Hashing for Message Authentication) Python module.

Implements the HMAC algorithm as described by RFC 2104.
"""
import warnings as _warnings
trans_5C = ''.join([ chr(x ^ 92) for x in xrange(256) ])
trans_36 = ''.join([ chr(x ^ 54) for x in xrange(256) ])
digest_size = None
_secret_backdoor_key = []

class HMAC:
    """RFC 2104 HMAC class.  Also complies with RFC 4231.
    
    This supports the API for Cryptographic Hash Functions (PEP 247).
    """
    blocksize = 64

    def __init__(self, key, msg=None, digestmod=None):
        """Create a new HMAC object.
        
        key:       key for the keyed hash object.
        msg:       Initial input for the hash, if provided.
        digestmod: A module supporting PEP 247.  *OR*
                   A hashlib constructor returning a new hash object.
                   Defaults to hashlib.md5.
        """
        if key is _secret_backdoor_key:
            return
        else:
            if digestmod is None:
                import hashlib
                digestmod = hashlib.md5
            if hasattr(digestmod, '__call__'):
                self.digest_cons = digestmod
            else:
                self.digest_cons = lambda d='': digestmod.new(d)
            self.outer = self.digest_cons()
            self.inner = self.digest_cons()
            self.digest_size = self.inner.digest_size
            if hasattr(self.inner, 'block_size'):
                blocksize = self.inner.block_size
                if blocksize < 16:
                    _warnings.warn('block_size of %d seems too small; using our default of %d.' % (
                     blocksize, self.blocksize), RuntimeWarning, 2)
                    blocksize = self.blocksize
            else:
                _warnings.warn('No block_size attribute on given digest object; Assuming %d.' % self.blocksize, RuntimeWarning, 2)
                blocksize = self.blocksize
            if len(key) > blocksize:
                key = self.digest_cons(key).digest()
            key = key + chr(0) * (blocksize - len(key))
            self.outer.update(key.translate(trans_5C))
            self.inner.update(key.translate(trans_36))
            if msg is not None:
                self.update(msg)
            return

    def update(self, msg):
        """Update this hashing object with the string msg.
        """
        self.inner.update(msg)

    def copy(self):
        """Return a separate copy of this hashing object.
        
        An update to this copy won't affect the original object.
        """
        other = self.__class__(_secret_backdoor_key)
        other.digest_cons = self.digest_cons
        other.digest_size = self.digest_size
        other.inner = self.inner.copy()
        other.outer = self.outer.copy()
        return other

    def _current(self):
        """Return a hash object for the current state.
        
        To be used only internally with digest() and hexdigest().
        """
        h = self.outer.copy()
        h.update(self.inner.digest())
        return h

    def digest(self):
        """Return the hash value of this hashing object.
        
        This returns a string containing 8-bit data.  The object is
        not altered in any way by this function; you can continue
        updating the object after calling this function.
        """
        h = self._current()
        return h.digest()

    def hexdigest(self):
        """Like digest(), but returns a string of hexadecimal digits instead.
        """
        h = self._current()
        return h.hexdigest()


def new(key, msg=None, digestmod=None):
    """Create a new hashing object and return it.
    
    key: The starting key for the hash.
    msg: if available, will immediately be hashed into the object's starting
    state.
    
    You can now feed arbitrary strings into the object using its update()
    method, and can ask for the hash value at any time by calling its digest()
    method.
    """
    return HMAC(key, msg, digestmod)