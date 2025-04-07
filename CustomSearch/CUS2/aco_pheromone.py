from typing import Mapping, Tuple
from utils import Graph


# Refer to aco.py for documentation

class PheromoneGraph(object):
    def __init__(self, graph: Graph):
        # The default pheromone is 1 for all edges
        self.pheromone = {node: {neighbour: 1 for neighbour in graph.adj_list[node]} for node in graph.adj_list.keys()}

        # The shorter path is more attractive (1 / dist)
        self.visibility = {node: {neighbour: 1 / dist for neighbour, dist in neighbours.items()} for node, neighbours in graph.adj_list.items()}


    # The ant path will look like this:
    # Node: (Parent, Distance)

    # Add pheromone to the ant path
    def add_pheromone(self, goal: str, path: Mapping[str, Tuple[str, float]], pheromone_intensity: float):
        path_distance = self.path_length(goal, path)
        if path_distance == 0: return

        cur_node = goal
        while path[cur_node][0] != cur_node: # Keep iterating the path until it reaches the source node
            prev_node = path[cur_node][0]
            self.pheromone[prev_node][cur_node] += pheromone_intensity / path_distance
            cur_node = prev_node

    # Evaporate pheromone to all paths
    def evaporate_pheromone(self, evaporate_rate: float):
        for cur_node in self.pheromone:
            for neighbor in self.pheromone[cur_node]:
                self.pheromone[cur_node][neighbor] *= (1 - evaporate_rate)


    @staticmethod
    def path_length(goal: str, path: Mapping[str, Tuple[str, float]]) -> float:
        cur_node = goal
        length = 0
        while path[cur_node][0] != cur_node: # Keep iterating the path until it reaches the source node
            length += path[cur_node][1]
            cur_node = path[cur_node][0]

        return length
