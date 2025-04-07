from utils import Graph
import heapq

def dijkstra(graph: Graph, root: str, goal: str):
    '''
    Dijkstra is the algorithm that finds the shortest path within a graph between start and end nodes.
    This search algorithm is uninformed and node selection is based on the smallest cost on the priority queue.
    There are # steps to achieve this:
    1. Mark all nodes as unvisited, set distances to inf, push start node to pq
    2. For the current node popped from pq, calculate the distance to all unvisited neighbours
    2.1. Update shortest distance, if new distance is shorter than old distance
    2.2. Update previous nodes map
    2.3. Push neighbors to priority queue
    3. Mark current node as visited
    4. Choose new current node from unvisited nodes with minimal distance
    5. Goes back to step 2 until pq is empty
    '''
    dist = {} # contains distance of each node from the start node
    prev = {} # contains previous node for each node
    visited = []

    for n in graph.nodes.keys():
        dist[n] = float('inf')
    dist[root] = 0

    pq = []
    heapq.heappush(pq, (0, root))

    while len(pq) != 0:
        current_dist, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        for child, weight in graph.adj_list[current_node]:
            if child in visited:
                continue
            potential_dist = current_dist + weight;
            if potential_dist < dist[child]:
                dist[child] = potential_dist
                prev[child] = current_node
                heapq.heappush(pq, (potential_dist, child))
        
        visited.append(current_node)

    current_node = goal
    result = [goal]
    while current_node != root:
        current_node = prev[current_node]
        result.append(current_node)

    result.reverse()
    if result[0] == root and result[-1] == goal:
        return result
    else:
        print("CUS1: There are some problems searching the path")
        return []