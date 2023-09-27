"""Lab3: Minimum spanning tree
Author: Oumayma El Hit """
#Kruskal's Algorithm 

## we define a Graph's Class 
class Graph :
    def __init__(self, nodes ):
        self.V = nodes
        self.graph = [] 
    # function to add edges to the graph 
    def add_edge(self, u, v, e):
        self.graph.append([u, v, e])
    # unction to find the precedent or the parent of a node.
    def search_precedent(self, precedent, i):
        if precedent[i] == i:
            return i
        return self.search_precedent(precedent, precedent[i])
    def union(self, precedent, order, node1, node2):
        node1_origin = self.search_precedent(precedent, node1)
        node2_origin = self.search_precedent(precedent, node2)
        if order[node1_origin] < order[node2_origin]:
            precedent[node1_origin] = node2_origin
        elif order[node1_origin] > order[node2_origin]:
            precedent[node2_origin] = node1_origin
        else:
            precedent[node2_origin] = node1_origin
            order[node1_origin] += 1
    # Now we are ready to define Kruskal's algorithm 
    def kruskal (self):
        result = []
        i, edge = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        precedent = []
        order= []
        for vertex in range(self.V):
            precedent.append(vertex)
            order.append(0)
        while edge < self.V - 1:
            u, v, e = self.graph[i]
            i = i + 1
            x = self.search_precedent(precedent, u)
            y = self.search_precedent(precedent, v)
            if x != y:
                edge = edge + 1
                result.append([u, v, e])
                self.union(precedent, order, x, y)
        total=0
        for u, v, weight in result:
            print("%d - %d: %d" % (u+1, v+1, weight))
            total+=weight
        print("The total weight of the tree :", total )
g = Graph(7)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 2)
g.add_edge(1, 0, 5)
g.add_edge(1, 3, 3)
g.add_edge(1, 4, 10)
g.add_edge(2, 0, 6)
g.add_edge(2, 3, 7)
g.add_edge(2, 5, 4)
g.add_edge(3, 0, 2)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 8)
g.add_edge(3, 1, 3)
g.add_edge(3, 6, 12)
g.add_edge(4, 6, 1)
g.add_edge(4, 1, 10)
g.add_edge(5, 6, 11)
g.add_edge(5, 2, 4)
g.add_edge(5, 3, 8)
g.add_edge(6, 3, 12)
g.add_edge(6, 5, 11)
g.add_edge(6, 4, 1)
g.kruskal()

##Result : 
"""
5 - 7: 1
1 - 4: 2
2 - 4: 3
3 - 6: 4
1 - 3: 6
4 - 5: 9
the total weight of the tree : 25

That's what we were expecting ! 

"""