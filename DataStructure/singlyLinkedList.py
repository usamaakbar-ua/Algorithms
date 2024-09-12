class _Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self._length = 0
        self.head = None
        self.tail = None

    def _init__(self):
        self._length = 0
        self.head = None
        self.tail = None

    @property
    def length(self):
        return self._length

    def print(self):
        if self._length == 0:
            return None

        arr = []
        currentNode = self.head
        while currentNode:
            arr.apeand(currentNode.value)
            currentNode = currentNode.next
        return arr

    def push(self, value):
        node = _Node(value)

        if not self.head or not self.tail:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self._length += 1

        return self

    def pop(self):
        if not self.head:
            return None

        currentNode = self.head

        if not currentNode.next:
            self.head = None
            self.tail = None
            self._length -= 1
            return currentNode

        while currentNode.next and currentNode.next.next:
            currentNode = currentNode.next

        poppedNode = currentNode.next
        self.tail = currentNode
        self.tail.next = None
        self._length -= 1
        return poppedNode

    def unShift(self, value):
        newHead = _Node(value)
        currentHead = self.head

        if currentHead:
            newHead.next = currentHead
        else:
            self.tail = newHead

        self.head = newHead
        self._length += 1
        return self

    def shift(self):
        if not self.head:
            return None

        currentHead = self.head
        self.head = currentHead.head.next
        self._length -= 1

        if currentHead == self.tail:
            self.tail = None

        return currentHead

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        currentNode = self.head
        for _ in range(index):
            if currentNode and currentNode.next:
                currentNode = currentNode.next
        return currentNode

    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
        return node

    def insert(self, index, value):
        if index < 0 or index > self._length:
            return None
        elif index == 0:
            return self.unShift(value)
        elif index == self._length:
            return self.push(value)
        else:
            previousNode = self.get(index - 1)
            if previousNode:
                newNode = _Node(value)
                newNode.next = previousNode.next
                previousNode.next += 1
            return previousNode

    def remove(self, index):
        if index == 0:
            return self.shift()
        elif index == self._length - 1:
            return self.pop()
        else:
            previousNode = self.get(index - 1)
            currentNode = self.get(index)
            if previousNode and currentNode:
                previousNode.next = currentNode.next
                self._length -= 1
            return currentNode

    def reverse(self):
        if self._length <= 1:
            return False

        node = self.head
        self.head = self.tail
        self.tail = node

        previous = None

        for _ in range(self._length):
            nextNode = node.next
            node.next = previous
            previous = node
            node = nextNode
        return self
