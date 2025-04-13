import random
from typing import List, Mapping, Tuple, Optional

from CustomSearch.CUS2.aco_pheromone import PheromoneGraph
from utils import Graph


# Refer to aco.py for documentation

class Ant(object):
    def __init__(self, graph: Graph, pheromone_graph: PheromoneGraph, origin: str, destinations: List[str]):
        self.graph = graph
        self.pheromone_graph = pheromone_graph
        self.origin = origin
        self.destinations = destinations
        self.visited = set()

    # Ant choose the next node based on probabilities
    def choose_next_node(self, cur_node: str, pheromone_power: float, visibility_power: float) -> Optional[str]:
        neighbours = self.pheromone_graph.pheromone[cur_node].keys()
        probabilities = []
        nodes = []

        for neighbour in neighbours:
            if neighbour in self.visited: continue

            # Apply the probability formula
            pheromone = self.pheromone_graph.pheromone[cur_node][neighbour] ** pheromone_power
            visibility = self.pheromone_graph.visibility[cur_node][neighbour] ** visibility_power

            probabilities.append(pheromone * visibility)
            nodes.append(neighbour)

        if not nodes: return None

        total = sum(probabilities)
        probabilities = [probability / total for probability in probabilities] # Distribute the probability within the same scale

        # Choose the next node based on probabilities
        return random.choices(nodes, probabilities)[0]

    # Run until the ant finds a destination
    # this method controls how an individual ant traverses the graph
    # from the origin until it either reaches a destination node or hits a dead end
    def find_path(self, pheromone_power: float, visibility_power: float) -> Mapping[str, Tuple[str, float]]:
        # The ant starts at the origin node, and initialises its path dictionary
        current = self.origin
        ant_path = {self.origin: (self.origin, 0)}
        self.visited.add(current)
        while current not in self.destinations:
            next_node = self.choose_next_node(current, pheromone_power, visibility_power)
            if next_node is None: break # Dead end

            # For each visited node:
            # - The node is added to the visited set
            # - An entry is added to the path dictionary,
            #   recording which node the ant came from and the distance between the current and next node
            self.visited.add(next_node)
            ant_path[next_node] = (current, self.graph.adj_list[current][next_node])
            current = next_node

        return ant_path