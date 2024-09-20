class Graph:
    def __init__(self):
        # Initialize an empty dictionary to store the adjacency list
        self.adjacencyList = {}

    @property
    def adjacencyList(self):
        # Getter to return the current adjacency list
        return self._adjacencyList

    @adjacencyList.setter
    def adjacencyList(self, value):
        # Setter to update the adjacency list
        self._adjacencyList = value

    def addVertex(self, vertex: str):
        """
        Adds a new vertex to the graph.
        Each vertex will have an empty list as its value,
        representing the edges (connections) of this vertex.
        """
        self._adjacencyList[vertex] = []
        return self._adjacencyList

    def addEdge(self, vertex1: str, vertex2: str) -> bool:
        """
        Adds an undirected edge between two vertices.
        It updates the adjacency list for both vertices.
        Returns True if the edge is successfully added, False otherwise.
        """
        if vertex1 in self._adjacencyList and vertex2 in self._adjacencyList:
            self._adjacencyList[vertex1].append(vertex2)
            self._adjacencyList[vertex2].append(vertex1)
            return True
        return False

    def removeEdge(self, vertex1: str, vertex2: str) -> bool:
        if vertex1 in self._adjacencyList and vertex2 in self.adjacencyList:
            self._adjacencyList[vertex1] = [
                v for v in self._adjacencyList[vertex1] if v != vertex2
            ]
            self._adjacencyList[vertex2] = [
                v for v in self._adjacencyList[vertex2] if v != vertex1
            ]
            return True
        return False

    def removeVertex(self, vertex: str) -> str | None:
        """
        Removes a vertex and all its edges from the graph.
        It first removes all the edges connected to the vertex,
        and then deletes the vertex from the adjacency list.
        Returns the removed vertex or None if the vertex does not exist.
        """
        if vertex in self._adjacencyList:
            for adjacentVertex in list(self._adjacencyList):
                self.removeEdge(adjacentVertex, vertex)
            del self._adjacencyList[vertex]
            return vertex
        return None
