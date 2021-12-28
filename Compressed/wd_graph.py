class WDGraph:
    
    def __init__(self, nb_verticies):

        self.verticies = list(range(nb_verticies))
        self.nb_verticies = nb_verticies
        self.edges = []
        
        for i in range(nb_verticies):
            self.edges.append([0] * nb_verticies)

    def add_vertex(self):

        to_add = self.nb_verticies
        self.nb_verticies += 1
        self.verticies.append(to_add)

        for row in self.weights:
            row.append(0)
            
        self.weights.append([0] * self.nb_nodes)
    
    def __str__(self):
        
        edges = []
        
        for i in range(self.nb_verticies):
            
            for j in range(self.nb_verticies):
                
                if self.edges[i][j] > 0:
                    edges.append("[" + str(i) + ", " + str(j) + ", " + str(self.edges[i][j]) + "]")
        
        string = ""
        
        for edge in edges:
            string += edge + "\n"
            
        return string
        
    def update_weight(self, v1, v2, weight):
        
        if weight < 1:
            print("Any weighted edge you add should have a weight equal to, or greater than 1. The edge won't be updated.")
            return
        
        if self.edges[v1][v2] > 0:
            print("An edge already exists between these nodes, use update_edge instead.")
            return
        
        if v1 not in self.verticies or v2 not in self.verticies:
            print("One, or both verticies are not yet in the graph")
            return
            
        self.edges[v1][v2] = weight
    
    def remove_edge(self, v1, v2):
        
        if v1 not in self.verticies or v2 not in self.verticies:
            print("One, or both verticies are not yet in the graph")
            return
        
        self.edges[v1][v2] = 0