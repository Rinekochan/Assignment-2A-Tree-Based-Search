import random
from typing import Tuple, List

from Research.nearest_neighbor import nearest_neighbor
from Research.research_utils import euclidean

# Calculate the fitness (total distance) of a candidate route."""
def genetic_fitness(candidate: List[str], nodes: dict) -> float:
    total_distance = 0
    for i in range(1, len(candidate)):
        total_distance += euclidean(nodes[candidate[i]], nodes[candidate[i - 1]])
    return total_distance

# Select parents using ranking and tournament selection.
def genetic_selection(population: List[List[str]], elite_size: int, parents_size: int, nodes: dict) -> Tuple[List[List[str]], List[List[str]]]:
    # Calculate the fitness of all chromosomes
    fitness_pool = [(chromosome, genetic_fitness(chromosome, nodes)) for chromosome in population]

    # Sort the population based on fitness
    fitness_pool.sort(key=lambda x: x[1])

    # Use the elitist method to select best parents
    elite_parents = [chromosome for chromosome, _ in fitness_pool[:elite_size]]
    parents = elite_parents[:]

    visited = [False] * len(population)
    while len(parents) < parents_size:

        # Randomly select two individuals for tournament selection
        select_1 = random.randint(elite_size, len(population) - 1)
        select_2 = random.randint(elite_size, len(population) - 1)

        while select_2 == select_1: # Ensure we have two different chromosomes
            select_2 = random.randint(elite_size, len(population) - 1)

        # Calculate the fitness of these two new selected chromosomes
        select_1_fitness = genetic_fitness(population[select_1], nodes)
        select_2_fitness = genetic_fitness(population[select_2], nodes)

        # Compare two new select chromosome, and choose the better one
        if select_1_fitness < select_2_fitness and not visited[select_1]:
            parents.append(population[select_1])
            visited[select_1] = True
        elif not visited[select_2]:
            parents.append(population[select_2])
            visited[select_2] = True

    return parents, elite_parents

# We randomly swap two nodes in the path of a parent with a mutation rate
def genetic_mutation(offspring: List[str]) -> List[str]:
    rand_1, rand_2 = random.sample(range(len(offspring)), 2)
    offspring[rand_1], offspring[rand_2] = offspring[rand_2], offspring[rand_1]
    return offspring

# Perform two point crossover between pairs of parents to create offspring
def genetic_crossover(parents: List[List[str]], offspring_size: int, mutation_rate: float) -> List[List[str]]:
    offsprings = []
    visited = [[False] * len(parents) for _ in range(len(parents))]  # Track visited parent pairs

    while len(offsprings) < offspring_size:
        # Randomly select two distinct parents for crossover
        rand_1, rand_2 = random.sample(range(len(parents)), 2)

        while visited[rand_1][rand_2] or rand_1 == rand_2: # We won't continue if the parents already selected, or they are the same
            rand_1, rand_2 = random.sample(range(len(parents)), 2)

        parent_1, parent_2 = parents[rand_1], parents[rand_2]
        # Randomly select two crossover points
        rand_point_1, rand_point_2 = sorted(random.sample(range(1, len(parent_1) - 1), 2))

        # Create a crossover chromosome from parent_1's section between the crossover points
        crossover_chromosome = parent_1[rand_point_1:rand_point_2]


        # Create an offspring by combining non-contained elements from parent_2
        offspring = []
        for i in range(len(parent_2)):
            if parent_2[i] not in crossover_chromosome:
                offspring.append(parent_2[i])

        # Combine the sections from crossover of parent_1 and parent_2
        offspring = crossover_chromosome + offspring

        # Apply mutation with some probability based on mutation_rate
        if random.random() < mutation_rate:
            offspring = genetic_mutation(offspring)

        offsprings.append(offspring)
        visited[rand_1][rand_2] = True
        visited[rand_2][rand_1] = True

    return offsprings

# Evaluate the population and return the best path (shortest route) and its total cost (distance)
def genetic_evaluation(population: List[List[str]], nodes: dict) -> Tuple[List[str], float]:
    best_path = None
    best_cost = float('inf')

    for chromosome in population:
        cost = genetic_fitness(chromosome, nodes)
        if cost < best_cost:
            best_cost = cost
            best_path = chromosome

    return best_path, best_cost

def run(iterations: int = 100, population_size: int = 50, mutation_rate: int = 0.2, elite_size: int = 5, nodes: dict = {}):
    visited_nodes = 0
    population = [nearest_neighbor(nodes)[0]] # Add initial parent first

    # Fill up population
    node_labels = list(nodes.keys())
    while len(population) < population_size:
        candidate = node_labels[:]
        random.shuffle(candidate)
        if candidate not in population:
            population.append(candidate)

    parent_size = max(2, population_size // 4)

    for _ in range(iterations):
        parents, elite_parents = genetic_selection(population, elite_size, parent_size, nodes)
        offspring_size = population_size - len(elite_parents)
        offsprings = genetic_crossover(parents, offspring_size, mutation_rate)
        population = elite_parents + offsprings

    best_path, best_cost = genetic_evaluation(population, nodes)

    return best_path, visited_nodes, best_cost

def genetic_algorithm(nodes: dict[Tuple[int]]):
    return run(nodes = nodes)
