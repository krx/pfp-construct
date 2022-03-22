#!/usr/bin/env python
# encoding: utf-8

"""
This module of native functions is implemented for
compatability with 010 editor functions. Some of these functions
are nops, some are fully implemented.
"""

import sys

from pfp.native import native
# import pfp.fields
import construct as C

# http://www.sweetscape.com/010editor/manual/FuncMath.htm

# double Abs( double x )
@native(name="Abs", ret=C.Double)
def Abs(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# double Ceil( double x )
@native(name="Ceil", ret=C.Double)
def Ceil(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# double Cos( double a )
@native(name="Cos", ret=C.Double)
def Cos(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# double Exp( double x )
@native(name="Exp", ret=C.Double)
def Exp(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# double Floor( double x)
@native(name="Floor", ret=C.Double)
def Floor(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# double Log( double x )
@native(name="Log", ret=C.Double)
def Log(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# double Max( double a, double b )
@native(name="Max", ret=C.Double)
def Max(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# double Min( double a, double b)
@native(name="Min", ret=C.Double)
def Min(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# double Pow( double x, double y)
@native(name="Pow", ret=C.Double)
def Pow(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# int Random( int maximum )
@native(name="Random", ret=C.Int)
def Random(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# double Sin( double a )
@native(name="Sin", ret=C.Double)
def Sin(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# double Sqrt( double x )
@native(name="Sqrt", ret=C.Double)
def Sqrt(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# data_type SwapBytes( data_type x )
@native(name="SwapBytes", ret=C.Int)
def SwapBytes(params, ctxt, scope, stream, coord):
    raise NotImplementedError()


# double Tan( double a )
@native(name="Tan", ret=C.Double)
def Tan(params, ctxt, scope, stream, coord):
    raise NotImplementedError()
