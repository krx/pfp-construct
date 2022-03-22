#!/usr/bin/env python
# encoding: utf-8

"""
This module of native functions is implemented for
compatability with 010 editor functions. Some of these functions
are nops, some are fully implemented.
"""

import six
import sys

from pfp.native import native
import pfp.errors as errors
# import pfp.fields
import construct as C


def _cmp(a, b):
    if six.PY3:
        return (a > b) - (a < b)
    else:
        return cmp(a, b)


# http://www.sweetscape.com/010editor/manual/FuncString.htm

# double Atof( const char s[] )
@native(name="Atof", ret=C.Double)
def Atof(params, ctxt, scope, stream, coord):
    if len(params) < 1:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "one arg"
        )
    return float(PYSTR(params[0]))


# int Atoi( const char s[] )
@native(name="Atoi", ret=C.Int)
def Atoi(params, ctxt, scope, stream, coord):
    if len(params) < 1:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "one arg"
        )
    return int(PYSTR(params[0]))


# int64 BinaryStrToInt( const char s[] )
@native(name="BinaryStrToInt", ret=C.Long)
def BinaryStrToInt(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] ConvertString( const char src[], int srcCharSet, int destCharSet )
@native(name="ConvertString", ret=C.CString)
def ConvertString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# string DosDateToString( DOSDATE d, char format[] = "MM/dd/yyyy" )
@native(name="DosDateToString", ret=C.CString)
def DosDateToString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# string DosTimeToString( DOSTIME t, char format[] = "hh:mm:ss" )
@native(name="DosTimeToString", ret=C.CString)
def DosTimeToString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# string EnumToString( enum e )
@native(name="EnumToString", ret=C.CString)
def EnumToString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] FileNameGetBase( const char path[], int includeExtension=true )
@native(name="FileNameGetBase", ret=C.CString)
def FileNameGetBase(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wchar_t[] FileNameGetBaseW( const wchar_t path[], int includeExtension=true )
@native(name="FileNameGetBaseW", ret=C.CString)
def FileNameGetBaseW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] FileNameGetExtension( const char path[] )
@native(name="FileNameGetExtension", ret=C.CString)
def FileNameGetExtension(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wchar_t[] FileNameGetExtensionW( const wchar_t path[] )
@native(name="FileNameGetExtensionW", ret=C.CString)
def FileNameGetExtensionW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] FileNameGetPath( const char path[], int includeSlash=true )
@native(name="FileNameGetPath", ret=C.CString)
def FileNameGetPath(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wchar_t[] FileNameGetPathW( const wchar_t path[], int includeSlash=true )
@native(name="FileNameGetPathW", ret=C.CString)
def FileNameGetPathW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] FileNameSetExtension( const char path[], const char extension[] )
@native(name="FileNameSetExtension", ret=C.CString)
def FileNameSetExtension(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wchar_t[] FileNameSetExtensionW( const wchar_t path[], const wchar_t extension[] )
@native(name="FileNameSetExtensionW", ret=C.CString)
def FileNameSetExtensionW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# string FileTimeToString( FILETIME ft, char format[] = "MM/dd/yyyy hh:mm:ss" )
@native(name="FileTimeToString", ret=C.CString)
def FileTimeToString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] IntToBinaryStr( int64 num, int numGroups=0, int includeSpaces=true )
@native(name="IntToBinaryStr", ret=C.CString)
def IntToBinaryStr(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int Memcmp( const uchar s1[], const uchar s2[], int n )
@native(name="Memcmp", ret=C.Int)
def Memcmp(params, ctxt, scope, stream, coord):
    """
    int Memcmp( const uchar s1[], const uchar s2[], int n )

    Compares the first n bytes of s1 and s2. Returns a value less than zero if
    s1 is less than s2, zero if they are equal, or a value greater than zero if
    s1 is greater than s2.
    """
    if len(params) < 3:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "3 arguments",
        )
    s1 = PYSTR(params[0])
    s2 = PYSTR(params[1])
    n = PYVAL(params[2])

    s1_sub = s1[:n]
    s2_sub = s2[:n]

    return _cmp(s1_sub, s2_sub)


