class _Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        node = _Node(value)
        if not self.root:
            self.root = node
        else:
            currentNode = self.root
            while True:
                if value == currentNode.value:
                    return None

                if value < currentNode.value:
                    if currentNode.left:
                        currentNode = currentNode.left
                    else:
                        currentNode.left = node
                        break
                else:
                    if currentNode.right:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = node
                        break
        return self

    def have(self, value: int) -> bool:
        currentNode = self.root
        while currentNode:
            if value == currentNode.value:
                return True
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return False


# Example usage:
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(20)
print(bst.have(5))  # Output: True
print(bst.have(15))  # Output: False
