from utils import Graph

# Breadth-first-search algorithm
# return visited array if goal is achieved, otherwise None
def bfs(graph: Graph, root: str, goal: str):
    queue = []
    visited = []

    queue.append(root)
    visited.append(root)

    while len(queue) != 0:
        node = queue.pop(0)
        for neighbor, _ in graph.adj_list[node]:
            if neighbor not in visited:
                if neighbor == goal:
                    visited.append(neighbor)
                    return visited
                visited.append(neighbor)
                queue.append(neighbor)

    print("BFS: There are some problems searching the path")
    return []
