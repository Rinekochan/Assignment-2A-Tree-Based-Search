from utils import Graph, reconstruct_path

# Depth-first-search algorithm
# return visited array if goal is achieved, otherwise None
def dfs(graph: Graph, root: str, destinations: list):
    stack = [root]
    prev = {root: None}

    while stack:
        node = stack.pop()

        for neighbour, _ in sorted(graph.adj_list[node].items(),
                                   key=lambda item: int(item[0]) if item[0].isdigit() else item[0]):
            if neighbour not in prev:
                prev[neighbour] = node
                if neighbour in destinations:
                    return reconstruct_path(neighbour, prev), len(prev)
                stack.append(neighbour)

    print("DFS: No valid path was found")
    return [], len(prev)
