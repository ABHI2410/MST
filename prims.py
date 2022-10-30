import sys

from .graph import Graph

class prims:

    def __init__(self, nodes, matrix):
        self.nodes = nodes
        self.vertices = len(nodes)
        self.graph = matrix
    
    def min_node_weigh(self, key, mst):
        min = sys.maxsize

        for vertex in range(self.vertices):
            if key[vertex] < min and mst[vertex] == False:
                min = key[vertex]
                min_node = vertex
        return min_node

    def make_adj_matrix_mst(self, parent):
        g = Graph()
        for i in range(self.vertices):
            g.addEdge(self.nodes[i],self.nodes[parent[i]], self.graph[i][parent[i]])
        print(g)
        


    def MST(self):
        weight_of_node = [sys.maxsize for i in range(self.vertices)]
        parent = [None for i in range(self.vertices)]
        mst = [False for i in range(self.vertices)]
        weight_of_node[0] = 0
        parent[0] = -1

        for vertex in range(self.vertices):
            min = self.min_node_weigh(weight_of_node,mst)
            mst[min] = True

            for _vertex_ in range(self.vertices):
                if self.graph[min][_vertex_] > 0 and mst[_vertex_] == False and weight_of_node[_vertex_] > self.graph[min][_vertex_]:
                    weight_of_node[_vertex_] = self.graph[min][_vertex_]
                    parent[_vertex_] = min
        self.make_adj_matrix_mst(parent)
    
    

