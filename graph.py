class Graph:
    # initializing the graph variables
    # graph_nodes will keep the actual value of the graph nodes
    # graph_matrix will keep the track if all the edges and the weight of edges
    def __init__(self):
        self.graph_nodes = []
        self.graph_matrix = []
    

    # Function to add a new edge in the graph.
    # If the graph is unweighted just use 1 as weight.
    def addEdge(self, node, neighbour,weight):
        if node != neighbour:
            # If the graph is empty/new without any node 
            # or a disjoint edge is to be added to the graph 
            # we need to add both the nodes with the corrosponding weight 
            if node not in self.graph_nodes and neighbour not in self.graph_nodes:
                # Adding the nodes to the graph_nodes list
                self.graph_nodes.append(node)
                self.graph_nodes.append(neighbour)
                for all_edges in self.graph_matrix:
                    all_edges.append(0)
                    all_edges.append(0)
                # Creating the list that will store the current node connection.
                new_node_connections = [0 for x in range(len(self.graph_nodes))]
                index_of_node = self.graph_nodes.index(node)
                index_of_neighbour = self.graph_nodes.index(neighbour)
                new_node_connections[index_of_neighbour] = weight
                # Adding the list to the graph_matrix
                self.graph_matrix.append(new_node_connections)
                # Creating the list that will store the current neighbour connection.
                new_node_connections = [0 for x in range(len(self.graph_nodes))]
                new_node_connections[index_of_node] = weight
                # Adding the list to the graph_matrix
                self.graph_matrix.append(new_node_connections)

            elif node in self.graph_nodes and neighbour not in self.graph_nodes:
                # Adding the neighbour to the graph_nodes list
                self.graph_nodes.append(neighbour)
                index_of_node = self.graph_nodes.index(node)  
                index_of_neighbour = self.graph_nodes.index(neighbour) 
                # Creating the list that will store the current node connection.         
                new_node_connections = [0 for x in range(len(self.graph_nodes))]
                new_node_connections[index_of_node] = weight
                # Adjusting the graph_matrix with the respect to the new edge that is to be added. 
                for all_edges in self.graph_matrix:
                    all_edges.append(0)
                self.graph_matrix[index_of_node][index_of_neighbour] = weight
                # Adding the list to the graph_matrix
                self.graph_matrix.append(new_node_connections)

            elif node not in self.graph_nodes and neighbour in self.graph_nodes:
                # Adding the node to the graph_nodes list
                self.graph_nodes.append(node)
                index_of_node = self.graph_nodes.index(node)  
                index_of_neighbour = self.graph_nodes.index(neighbour)  
                # Creating the list that will store the current node connection.         
                new_node_connections = [0 for x in range(len(self.graph_nodes))]
                new_node_connections[index_of_neighbour] = weight
                # Adjusting the graph_matrix with the respect to the new edge that is to be added.
                for all_edges in self.graph_matrix:
                    all_edges.append(0)
                self.graph_matrix[index_of_neighbour][index_of_node] = weight
                # Adding the list to the graph_matrix
                self.graph_matrix.append(new_node_connections)

            else:
                # If both node and neighbour are in the graph already we just add the edge to the matrix
                # find the index of both node and neighbour and change the value of the weight in matrix
                index_of_node = self.graph_nodes.index(node)  
                index_of_neighbour = self.graph_nodes.index(neighbour)
                self.graph_matrix[index_of_neighbour][index_of_node] = weight
                self.graph_matrix[index_of_node][index_of_neighbour] = weight

        if node == neighbour:
            if node not in self.graph_nodes:
                self.graph_nodes.append(node)
                for all_edges in self.graph_matrix:
                    all_edges.append(0)
                new_node_connections = [0 for x in range(len(self.graph_nodes))]
                index_of_node = self.graph_nodes.index(node)
                new_node_connections[index_of_node] = weight
                self.graph_matrix.append(new_node_connections)
            if node in self.graph_nodes:
                index_of_node = self.graph_nodes.index(node)  
                self.graph_matrix[index_of_node][index_of_node] = weight


    
    # Function to print the nodes and adj. matrix of the graph.
    def __repr__(self):
        graph = ''
        print("The nodes of graphs are:"," ".join(str(element) for element in self.graph_nodes))
        print("The matrix of graph is:")
        for i in self.graph_matrix:
            edge_of_grpah = " ".join(str(element) for element in i)
            graph = graph + edge_of_grpah + "\n"
        return graph


  
