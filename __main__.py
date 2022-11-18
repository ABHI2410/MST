from time import time 
import networkx as nx
from .visual import graphvisual
from .graph import Graph
from .prims import prims
import matplotlib.pyplot as plt

if __name__ == "__main__":

    G = nx.Graph()
    with open ("Dataset/usairport.txt",'r') as f:
        for line in f:
            edge_details = [float(x) for x in line.split()]
            G.add_edge(edge_details[0],edge_details[1],weight = edge_details[2])

    # V = graphvisual(G.graph_nodes,G.graph_matrix)
    # V.visualize()

    p = prims(G)
    p.MST()






    