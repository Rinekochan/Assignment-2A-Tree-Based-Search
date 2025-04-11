from utils import Graph, reconstruct_path
from collections import deque   # deque is more efficient than using lists as a queue

# Breadth-first-search algorithm
# return visited array if goal is achieved, otherwise None
def bfs(graph: Graph, root: str, destinations: list):
    queue = deque([root])
    prev = {root: None}

    while queue:
        node = queue.popleft()
        
        for neighbour, _ in graph.adj_list[node].items():
            if neighbour not in prev:
                prev[neighbour] = node
                if neighbour in destinations:
                    return reconstruct_path(neighbour, prev), len(prev)
                queue.append(neighbour)

    print("BFS: No valid path was found")
    return [], len(prev)
