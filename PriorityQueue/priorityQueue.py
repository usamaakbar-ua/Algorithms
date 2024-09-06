#PriorityQueue

class INode:
    def __init__(self, value, priority=0):
        self.value = value
        self.priority = priority


class _Node(INode):
    def __init__(self, value, priority=0):
        super().__init__(value, priority)


class PriorityQueue:
    def __init__(self):
        self._values = []

    @property
    def values(self):
        return self._values

    def sinkingUp(self, node):
        valueIndex = len(self._values) - 1
        while valueIndex > 0:
            parentIndex = (valueIndex - 1) // 2
            parent = self._values[parentIndex]

            if node.priority >= parent.priority:
                break

            self._values[parentIndex] = node
            self._values[valueIndex] = parent

            valueIndex = parentIndex

    def sinkingDown(self):
        targetIndex = 0
        while True:
            leftChildIndex = targetIndex * 2 + 1
            rightChildIndex = targetIndex * 2 + 2

            target = self._values[targetIndex]
            leftChild = self._values[leftChildIndex] if leftChildIndex < len(self._values) else None
            rightChild = self._values[rightChildIndex] if rightChildIndex < len(self._values) else None

            if (leftChild and rightChild and target.priority > leftChild.priority
                    and target.priority > rightChild.priority):
                if rightChild.priority < leftChild.priority:
                    self._values[targetIndex], self._values[rightChildIndex] = (
                        self._values[rightChildIndex], self._values[targetIndex]
                    )
                    targetIndex = rightChildIndex
                else:
                    self._values[targetIndex], self._values[leftChildIndex] = (
                        self._values[leftChildIndex], self._values[targetIndex]
                    )
                    targetIndex = leftChildIndex
                continue
            elif rightChild and rightChild.priority <= target.priority:
                self._values[targetIndex], self._values[rightChildIndex] = (
                    self._values[rightChildIndex], self._values[targetIndex]
                )
                targetIndex = rightChildIndex
                continue
            elif leftChild and leftChild.priority <= target.priority:
                self._values[targetIndex], self._values[leftChildIndex] = (
                    self._values[leftChildIndex], self._values[targetIndex]
                )
                targetIndex = leftChildIndex
                continue

            break

    def enqueue(self, value, priority=0):
        node = _Node(value, priority)
        self._values.append(node)
        self.sinkingUp(node)
        return self._values

    def dequeue(self):
        if not self._values:
            return None
        root = self._values[0]
        self._values[0] = self._values.pop()
        self.sinkingDown()
        return root
