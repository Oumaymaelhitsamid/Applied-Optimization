""""
Lab2 - Shortest paths 
Auhtor : Oumayma El Hit 

"""

""""
Question 1 : Unweighted Single-Source Shortest Paths 
"""
from queue import Queue
# we build a graph class 
class Graph:
    def __init__(self, number_verteces, directed=True):
        self.m_number_verteces = number_verteces
        self.m_verteces = range(self.m_number_verteces)
        # we consider directed graphs as it is the case for our graph 
        self.m_directed = directed
        # we represent our graph(adjacency matrix ) as  a dictionary 
        self.m_adjacency = {vertex: set() for vertex in self.m_verteces}      
	
    # we define a method to create edges 
    def add_edge(self, vertex1, vertex2, weight=1): # unweighted 
        self.m_adjacency[vertex1].add((vertex2, weight))

        if not self.m_directed:
            self.m_adjacency[vertex2].add((vertex1, weight))
    
    def breadth_first(self, start, target): # We define the breadth first search algorithm 
        visited = set() #we denote the visited verteces 
        queue = Queue()

        # we initialise the queue and the set of visited  verteces by the start vertex  ('5' in our case)
        queue.put(start)
        visited.add(start)
    
        # the first vertex has no precednt or parent 
        precedent = dict()
        precedent[start] = None

        path = False
        while not queue.empty():
            current = queue.get()
            if current == target:
               path = True 
               break

            for (next, weight) in self.m_adjacency[current]:
                if next not in visited:
                    queue.put(next )
                    precedent[next] = current
                    visited.add(next)
                
       
        Shortest_path = []
        if path:
            Shortest_path.append(target)
            while precedent[target] is not None:
                Shortest_path.append(precedent[target]) 
                target = precedent[target]
            
            Shortest_path.reverse()
        return Shortest_path 


graph = Graph(9, directed=True)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(1, 7)
graph.add_edge(1, 8)
graph.add_edge(3, 2)
graph.add_edge(3, 7)
graph.add_edge(4, 3)
graph.add_edge(5, 1)
graph.add_edge(5, 4)
graph.add_edge(6, 1)
graph.add_edge(6, 5)
graph.add_edge(7, 2)
graph.add_edge(7, 8)
graph.add_edge(8, 6)

paths=[]
for i in range(1,9):
    paths.append(graph.breadth_first(5, i))
print(paths)

# Output: [[5, 1], [5, 1, 3, 2], [5, 1, 3], [5, 4], [5], [5, 1, 8, 6], [5, 1, 7], [5, 1, 8]]

"""
Question 2 : Positive Weighted Single-Source Shortest Paths :
"""
import math 

class Dijkstra:
    def __init__(self, graph, start):
        self.graph2 = graph2;
        self.start= start
        self.vertices = list(graph.keys())
        self.vertex_properties = {vertex: {'distance': math.inf, 'precedent': '-'} for vertex in self.vertices} # we denote a no existing path by  '-'
        self.vertex_properties[start]['distance'] = 0 # the distance of the start vertex from itself is null 
    def add_weight(self, vertex1, vertex2):# we define the weight of the edge between vertex1 and vertex2 
        try:
            return self.graph2[vertex1][vertex2]
        except KeyError:
            return math.inf
    def set_property(self, vertex, weight, precedent=''):
        self.vertex_properties[vertex]['distance'] = weight

        if precedent:
            self.vertex_properties[vertex]['precedent'] = precedent


    def get_property(self, vertex):
        return self.vertex_properties[vertex]
    def dijkstra(self):
        precedents= [self.start]
        max = len(self.vertices)
        while True:
            not_precedents = [vertex for vertex in self.vertices if vertex not in precedents]

            # Nearest vertex to start vertex
            nearest = '-'

            # Distance from start index
            nearest_dist = math.inf
            
            for not_precedent in not_precedents:
                not_precedent_property= self.get_property(not_precedent)

                # Shortest  distance of current outerior from start vertex
                shortest_dist= not_precedent_property['distance']

                # Last vertex through which we reached current exterior with shortest distance
                precedent1= not_precedent_property['precedent']
                for precedent in precedents:
                    # Shortest discovered distance of current interior from start vertex + distance of current interior from current exterior
                    dist_from_not_precedent = self.get_property(precedent)['distance'] + self.add_weight(precedent, not_precedent)

                    if dist_from_not_precedent< shortest_dist:
                        shortest_dist = dist_from_not_precedent
                        precedent1 = precedent
            
                self.set_property(not_precedent, shortest_dist, precedent1)

                # Attempt to find the nearest exterior to start vertex
                if shortest_dist < nearest_dist:
                    nearest_distance = shortest_dist
                    nearest = not_precedent
            
            precedents.append(nearest)
            if len(precedents) == max:
                break
    def path(self, vertex): 
        if vertex == '-':
            return[]
        return self.path(self.vertex_properties[vertex]['precedent']) + [vertex]
import pprint
graph2 = {'1': {'3': 4, '4': 5, '7': 6, '8':8 },
         '2': {},
         '3': {'2': 5, '7': 1},
         '4': {'3': 2},
         '5': {'1': 7,'4' :8},
         '6': {'1': 3, '5': 9},
         '7': {'2': 3, '8': 1},
         '8': {'6': 4}}
dijkstra = Dijkstra(graph2, start='5')

dijkstra.dijkstra()
pprint.pprint(dijkstra.vertex_properties)
for vertex in dijkstra.vertices:
    print('The path from 5 to ', vertex + ':', dijkstra.path(vertex))

# Output : 
"""
{'1': {'distance': 7, 'precedent': '5'},
 '2': {'distance': 14, 'precedent': '7'},
 '3': {'distance': 10, 'precedent': '4'},
 '4': {'distance': 8, 'precedent': '5'},
 '5': {'distance': 0, 'precedent': '-'},
 '6': {'distance': 16, 'precedent': '8'},
 '7': {'distance': 11, 'precedent': '3'},
 '8': {'distance': 12, 'precedent': '7'}}
The path from 5 to  1: ['5', '1']
The path from 5 to  2: ['5', '4', '3', '7', '2']
The path from 5 to  3: ['5', '4', '3']
The path from 5 to  4: ['5', '4']
The path from 5 to  5: ['5']
The path from 5 to  6: ['5', '4', '3', '7', '8', '6']
The path from 5 to  7: ['5', '4', '3', '7']
The path from 5 to  8: ['5', '4', '3', '7', '8']

"""

### Complexity: 
""""
1) The breadth first search algorithm runs in  O(V+E) time: we call V the number of verteces  and E the number of 
edges.Actually, each vertex is visited at most one time as only the first time that it is reached is its distance null. 
For edges, we check if an edge is incident of a vertex when we visit it from it. Each edge is checked at most twice 
because it is incident on two verteces.
2) Finding the shortest path through Dijkstra requires generally a complexity of O(Elog(V)): 
E is always the total number of edges 
V is the number of vertices 

In fact: Each vertex can be connected to (V-1) vertices, hence the number of adjacent edges to each vertex is V - 1.
we can say that E represents V-1 edges connected each to a  vertex.
Finding & Updating each adjacent vertex's weight is O(log(V))
Thus, the time complexity for Dijkstra Algorithm is O(ElogV)

"""