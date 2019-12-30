# decorator example 1

# Define a function to be executed at exit. Note that the function isn't actually "wrapped" in the usual sense.



def onexit(f):
    print('I am inside decorator')
    import atexit
    atexit.register(f)
    return f

@onexit
def func():
    print('This function will be executed at exit of program')

