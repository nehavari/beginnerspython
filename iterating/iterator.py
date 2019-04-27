class NodeIterator(object):

    def __init__(self, node):
        self._node = node

    def __iter__(self):
        return self

    def __next__(self):
        if not self._node:
            raise StopIteration()
        currentNode = self._node
        self._node = self._node.getNextNode()
        return currentNode

class Node(object):

    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def getValue(self):
        return self._value

    def getNextNode(self):
        return self._next

    def setNextNode(self, node):
        self._next = node

    def __iter__(self):
        return NodeIterator(self)

    def __str__(self):
        return str(self._value)


class SinglyLinkedList(object):

    def __init__(self, node):
        self.head = node

    def append(self, node):
        lastNode = None

        for h in self.head:
            lastNode = h
        lastNode.setNextNode(node)

    def __str__(self):
        return str(self.head.getValue())

    def __iter__(self):
        return NodeIterator(self.head)


def main():
    list1 = SinglyLinkedList(Node(1))
    list1.append(Node(2))
    list1.append(Node(3))
    for l in list1:
        print(l)

if __name__ == '__main__':
    main()