# void Memcpy( uchar dest[], const uchar src[], int n, int destOffset=0, int srcOffset=0 )
@native(name="Memcpy", ret=C.Pass)
def Memcpy(params, ctxt, scope, stream, coord):
    if len(params) < 3:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "at least 3 args"
        )
    if len(params) > 5:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "at most 5 args"
        )

    dest = params[0]
    src = params[1]
    n = PYVAL(params[2])

    if len(params) > 3:
        dest_offset = PYVAL(params[3])
    else:
        dest_offset = 0

    if len(params) > 4:
        src_offset = PYVAL(params[4])
    else:
        src_offset = 0

    if not isinstance(dest, pfp.fields.Array):
        raise errors.InvalidArguments(
            coord, dest.__class__.__name__, "an array"
        )

    if not isinstance(src, pfp.fields.Array):
        raise errors.InvalidArguments(
            coord, src.__class__.__name__, "an array"
        )

    count = 0
    while n > 0:
        val = dest.field_cls()
        val._pfp__set_value(src[src_offset + count]._pfp__value)
        # TODO clone it
        dest[dest_offset + count] = val
        count += 1
        n -= 1


# void Memset( uchar s[], int c, int n )
@native(name="Memset", ret=C.Pass)
def Memset(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# string OleTimeToString( OLETIME ot, char format[] = "MM/dd/yyyy hh:mm:ss" )
@native(name="OleTimeToString", ret=C.CString)
def OleTimeToString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int RegExMatch( string str, string regex );
@native(name="RegExMatch", ret=C.Int)
def RegExMatch(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int RegExMatchW( wstring str, wstring regex );
@native(name="RegExMatchW", ret=C.Int)
def RegExMatchW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int RegExSearch( string str, string regex, int &matchSize, int startPos=0 );
@native(name="RegExSearch", ret=C.Int)
def RegExSearch(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int RegExSearchW( wstring str, wstring regex, int &matchSize, int startPos=0 );
@native(name="RegExSearchW", ret=C.Int)
def RegExSearchW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int SPrintf( char buffer[], const char format[] [, argument, ... ] )
@native(name="SPrintf", ret=C.Int)
def SPrintf(params, ctxt, scope, stream, coord):
    if len(params) < 2:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "at least 2 args"
        )

    if len(params) == 2:
        params[0]._pfp__set_value(PYSTR(params[1]))
        return len(PYSTR(params[1]))

    parts = []
    for part in params[2:]:
        if isinstance(part, pfp.fields.Array) or isinstance(
            part, C.CString
        ):
            parts.append(PYSTR(part))
        else:
            parts.append(PYVAL(part))

    new_value = PYSTR(params[1]) % tuple(parts)
    params[0]._pfp__set_value(new_value)
    return len(new_value)


# int SScanf( char str[], char format[], ... )
@native(name="SScanf", ret=C.Int)
def SScanf(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void Strcat( char dest[], const char src[] )
@native(name="Strcat", ret=C.Pass)
def Strcat(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int Strchr( const char s[], char c )
@native(name="Strchr", ret=C.Int)
def Strchr(params, ctxt, scope, stream, coord):
    if len(params) != 2:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "2 arguments"
        )

    haystack = PYSTR(params[0])
    needle = chr(PYVAL(params[1]))

    try:
        return haystack.index(needle)

    # expected condition when the substring doesn't exist
    except ValueError as e:
        return -1


# int Strcmp( const char s1[], const char s2[] )
@native(name="Strcmp", ret=C.Int)
def Strcmp(params, ctxt, scope, stream, coord):
    if len(params) != 2:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "2 arguments"
        )
    str1 = PYSTR(params[0])
    str2 = PYSTR(params[1])

    return _cmp(str1, str2)


# void Strcpy( char dest[], const char src[] )
@native(name="Strcpy", ret=C.Pass)
def Strcpy(params, ctxt, scope, stream, coord):
    if len(params) != 2:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "2 arguments"
        )

    params[0]._pfp__set_value(PYSTR(params[1]))


# char[] StrDel( const char str[], int start, int count )
@native(name="StrDel", ret=C.CString)
def StrDel(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int Stricmp( const char s1[], const char s2[] )
@native(name="Stricmp", ret=C.Int)
def Stricmp(params, ctxt, scope, stream, coord):
    if len(params) != 2:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "2 arguments"
        )
    str1 = PYSTR(params[0]).lower()
    str2 = PYSTR(params[1]).lower()

    return _cmp(str1, str2)


# int StringToDosDate( string s, DOSDATE &d, char format[] = "MM/dd/yyyy" )
@native(name="StringToDosDate", ret=C.Int)
def StringToDosDate(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int StringToDosTime( string s, DOSTIME &t, char format[] = "hh:mm:ss" )
@native(name="StringToDosTime", ret=C.Int)
def StringToDosTime(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int StringToFileTime( string s, FILETIME &ft, char format[] = "MM/dd/yyyy hh:mm:ss" )
@native(name="StringToFileTime", ret=C.Int)
def StringToFileTime(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int StringToOleTime( string s, OLETIME &ot, char format[] = "MM/dd/yyyy hh:mm:ss" )
@native(name="StringToOleTime", ret=C.Int)
def StringToOleTime(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int StringToTimeT( string s, time_t &t, char format[] = "MM/dd/yyyy hh:mm:ss" )
@native(name="StringToTimeT", ret=C.Int)
def StringToTimeT(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] StringToUTF8( const char src[], int srcCharSet=CHARSET_ANSI )
@native(name="StringToUTF8", ret=C.CString)
def StringToUTF8(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wstring StringToWString( const char str[], int srcCharSet=CHARSET_ANSI )
@native(name="StringToWString", ret=C.CString)
def StringToWString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int Strlen( const char s[] )
@native(name="Strlen", ret=C.Int)
def Strlen(params, ctxt, scope, stream, coord):
    if len(params) != 1:
        raise errors.InvalidArguments(
            coord, "1 argument", "{} args".format(len(params))
        )
    val = params[0]
    if isinstance(val, pfp.fields.Array):
        val = val._array_to_str()
    else:
        val = PYVAL(val)
    return len(val)


# int Strncmp( const char s1[], const char s2[], int n )
@native(name="Strncmp", ret=C.Int)
def Strncmp(params, ctxt, scope, stream, coord):
    if len(params) != 3:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "3 arguments"
        )
    max_chars = PYVAL(params[2])
    str1 = PYSTR(params[0])[:max_chars]
    str2 = PYSTR(params[1])[:max_chars]

    return _cmp(str1, str2)


# void Strncpy( char dest[], const char src[], int n )
@native(name="Strncpy", ret=C.Pass)
def Strncpy(params, ctxt, scope, stream, coord):
    if len(params) != 3:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "3 arguments"
        )

    max_len = PYVAL(params[2])
    params[0]._pfp__set_value(PYSTR(params[1])[:max_len])


# int Strnicmp( const char s1[], const char s2[], int n )
@native(name="Strnicmp", ret=C.Int)
def Strnicmp(params, ctxt, scope, stream, coord):
    if len(params) != 3:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "3 arguments"
        )
    max_chars = PYVAL(params[2])
    str1 = PYSTR(params[0])[:max_chars].lower()
    str2 = PYSTR(params[1])[:max_chars].lower()

    return _cmp(str1, str2)


# int Strstr( const char s1[], const char s2[] )
@native(name="Strstr", ret=C.Int)
def Strstr(params, ctxt, scope, stream, coord):
    if len(params) != 2:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "2 arguments"
        )

    haystack = PYSTR(params[0])
    needle = PYSTR(params[1])

    try:
        return haystack.index(needle)

    # expected condition when the substring doesn't exist
    except ValueError as e:
        return -1


# char[] SubStr( const char str[], int start, int count=-1 )
@native(name="SubStr", ret=C.CString)
def SubStr(params, ctxt, scope, stream, coord):
    if len(params) < 2:
        raise errors.InvalidArguments(
            coord, "2 arguments", "{} args".format(len(params))
        )

    string = PYSTR(params[0])
    start = PYVAL(params[1])
    count = -1
    if len(params) > 2:
        count = PYVAL(params[2])
    if count < 0:
        count = -1

    if count == -1:
        return string[start:]
    else:
        return string[start : start + count]


# string TimeTToString( time_t t, char format[] = "MM/dd/yyyy hh:mm:ss" )
@native(name="TimeTToString", ret=C.CString)
def TimeTToString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char ToLower( char c )
@native(name="ToLower", ret=C.Byte)
def ToLower(params, ctxt, scope, stream, coord):
    if len(params) != 1:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "1 argument"
        )
    return ord(chr(PYVAL(params[0])).lower())


# wchar_t ToLowerW( wchar_t c )
@native(name="ToLowerW", ret=C.Short)
def ToLowerW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char ToUpper( char c )
@native(name="ToUpper", ret=C.Byte)
def ToUpper(params, ctxt, scope, stream, coord):
    if len(params) != 1:
        raise errors.InvalidArguments(
            coord, "{} args".format(len(params)), "1 argument"
        )
    return ord(chr(PYVAL(params[0])).upper())


# void WMemcmp( const wchar_t s1[], const wchar_t s2[], int n )
@native(name="WMemcmp", ret=C.Pass)
def WMemcmp(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WMemcpy( wchar_t dest[], const wchar_t src[], int n, int destOffset=0, int srcOffset=0 )
@native(name="WMemcpy", ret=C.Pass)
def WMemcpy(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WMemset( wchar_t s[], int c, int n )
@native(name="WMemset", ret=C.Pass)
def WMemset(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WStrcat( wchar_t dest[], const wchar_t src[] )
@native(name="WStrcat", ret=C.Pass)
def WStrcat(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int WStrchr( const wchar_t s[], wchar_t c )
@native(name="WStrchr", ret=C.Int)
def WStrchr(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int WStrcmp( const wchar_t s1[], const wchar_t s2[] )
@native(name="WStrcmp", ret=C.Int)
def WStrcmp(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WStrcpy( wchar_t dest[], const wchar_t src[] )
@native(name="WStrcpy", ret=C.Pass)
def WStrcpy(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wchar_t[] WStrDel( const whar_t str[], int start, int count )
@native(name="WStrDel", ret=C.CString)
def WStrDel(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int WStricmp( const wchar_t s1[], const wchar_t s2[] )
@native(name="WStricmp", ret=C.Int)
def WStricmp(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] WStringToString( const wchar_t str[], int destCharSet=CHARSET_ANSI )
@native(name="WStringToString", ret=C.CString)
def WStringToString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] WStringToUTF8( const wchar_t str[] )
@native(name="WStringToUTF8", ret=C.CString)
def WStringToUTF8(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int WStrlen( const wchar_t s[] )
@native(name="WStrlen", ret=C.Int)
def WStrlen(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int WStrncmp( const wchar_t s1[], const wchar_t s2[], int n )
@native(name="WStrncmp", ret=C.Int)
def WStrncmp(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WStrncpy( wchar_t dest[], const wchar_t src[], int n )
@native(name="WStrncpy", ret=C.Pass)
def WStrncpy(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int WStrnicmp( const wchar_t s1[], const wchar_t s2[], int n )
@native(name="WStrnicmp", ret=C.Int)
def WStrnicmp(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int WStrstr( const wchar_t s1[], const wchar_t s2[] )
@native(name="WStrstr", ret=C.Int)
def WStrstr(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wchar_t[] WSubStr( const wchar_t str[], int start, int count=-1 )
@native(name="WSubStr", ret=C.CString)
def WSubStr(params, ctxt, scope, stream, coord):
    raise NotImplementedError()
