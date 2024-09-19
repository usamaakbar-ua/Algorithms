class MaxBinaryHeap:
    def __init__(self):
        self._values = []

    @property
    def values(self):
        return self._values

    def SinkingUp(self, value):
        valueIndex = len(self._values) - 1
        while valueIndex > 0:
            parentIndex = (valueIndex - 1) // 2
            parent = self._values[parentIndex]

            if value <= parent:
                break

            #Swap the current value with its parent
            self._values[parentIndex], self._values[valueIndex] = value, parent
            valueIndex = parentIndex

    def SinkingDown(self):
        targetIndex = 0
        length = len(self._values)
        target = self._values[targetIndex]

        while True:
            leftChildIndex = 2 * targetIndex + 1
            rightChildIndex = 2 * targetIndex + 2

            leftChild = rightChild = None
            swap = None

            if leftChildIndex < length:
                leftChild = self._values[leftChildIndex]
                if leftChild > target:
                    swap = leftChildIndex

            if rightChildIndex < length:
                rightChild = self._values[rightChildIndex]
                if (swap is None and rightChild > target) or (swap is not None and rightChild > leftChild):
                    swap = rightChildIndex
            if swap is None:
                break

            #Swap target with larger Child
            self._values[targetIndex], self._values[swap] = self._values[swap], self._values[targetIndex]
            targetIndex = swap

    def insert(self, value):
        self._values.append(value)
        self.SinkingUp(value)
        return self._values

    def extractMax(self):
        if len(self._values) == 0:
            return None

        root = self._values[0]
        self._values[0] = self._values.pop()
        if len(self._values) > 0:
            self.SinkingDown()

        return root
