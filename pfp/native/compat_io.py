#!/usr/bin/env python
# encoding: utf-8

"""
This module of native functions is implemented for
compatability with 010 editor functions. Some of these functions
are nops, some are fully implemented.
"""

from pytest import skip
import six
import sys

from pfp.native import native
import pfp.interp
import pfp.errors as errors
import pfp.bitwrap as bitwrap
import construct as C

from pfp.utils import evaluate

# http://www.sweetscape.com/010editor/manual/FuncIO.htm

# void BigEndian()
@native(name="BigEndian", ret=None)
def BigEndian(params, ctxt, scope, stream, coord):
    if len(params) > 0:
        raise errors.InvalidArguments(
            coord, "0 arguments", "{} args".format(len(params))
        )
    pfp.interp.Endian.current = pfp.interp.Endian.BIG


# void BitfieldDisablePadding()
@native(name="BitfieldDisablePadding", ret=None, send_interp=True)
def BitfieldDisablePadding(params, ctxt, scope, stream, coord, interp):
    if len(params) > 0:
        raise errors.InvalidArguments(
            coord, "0 arguments", "{} args".format(len(params))
        )
    interp.set_bitfield_padded(False)


# void BitfieldEnablePadding()
@native(name="BitfieldEnablePadding", ret=None, send_interp=True)
def BitfieldEnablePadding(params, ctxt, scope, stream, coord, interp):
    if len(params) > 0:
        raise errors.InvalidArguments(
            coord, "0 arguments", "{} args".format(len(params))
        )
    interp.set_bitfield_padded(True)


# void BitfieldLeftToRight()
@native(name="BitfieldLeftToRight", ret=None, send_interp=True)
def BitfieldLeftToRight(params, ctxt, scope, stream, coord, interp):
    if len(params) > 0:
        raise errors.InvalidArguments(
            coord, "0 arguments", "{} args".format(len(params))
        )
    interp.set_bitfield_direction(interp.BITFIELD_DIR_LEFT_RIGHT)


# void BitfieldRightToLeft()
@native(name="BitfieldRightToLeft", ret=None, send_interp=True)
def BitfieldRightToLeft(params, ctxt, scope, stream, coord, interp):
    if len(params) > 0:
        raise errors.InvalidArguments(
            coord, "0 arguments", "{} args".format(len(params))
        )
    interp.set_bitfield_direction(interp.BITFIELD_DIR_RIGHT_LEFT)


