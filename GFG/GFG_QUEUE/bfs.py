from collections import defaultdict


class Graph():
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    def addEdge(self, start, end):
        self.graph[start].append(end)
    def BFS(self, startingPoint):
        queue = []
        visited = []
        queue.append(startingPoint)
        visited.append(startingPoint)
        while queue:
            processingNode = queue.pop(0)
            print(processingNode, end=" ")
            for connectedNode in self.graph[processingNode]:
                if connectedNode not in visited:
                    queue.append(connectedNode)
                    visited.append(connectedNode)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.BFS(2)

        

