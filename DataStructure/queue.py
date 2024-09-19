class _Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._length = 0

    @property
    def length(self):
        return self._length

    def enqueue(self, value):
        node = _Node(value)
        if not self.last:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self._length += 1
        return self

    def dequeue(self):
        currentFirst = self.first
        if currentFirst:
            if self.first == self.last:
                self.last = None
                self.first = currentFirst.next
                self._length -= 1
                return currentFirst

# Example usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue().value)
print(q.dequeue().value)
