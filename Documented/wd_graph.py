class WDGraph:

    # This graph is implemented using an adjacency matrix, which contains the weight of edges
    
    # Constructor
    def __init__(self, nb_verticies):

        # Takes a list of verticies, which are integers.
        # We subtract one because verticies are numbered 0, 1, 2...
        self.verticies = list(range(nb_verticies))

        # Stores an integer, indicating the number of verticies
        self.nb_verticies = nb_verticies

        # Creates a matrix, which represents an adjacency matrix filled with a weight of zero
        self.edges = []
        for i in range(nb_verticies):
            self.edges.append([0] * nb_verticies)



    # This function will add a vertex to the graph.
    # Note that verticies are added in ascending order, meaning they are created in the order 0, 1, 2...
    def add_vertex(self):

        # Storing the integer value of the vertex that should be added
        to_add = self.nb_verticies
        
        # Updating the number of verticies
        self.nb_verticies += 1
        
        # Appending the vertext to the vertex list
        self.verticies.append(to_add)

        # Adding the vertex to the adjacency matrix
        for row in self.weights:
            row.append(0)
        self.weights.append([0] * self.nb_nodes)
    
    
    
    # This function prints the graph
    def __str__(self):
        
        edges = []
        
        # Looping through each possible edge in the adjacency matrix
        for i in range(self.nb_verticies):
            for j in range(self.nb_verticies):
                
                # Checking to see if the edge exists (has a weight greater than zero)
                if self.edges[i][j] > 0:
                    
                    edges.append("[" + str(i) + ", " + str(j) + ", " + str(self.edges[i][j]) + "]")
        
        string = ""
        
        # Printing each edge
        for edge in edges:
            string += edge + "\n"
            
        return string
        
                    
        
    # This function will add or update the edge between two edges in a graph.
    def update_weight(self, v1, v2, weight):
        
        # Checking to see if the weight is positive
        if weight < 1:
            
            print("Any weighted edge you add should have a weight equal to, or greater than 1. The edge won't be updated.")
            return
        
        # Checking to see if the edge exists
        if self.edges[v1][v2] > 0:
            
            print("An edge already exists between these nodes, use update_edge instead.")
            return
        
        # Making sure the verticies are in the graph
        if v1 not in self.verticies or v2 not in self.verticies:
            
            print("One, or both verticies are not yet in the graph")
            return
            
        # Adding the weighted edge to the adjacency matrix
        self.edges[v1][v2] = weight
    
    
    
    # This function removes an edge (sets the value in the adjacency matrix to 0)
    def remove_edge(self, v1, v2):
        
        # Making sure the verticies are in the graph
        if v1 not in self.verticies or v2 not in self.verticies:
            
            print("One, or both verticies are not yet in the graph")
            return
        
        self.edges[v1][v2] = 0