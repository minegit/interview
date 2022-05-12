class Graph():
    def __init__(self, vertices) -> None:
        self.vertices = vertices
        self.graph = [[0 for col in range(vertices)]for row in range(vertices)]

    def isSafe(self, v, color, c):
        for vertix in range(self.vertices):
            # if v is connected to any vertix and color of that vertix is c then return false
            if self.graph[v][vertix] ==1 and color[vertix] == c:
                return False
        return True

    def colorGraphUtil(self, m, color, v):
        if self.vertices == v:
            return True
        for c in range(1, m+1):
            if self.isSafe(v, color, c):
                color[v] = c
                if self.colorGraphUtil(m, color, v+1):
                    return True
                color[v] = 0
    def isHSafe(self, vertix, visited, currentVertix,startingPoint):
        if vertix == startingPoint:
            if self.graph[currentVertix][vertix] ==1 and len(visited) == self.vertices:
                return True
            if len(visited) < self.vertices and len(visited) > 0:
                return False
        if self.graph[currentVertix][vertix] ==1 and vertix not in visited:
            return True
        return False
    def isHUtil(self, currentVertex, visited,startingPoint):
        if len(visited)-1 == self.vertices:
            return True
        for vertix in range(self.vertices):
            if vertix != currentVertex:
                if self.isHSafe(vertix, visited, currentVertex,startingPoint):
                    visited.append(vertix)
                    if self.isHUtil(vertix, visited,startingPoint):
                        return True
                    visited.remove(vertix)
                


    def colorGraph(self, m):
        color = [0] * self.vertices
        if self.colorGraphUtil(m, color, 0):
            print(color)
        else:
            print(None)
    
    def printHamiltonian(self):
        for vertex in range(self.vertices):
            visited = [vertex]
            startingPoint = vertex
            if self.isHUtil(vertex,visited, startingPoint):
                print(visited)
                


if __name__ == "__main__":
    g = Graph(5)
    # g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    g.graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
            [1, 1, 0, 0, 1,],[1, 1, 0, 0, 1],
            [1, 1, 1, 1, 0], ]
    # g.graph = [[1]*5]*5
    m = 3
    # g.colorGraph(m)
    g.printHamiltonian()