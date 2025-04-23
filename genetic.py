import random

def create_population(size, length):
    return [[random.randint(0, 5) for _ in range(length)] for _ in range(size)]

def fitness(individual):
    return sum(individual)

def select_parents(population):
    return sorted(population, key=fitness, reverse=True)[:2]

def crossover(parent1, parent2):
    return parent1[:3] + parent2[3:]

def mutate(individual):
    if random.random() < 0.1:
        individual[random.randint(0, len(individual) - 1)] ^= 1 # flip bit
        
def genetic_algorithm():
    population = create_population(10, 5)
    for gen in range(5): # 5 generations
        print(f"Generation {gen + 1}: {population}")
        parent1, parent2 = select_parents(population)
        child = crossover(parent1, parent2)
        mutate(child)
        population.append(child)
        population = sorted(population, key=fitness, reverse=True)[:10] # keep top 10
    best = max(population, key=fitness)
    print("Best individual:", best, "Fitness:", fitness(best))
# Example usage
genetic_algorithm()