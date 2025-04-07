from utils import Graph
from queue import PriorityQueue
import math

#Greedy Best First Search
#Calculates heuristic (euclidean distance / straight line distance)
#Potential issue: can reach dead ends (will not move further, ends path without reaching destination)
#Tutor question: is number_of_nodes the total visited or the total of the path?
def gbfs(graph: Graph, root: str, destinations: list):
    prioQueue = PriorityQueue()
    prioQueue.put((0, root))

    visited = []
    parents = {root: None} #track parent of each node (which node we previously came from)

    while not prioQueue.empty():
        _, node = prioQueue.get()
        if node in visited:
            continue
        visited.append(node)
        if node in destinations:
            path = []
            current = node
            while current is not None:
                path.append(current)
                current = parents[current]
            path.reverse()
            return path
        closest = min(destinations, key=lambda goal: math.dist(graph.nodes[node], graph.nodes[goal]))
        for neighbour, _ in graph.adj_list.get(node,[]):
            if neighbour not in visited:
                heuristic = math.dist(graph.nodes[neighbour], graph.nodes[closest])
                prioQueue.put((heuristic, neighbour))
                if neighbour not in parents:
                    parents[neighbour] = node

    print("GBFS: There are some problems searching the path")
    return [visited] #prints all accessed nodes before encountering issues