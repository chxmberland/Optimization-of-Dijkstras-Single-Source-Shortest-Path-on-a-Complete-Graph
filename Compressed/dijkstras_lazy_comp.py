def dijkstras_lazy(WD_graph, source):
    
    if source not in WD_graph.verticies:
        print("The source does not exist in the graph")
        return
    
    queue = []
    dist = {}
    prev = {}
    
    for vertex in WD_graph.verticies:  
              
        if vertex != source:
            dist[vertex] = float('inf')
            prev[vertex] = -1
            
    dist[source] = 0
    queue.append(source)
    
    while len(queue) > 0:        
        cur_vertex = queue.pop(0)
        
        for i in range(WD_graph.nb_verticies):
            dist_to_neighbor = WD_graph.edges[cur_vertex][i]
            alt_dist = dist[cur_vertex] + dist_to_neighbor
            
            if dist_to_neighbor > 0 and alt_dist < dist[i]:
                dist[i] = alt_dist
                prev[i] = cur_vertex
                updates = updates + 1
                
                if i not in queue:
                    queue.append(i)

    return updates