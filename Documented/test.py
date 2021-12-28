# Importing the necessary data structures
from wd_graph import WDGraph as wdg
import pq

# Importing modules that will be used for testing
import time
import random

# Importing the algorithms that will be tested
from dijsktras_pq_log import dijkstras_pq_log
from dijkstras_lazy import dijkstras_lazy
from dijkstras_pq_lin import dijkstras_pq_lin



# This function tests to see if the algorithm works at a basic capacity
def test_alg(alg):

    wd_graph = wdg(6)

    wd_graph.update_weight(0, 1, 1)
    wd_graph.update_weight(0, 2, 8)

    wd_graph.update_weight(1, 3, 7)
    wd_graph.update_weight(1, 4, 1)

    wd_graph.update_weight(2, 3, 10)
    wd_graph.update_weight(2, 4, 6)

    wd_graph.update_weight(3, 5, 10)
    wd_graph.update_weight(4, 5, 1)

    # Getting the shortest path using the algorithm specified
    return get_path(alg, wd_graph, 0, 5)



# This function will print the shortest path in a graph using an algorithm
def get_path(alg, wd_graph, source, destination):
    
    # Using Dijktra's
    dist, prev = alg(wd_graph, source)
    
    # Finding the shortest path by backtracking
    cur = destination
    path = []
    
    while cur != source:
        
        if prev[cur] == -1:
            
            return "No path exists between these two nodes."
        
        path.append(cur)
        cur = prev[cur]
    
    # Formatting the shortest path
    path = [source] + path[::-1]
    
    return " > ".join([str(vertex) for vertex in path])



# This algorithm tests the runtime of some algorithm
def test_runtime(alg, n):

    # Creating the Weighted Directed Graph
    wd_graph = wdg(n)

    # Adding nodes to the graph (each node has an edge with EVERY other node, which makes it a complete graph)
    for i in range(0, n):
        
        for j in range(0, n):
            
            if i != j:
                
                wd_graph.update_weight(i, j, random.randint(1, 20))

    # Beginning the timer
    start = time.time()

    # Executing the algorithm
    updates = dijkstras_lazy(wd_graph, 0)
    
    print("Updates to D and P: " + str(updates))

    # Stopping the timer and printing the results
    return "--- %s seconds ---" % (time.time() - start) + " with input " + str(n)



# Testing:

print(test_runtime(dijkstras_lazy, 2))