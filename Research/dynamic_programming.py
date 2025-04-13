from functools import lru_cache
from typing import Tuple

from Research.research_utils import euclidean


def dynamic_programming(nodes: dict[Tuple[int]]):
    if len(nodes) > 20: raise ValueError("Dynammic Programming can't run any graphs with more than 20 nodes")

    node_ids = list(nodes.keys())
    coords = [nodes[nid] for nid in node_ids]
    n = len(coords)

    @lru_cache(maxsize=None) # Using Python memoization to avoid recomputation
    def dp(pos: int, visited: int) -> float:
        if visited == (1 << n) - 1:
            return 0  # No return to start

        min_cost = float('inf')
        for nxt in range(n):
            if not (visited >> nxt) & 1:
                # Recursively calculate cost to next node + remaining path
                cost = euclidean(coords[pos], coords[nxt]) + dp(nxt, visited | (1 << nxt))
                if cost < min_cost:
                    min_cost = cost
        return min_cost

    # Best path details
    best_distance = float('inf')
    best_start = 0

    # Try all starting positions
    for start in range(n):
        total_distance = dp(start, 1 << start) # Start from this node with its bit set in visited
        if total_distance < best_distance:
            best_distance = total_distance
            best_start = start

    # Reconstruct path for best_start using a greedy traceback
    def reconstruct(start):
        pos = start
        visited = 1 << pos
        path = [pos]

        while visited != (1 << n) - 1:
            best_next = None
            min_cost = float('inf')
            for nxt in range(n):
                if not (visited >> nxt) & 1:
                    # Estimate cost of going to 'nxt' and completing the rest
                    cost = euclidean(coords[pos], coords[nxt]) + dp(nxt, visited | (1 << nxt)) # The dp result is already saved, so there will be no recomputed
                    if cost < min_cost:
                        min_cost = cost
                        best_next = nxt
            if best_next is None:
                break
            path.append(best_next)
            visited |= (1 << best_next)
            pos = best_next

        return path

    best_path_indices = reconstruct(best_start)
    path_ids = [node_ids[i] for i in best_path_indices]
    return path_ids, len(path_ids), best_distance