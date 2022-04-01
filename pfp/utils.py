#!/usr/bin/env python
# encoding: utf-8

import contextlib
import six
import sys
import time
import construct as C

@contextlib.contextmanager
def timeit(msg, num=None):
    start = time.time()
    yield
    end = time.time()
    if num is None:
        print("{} took {:.04f}s".format(msg, end - start))
    else:
        print("{} with {:.04f}/s".format(msg, (num / (end - start))))


def is_str(s):
    for type_ in six.string_types:
        if isinstance(s, type_):
            return True
    if isinstance(s, bytes):
        return True
    return False

def _eval(param, context):
    while callable(param):
        param = param(context)
    return param

def evaluate(param, context, recurse=True):
    if recurse:
        if isinstance(param, C.BinExpr):
            # The lhs and rhs might be in different contexts,
            # so manually resolve them both
            lhs = evaluate(param.lhs, context)
            rhs = evaluate(param.rhs, context)
            param = param.op(lhs, rhs)

        # Keep walking up contexts until we resolve the param
        while hasattr(context, '_') and context._ is not None:
            try:
                return _eval(param, context)
            except KeyError:
                context = context._
    return _eval(param, context)

def set_field(path, ctxt, src):
    if isinstance(path, C.Path):
        path = get_field_names(path)
    dst = ctxt
    for name in path[:-1]:
        dst = dst[name]
    dst[path[-1]] = src


def get_field_names(path: C.Path):
    parent = path._Path__parent
    names = []

    while parent is not None:
        names.append(path._Path__field)
        path = parent
        parent = path._Path__parent

    return names[::-1]

def get_field_name(path: C.Path):
    return path._Path__field

# Useful for very coarse version differentiation.
PY3 = sys.version_info[0] == 3

if PY3:
    from queue import Queue

    def string_escape(s):
        return bytes(string(s), "utf-8").decode("unicode_escape")

    def binary(s):
        if type(s) is bytes:
            return s
        return s.encode("ISO-8859-1")

    def string(s):
        if type(s) is bytes:
            return s.decode("ISO-8859-1")
        return s


else:
    from Queue import Queue

    def string_escape(s):
        return string(s).decode("string_escape")

    def binary(s):
        return s

    def string(s):
        return s
