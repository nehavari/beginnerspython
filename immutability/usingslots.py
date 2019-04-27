class Immutable(object):

    __slots__ = ['attribute', 'listAttribute', 'dictAttribute']

    def __init__(self, attribute, listAttribute=[], dictAttribute={}):
        super().__setattr__('attribute', attribute)
        super().__setattr__('listAttribute', listAttribute)
        super().__setattr__('dictAttribute', dictAttribute)

    def __setattr__(self, key, value):
        raise AttributeError("Can't set in an immutable object")

    def __delattr__(self, item):
        raise AttributeError("Can't delete in an immutable object")


immutable = Immutable(10, [1, 2, 3], {1: 'a'})
print('attribute = ', immutable.attribute)
print('listAttribute = ', immutable.listAttribute)
delattr(immutable, 'listAttribute')   # Not possible
immutable.listAttribute = 11   # Not possible
immutable.listAttribute.append(4)   # Possible
immutable.attributNew = 'Newly added '  # Not Possible
object.__setattr__(immutable, 'attribute', 11)  # one way to break the immutability in this solution
immutable.__dict__['attribute'] = 12  # Not Possible

print('updated attribute', immutable.attribute)






