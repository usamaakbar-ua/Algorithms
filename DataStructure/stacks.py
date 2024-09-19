#Stack using array (list in python)

stack = [1, 2, 3]
stack.appeand(4)
print(stack)
stack.pop()
print(stack)

# Stacks only have push and pop, but Python lists support more
stack.insert(0, 0)
print(stack)
stack.pop(0)
print(stack)


#Stack using a singly linked list

class _Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self._length = 0

    #property to get the length of the stack
    @property
    def length(self):
        return self._length

    #push method
    def push(self, value):
        node = _Node(value)
        currentFirst = self.first
        self.first = node
        self.first.next = currentFirst

        if not currentFirst:
            self.last = node

        self._length += 1
        return self

    #Pop Method
    def pop(self):
        currentFirst = self.first
        if currentFirst:
            if self.first == self.last:
                self.last = None
            self.first = currentFirst.next
            self._length -= 1
        return currentFirst


# Example
stack = Stack()
stack.push(1).push(2).push(3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.length)
