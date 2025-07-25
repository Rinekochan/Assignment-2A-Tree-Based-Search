from utils import Graph, pythagoras
from queue import PriorityQueue
import math

#Greedy Best First Search
#Calculates heuristic using pythagoras (euclidean distance / straight line distance)
#Potential issue: can reach dead ends (will not move further, ends path without reaching destination)
def gbfs(graph: Graph, root: str, destinations: list):

    #Set heuristic to euclidean distance using pythagoras
    heuristic = pythagoras(graph, destinations)

    prioQueue = PriorityQueue()
    counter = 0 #chronological counter for tie-breaking
    prioQueue.put((0, root, counter))
    counter += 1

    visited = []
    parents = {root: None} #track parent of each node (which node we previously came from)

    while not prioQueue.empty():
        _, node, _ = prioQueue.get()

        if node in visited:
            continue

        #Current node is added to the visited list
        visited.append(node)

        #If current node is a destination, begins creating the path taken
        if node in destinations:
            path = []
            current = node

            while current is not None:
                path.append(current)
                current = parents[current]

            path.reverse()
            return path, len(visited)

        #for each neighbour, puts it into priority queue with its heuristic - distance from goal
        for neighbour, _ in graph.adj_list[node].items():

            if neighbour not in visited:
                prioQueue.put((heuristic[neighbour], neighbour, counter))
                counter += 1;

                if neighbour not in parents:
                    parents[neighbour] = node

    print("GBFS: No valid path was found")
    return [], len(visited)