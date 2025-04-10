from utils import Graph, pythagoras, reconstruct_path
import heapq
from itertools import count

def astar(graph: Graph, root: str, goals: list):
    """
    A* is a best-first search algorithm that finds the shortest path from a start to a goal node
    It uses:
    - g(n) = cost from the start to node n
    - h(n) = heuristic estimate of cost from node n to the goal
    - f(n) = g(n) + h(n) = total estimated cost

    The algorithm works as follows:
    1. Setup frontier, heuristics and cost tracking
    2. Pop lowest f(n) cost node from the frontier
    3. Go back to step 2 if node is not using the best known total path cost
    4. Return the path if node is the goal
    5. Calculate estimated costs to go to each neighbour
    5.1. Update cost tracking for the neighbour if the new cost is lower than the old cost
    5.2. Push neighbour with the new cost onto the frontier
    6. Go back to step 2, until the frontier is empty
    """

    # Compute dictionary of euclidean distances, h(n)
    heuristic = pythagoras(graph, goals)

    # Setup frontier as priority queue
    frontier = []
    counter = count()   # Chronological tie-breaker when same f(n)
    heapq.heappush(frontier, (heuristic[root], root, next(counter)))

    prev = {root: None}       # Tracks current path

    # Cost from start to each node, g(n)
    path_sums = {node: float("inf") for node in graph.nodes}
    path_sums[root] = 0

    # Total cost, f(n) = g(n) + h(n)
    costs = {node: float("inf") for node in graph.nodes}
    costs[root] = heuristic[root]


    while frontier:
        current_cost, current_node, _ = heapq.heappop(frontier)

        # Stale checking
        # Since the node can get added to the frontier multiple times,
        # only the best cost path is evaluated.
        # Effectively acts as repeated state checking
        if current_cost > costs[current_node]:
            continue

        if current_node in goals:
            return reconstruct_path(current_node, prev)

        for neighbour, cost in graph.adj_list[current_node].items():
            potential_path_sum = path_sums[current_node] + cost

            # Update best known path to neighbour and push the neighbour onto the frontier
            if potential_path_sum < path_sums[neighbour]:
                prev[neighbour] = current_node
                path_sums[neighbour] = potential_path_sum
                costs[neighbour] = potential_path_sum + heuristic[neighbour]

                heapq.heappush(frontier, (costs[neighbour], neighbour, next(counter)))

    # If goal is not found
    print("AS: No valid path was found")
    return []