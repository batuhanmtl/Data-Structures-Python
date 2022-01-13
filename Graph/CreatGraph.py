class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight

    def __str__(self):
        return str(self.id) + " connected to : " + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]


class Graph:

    def __init__(self):
        self.vertlist = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertlist[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n is self.vertlist:
            return self.vertlist[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertlist

    def addEdge(self, f, t, cost=0):
        if f not in self.vertlist:
            nv = self.addVertex(f)
        if t not in self.vertlist:
            nv = self.addVertex(t)
        self.vertlist[f].addNeighbor(self.vertlist[t], cost)

    def getVertices(self):
        return self.vertlist.keys()

    def __iter__(self):
        return iter(self.vertlist.values())


g = Graph()

g.addVertex("a")
g.addVertex("b")
g.addVertex("c")
g.addVertex("d")
g.addVertex("e")
g.addVertex("f")

g.addEdge("a", "b", 3)
g.addEdge("a", "c", 2)
g.addEdge("a", "f", 4)

g.addEdge("b", "a", 3)
g.addEdge("b", "c", 5)
g.addEdge("b", "d", 3)

g.addEdge("c", "b", 5)
g.addEdge("c", "d", 2)
g.addEdge("c", "e", 7)
g.addEdge("c", "a", 2)

g.addEdge("d", "e", 4)
g.addEdge("d", "b", 3)
g.addEdge("d", "c", 2)

g.addEdge("e", "d", 4)
g.addEdge("e", "c", 7)
g.addEdge("e", "f", 6)

g.addEdge("f", "e", 6)
g.addEdge("f", "a", 4)

for v in g:
    print(v)
    print(v.getConnections())
