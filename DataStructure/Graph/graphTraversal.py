class Graph:
    def __init__(self):
        self._adjacencyList = {}

    @property
    def adjacencyList(self):
        return self._adjacencyList

    @adjacencyList.setter
    def adjacencyList(self, value):
        self._adjacencyList = value

    def addVertex(self, vertex):
        self._adjacencyList[vertex] = []
        return self._adjacencyList

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self._adjacencyList and vertex2 in self._adjacencyList:
            self._adjacencyList[vertex1].append(vertex2)
            self._adjacencyList[vertex2].append(vertex1)
            return True
        return False

    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self._adjacencyList and vertex2 in self._adjacencyList:
            self._adjacencyList[vertex1] = [v for v in self._adjacencyList[vertex1]]
            self._adjacencyList[vertex2] = [v for v in self._adjacencyList[vertex2]]
            return True
        return False

    def removeVertex(self, vertex):
        if vertex in self._adjacencyList:
            for key in self._adjacencyList:
                self.removeEdge(key, vertex)
            del self._adjacencyList[vertex]
            return vertex
        return None

    def dfsRecursive(self, startingVertex):
        results = []
        visitedVertex = {}
        adjacencyList = self._adjacencyList

        def traverse(vertex):
            if not vertex:
                return
            if vertex not in visitedVertex:
                visitedVertex[vertex] = True
                results.append(vertex)
                for neighbor in adjacencyList[vertex]:
                    if neighbor not in visitedVertex:
                        traverse(neighbor)
        if startingVertex in adjacencyList:
            traverse(startingVertex)

        return results

    def dfsIterative(self, startingVertex):
        results = []
        visitedVertex = {}
        stack = [startingVertex]

        while stack:
            currentVertex = stack.pop()
            if currentVertex not in visitedVertex:
                visitedVertex[currentVertex] = True
                results.append(currentVertex)
                stack.extend(self._adjacencyList[currentVertex])

        return results

    def breadthFirstSearch(self, startingVertex):
        results = []
        visitedVertex = {}
        queue = [startingVertex]

        while queue:
            currentVertex = queue.pop(0)
            if currentVertex not in visitedVertex:
                visitedVertex[currentVertex] = True
                results.append(currentVertex)
                queue.extend(self._adjacencyList[currentVertex])

        return results

