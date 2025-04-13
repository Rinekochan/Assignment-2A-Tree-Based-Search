from typing import Tuple

from Research.research_utils import euclidean


def nearest_neighbor(nodes: dict[Tuple[int]]):
    node_ids = list(nodes.keys())
    visited = [node_ids[0]] # This should be random, but we will just put it as the first id for demonstration
    total_distance = 0

    current = visited[0]
    while len(visited) < len(node_ids):
        nearest = None
        min_dist = float('inf')
        for nid in node_ids:
            if nid not in visited:
                dist = euclidean(nodes[current], nodes[nid])
                if dist < min_dist:
                    min_dist = dist
                    nearest = nid
        visited.append(nearest)
        total_distance += min_dist
        current = nearest

    # Optionally return to start
    total_distance += euclidean(nodes[current], nodes[visited[0]])

    return visited, len(visited), total_distance