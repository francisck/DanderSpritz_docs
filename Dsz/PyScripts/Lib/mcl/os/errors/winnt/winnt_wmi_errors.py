# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: winnt_wmi_errors.py


def getErrorString(error):
    if error == 2147749889L:
        return 'Call failed.'
    else:
        if error == 2147749890L:
            return 'Object cannot be found.'
        if error == 2147749891L:
            return 'Current user does not have permission to perform the action.'
        if error == 2147749892L:
            return 'Provider has failed at some time other than during initialization.'
        if error == 2147749893L:
            return 'Type mismatch occurred.'
        if error == 2147749894L:
            return 'Not enough memory for the operation.'
        if error == 2147749895L:
            return 'The IWbemContext object is not valid.'
        if error == 2147749896L:
            return 'One of the parameters to the call is not correct.'
        if error == 2147749897L:
            return 'Resource, typically a remote server, is not currently available.'
        if error == 2147749898L:
            return 'Internal, critical, and unexpected error occurred. Report the error to Microsoft Technical Support.'
        if error == 2147749899L:
            return 'One or more network packets were corrupted during a remote session.'
        if error == 2147749900L:
            return 'Feature or operation is not supported.'
        if error == 2147749901L:
            return 'Parent class specified is not valid.'
        if error == 2147749902L:
            return 'Namespace specified cannot be found.'
        if error == 2147749903L:
            return 'Specified instance is not valid.'
        if error == 2147749904L:
            return 'Specified class is not valid.'
        if error == 2147749905L:
            return 'Provider referenced in the schema does not have a corresponding registration.'
        if error == 2147749906L:
            return 'Provider referenced in the schema has an incorrect or incomplete registration.'
        if error == 2147749907L:
            return 'COM cannot locate a provider referenced in the schema.'
        if error == 2147749908L:
            return 'Component, such as a provider, failed to initialize for internal reasons.'
        if error == 2147749909L:
            return 'Networking error that prevents normal operation has occurred.'
        if error == 2147749910L:
            return 'Requested operation is not valid. This error usually applies to invalid attempts to delete classes or properties.'
        if error == 2147749911L:
            return 'Query was not syntactically valid.'
        if error == 2147749912L:
            return 'Requested query language is not supported.'
        if error == 2147749913L:
            return 'In a put operation, the wbemChangeFlagCreateOnly flag was specified, but the instance already exists.'
        if error == 2147749914L:
            return 'Not possible to perform the add operation on this qualifier because the owning object does not permit overrides.'
        if error == 2147749915L:
            return 'User attempted to delete a qualifier that was not owned. The qualifier was inherited from a parent class.'
        if error == 2147749916L:
            return 'User attempted to delete a property that was not owned. The property was inherited from a parent class.'
        if error == 2147749917L:
            return 'Client made an unexpected and illegal sequence of calls, such as calling EndEnumeration before calling BeginEnumeration.'
        if error == 2147749918L:
            return 'User requested an illegal operation, such as spawning a class from an instance.'
        if error == 2147749919L:
            return 'Illegal attempt to specify a key qualifier on a property that cannot be a key. The keys are specified in the class definition for an object and cannot be altered on a per-instance basis.'
        if error == 2147749920L:
            return 'Current object is not a valid class definition. Either it is incomplete or it has not been registered with WMI using SWbemObject.Put_.'
        if error == 2147749921L:
            return 'Query is syntactically invalid.'
        if error == 2147749922L:
            return 'Reserved for future use.'
        if error == 2147749923L:
            return 'An attempt was made to modify a read-only property.'
        if error == 2147749924L:
            return 'Provider cannot perform the requested operation. This can include a query that is too complex, retrieving an instance, creating or updating a class, deleting a class, or enumerating a class.'
        if error == 2147749925L:
            return 'Attempt was made to make a change that invalidates a subclass.'
        if error == 2147749926L:
            return 'Attempt was made to delete or modify a class that has instances.'
        if error == 2147749927L:
            return 'Reserved for future use.'
        if error == 2147749928L:
            return 'Value of Nothing/NULL was specified for a property that must have a value, such as one that is marked by a Key, Indexed, or Not_Null qualifier.'
        if error == 2147749929L:
            return 'Variant value for a qualifier was provided that is not a legal qualifier type.'
        if error == 2147749930L:
            return 'CIM type specified for a property is not valid.'
        if error == 2147749931L:
            return 'Request was made with an out-of-range value or it is incompatible with the type.'
        if error == 2147749932L:
            return 'Illegal attempt was made to make a class singleton, such as when the class is derived from a non-singleton class.'
        if error == 2147749933L:
            return 'CIM type specified is invalid.'
        if error == 2147749934L:
            return 'Requested method is not available.'
        if error == 2147749935L:
            return 'Parameters provided for the method are invalid.'
        if error == 2147749936L:
            return 'There was an attempt to get qualifiers on a system property.'
        if error == 2147749937L:
            return 'Property type is not recognized.'
        if error == 2147749938L:
            return 'Asynchronous process has been canceled internally or by the user. Note that due to the timing and nature of the asynchronous operation, the operation may not have been truly canceled.'
        if error == 2147749939L:
            return 'User has requested an operation while WMI is in the process of shutting down.'
        if error == 2147749940L:
            return 'Attempt was made to reuse an existing method name from a parent class and the signatures do not match.'
        if error == 2147749941L:
            return 'One or more parameter values, such as a query text, is too complex or unsupported. WMI is therefore requested to retry the operation with simpler parameters.'
        if error == 2147749942L:
            return 'Parameter was missing from the method call.'
        if error == 2147749943L:
            return 'Method parameter has an invalid ID qualifier.'
        if error == 2147749944L:
            return 'One or more of the method parameters have ID qualifiers that are out of sequence.'
        if error == 2147749945L:
            return 'Return value for a method has an ID qualifier.'
        if error == 2147749946L:
            return 'Specified object path was invalid.'
        if error == 2147749947L:
            return 'Disk is out of space or the 4 GB limit on WMI repository (CIM repository) size is reached.'
        if error == 2147749948L:
            return 'Supplied buffer was too small to hold all of the objects in the enumerator or to read a string property.'
        if error == 2147749949L:
            return 'Provider does not support the requested put operation.'
        if error == 2147749950L:
            return 'Object with an incorrect type or version was encountered during marshaling.'
        if error == 2147749951L:
            return 'Packet with an incorrect type or version was encountered during marshaling.'
        if error == 2147749952L:
            return 'Packet has an unsupported version.'
        if error == 2147749953L:
            return 'Packet appears to be corrupt.'
        if error == 2147749954L:
            return 'Attempt was made to mismatch qualifiers, such as putting [key] on an object instead of a property.'
        if error == 2147749955L:
            return 'Duplicate parameter was declared in a CIM method.'
        if error == 2147749956L:
            return 'Reserved for future use.'
        if error == 2147749957L:
            return 'Call to IWbemObjectSink):):Indicate has failed. The provider can refire the event.'
        if error == 2147749958L:
            return 'Specified qualifier flavor was invalid.'
        if error == 2147749959L:
            return 'Attempt was made to create a reference that is circular (for example, deriving a class from itself).'
        if error == 2147749960L:
            return 'Specified class is not supported.'
        if error == 2147749961L:
            return 'Attempt was made to change a key when instances or subclasses are already using the key.'
        if error == 2147749968L:
            return 'An attempt was made to change an index when instances or subclasses are already using the index.'
        if error == 2147749969L:
            return 'Attempt was made to create more properties than the current version of the class supports.'
        if error == 2147749970L:
            return 'Property was redefined with a conflicting type in a derived class.'
        if error == 2147749971L:
            return 'Attempt was made in a derived class to override a qualifier that cannot be overridden.'
        if error == 2147749972L:
            return 'Method was re-declared with a conflicting signature in a derived class.'
        if error == 2147749973L:
            return 'Attempt was made to execute a method not marked with [implemented] in any relevant class.'
        if error == 2147749974L:
            return 'Attempt was made to execute a method marked with [disabled].'
        if error == 2147749975L:
            return 'Refresher is busy with another operation.'
        if error == 2147749976L:
            return 'Filtering query is syntactically invalid.'
        if error == 2147749977L:
            return 'The FROM clause of a filtering query references a class that is not an event class (not derived from __Event).'
        if error == 2147749978L:
            return 'A GROUP BY clause was used without the corresponding GROUP WITHIN clause.'
        if error == 2147749979L:
            return 'A GROUP BY clause was used. Aggregation on all properties is not supported.'
        if error == 2147749980L:
            return 'Dot notation was used on a property that is not an embedded object.'
        if error == 2147749981L:
            return 'A GROUP BY clause references a property that is an embedded object without using dot notation.'
        if error == 2147749983L:
            return 'Event provider registration query (__EventProviderRegistration) did not specify the classes for which events were provided.'
        if error == 2147749984L:
            return 'Request was made to back up or restore the repository while it was in use by WinMgmt.exe, or in Windows XP or later, the SVCHOST process that contains the Windows Management service.'
        if error == 2147749985L:
            return 'Asynchronous delivery queue overflowed from the event consumer being too slow.'
        if error == 2147749986L:
            return 'Operation failed because the client did not have the necessary security privilege.'
        if error == 2147749987L:
            return 'Operator is invalid for this property type.'
        if error == 2147749988L:
            return 'User specified a username/password/authority on a local connection. The user must use a blank username/password and rely on default security.'
        if error == 2147749989L:
            return 'Class was made abstract when its parent class is not abstract.'
        if error == 2147749990L:
            return 'Amended object was written without the WBEM_FLAG_USE_AMENDED_QUALIFIERS flag being specified.'
        if error == 2147749991L:
            return "Windows Server 2003 and Windows XP):  Client did not retrieve objects quickly enough from an enumeration. This constant is returned when a client creates an enumeration object, but does not retrieve objects from the enumerator in a timely fashion, causing the enumerator's object caches to back up."
        if error == 2147749992L:
            return 'Windows Server 2003 and Windows XP):  Null security descriptor was used.'
        if error == 2147749993L:
            return 'Windows Server 2003 and Windows XP):  Operation timed out.'
        if error == 2147749994L:
            return 'Windows Server 2003 and Windows XP):  Association is invalid.'
        if error == 2147749995L:
            return 'Windows Server 2003 and Windows XP):  Operation was ambiguous.'
        if error == 2147749996L:
            return 'Windows Server 2003 and Windows XP):  WMI is taking up too much memory. This can be caused by low memory availability or excessive memory consumption by WMI.'
        if error == 2147749997L:
            return 'Windows Server 2003 and Windows XP):  Operation resulted in a transaction conflict.'
        if error == 2147749998L:
            return 'Windows Server 2003 and Windows XP):  Transaction forced a rollback.'
        if error == 2147749999L:
            return 'Windows Server 2003 and Windows XP):  Locale used in the call is not supported.'
        if error == 2147750000L:
            return 'Windows Server 2003 and Windows XP):  Object handle is out-of-date.'
        if error == 2147750001L:
            return 'Windows Server 2003 and Windows XP):  Connection to the SQL database failed.'
        if error == 2147750002L:
            return 'Windows Server 2003 and Windows XP):  Handle request was invalid.'
        if error == 2147750003L:
            return 'Windows Server 2003 and Windows XP):  Property name contains more than 255 characters.'
        if error == 2147750004L:
            return 'Windows Server 2003 and Windows XP):  Class name contains more than 255 characters.'
        if error == 2147750005L:
            return 'Windows Server 2003 and Windows XP):  Method name contains more than 255 characters.'
        if error == 2147750006L:
            return 'Windows Server 2003 and Windows XP):  Qualifier name contains more than 255 characters.'
        if error == 2147750007L:
            return 'Windows Server 2003 and Windows XP):  The SQL command must be rerun because there is a deadlock in SQL. This can be returned only when data is being stored in an SQL database.'
        if error == 2147750008L:
            return 'Windows Server 2003 and Windows XP):  Database version does not match the version that the repository driver understands.'
        if error == 2147750009L:
            return 'Windows Server 2003 and Windows XP):  WMI cannot execute the delete operation because the provider does not allow it.'
        if error == 2147750010L:
            return 'Windows Server 2003 and Windows XP):  WMI cannot execute the put operation because the provider does not allow it.'
        if error == 2147750016L:
            return 'Windows Server 2003 and Windows XP):  Specified locale identifier was invalid for the operation.'
        if error == 2147750017L:
            return 'Windows Server 2003 and Windows XP):  Provider is suspended.'
        if error == 2147750018L:
            return 'Windows Server 2003 and Windows XP):  Object must be written to the WMI repository and retrieved again before the requested operation can succeed. This constant is returned when an object must be committed and retrieved to see the property value.'
        if error == 2147750019L:
            return 'Windows Server 2003 and Windows XP):  Operation cannot be completed no schema is available.'
        if error == 2147750020L:
            return 'Windows Server 2003 and Windows XP):  Provider cannot be registered because it is already registered.'
        if error == 2147750021L:
            return 'Windows Server 2003 and Windows XP):  Provider was not registered.'
        if error == 2147750022L:
            return 'Windows Server 2003 and Windows XP):  Fatal transport error occurred.'
        if error == 2147750023L:
            return 'Windows Server 2003 and Windows XP):  User attempted to set a computer name or domain without an encrypted connection.'
        if error == 2147750024L:
            return 'Windows Server 2003 and Windows XP):  A provider failed to report results within the specified timeout.'
        if error == 2147750025L:
            return 'Windows Server 2003 and Windows XP):  User attempted to put an instance with no defined key.'
        if error == 2147750026L:
            return 'Windows Server 2003 and Windows XP):  User attempted to register a provider instance but the COM server for the provider instance was unloaded.'
        if error == 2147753987L:
            return 'This computer does not have the necessary domain permissions to support the security functions that relate to the created subscription instance. Contact the Domain Administrator to get this computer added to the Windows Authorization Access Group.'
        if error == 2147753985L:
            return 'Provider registration overlaps with the system event domain.'
        if error == 2147753986L:
            return 'A WITHIN clause was not used in this query.'
        if error == 2147758081L:
            return 'Reserved for future use.'
        if error == 2147758082L:
            return 'Reserved for future use.'
        if error == 2147762177L:
            return 'Expected a qualifier name.'
        if error == 2147762178L:
            return "Expected semicolon or '='."
        if error == 2147762179L:
            return 'Expected an opening brace.'
        if error == 2147762180L:
            return 'Missing closing brace or an illegal array element.'
        if error == 2147762181L:
            return 'Expected a closing bracket.'
        if error == 2147762182L:
            return 'Expected closing parenthesis.'
        if error == 2147762183L:
            return 'Numeric value out of range or strings without quotes.'
        if error == 2147762184L:
            return 'Expected a type identifier.'
        if error == 2147762185L:
            return 'Expected an open parenthesis.'
        if error == 2147762186L:
            return 'Unexpected token in the file.'
        if error == 2147762187L:
            return 'Unrecognized or unsupported type identifier.'
        if error == 2147762188L:
            return 'Expected property or method name.'
        if error == 2147762189L:
            return 'Typedefs and enumerated types are not supported.'
        if error == 2147762190L:
            return 'Only a reference to a class object can have an alias value.'
        if error == 2147762191L:
            return 'Unexpected array initialization. Arrays must be declared with [].'
        if error == 2147762192L:
            return 'Invalid namespace path syntax.'
        if error == 2147762193L:
            return 'Duplicate amendment specifiers.'
        if error == 2147762194L:
            return '#pragma must be followed by a valid keyword.'
        if error == 2147762195L:
            return 'Invalid namespace path syntax.'
        if error == 2147762196L:
            return 'Unexpected character in class name must be an identifier.'
        if error == 2147762197L:
            return 'The value specified cannot be made into the appropriate type.'
        if error == 2147762198L:
            return 'Dollar sign must be followed by an alias name as an identifier.'
        if error == 2147762199L:
            return 'Invalid class declaration.'
        if error == 2147762200L:
            return "The instance declaration is invalid. It must start with 'instance of'"
        if error == 2147762201L:
            return "Expected dollar sign. An alias in the form '$name' must follow the 'as' keyword."
        if error == 2147762202L:
            return "'CIMTYPE' qualifier cannot be specified directly in a MOF file. Use standard type notation."
        if error == 2147762203L:
            return 'Duplicate property name was found in the MOF.'
        if error == 2147762204L:
            return 'Invalid namespace syntax. References to other servers are not allowed.'
        if error == 2147762205L:
            return 'Value out of range.'
        if error == 2147762206L:
            return 'The file is not a valid text MOF file or binary MOF file.'
        if error == 2147762207L:
            return 'Embedded objects cannot be aliases.'
        if error == 2147762208L:
            return 'NULL elements in an array are not supported.'
        if error == 2147762209L:
            return 'Qualifier was used more than once on the object.'
        if error == 2147762210L:
            return 'Expected a flavor type such as ToInstance, ToSubClass, EnableOverride, or DisableOverride.'
        if error == 2147762211L:
            return 'Combining EnableOverride and DisableOverride on same qualifier is not legal.'
        if error == 2147762212L:
            return 'An alias cannot be used twice.'
        if error == 2147762213L:
            return 'Combining Restricted, and ToInstance or ToSubClass is not legal.'
        if error == 2147762214L:
            return 'Methods cannot return array values.'
        if error == 2147762215L:
            return 'Arguments must have an In or Out qualifier.'
        if error == 2147762216L:
            return 'Invalid flags syntax.'
        if error == 2147762217L:
            return 'The final brace and semi-colon for a class are missing.'
        if error == 2147762218L:
            return 'A CIM version 2.2 feature is not supported for a qualifier value.'
        if error == 2147762219L:
            return 'The CIM version 2.2 data type is not supported.'
        if error == 2147762220L:
            return "Invalid delete instance syntax. It should be #pragma DeleteInstance('instancepath', FAIL|NOFAIL)."
        if error == 2147762221L:
            return 'Invalid qualifier syntax. It should be qualifiername):type=value,scope(class|instance), flavorname.'
        if error == 2147762222L:
            return 'The qualifier is used outside of its scope.'
        if error == 2147762223L:
            return 'Error creating temporary file. The temporary file is an intermediate stage in the MOF compilation.'
        if error == 2147762224L:
            return 'A file included in the MOF by the preprocessor command #include is invalid.'
        if error == 2147762225L:
            return 'The syntax for the preprocessor commands #pragma deleteinstance or #pragma deleteclass is invalid.'
        return None
        return None