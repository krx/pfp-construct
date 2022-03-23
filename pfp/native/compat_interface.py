#!/usr/bin/env python
# encoding: utf-8

"""
This module of native functions is implemented for
compatability with 010 editor functions. Some of these functions
are nops, some are fully implemented.
"""

import sys

from matplotlib.style import context

from pfp.native import native, predefine
# import pfp.fields
import pfp.errors as errors
import construct as C

# http://www.sweetscape.com/010editor/manual/FuncInterface.htm

# void AddBookmark(
#    int64 pos,
#    string name,
#    string typename,
#    int arraySize=-1,
#    int forecolor=cNone,
#    int backcolor=0xffffc4,
#    int moveWithCursor=false )
@native(name="AddBookmark", ret=C.Pass)
def AddBookmark(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void ClearClipboard()
@native(name="ClearClipboard", ret=C.Pass)
def ClearClipboard(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void CopyBytesToClipboard( uchar buffer[], int size, int charset=CHARSET_ANSI, int bigendian=false )
@native(name="CopyBytesToClipboard", ret=C.Pass)
def CopyBytesToClipboard(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void CopyStringToClipboard( const char str[], int charset=CHARSET_ANSI )
@native(name="CopyStringToClipboard", ret=C.Pass)
def CopyStringToClipboard(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void CopyToClipboard()
@native(name="CopyToClipboard", ret=C.Pass)
def CopyToClipboard(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void CutToClipboard()
@native(name="CutToClipboard", ret=C.Pass)
def CutToClipboard(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int DeleteFile( char filename[] )
@native(name="DeleteFile", ret=C.Int)
def DeleteFile(params, ctxt, scope, stream, coord):
    return 0


# void DisableUndo()
@native(name="DisableUndo", ret=C.Pass)
def DisableUndo(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void DisplayFormatBinary()
@native(name="DisplayFormatBinary", ret=C.Pass)
def DisplayFormatBinary(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void DisplayFormatDecimal()
@native(name="DisplayFormatDecimal", ret=C.Pass)
def DisplayFormatDecimal(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void DisplayFormatHex()
@native(name="DisplayFormatHex", ret=C.Pass)
def DisplayFormatHex(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void DisplayFormatOctal()
@native(name="DisplayFormatOctal", ret=C.Pass)
def DisplayFormatOctal(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void EnableUndo()
@native(name="EnableUndo", ret=C.Pass)
def EnableUndo(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int Exec( const char program[], const char arguments[], int wait, int &errorCode )
@native(name="Exec", ret=C.Int)
def Exec(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void Exit( int errorcode )
@native(name="Exit", ret=C.Pass)
def Exit(params, ctxt, scope, stream, coord):
    if len(params) != 1:
        raise errors.InvalidArguments(
            coord, "1 arguments", "{} args".format(len(params))
        )
    error_code = PYVAL(params[0])
    raise errors.InterpExit(error_code)


# void ExpandAll()
@native(name="ExpandAll", ret=C.Pass)
def ExpandAll(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void ExportCSV( const char filename[] )
@native(name="ExportCSV", ret=C.Pass)
def ExportCSV(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void ExportXML( const char filename[] )
@native(name="ExportXML", ret=C.Pass)
def ExportXML(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void FileClose()
@native(name="FileClose", ret=C.Pass)
def FileClose(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int FileCount()
@native(name="FileCount", ret=C.Int)
def FileCount(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int FileExists( const char filename[] )
@native(name="FileExists", ret=C.Int)
def FileExists(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int FileNew( char interface[]="", int makeActive=true )
@native(name="FileNew", ret=C.Int)
def FileNew(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int FileOpen( const char filename[], int runTemplate=false, char interface[]="", int openDuplicate=false )
@native(name="FileOpen", ret=C.Int)
def FileOpen(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int FileSave()
# int FileSave( const char filename[] )
# int FileSave( const wchar_t filename[] )
@native(name="FileSave", ret=C.Int)
def FileSave(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int FileSaveRange( const char filename[], int64 start, int64 size )
# int FileSaveRange( const wchar_t filename[], int64 start, int64 size )
@native(name="FileSaveRange", ret=C.Int)
def FileSaveRange(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void FileSelect( int index )
@native(name="FileSelect", ret=C.Pass)
def FileSelect(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int FindOpenFile( const char path[] )
@native(name="FindOpenFile", ret=C.Int)
def FindOpenFile(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int FindOpenFileW( const wchar_t path[] )
@native(name="FindOpenFileW", ret=C.Int)
def FindOpenFileW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] GetArg( int index )
@native(name="GetArg", ret=C.CString)
def GetArg(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wchar_t[] GetArgW( int index )
@native(name="GetArgW", ret=C.CString)
def GetArgW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int GetBackColor()
@native(name="GetBackColor", ret=C.Int)
def GetBackColor(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int GetBookmarkArraySize( int index )
@native(name="GetBookmarkArraySize", ret=C.Int)
def GetBookmarkArraySize(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int GetBookmarkBackColor( int index )
@native(name="GetBookmarkBackColor", ret=C.Int)
def GetBookmarkBackColor(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int GetBookmarkForeColor( int index )
@native(name="GetBookmarkForeColor", ret=C.Int)
def GetBookmarkForeColor(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int GetBookmarkMoveWithCursor( int index )
@native(name="GetBookmarkMoveWithCursor", ret=C.Int)
def GetBookmarkMoveWithCursor(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# string GetBookmarkName( int index )
@native(name="GetBookmarkName", ret=C.CString)
def GetBookmarkName(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int64 GetBookmarkPos( int index )
@native(name="GetBookmarkPos", ret=C.Long)
def GetBookmarkPos(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# string GetBookmarkType( int index )
@native(name="GetBookmarkType", ret=C.CString)
def GetBookmarkType(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int GetBytesPerLine()
@native(name="GetBytesPerLine", ret=C.Int)
def GetBytesPerLine(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int GetClipboardBytes( uchar buffer[], int maxBytes )
@native(name="GetClipboardBytes", ret=C.Int)
def GetClipboardBytes(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int GetClipboardIndex()
@native(name="GetClipboardIndex", ret=C.Int)
def GetClipboardIndex(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# string GetClipboardString()
@native(name="GetClipboardString", ret=C.CString)
def GetClipboardString(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# string GetCurrentTime( char format[] = "hh:mm:ss" )
@native(name="GetCurrentTime", ret=C.CString)
def GetCurrentTime(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# string GetCurrentDate( char format[] = "MM/dd/yyyy" )
@native(name="GetCurrentDate", ret=C.CString)
def GetCurrentDate(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# string GetCurrentDateTime( char format[] = "MM/dd/yyyy hh:mm:ss" )
@native(name="GetCurrentDateTime", ret=C.CString)
def GetCurrentDateTime(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int64 GetCursorPos()
@native(name="GetCursorPos", ret=C.Long)
def GetCursorPos(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] GetEnv( const char str[] )
@native(name="GetEnv", ret=C.CString)
def GetEnv(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int GetFileAttributesUnix()
@native(name="GetFileAttributesUnix", ret=C.Int)
def GetFileAttributesUnix(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int GetFileAttributesWin()
@native(name="GetFileAttributesWin", ret=C.Int)
def GetFileAttributesWin(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int GetFileCharSet()
@native(name="GetFileCharSet", ret=C.Int)
def GetFileCharSet(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] GetFileInterface()
@native(name="GetFileInterface", ret=C.CString)
def GetFileInterface(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] GetFileName()
@native(name="GetFileName", ret=C.CString, send_interp=True)
def GetFileName(params, ctxt, scope, stream, coord, interp):
    return interp.get_filename()


# wchar_t[] GetFileNameW()
@native(name="GetFileNameW", ret=C.CString)
def GetFileNameW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int GetFileNum()
@native(name="GetFileNum", ret=C.Int)
def GetFileNum(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int GetForeColor()
@native(name="GetForeColor", ret=C.Int)
def GetForeColor(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int GetMouseWheelScrollSpeed()
@native(name="GetMouseWheelScrollSpeed", ret=C.Int)
def GetMouseWheelScrollSpeed(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int GetNumArgs()
@native(name="GetNumArgs", ret=C.Int)
def GetNumArgs(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int GetNumBookmarks()
@native(name="GetNumBookmarks", ret=C.Int)
def GetNumBookmarks(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int GetReadOnly()
@native(name="GetReadOnly", ret=C.Int)
def GetReadOnly(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] GetScriptName()
@native(name="GetScriptName", ret=C.CString)
def GetScriptName(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wchar_t[] GetScriptNameW()
@native(name="GetScriptNameW", ret=C.CString)
def GetScriptNameW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] GetScriptFileName()
@native(name="GetScriptFileName", ret=C.CString)
def GetScriptFileName(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wchar_t[] GetScriptFileNameW()
@native(name="GetScriptFileNameW", ret=C.CString)
def GetScriptFileNameW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int64 GetSelSize()
@native(name="GetSelSize", ret=C.Long)
def GetSelSize(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int64 GetSelStart()
@native(name="GetSelStart", ret=C.Long)
def GetSelStart(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# string GetTempDirectory()
@native(name="GetTempDirectory", ret=C.CString)
def GetTempDirectory(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] GetTempFileName()
@native(name="GetTempFileName", ret=C.CString)
def GetTempFileName(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] GetTemplateName()
@native(name="GetTemplateName", ret=C.CString)
def GetTemplateName(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wchar_t[] GetTemplateNameW()
@native(name="GetTemplateNameW", ret=C.CString)
def GetTemplateNameW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] GetTemplateFileName()
@native(name="GetTemplateFileName", ret=C.CString)
def GetTemplateFileName(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wchar_t[] GetTemplateFileNameW()
@native(name="GetTemplateFileNameW", ret=C.CString)
def GetTemplateFileNameW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] GetWorkingDirectory()
@native(name="GetWorkingDirectory", ret=C.CString)
def GetWorkingDirectory(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wchar_t[] GetWorkingDirectoryW()
@native(name="GetWorkingDirectoryW", ret=C.CString)
def GetWorkingDirectoryW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] InputDirectory( const char title[], const char defaultDir[]="" , coord)
@native(name="InputDirectory", ret=C.CString)
def InputDirectory(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# double InputFloat(const char title[], const char caption[], const char defaultValue[] , coord)
@native(name="InputFloat", ret=C.Double)
def InputFloat(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int InputNumber(const char title[], const char caption[], const char defaultValue[] , coord)
@native(name="InputNumber", ret=C.Int)
def InputNumber(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] InputOpenFileName(
#    char title[],
#    char filter[]="All files (*.*)",
#    char filename[]="" )
@native(name="InputOpenFileName", ret=C.CString)
def InputOpenFileName(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# TOpenFileNames InputOpenFileNames(
#    char title[],
#    char filter[]="All files (*.*)",
#    char filename[]="" )
@native(name="InputOpenFileNames", ret=C.Pass)
def InputOpenFileNames(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int InputRadioButtonBox(
#    const char title[],
#    const char caption[],
#    int defaultIndex,
#    const char str1[], const char str2[], const char str3[]="",
#    const char str4[]="", const char str5[]="", const char str6[]="",
#    const char str7[]="", const char str8[]="", const char str9[]="",
#    const char str10[]="", const char str11[]="", const char str12[]="",
#    const char str13[]="", const char str14[]="", const char str15[]="" )
@native(name="InputRadioButtonBox", ret=C.Int)
def InputRadioButtonBox(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] InputSaveFileName(
#    char title[],
#    char filter[]="All files (*.*)",
#    char filename[]="",
#    char extension[]="" )
@native(name="InputSaveFileName", ret=C.CString)
def InputSaveFileName(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# char[] InputString(
#    const char title[],
#    const char caption[],
#    const char defaultValue[] , coord)
@native(name="InputString", ret=C.CString)
def InputString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wstring InputWString(
#    const char title[],
#    const char caption[],
#    const wstring defaultValue , coord)
@native(name="InputWString", ret=C.CString)
def InputWString(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int InsertFile( const char filename[], int64 position )
@native(name="InsertFile", ret=C.Int)
def InsertFile(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int IsEditorFocused()
@native(name="IsEditorFocused", ret=C.Int)
def IsEditorFocused(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int IsModified()
@native(name="IsModified", ret=C.Int)
def IsModified(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int IsNoUIMode()
@native(name="IsNoUIMode", ret=C.Int)
def IsNoUIMode(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int MessageBox( int mask, const char title[], const char format[] [, argument, ... ] )
@native(name="MessageBox", ret=C.Int)
def MessageBox(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void OutputPaneClear()
@native(name="OutputPaneClear", ret=C.Pass)
def OutputPaneClear(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int OutputPaneSave( const char filename[] )
@native(name="OutputPaneSave", ret=C.Int)
def OutputPaneSave(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void OutputPaneCopy()
@native(name="OutputPaneCopy", ret=C.Pass)
def OutputPaneCopy(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void PasteFromClipboard()
@native(name="PasteFromClipboard", ret=C.Pass)
def PasteFromClipboard(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int Printf( const char format[] [, argument, ... ] )
@native(name="Printf", ret=int, send_interp=True)
def Printf(params, ctxt, scope, stream, coord, interp):
    """Prints format string to stdout

    :params: TODO
    :returns: TODO

    """
    if len(params) == 1:
        if interp._printf:
            sys.stdout.write(params[0])
        return len(params[0])

    parts = []
    for part in params[1:]:
        # This value may be nested down a bunch of lambda statements,
        # so keep calling it until we get a value
        while callable(part):
            part = part(ctxt)
        parts.append(part)

    to_print = str(params[0]) % tuple(parts)
    res = len(to_print)

    if interp._printf:
        sys.stdout.write(to_print)
        sys.stdout.flush()
    return res


# int64 ProcessGetHeapLocalAddress( int index )
@native(name="ProcessGetHeapLocalAddress", ret=C.Long)
def ProcessGetHeapLocalAddress(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# wchar_t[] ProcessGetHeapModule( int index )
@native(name="ProcessGetHeapModule", ret=C.CString)
def ProcessGetHeapModule(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int ProcessGetHeapSize( int index )
@native(name="ProcessGetHeapSize", ret=C.Int)
def ProcessGetHeapSize(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int64 ProcessGetHeapStartAddress( int index )
@native(name="ProcessGetHeapStartAddress", ret=C.Long)
def ProcessGetHeapStartAddress(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int ProcessGetNumHeaps()
@native(name="ProcessGetNumHeaps", ret=C.Int)
def ProcessGetNumHeaps(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int64 ProcessHeapToLocalAddress( int64 memoryAddress )
@native(name="ProcessHeapToLocalAddress", ret=C.Long)
def ProcessHeapToLocalAddress(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int64 ProcessLocalToHeapAddress( int64 localAddress )
@native(name="ProcessLocalToHeapAddress", ret=C.Long)
def ProcessLocalToHeapAddress(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void RemoveBookmark( int index )
@native(name="RemoveBookmark", ret=C.Pass)
def RemoveBookmark(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int RenameFile( const char originalname[], const char newname[] )
@native(name="RenameFile", ret=C.Int)
def RenameFile(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void RequiresFile()
@native(name="RequiresFile", ret=C.Pass)
def RequiresFile(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void RequiresVersion( int majorVer, int minorVer=0, int revision=0 )
@native(name="RequiresVersion", ret=C.Pass)
def RequiresVersion(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void RunTemplate( const char filename[]="", int clearOutput=false )
@native(name="RunTemplate", ret=C.Pass)
def RunTemplate(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


predefine(
    """
const int cBlack = 0x000000;
const int cRed = 0x0000ff;
const int cDkRed = 0x000080;
const int cLtRed = 0x8080ff;
const int cGreen = 0x00ff00;
const int cDkGreen = 0x008000;
const int cLtGreen = 0x80ff80;
const int cBlue = 0xff0000;
const int cDkBlue = 0x800000;
const int cLtBlue = 0xff8080;
const int cPurple = 0xff00ff;
const int cDkPurple = 0x800080;
const int cLtPurple = 0xffe0ff;
const int cAqua = 0xffff00;
const int cDkAqua = 0x808000;
const int cLtAqua = 0xffffe0;
const int cYellow = 0x00ffff;
const int cDkYellow = 0x008080;
const int cLtYellow = 0x80ffff;
const int cDkGray = 0x404040;
const int cGray = 0x808080;
const int cSilver = 0xc0c0c0;
const int cLtGray = 0xe0e0e0;
const int cWhite = 0xffffff;
const int cNone = 0xffffffff;
"""
)


# void SetBackColor( int color )
@native(name="SetBackColor", ret=C.Pass)
def SetBackColor(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void SetColor( int forecolor, int backcolor )
@native(name="SetColor", ret=C.Pass)
def SetColor(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void SetForeColor( int color )
@native(name="SetForeColor", ret=C.Pass)
def SetForeColor(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# int SetClipboardIndex( int index )
@native(name="SetClipboardIndex", ret=C.Int)
def SetClipboardIndex(params, ctxt, scope, stream, coord):
    # resolved: won't implement
    pass


# void SetCursorPos( int64 pos )
@native(name="SetCursorPos", ret=C.Pass)
def SetCursorPos(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int SetEnv( const char str[], const char value[] )
@native(name="SetEnv", ret=C.Int)
def SetEnv(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int SetFileAttributesUnix( int attributes )
@native(name="SetFileAttributesUnix", ret=C.Int)
def SetFileAttributesUnix(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int SetFileAttributesWin( int attributes )
@native(name="SetFileAttributesWin", ret=C.Int)
def SetFileAttributesWin(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int SetFileInterface( const char name[] )
@native(name="SetFileInterface", ret=C.Int)
def SetFileInterface(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void SetMouseWheelScrollSpeed( int speed )
@native(name="SetMouseWheelScrollSpeed", ret=C.Pass)
def SetMouseWheelScrollSpeed(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int SetReadOnly( int readonly )
@native(name="SetReadOnly", ret=C.Int)
def SetReadOnly(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void SetSelection( int64 start, int64 size )
@native(name="SetSelection", ret=C.Pass)
def SetSelection(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int SetWorkingDirectory( const char dir[] )
@native(name="SetWorkingDirectory", ret=C.Int)
def SetWorkingDirectory(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int SetWorkingDirectoryW( const wchar_t dir[] )
@native(name="SetWorkingDirectoryW", ret=C.Int)
def SetWorkingDirectoryW(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void Sleep( int milliseconds )
@native(name="Sleep", ret=C.Pass)
def Sleep(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# void StatusMessage( const char format[] [, argument, ... ] )
@native(name="StatusMessage", ret=C.Pass)
def StatusMessage(params, ctxt, scope, stream, coord):
    pass


# void Terminate( int force=true )
@native(name="Terminate", ret=C.Pass)
def Terminate(params, ctxt, scope, stream, coord):
    raise errors.InterpExit()


# void Warning( const char format[] [, argument, ... ] )
@native(name="Warning", ret=C.Pass)
def Warning(params, ctxt, scope, stream, coord):
    pass


# void Assert( int value, const char msg[] = "" )
@native(name="Assert", ret=None)
def Assert(params, ctxt, scope, stream, coord):
    pass
