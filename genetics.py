from math import sin, sqrt
import random

def F6(x, y):
    return 0.5 - (sin(sqrt(x**2 + y**2))**2 - 0.5)/(1 + 0.001*(x**2 + y**2))**2

def solution_fitness(solution):
    x = int(solution[0:20], 2) * (200/(2**22 - 1))
    y = int(solution[20:40], 2) * (200/(2**22 - 1))
    return F6(x, y)

def solution_to_humans(solution):
    x = int(solution[0:20], 2) * (200/(2**22 - 1))
    y = int(solution[20:40], 2) * (200/(2**22 - 1))
    return (x, y)

def generate_solution():
    bits = ''
    for _ in range(0, 40):
        bits += '0' if random.random() > 0.5 else '1'
    return bits

def generate_roullete_association(population):
    accumulator = 0
    assoc = []
    for s in population:
        fitness = solution_fitness(s)
        assoc.append((s, accumulator + fitness))
        accumulator += fitness
    return assoc

def roll_roullete(population):
    roullete_association = generate_roullete_association(population)
    pivot = random.uniform(0, max([y for _, y in roullete_association]))
    for s, a in roullete_association:
        if pivot < a:
            return s

def mutate(solution, factor):
    return ''.join([(('0' if c == '1' else '1') if random.random() < factor else c) for c in solution])

def reproduce(father, mother):
    # Crossover
    child1 = father[0:20] + mother[20:40]
    child2 = mother[0:20] + father[20:40]

    # Mutação
    child1 = mutate(child1, 0.1)
    child2 = mutate(child2, 0.1)

    return child1, child2

def generate_next_population(population, population_size):
    new_population = []
    for _ in range(0, population_size//2):
        father = roll_roullete(population)
        mother = roll_roullete(population)
        c1, c2 = reproduce(father, mother)
        new_population.append(c1)
        new_population.append(c2)
    return new_population