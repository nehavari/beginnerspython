'''
Enforce function argument and return types.
Note that this copies the func_name attribute from the old to the new function.
__name__ was made writable in Python 2.4a3
'''

import functools


def accepts(*types):
    print("* Inside accepts *")

    def _decorator(f):
        print("** Inside check_accepts **")
        # assert len(types) == f.__code__.co_argcount

        @functools.wraps(f)  # automatic name
        def _wrapper(*args, **kwds):  # This is the wrapper on decorated function "func"
            print("*** Inside accepts _wrapper ***")
            for (a, t) in zip(args, types):
                assert isinstance(a, t), "arg %r does not match %s" % (a, t)
            return f(*args, **kwds)
        return _wrapper
    return _decorator


def returns(rtype):
    print("* Inside Returns *")

    def _decorator(f):
        print("** Inside check_returns **")

        def _wrapper(*args, **kwds):  # This is the wrapper on decorated function "func"
            print("*** Inside returns _wrapper ***")
            result = f(*args, **kwds)  # This will Not Execute the function, function will be execute when user will
            # call decorated function func() from main() method
            assert isinstance(result, rtype), "return value %r does not match %s" % (result, rtype)
            return result
        _wrapper.__name__ = f.__name__
        return _wrapper
    return _decorator


@accepts(int, (int, float))
@returns((int, float))
def func(arg1, arg2):
    print("Inside Decorated func")
    return arg1 * arg2


def main():
    print(func(30, 10.2))


if __name__ == '__main__':
    main()

