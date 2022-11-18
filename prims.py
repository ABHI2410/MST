import sys

from .visual import graphvisual

from .graph import Graph

class prims:

    def __init__(self, graph):
        self.graph = graph
        self.vertices = len(graph.nodes)
    
    def min_node_weigh(self, key, mst):
        min = sys.maxsize
        for vertex in range(self.vertices):
            if key[vertex] < min and mst[vertex] == False:
                min = key[vertex]
                min_node = vertex
                
        return min_node
        


    def MST(self):
        weight_of_node = [sys.maxsize for i in range(self.vertices)]
        parent = [None for i in range(self.vertices)]
        mst = [False for i in range(self.vertices)]
        weight_of_node[0] = 0
        parent[0] = -1
        count = 0

        for vertex in range(self.vertices):
            min = self.min_node_weigh(weight_of_node,mst)
            mst[min] = True
            count +=1
            print(count)
            for _vertex_ in range(self.vertices):
                edge_between_vertex_and_min = self.graph.get_edge_data(_vertex_,min)
                if edge_between_vertex_and_min is not None: 
                    weight_between_vertex_and_min = edge_between_vertex_and_min["weight"]
                else:
                    weight_between_vertex_and_min = 0
                if weight_between_vertex_and_min > 0 and mst[_vertex_] == False and weight_of_node[_vertex_] > self.graph[min][_vertex_]:
                    weight_of_node[_vertex_] = self.graph[min][_vertex_]
                    parent[_vertex_] = min
        self.make_adj_matrix_mst(parent)
        V = graphvisual(self.nodes,self.graph)
        V.visualize()
    
    

# 