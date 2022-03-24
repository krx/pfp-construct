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
        while hasattr(context, '_') and context._ is not None:
            try:
                return _eval(param, context)
            except KeyError:
                context = context._
    return _eval(param, context)

def get_field_name(path):
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
