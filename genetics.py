from math import sin, sqrt
import random

def F6(x, y):
    return 0.5 - (sin(sqrt(x**2 + y**2))**2 - 0.5)/(1 + 0.001*(x**2 + y**2))**2

def solution_fitness(solution):
    x = int(solution[0:22], 2)
    x *= 200/(2**22 - 1)
    x -= 100

    y = int(solution[22:44], 2)
    y *= 200/(2**22 - 1)
    y -= 100

    return F6(x, y)

def solution_to_humans(solution):
    x = int(solution[0:22], 2) 
    x *= 200/(2**22 - 1)
    x -= 100

    y = int(solution[22:44], 2)
    y *= 200/(2**22 - 1)
    y -= 100

    return (x, y)

def generate_solution():
    bits = ''
    for _ in range(0, 44):
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
        if  pivot < a:
            return s

def mutate(solution, factor):
    return ''.join([(('0' if c == '1' else '1') if random.random() < factor else c) for c in solution])

def reproduce(father, mother):
    # Crossover
    child1 = father[0:22] + mother[22:44]
    child2 = mother[0:22] + father[22:44]

    # Mutação
    child1 = mutate(child1, 0.0002)
    child2 = mutate(child2, 0.0002)

    return child1, child2

def best_solution(population):
    bs = population[0]
    for i in range(1, len(population)):
        if solution_fitness(population[i]) > solution_fitness(bs):
            bs = population[i]
    return bs

def generate_next_population(population, population_size):
    new_population = []
    for _ in range(0, population_size//2):
        father = roll_roullete(population)
        mother = roll_roullete(population)
        c1, c2 = reproduce(father, mother)
        new_population.append(c1)
        new_population.append(c2)

    new_population[random.randint(0, len(new_population) - 1)] = best_solution(population)

    return new_population
