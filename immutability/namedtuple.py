from collections import namedtuple

Immutable = namedtuple('Immutable', ['attribute1', 'attribute2'])

object1 = Immutable(10, [1, 2])

print(object1.attribute1)
print(object1.attribute2)
object1.attribute2.append(3)    # Possible
object1.attribute2 = ['n', 'e', 'h', 'a']     # Not Possible





