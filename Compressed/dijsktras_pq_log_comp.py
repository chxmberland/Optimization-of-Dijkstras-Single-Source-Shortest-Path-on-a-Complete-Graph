# Importing Python's priority queue
from pq_log_comp import LogarithmicPriorityQueue as log_pq

def dijkstras_pq_log(WD_graph, source):
    
    if source not in WD_graph.verticies:
        print("The source does not exist in the graph")
        return
    
    pq = log_pq()
    visited = []
    dist = {}
    prev = {}
    
    for vertex in WD_graph.verticies:
        
        if vertex != source:
            dist[vertex] = float('inf')
            prev[vertex] = -1
            
    dist[source] = 0
    pq.__setitem__(source, 0)
        
    while len(pq.heap) > 0:
        cur_vertex = pq.popitem()[0]
        visited.append(cur_vertex)

        for i in range(WD_graph.nb_verticies):
            
            dist_to_neighbor = WD_graph.edges[cur_vertex][i]
            alt_dist = dist[cur_vertex] + dist_to_neighbor

            if dist_to_neighbor > 0 and alt_dist < dist[i]:
                dist[i] = alt_dist
                prev[i] = cur_vertex
                
                if i not in visited:
                    pq.__setitem__(i, dist[i])

    return (dist, prev)