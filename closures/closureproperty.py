'''
Demo on __closure__ property of function.
'''

def foo(x):
    """docstring for foo"""

    def bar(y):
        q = 777

        def baz(z):
            print(locals())  # {'y': 20, 'x': 10, 'z': 30, 'q': 10}
            print(vars())  # {'y': 20, 'x': 10, 'z': 30, 'q': 10}
            return x + y + q + z
        return baz
    return bar


print(foo(100)(20)(30))  # 927

# Lexical environment (closure) cells of "foo":
print(foo.__closure__)  # None

# "bar" is returned
bar = foo(100)

# Closure cells of "bar":
# (
#     <cell at 0x0000013138B7DDC8: int object at 0x00007FFEA8ACD540>, "x": 10
# )
print('bar\'s closure', bar.__closure__)

# "baz" is returned
baz = bar(20)

#
# Closure cells of "bar":
# (
#     <cell at 0x0000019FE05FEF18: int object at 0x00007FFEA3DCD540>, "q": 777
#     <cell at 0x0000019FE05FEDC8: int object at 0x00007FFEA3DCD540>, "x": 100
#     <cell at 0x0000019FE05FED98: int object at 0x00007FFEA3DCD680>, "y": 20
# )
#
print(baz.__closure__)

# So, we see that a "__closure__" property is a tuple
# (immutable list/array) of closure *cells*; we may refer them
# and their contents explicitly -- a cell has property "cell_contents"

print(baz.__closure__[0])  # <cell at 0x0000019FE05FEF18: int object at 0x00007FFEA3DCD540>
print('index 0', baz.__closure__[0].cell_contents)  # 777 -- this is our closured "q"

# the same for "x" and "y"
print('index 1', baz.__closure__[1].cell_contents)  # "x": 10
print('index 2', baz.__closure__[2].cell_contents)  # "y": 20

# Then, when "baz" is activated it's own environment
# frame is created (which contains local variable "z")
# and merged with property __closure__. The result dictionary
# we may refer it via "locals()" or "vars()" funtions.
# Being able to refer all saved (closured) free variables,
# we get correct result -- 927:
print(baz(30))  # 927