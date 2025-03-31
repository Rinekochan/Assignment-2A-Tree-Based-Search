from utils import Graph
import heapq

def dijkstra(graph: Graph, root: str, goal: str):
    dist = {}
    for n in graph.nodes.keys():
        dist[n] = float('inf')
    dist[root] = 0

    pq = []
    heapq.heappush(pq, (0, root))

    visited = []

    while len(pq) != 0:
        current_dist, current_node = heapq.heappop(pq)

        if current_node == goal:
            return visited

        if current_node in visited:
            visited.append(goal)
            return visited

        visited.append(current_node)
        
        for child, weight in graph.adj_list[current_node]:
            if child in visited:
                continue
            potential_dist = current_dist + weight;
            if potential_dist < dist[child]:
                dist[child] = potential_dist
                heapq.heappush(pq, (potential_dist, child))

    raise ValueError("There are some problems search the path")
