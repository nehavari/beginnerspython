
'''
Add attributes to a function.
'''

def attrs(**kwds):
    def decorate(f):
        print("Inside decorate , its argument is ", f)
        for k in kwds:
            setattr(f, k, kwds[k])
        return f
    return decorate


@attrs(versionadded="2.2", author="Guido van Rossum")
def mymethod(f):
    print(f)


def main():
    mymethod("Neha")
    print(mymethod.author)  # prints Guido van Rossum


if __name__ == '__main__':
    main()
