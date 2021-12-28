class LinearPriorityQueue:
    
    def __init__(self):
        self.queue = []
        self.priorities = {}

    def enqueue(self, element, priority):
        
        if element in self.queue:
            print("This element (" + str(element) + ") is already in the queue, use update_priority instead!")
            return
        
        else:
            self.insert(element, priority)

    def dequeue(self):
        
        if len(self.queue) > 0:
            to_del = self.queue.pop(0)
            del self.priorities[to_del]
            
            return to_del
            
    def update_priority(self, element, priority):
        
        if element not in self.queue:
            print("The element (" + str(element) + ") is not the queue yet. Use enqueue instead!")
            return
            
        else:
            del self.priorities[element]
            self.queue.remove(element)
            self.insert(element, priority)
            
    def insert(self, element, priority):
        
        self.priorities[element] = priority

        if len(self.queue) == 0:
            self.queue.append(element)
        
        else:
            
            for i in range(len(self.queue)):
                
                if priority <= self.priorities[self.queue[i]]:
                    self.queue = self.queue[0 :  i] + [element] + self.queue[i:]
                    
                    return
                    
        if element not in self.queue:
            self.queue.append(element)

def dijkstras_pq_lin(WD_graph, source):
    
    if source not in WD_graph.verticies:    
        print("The source does not exist in the graph")
        return
    
    pq = LinearPriorityQueue()
    dist = {}
    prev = {}
    
    for vertex in WD_graph.verticies:
        
        if vertex != source:
            
            dist[vertex] = float('inf')
            prev[vertex] = -1
            
    dist[source] = 0
    pq.enqueue(source, 0)
        
    while len(pq.queue) > 0:
        
        cur_vertex = pq.dequeue()
        
        for i in range(WD_graph.nb_verticies):
            
            dist_to_neighbor = WD_graph.edges[cur_vertex][i]
            alt_dist = dist[cur_vertex] + dist_to_neighbor

            if dist_to_neighbor > 0 and alt_dist < dist[i]:
                
                dist[i] = alt_dist
                prev[i] = cur_vertex
                
                if i in pq.queue:
                    pq.update_priority(i, dist[i])
                    
                else:
                    pq.enqueue(i, dist[i])
    
    return (dist, prev)