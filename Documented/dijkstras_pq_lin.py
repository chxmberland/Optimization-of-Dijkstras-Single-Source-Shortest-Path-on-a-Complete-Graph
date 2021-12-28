# Custom Priortiy Queue class
class LinearPriorityQueue:
    
    def __init__(self):
        
        # This is a list which contains the elements of the queue
        self.queue = []
        
        # This dictionary contains the elements and their related priority
        self.priorities = {}
        
    
    
    # This function will enqueue an element to the queue.
    # It will then adjust the queue accordingly, based on priority.
    # Since we are using this PQ for a shortest path in a weighted graph, lower values get priority.
    def enqueue(self, element, priority):
        
        # Checking to see if an element is in the queue already
        if element in self.queue:
            
            print("This element (" + str(element) + ") is already in the queue, use update_priority instead!")
            return
        
        # If it is not, it should be inserted in the correct spot
        else:
            
            self.insert(element, priority)
    
    
    
    # This function will dequeue and element from the queue.
    # Dequeuing means to remove the first element in the list, and shifting everything.
    def dequeue(self):
        
        # Making sure the list is not empty
        if len(self.queue) > 0:
            
            # Removing the first element from the queue
            to_del = self.queue.pop(0)
            
            # Deleting the item from the priority dictionary
            del self.priorities[to_del]
            
            return to_del
            
    
    
    # This function will update the priority of an element if it is less than before
    def update_priority(self, element, priority):
        
        # Checking to see if the elemen is in the queue
        if element not in self.queue:
            
            print("The element (" + str(element) + ") is not the queue yet. Use enqueue instead!")
            return
            
        # If it is, we can just remove it and insert it again
        else:
            
            # Removing the element from the priority dictionary
            del self.priorities[element]
            
            # Removing the element from the queue        
            self.queue.remove(element)
                    
            # Using enqueue to re-insert the item in the correct place
            self.insert(element, priority)
            
            
    
    # This function inserts an element in the list based on it's priority
    def insert(self, element, priority):
        
        # Adding the item to the priority dictionary
        self.priorities[element] = priority
        
        # If this is the first element you're enqueing, you should just put it at the front
        if len(self.queue) == 0:
            
            self.queue.append(element)
        
        # Otherwise, if it's not the first element, consider it's priority
        else:
                
            # Looping through each value in the list to see where the new element should go
            for i in range(len(self.queue)):
                
                # Comparing the priority of the element in the list against the priority of the element to insert
                if priority <= self.priorities[self.queue[i]]:

                    # Inserts the element into the queue
                    self.queue = self.queue[0 :  i] + [element] + self.queue[i:]
                    
                    # The function should stop executing at this point
                    return
                    
        # If the priority is lower than every other element, it wouldn't have been inserted, so we insert it now
        if element not in self.queue:
            
            self.queue.append(element)



# This function will execute Dijkstra's algorithm on a weighted, directed graph, using a priority queue
def dijkstras_pq_lin(WD_graph, source):
    
    # Checking to see if the source node is in the graph
    if source not in WD_graph.verticies:
        
        print("The source does not exist in the graph")
        return
    
    # Initializing the priority queue 
    pq = LinearPriorityQueue()
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
    pq.enqueue(source, 0)
        
    # Finiding the shortest path to all nodes
    while len(pq.queue) > 0:
        
        # Removing the first node in the priority queue
        cur_vertex = pq.dequeue()
        
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
                if i in pq.queue:
                    
                    # Updating the priority queue
                    pq.update_priority(i, dist[i])
                    
                # If it's not, we must enqueue it
                else:
                    
                    pq.enqueue(i, dist[i])
    
    # Returning the shortest distances and previous nodes
    return (dist, prev)