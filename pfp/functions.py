import six

import pfp.bitwrap as bitwrap
import pfp.errors as errors
import pfp.utils as utils
# import pfp.fields


class BaseFunction(object):
    pass


class Function(BaseFunction):
    """A class to maintain function state and arguments"""

    def __init__(self, return_type, params, scope):
        """
        Initialized the function. The Function body is intended to be set
        after the Function object has been created.
        """
        super(Function, self).__init__()

        self.name = None
        self.body = None

        # note that the _scope is determined by where the function is
        # declared, not where it is called from
        # TODO see the comment in Scope.clone for potential future work/bugs
        self._scope = scope.clone()
        self._params = params

    def call(self, args, ctxt, scope, stream, interp, coord, no_cast=False):
        # the no_cast arg does nothing for interpreted functions
        if self.body is None:
            raise errors.InvalidState(coord)

        # scopes will be pushed and popped by the Compound node handler!
        # If a return statement is interpreted in the function,
        # the Compound statement will pop the scope before the exception
        # bubbles up to here

        self._scope.push()

        params = self._params.instantiate(self._scope, args, ctxt)
        ret_val = self.body._parsereport(ctxt._io, ctxt, "")

        # ret_val = None
        # try:
        #     interp._handle_node(self.body, self._scope, ctxt, stream)
        # except errors.InterpReturn as e:
        #     # TODO do some type checking on the return value??
        #     # perhaps this should be done when initially traversing
        #     # the AST of the function... a dry run traversing it to find
        #     # return values??
        #     ret_val = e.value
        # finally:
        #     self._scope.pop()

        return ret_val


class NativeFunction(BaseFunction):
    """A class for native functions"""

    def __init__(self, name, func, ret, send_interp=False):
        """
        """
        super(NativeFunction, self).__init__()
        self._pfp__name = name
        self.name = name
        self.func = func
        self.ret = ret
        self.send_interp = send_interp

    def call(self, args, ctxt, scope, stream, interp, coord, no_cast=False):
        # args = [utils.evaluate(arg, ctxt) for arg in args]
        if self.send_interp:
            res = self.func(args, ctxt, scope, stream, coord, interp)
        else:
            res = self.func(args, ctxt, scope, stream, coord)

        if no_cast:
            res_field = res
        elif utils.is_str(res) and self.ret == list:
            tmp_stream = bitwrap.BitwrappedStream(six.BytesIO(res))
            res_field = pfp.fields.Array(len(res), pfp.fields.Char, tmp_stream)
        elif utils.is_str(self.ret) and scope.get_type(self.ret) is not None:
            # TODO should we do any type-checking here to make sure that the
            # return value matches what is declared as the return type?
            res_field = res
        elif self.ret is None:
            res_field = res
        else:
            # res_field = self.ret.parse(res)
            # res_field._pfp__set_value(res)
            res_field = self.ret(res)

        return res_field


class ParamClsWrapper(object):
    """This is a temporary wrapper around a param class
    that can store temporary information, such as byref values
    """

    def __init__(self, param_cls):
        self._cls = param_cls

    def __call__(self, *args, **kwargs):
        """This should be fairly transparent in use and should
        behave as if a new object of `self._cls` was directly
        instantiated
        """
        return self._cls(*args, **kwargs)


class ParamListDef(object):
    """docstring for ParamList"""

    def __init__(self, params, coords):
        super(ParamListDef, self).__init__()

        self._params = params
        self._coords = coords

    def instantiate(self, scope, args, ctxt):
        """Create a ParamList instance for actual interpretation

        :args: TODO
        :returns: A ParamList object

        """
        if len(args) != len(self._params):
            raise errors.InvalidArguments(
                self._coords,
                [x.__class__.__name__ for x in args],
                [x for x in self._params],
            )
        param_instances = []

        BYREF = "byref"

        # TODO are default values for function parameters allowed in 010?
        for (param_name, param_cls), arg in zip(self._params, args):
            arg = utils.evaluate(arg, ctxt)

            # we don't instantiate a copy of byref params
            if getattr(param_cls, BYREF, False):
                param_instances.append(arg)
                ctxt[param_name] = arg
            else:
                # field = param_cls()
                # field._pfp__name = param_name
                # param_instances.append(arg.clone())
                ctxt[param_name] = arg


        # TODO type checking on provided types

        # for x in six.moves.range(len(args)):
        #     param = param_instances[x]

        #     # arrays are simply passed through into the function. We shouldn't
        #     # have to worry about frozenness/unfrozenness at this point
        #     if param is BYREF or isinstance(param, pfp.fields.Array):
        #         param = args[x]
        #         param_instances[x] = param
        #         scope.add_local(self._params[x][0], param)
        #     else:
        #         param._pfp__set_value(args[x])
        #         scope.add_local(param._pfp__name, param)
        #     param._pfp__interp = interp

        # return ParamList(param_instances)


class ParamList(object):
    """Used for when a function is actually called. See ParamListDef
    for how function definitions store function parameter definitions
    """

    def __init__(self, params):
        super(ParamList, self).__init__()
        self.params = params

        # for use by __getitem__
        self._params_map = {}
        for param in self.params:
            self._params_map[param._pfp__name] = param

    def __iter__(self):
        """Return an iterator that will iterate through each of the
        parameters in order

        """
        for param in self.params:
            yield param

    def __getitem__(self, name):
        if name in self._params_map:
            return self._params_map[name]
        raise KeyError(name)

    # def __setitem__???
