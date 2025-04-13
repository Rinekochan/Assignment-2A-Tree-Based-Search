from functools import lru_cache
from typing import Tuple

from Research.research_utils import euclidean


def dynamic_programming(nodes: dict[Tuple[int]]):
    if len(nodes) > 20: raise ValueError("Dynammic Programming can't run any graphs with more than 20 nodes")
    # Convert the node dict into a list of node IDs and positions for easier indexing.
    node_ids = list(nodes.keys())
    coords = [nodes[nid] for nid in node_ids]  # List of coordinates
    n = len(coords)

    # Store next move for (current_node_index, visited_mask)
    next_move = {}

    @lru_cache(maxsize=None) # Use cache in python as a method to memorize precalculated results for dynammic programming
    def dp(pos: int, visited: int) -> float:
        if visited == (1 << n) - 1:
            return euclidean(coords[pos], coords[0])  # Return to start

        min_cost = float('inf')
        best_next = None
        for nxt in range(n):
            if not (visited >> nxt) & 1:  # If nxt is not visited
                cost = euclidean(coords[pos], coords[nxt]) + dp(nxt, visited | (1 << nxt))
                if cost < min_cost:
                    min_cost = cost
                    best_next = nxt

        next_move[(pos, visited)] = best_next  # Save decision
        return min_cost

    # Run DP to compute min cost
    distance = dp(0, 1 << 0)

    # Reconstruct the path
    path_indices = [0]
    pos = 0
    visited = 1 << 0
    while (pos, visited) in next_move:
        next_pos = next_move[(pos, visited)]
        path_indices.append(next_pos)
        visited |= (1 << next_pos)
        pos = next_pos

    path_ids = [node_ids[i] for i in path_indices]

    return path_ids, len(path_ids), distance