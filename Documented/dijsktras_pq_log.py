# Importing Python's priority queue
from pq_log import LogarithmicPriorityQueue as log_pq



# Implementing DIjkstra's algorithm 
def dijkstras_pq_log(WD_graph, source):
    
    # Couting updates to P and D
    updates = 0
    
    # Checking to see if the source node is in the graph
    if source not in WD_graph.verticies:
        
        print("The source does not exist in the graph")
        return
    
    # Initializing the priority queue 
    pq = log_pq()
    visited = []
    dist = {}
    prev = {}
    
    # Setting all the distances to infinity and previous nodes to unknown
    for vertex in WD_graph.verticies:
        
        if vertex != source:
            
            dist[vertex] = float('inf')
            prev[vertex] = -1
            
    # Setting the distance of the source to zero
    dist[source] = 0
    
    # Queueing the source
    pq.__setitem__(source, 0)
        
    # Finiding the shortest path to all nodes
    while len(pq.heap) > 0:
        
        # Removing the first node in the priority queue
        cur_vertex = pq.popitem()[0]
        visited.append(cur_vertex)
        
        # Checking each neighbor of the current node
        for i in range(WD_graph.nb_verticies):
            
            # Getting the distance to the neighbor
            dist_to_neighbor = WD_graph.edges[cur_vertex][i]
            
            # Getting the distance from the current node to the neighbor
            alt_dist = dist[cur_vertex] + dist_to_neighbor
            
            # If the new caulculated distance to the neighbor is less, then the dist and prev dictionaries
            # are updated accordingly
            if dist_to_neighbor > 0 and alt_dist < dist[i]:
                
                # Updating the shortest path and previous node
                dist[i] = alt_dist
                prev[i] = cur_vertex
                
                # We now must update the neigbors position in the priorotiy queue
                if i not in visited:
                    
                    # Since Python's priority queue dosen't support a decrease key operation,
                    # this method becomes incredibly wasteful as there will be many duplicate keys.
                    pq.__setitem__(i, dist[i])

    # Returning the shortest distances and previous nodes
    return (dist, prev)