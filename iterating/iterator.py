from collections.abc import Iterable, Iterator


class Node(object):

    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def __next__(self):
        if self._next:
            return self._next

        raise StopIteration()

    def append(self, node):
        self._next = node
        return node

    def __str__(self):
        return str(self._value)

    def __iter__(self):
        return self


list1 = Node(1)
list1.append(Node(2)).append(Node(3))

for l in list1:
    print(l)

print(list1)
print(next(list1))
print(next(next(list1)))
print(next(next(next(list1))))
