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

    #Breadth-First Search (BFS)

    def bfs(self):
        visited = []
        if self.root:
            queue = [self.root]
            while queue:
                currentNode = queue.pop(0)
                visited.append(currentNode)

                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
        return visited

    #Depth-First Search (DFS) -PreOrder
    def dfsPreOrder(self):
        visited = []

        def traverse(node):
            visited.append(node)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        if self.root:
            traverse(self.root)
        return visited

    # Depth-First Search (DFS) - PostOrder
    def dfsPostOrder(self):
        visited = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            visited.append(node)

        if self.root:
            traverse(self.root)
        return visited

    #Depth-First Search (DFS) -InOrder
    def dfsInOrder(self):
        visited = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            visited.append(node)

        if self.root:
            traverse(self.root)
        return visited


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(20)

# BFS traversal
bfs_nodes = [node.value for node in bst.bfs()]
print("BFS:", bfs_nodes)  # Output: BFS: [10, 5, 20]

# DFS PreOrder traversal
dfs_pre_nodes = [node.value for node in bst.dfsPreOrder()]
print("DFS PreOrder:", dfs_pre_nodes)  # Output: DFS PreOrder: [10, 5, 20]

# DFS PostOrder traversal
dfs_post_nodes = [node.value for node in bst.dfsPostOrder()]
print("DFS PostOrder:", dfs_post_nodes)  # Output: DFS PostOrder: [5, 20, 10]

# DFS InOrder traversal
dfs_in_nodes = [node.value for node in bst.dfsInOrder()]
print("DFS InOrder:", dfs_in_nodes)  # Output: DFS InOrder: [5, 10, 20]
