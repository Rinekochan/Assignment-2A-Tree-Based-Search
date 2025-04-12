from CustomSearch.CUS2.aco_ant import Ant
from CustomSearch.CUS2.aco_pheromone import PheromoneGraph
from utils import Graph

# We will have Probability(path) = (pheromone^α) × (visibility^β)
# α is the power of pheromone to affect the probability
# β is the power of visibility to affect the probability (visibility is just the distance of the edges, the shorter it is, the higher the value)
# If a shorter path has a high probability, it will eventually choose that path overtime since its pheromone will keep increasing

# We have to customise our α β, we need to be careful about these values:
# If α is too high, a path might already being chosen over just a short time when the ants haven't even discovered the optimal path yet
# If α is too low, it will take a long time to search for the optimal path since higher pheromone doesn't contribute much to the probabilities
# If β is too high, of course it's just following greedy path blindly
# If β is too low, the search will take a long time since shorter distance doesn't contribute much to the probabilities

# We also have p, which is the evaporation values that will make the pheromone of other edges fades away (decreasing its pheromone values)
# And Q, the pheromone intensity indicates the rate that the chosen ant path is increasing

# Algorithm Structure:
# aco.py will be the main class of the algorithm that controls the ant and pheromone class
# aco_ant.py will be the ant of the ACO algorithm
# aco_pheromone.p will be the graph representation of the pheromone in the ACO algorithm

class ACO(object):

    def __init__(self, graph: Graph, pheromone_power = 2, visibility_power = 1, evaporation_rate = 0.3, pheromone_intensity = 10, nums_ants = 50, nums_iterations = 100):
        self.graph = graph

        self.pheromone_power = pheromone_power # or alpha
        self.visibility_power = visibility_power # or beta

        self.evaporation_rate = evaporation_rate # or p
        self.pheromone_intensity = pheromone_intensity # or Q

        self.nums_ants = nums_ants
        self.nums_iterations = nums_iterations

        self.pheromone_graph = PheromoneGraph(graph)

    def run(self, origin, destinations):
        current_goal = None
        best_path = None
        best_length = float('inf')

        for _ in range(self.nums_iterations):
            paths = []

            for _ in range(self.nums_ants):
                ant = Ant(self.graph, self.pheromone_graph, origin, destinations)
                path = ant.find_path(self.pheromone_power, self.visibility_power)
                for node in path.keys():
                    if node in destinations:
                        paths.append((node, path))

            self.pheromone_graph.evaporate_pheromone(self.evaporation_rate)

            for goal, path in paths:
                self.pheromone_graph.add_pheromone(goal, path, self.pheromone_intensity)
                length = self.pheromone_graph.path_length(goal, path)
                if length < best_length:
                    current_goal = goal
                    best_path = path
                    best_length = length

            if current_goal is None: return []

            return self.pheromone_graph.get_path_to_array(current_goal, best_path)