# double ConvertBytesToDouble( uchar byteArray[] )
@native(name="ConvertBytesToDouble", ret=C.Double)
def ConvertBytesToDouble(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# float ConvertBytesToFloat( uchar byteArray[] )
@native(name="ConvertBytesToFloat", ret=C.Single)
def ConvertBytesToFloat(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# hfloat ConvertBytesToHFloat( uchar byteArray[] )
@native(name="ConvertBytesToHFloat", ret=C.Single)
def ConvertBytesToHFloat(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int ConvertDataToBytes( data_type value, uchar byteArray[] )
@native(name="ConvertDataToBytes", ret=C.Int)
def ConvertDataToBytes(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void DeleteBytes( int64 start, int64 size )
@native(name="DeleteBytes", ret=None)
def DeleteBytes(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int DirectoryExists( string dir )
@native(name="DirectoryExists", ret=C.Int)
def DirectoryExists(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int FEof()
@native(name="FEof", ret=bool)
def FEof(params, ctxt, scope, stream, coord):
    if len(params) > 0:
        raise errors.InvalidArguments(
            coord, "0 arguments", "{} args".format(len(params))
        )

    # now that streams are _ALL_ BitwrappedStreams, we can use BitwrappedStream-specific
    # functions
    return C.stream_iseof(ctxt._io)


# int64 FileSize()
@native(name="FileSize", ret=int)
def FileSize(params, ctxt, scope, stream, coord):
    if len(params) > 0:
        raise errors.InvalidArguments(
            coord, "0 arguments", "{} args".format(len(params))
        )
    return ctxt._io.size()


# TFileList FindFiles( string dir, string filter )
@native(name="FindFiles", ret=None)
def FindFiles(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int FPrintf( int fileNum, char format[], ... )
@native(name="FPrintf", ret=C.Int)
def FPrintf(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int FSeek( int64 pos )
@native(name="FSeek", ret=int)
def FSeek(params, ctxt, scope, stream, coord):
    """Returns 0 if successful or -1 if the address is out of range
    """
    if len(params) != 1:
        raise errors.InvalidArguments(
            coord,
            "{} args".format(len(params)),
            "FSeek accepts only one argument",
        )

    pos = params[0]
    while callable(pos):
        pos = pos(ctxt)
    return C.stream_seek(ctxt._io, pos, 0, "")
    # curr_pos = stream.tell()

    # fsize = stream.size()

    # if pos > fsize:
    #     stream.seek(fsize)
    #     return -1
    # elif pos < 0:
    #     stream.seek(0)
    #     return -1

    # diff = pos - curr_pos
    # if diff < 0:
    #     stream.seek(pos)
    #     return 0

    # data = stream.read(diff)

    # # let the ctxt automatically append numbers, as needed, unless the previous
    # # child was also a skipped field
    # skipped_name = "_skipped"

    # if len(ctxt._pfp__children) > 0 and ctxt._pfp__children[
    #     -1
    # ]._pfp__name.startswith("_skipped"):
    #     old_name = ctxt._pfp__children[-1]._pfp__name
    #     data = ctxt._pfp__children[-1].raw_data + data
    #     skipped_name = old_name
    #     ctxt._pfp__children = ctxt._pfp__children[:-1]
    #     del ctxt._pfp__children_map[old_name]

    # tmp_stream = bitwrap.BitwrappedStream(six.BytesIO(data))
    # new_field = pfp.fields.Array(len(data), C.Byte, tmp_stream)
    # ctxt._pfp__add_child(skipped_name, new_field, stream)
    # scope.add_var(skipped_name, new_field)

    # return 0


# int FSkip( int64 offset )
@native(name="FSkip", ret=int)
def FSkip(params, ctxt, scope, stream, coord):
    """Returns 0 if successful or -1 if the address is out of range
    """
    if len(params) != 1:
        raise errors.InvalidArguments(
            coord,
            "{} args".format(len(params)),
            "FSkip accepts only one argument",
        )

    skip_amt = params[0]
    while callable(skip_amt):
        skip_amt = skip_amt(ctxt)

    return C.stream_seek(ctxt._io, skip_amt, whence=1, path="")
    # pos = skip_amt + stream.tell()
    # return FSeek([pos], ctxt, scope, stream, coord)


# int64 FTell()
@native(name="FTell", ret=int)
def FTell(params, ctxt, scope, stream, coord):
    if len(params) > 0:
        raise errors.InvalidArguments(
            coord, "0 arguments", "{} args".format(len(params))
        )
    # print()
    return C.stream_tell(ctxt._io, None)


# void InsertBytes( int64 start, int64 size, uchar value=0 )
@native(name="InsertBytes", ret=None)
def InsertBytes(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int IsBigEndian()
@native(name="IsBigEndian", ret=bool)
def IsBigEndian(params, ctxt, scope, stream, coord):
    if len(params) > 0:
        raise errors.InvalidArguments(
            coord, "0 arguments", "{} args".format(len(params))
        )
    return pfp.interp.Endian.current == pfp.interp.Endian.BIG


# int IsLittleEndian()
@native(name="IsLittleEndian", ret=bool)
def IsLittleEndian(params, ctxt, scope, stream, coord):
    if len(params) > 0:
        raise errors.InvalidArguments(
            coord, "0 arguments", "{} args".format(len(params))
        )
    return pfp.interp.Endian.current == pfp.interp.Endian.LITTLE


# void LittleEndian()
@native(name="LittleEndian", ret=None)
def LittleEndian(params, ctxt, scope, stream, coord):
    if len(params) > 0:
        raise errors.InvalidArguments(
            coord, "0 arguments", "{} args".format(len(params))
        )
    pfp.interp.Endian.current = pfp.interp.Endian.LITTLE


# int MakeDir( string dir )
@native(name="MakeDir", ret=C.Int)
def MakeDir(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void OverwriteBytes( int64 start, int64 size, uchar value=0 )
@native(name="OverwriteBytes", ret=None)
def OverwriteBytes(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


def _read_data(params, ctxt, cls, coord):
    stream = ctxt._io
    bits = stream._bits
    curr_pos = stream.tell()

    if len(params) == 1:
        pos = evaluate(params[0], ctxt)
        stream.seek(pos, 0)
    elif len(params) > 1:
        raise errors.InvalidArguments(
            coord, "at most 1 arguments", "{} args".format(len(params))
        )

    res = cls.parse_stream(stream)

    # reset the stream
    stream.seek(curr_pos, 0)
    stream._bits = bits

    return res


# char ReadByte( int64 pos=FTell() )
@native(name="ReadByte", ret=C.Byte)
def ReadByte(params, ctxt, scope, stream, coord):
    return _read_data(params, stream, C.Byte, coord)


# double ReadDouble( int64 pos=FTell() )
@native(name="ReadDouble", ret=C.Double)
def ReadDouble(params, ctxt, scope, stream, coord):
    return _read_data(params, stream, C.Double, coord)


# float ReadFloat( int64 pos=FTell() )
@native(name="ReadFloat", ret=C.Single)
def ReadFloat(params, ctxt, scope, stream, coord):
    return _read_data(params, stream, C.Single, coord)


# hfloat ReadHFloat( int64 pos=FTell() )
@native(name="ReadHFloat", ret=C.Single)
def ReadHFloat(params, ctxt, scope, stream, coord):
    return _read_data(params, stream, C.Single, coord)


# int ReadInt( int64 pos=FTell() )
@native(name="ReadInt", ret=int)
def ReadInt(params, ctxt, scope, stream, coord):
    return _read_data(params, ctxt, C.Int, coord)


# int64 ReadInt64( int64 pos=FTell() )
@native(name="ReadInt64", ret=C.Long)
def ReadInt64(params, ctxt, scope, stream, coord):
    return _read_data(params, stream, C.Long, coord)


# int64 ReadQuad( int64 pos=FTell() )
@native(name="ReadQuad", ret=C.Long)
def ReadQuad(params, ctxt, scope, stream, coord):
    return _read_data(params, stream, C.Long, coord)


# short ReadShort( int64 pos=FTell() )
@native(name="ReadShort", ret=C.Short)
def ReadShort(params, ctxt, scope, stream, coord):
    return _read_data(params, stream, pfp.fields.Short, coord)


# uchar ReadUByte( int64 pos=FTell() )
@native(name="ReadUByte", ret=int)
def ReadUByte(params, ctxt, scope, stream, coord):
    return _read_data(params, ctxt, C.Byte, coord)


# uint ReadUInt( int64 pos=FTell() )
@native(name="ReadUInt", ret=int)
def ReadUInt(params, ctxt, scope, stream, coord):
    return C.Peek(C.Int32ul if pfp.interp.Endian.is_LE() else C.Int32ub).parse_stream(ctxt._io)
    # return _read_data(params, stream, pfp.fields.UInt, coord)


# uint64 ReadUInt64( int64 pos=FTell() )
@native(name="ReadUInt64", ret=C.Int64ub)
def ReadUInt64(params, ctxt, scope, stream, coord):
    return _read_data(params, stream, pfp.fields.UInt64, coord)


# uint64 ReadUQuad( int64 pos=FTell() )
@native(name="ReadUQuad", ret=C.Int64ub)
def ReadUQuad(params, ctxt, scope, stream, coord):
    return _read_data(params, stream, pfp.fields.UInt64, coord)


# ushort ReadUShort( int64 pos=FTell() )
@native(name="ReadUShort", ret=int)
def ReadUShort(params, ctxt, scope, stream, coord):
    return _read_data(params, ctxt, C.Short, coord)


# char[] ReadLine( int64 pos, int maxLen=-1, int includeLinefeeds=true )
@native(name="ReadLine", ret=C.CString)
def ReadLine(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void ReadBytes( uchar buffer[], int64 pos, int n )
@native(name="ReadBytes", ret=None)
def ReadBytes(params, ctxt, scope, stream, coord):
    if len(params) != 3:
        raise errors.InvalidArguments(
            coord,
            "3 arguments (buffer, pos, n)",
            "{} args".format(len(params)),
        )
    if not isinstance(params[0], pfp.fields.Array):
        raise errors.InvalidArguments(
            coord, "buffer must be an array", params[0].__class__.__name__
        )
    if params[0].field_cls not in [pfp.fields.UChar, C.Byte]:
        raise errors.InvalidArguments(
            coord,
            "buffer must be an array of uchar or char",
            params[0].field_cls.__name__,
        )

    if not isinstance(params[1], C.IntBase):
        raise errors.InvalidArguments(
            coord, "pos must be an integer", params[1].__class__.__name__
        )

    if not isinstance(params[2], C.IntBase):
        raise errors.InvalidArguments(
            coord, "n must be an integer", params[2].__class__.__name__
        )

    bits = stream._bits
    curr_pos = stream.tell()

    vals = [
        params[0].field_cls(stream) for x in six.moves.range(PYVAL(params[2]))
    ]

    stream.seek(curr_pos, 0)
    stream._bits = bits

    params[0]._pfp__set_value(vals)


# char[] ReadString( int64 pos, int maxLen=-1 )
@native(name="ReadString", ret=C.CString)
def ReadString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int ReadStringLength( int64 pos, int maxLen=-1 )
@native(name="ReadStringLength", ret=C.Int)
def ReadStringLength(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wstring ReadWLine( int64 pos, int maxLen=-1 )
@native(name="ReadWLine", ret=C.CString)
def ReadWLine(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wstring ReadWString( int64 pos, int maxLen=-1 )
@native(name="ReadWString", ret=C.CString)
def ReadWString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int ReadWStringLength( int64 pos, int maxLen=-1 )
@native(name="ReadWStringLength", ret=C.Int)
def ReadWStringLength(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int64 TextAddressToLine( int64 address )
@native(name="TextAddressToLine", ret=C.Long)
def TextAddressToLine(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int TextAddressToColumn( int64 address )
@native(name="TextAddressToColumn", ret=C.Int)
def TextAddressToColumn(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int64 TextColumnToAddress( int64 line, int column )
@native(name="TextColumnToAddress", ret=C.Long)
def TextColumnToAddress(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int64 TextGetNumLines()
@native(name="TextGetNumLines", ret=C.Long)
def TextGetNumLines(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int TextGetLineSize( int64 line, int includeLinefeeds=true )
@native(name="TextGetLineSize", ret=C.Int)
def TextGetLineSize(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int64 TextLineToAddress( int64 line )
@native(name="TextLineToAddress", ret=C.Long)
def TextLineToAddress(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int TextReadLine( char buffer[], int64 line, int maxsize, int includeLinefeeds=true )
@native(name="TextReadLine", ret=C.Int)
def TextReadLine(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int TextReadLineW( wchar_t buffer[], int64 line, int maxsize, int includeLinefeeds=true )
@native(name="TextReadLineW", ret=C.Int)
def TextReadLineW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void TextWriteLine( const char buffer[], int64 line, int includeLinefeeds=true )
@native(name="TextWriteLine", ret=None)
def TextWriteLine(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void TextWriteLineW( const wchar_t buffer[], int64 line, int includeLinefeeds=true )
@native(name="TextWriteLineW", ret=None)
def TextWriteLineW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteByte( int64 pos, char value )
@native(name="WriteByte", ret=None)
def WriteByte(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteDouble( int64 pos, double value )
@native(name="WriteDouble", ret=None)
def WriteDouble(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteFloat( int64 pos, float value )
@native(name="WriteFloat", ret=None)
def WriteFloat(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteHFloat( int64 pos, float value )
@native(name="WriteHFloat", ret=None)
def WriteHFloat(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteInt( int64 pos, int value )
@native(name="WriteInt", ret=None)
def WriteInt(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteInt64( int64 pos, int64 value )
@native(name="WriteInt64", ret=None)
def WriteInt64(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteQuad( int64 pos, int64 value )
@native(name="WriteQuad", ret=None)
def WriteQuad(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteShort( int64 pos, short value )
@native(name="WriteShort", ret=None)
def WriteShort(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteUByte( int64 pos, uchar value )
@native(name="WriteUByte", ret=None)
def WriteUByte(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteUInt( int64 pos, uint value )
@native(name="WriteUInt", ret=None)
def WriteUInt(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteUInt64( int64 pos, uint64 value )
@native(name="WriteUInt64", ret=None)
def WriteUInt64(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteUQuad( int64 pos, uint64 value )
@native(name="WriteUQuad", ret=None)
def WriteUQuad(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteUShort( int64 pos, ushort value )
@native(name="WriteUShort", ret=None)
def WriteUShort(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteBytes( const uchar buffer[], int64 pos, int n )
@native(name="WriteBytes", ret=None)
def WriteBytes(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteString( int64 pos, const char value[] )
@native(name="WriteString", ret=None)
def WriteString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void WriteWString( int64 pos, const wstring value )
@native(name="WriteWString", ret=None)
def WriteWString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()
