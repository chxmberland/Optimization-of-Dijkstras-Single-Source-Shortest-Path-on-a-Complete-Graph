from wd_graph import WDGraph as wdg
import pq_log_comp
import time
import random
from dijsktras_pq_log_comp import dijkstras_pq_log
from dijkstras_lazy_comp import dijkstras_lazy
from dijkstras_pq_lin_comp import dijkstras_pq_lin

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

    return get_path(alg, wd_graph, 0, 5)

def get_path(alg, wd_graph, source, destination):
    
    dist, prev = alg(wd_graph, source)
    cur = destination
    path = []
    
    while cur != source:
        
        if prev[cur] == -1:
            return "No path exists between these two nodes."
        
        path.append(cur)
        cur = prev[cur]
    
    path = [source] + path[::-1]
    
    return " > ".join([str(vertex) for vertex in path])

def test_runtime(alg, n):

    wd_graph = wdg(n)

    for i in range(0, n):
        
        for j in range(0, n):
            
            if i != j:
                wd_graph.update_weight(i, j, random.randint(1, 20))

    start = time.time()
    updates = dijkstras_lazy(wd_graph, 0)
    print("Updates to D and P: " + str(updates))

    return "--- %s seconds ---" % (time.time() - start) + " with input " + str(n)



# Testing:

print(test_runtime(dijkstras_lazy, 2))