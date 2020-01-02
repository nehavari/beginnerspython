'''
Enforce function argument and return types.
Note that this copies the func_name attribute from the old to the new function.
__name__ was made writable in Python 2.4a3
'''


def accepts(*types):
    print("* Inside accepts *")

    def check_accepts(f):
        print("** Inside check_accepts **")
        # assert len(types) == f.__code__.co_argcount

        def new_f(*args, **kwds):  # This is the wrapper on decorated function "func"
            print("*** Inside accepts new_f ***")
            for (a, t) in zip(args, types):
                assert isinstance(a, t), "arg %r does not match %s" % (a, t)
            return f(*args, **kwds)
        new_f.__name__ = f.__name__
        return new_f
    return check_accepts


def returns(rtype):
    print("* Inside Returns *")

    def check_returns(f):
        print("** Inside check_returns **")

        def new_f(*args, **kwds):  # This is the wrapper on decorated function "func"
            print("*** Inside returns new_f ***")
            result = f(*args, **kwds)  # This will Not Execute the function, function will be execute when user will
            # call decorated function func() from main() method
            assert isinstance(result, rtype), "return value %r does not match %s" % (result, rtype)
            return result
        new_f.__name__ = f.__name__
        return new_f
    return check_returns


@accepts(int, (int, float))
@returns((int, float))
def func(arg1, arg2):
    print("Inside Decorated func")
    return arg1 * arg2


def main():
    print(func(30, 10.2))


if __name__ == '__main__':
    main()

