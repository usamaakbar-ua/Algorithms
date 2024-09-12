class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    @property
    def length(self):
        return self._length

    @property
    def printList(self):
        if self._length == 0:
            return None

        result = []
        currentNode = self.head
        while currentNode:
            result.append(currentNode.value)
            currentNode = currentNode.next
        return result

    def push(self, value):
        node = Node(value)

        if not self.tail:
            self.head = node
        else:
            self.tail.next = node
            node.previous = self.tail
        self.tail = node
        self._length += 1
        return self

    def pop(self):
        if not self.tail:
            return None

        currentTail = self.tail
        if currentTail.previous:
            self.tail = currentTail.previous
            self.tail.next = None
            currentTail.previous = None
        else:
            self.head = None
            self.tail = None

        self._length -= 1
        return currentTail

    def shift(self):
        if not self.head:
            return None

        currentHead = self.head
        if currentHead.next:
            self.head = currentHead.next
            self.head.previous = None
            currentHead.next = None
        else:
            return self.pop()

        self._length -= 1
        return currentHead

    def unShift(self, value):
        if not self.head:
            return self.push(value)

        node = Node(value)
        currentHead = self.head

        self.head = node
        self.head.next = currentHead
        currentHead.previous = self.head

        self._length += 1
        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if index < self._length // 2:
            currentNode = self.head
            for i in range(index):
                currentNode = currentNode.previous
        else:
            currentNode = self.tail
            for i in range(self._length - 1, index, -1):
                currentNode = currentNode.previous

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
            nextNode = self.get(index)

            if previousNode and nextNode:
                newNode = Node(value)
                previousNode.next = newNode
                newNode.previous = previousNode
                newNode.next = nextNode
                nextNode.prev = newNode

            self._length += 1
        return self

    def remove(self, index):
        if index < 0 or index >= self._length:
            return None
        elif index == 0:
            self.shift()
        elif index == self._length - 1:
            self.pop()
        else:
            node = self.get(index)
            if node and node.previous and node.next:
                node.previous.next = node.next
                node.previous.prev = node.prev
                node.next = None
                node.previous = None

            self._length -= 1
        return self
