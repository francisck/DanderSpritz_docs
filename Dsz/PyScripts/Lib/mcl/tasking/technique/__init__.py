# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
TECHNIQUE_PROVIDER_ANY = 0
TECHNIQUE_MCL_INJECT = 'Mcl_ThreadInject'
TECHNIQUE_MCL_MEMORY = 'Mcl_Memory'
TECHNIQUE_MCL_PRIVILEGE = 'Mcl_Privilege'
TECHNIQUE_MCL_NTNATIVEAPI = 'Mcl_NtNativeApi'

def Lookup(cmdName, ifaceName, desiredTechnique):
    import mcl_platform.tasking.technique
    if len(ifaceName) == 0:
        return TECHNIQUE_PROVIDER_ANY
    else:
        fullTech = '_PROV_%s' % ifaceName
        if desiredTechnique != None and len(desiredTechnique) > 0:
            rtn, provider = mcl_platform.tasking.technique.Lookup(fullTech, desiredTechnique)
            if not rtn:
                raise RuntimeError("Lookup for technique '%s' failed" % desiredTechnique)
            return provider
        if cmdName != None and len(cmdName) > 0:
            rtn, provider = mcl_platform.tasking.technique.Lookup(fullTech, cmdName)
            if rtn:
                return provider
        rtn, provider = mcl_platform.tasking.technique.Lookup(fullTech, 'Default')
        if not rtn:
            return TECHNIQUE_PROVIDER_ANY
        return provider
        return