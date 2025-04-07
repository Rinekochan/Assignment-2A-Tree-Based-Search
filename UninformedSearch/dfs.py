from utils import Graph

# Depth-first-search algorithm
# return visited array if goal is achieved, otherwise None
def dfs(graph: Graph, root: str, goal: str):
    stack = []
    visited = []

    stack.append(root)
    visited.append(root)

    while len(stack) != 0:
        node = stack.pop()
        for neighbor, _ in graph.adj_list[node]:
            if neighbor not in visited:
                if neighbor == goal:
                    visited.append(neighbor)
                    return visited
                visited.append(neighbor)
                stack.append(neighbor)

    print("DFS: There are some problems searching the path")
    return []
