from utils import Graph, reconstruct_path

# Depth-first-search algorithm
# return visited array if goal is achieved, otherwise None
def dfs(graph: Graph, root: str, destinations: list):
    stack = []
    visited = []
    prev = {}

    stack.append(root)
    visited.append(root)

    while len(stack) != 0:
        node = stack.pop()
        for neighbour, _ in graph.adj_list[node].items():
            if neighbour not in visited:
                if neighbour in destinations:
                    prev[neighbour] = node
                    return reconstruct_path(neighbour, prev)
                visited.append(neighbour)
                stack.append(neighbour)
                prev[neighbour] = node

    print("DFS: No valid path was found")
    return []
