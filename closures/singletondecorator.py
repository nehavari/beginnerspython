"""
Amazing decorator use for defining a singleton class in python
"""


def singleton(cls):
    instances = {}
    print("I am inside singleton")  # executes only once, during parse time

    def getInstance():
        print(" **I am inside get Instance **")  # execute everytime MyClass is instantiated.
        if cls not in instances:
            print("**** cls not in instances")
            instances[cls] = cls()
        return instances[cls]

    return getInstance


@singleton
class MyClass:

    def m1(self):
        print("I am in in m1")


def main():
    print("I am inside main")
    c = MyClass()
    c1 = MyClass()
    c3 = MyClass  # this doest not execute the closure
    print(id(c), id(c1))

main()