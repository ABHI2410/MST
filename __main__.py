import numbers
import sys
from time import time 
import os
import itertools
import random
from .graph import Graph
from .prims import prims

if __name__ == "__main__":
    GRAPH_SIZE = 5
    GRAPH_SPARSITY = 0.40
    possible_numbers = range(0,20)
    nodes = random.sample(possible_numbers,GRAPH_SIZE)
    possible_edges = list(itertools.combinations_with_replacement(nodes,2))
    edges = random.sample(possible_edges,int(len(possible_edges)*GRAPH_SPARSITY))
    g = Graph()
    for edge in edges:
        weight = random.randint(1,10)
        g.addEdge(edge[0],edge[1],weight)
    print(g)

    p = prims(g.graph_nodes,g.graph_matrix)
    p.MST()






    