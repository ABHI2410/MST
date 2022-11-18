import networkx as nx
import matplotlib.pyplot as plt

class graphvisual():
    def __init__(self,nodes,graph):
        self.matrix = graph
        self.node = nodes
        self.edges = []
    
    def visualize(self):
        G = nx.Graph()
        i = len(self.node)-1
        while i>=0:
            j = 0
            while j<=i:
                if self.matrix[i][j] != 0:
                    G.add_edge(self.node[i],self.node[j],weight=self.matrix[i][j])
                j += 1
            i = i - 1
        print(nx.info(G))

        pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
        # nx.draw(G, pos, with_labels = True)
        nx.draw_networkx_edge_labels(G,pos)
        # # nodes
        nx.draw_networkx_nodes(G, pos, node_size=500)

        # # edges
        nx.draw_networkx_edges(G, pos, edgelist=G.edges, width=6, alpha=0.5, edge_color="b")

        # node labels
        nx.draw_networkx_labels(G, pos, font_size=20,font_family="sans-serif")

        # edge weight labels

        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()