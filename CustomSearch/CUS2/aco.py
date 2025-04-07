from utils import Graph

# We will have Probability(node) = (pheromone^α) × (visibility^β)
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

class ACO(object):
    pheromone_power = 2 # or alpha
    visibility_power = 1 # or beta

    evaporation_rate = 0.3 # or p
    pheromone_intensity = 10 # or Q

    def __init__(self, graph: Graph):
        # The default pheromone is 1 for all edges
        self.pheromone = {node: {neighbour: 1 for neighbour in graph.adj_list[node]} for node in graph.adj_list.keys()}

        # The shorter path is more attractive (1 / dist)
        self.visibility = {node: [(neighbour, 1 / dist) for neighbour, dist in neighbours.items()] for node, neighbours in graph.adj_list.items()}
