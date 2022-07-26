from math import sin, sqrt
import random
from utils import solution_x_y, best_solution
from roulette import choose_random_parent, generate_roulette_table

def F6(x, y):
    return 0.5 - (sin(sqrt(x**2 + y**2))**2 - 0.5)/(1 + 0.001*(x**2 + y**2))**2

# Função avaliadora
def solution_fitness(solution):
    x, y = solution_x_y(solution)
    return F6(x, y)

# Função de reprodução
def reproduce(father, mother, mutation_probability = 0.0002):
    # Crossover
    child1, child2 = crossover(father, mother)

    # Mutação
    child1 = mutate(child1, mutation_probability)
    child2 = mutate(child2, mutation_probability)

    return child1, child2

# Função para mutação de solução
def mutate(solution, probability):
    mutant_solution = list(solution)

    for i, c in enumerate(solution):
        if (random.random() < probability):
            mutant_solution[i] = '1' if c == '0' else '0'

    return ''.join(mutant_solution)

# Função de crossover
def crossover(father, mother):
    child1 = father[0:22] + mother[22:44]
    child2 = mother[0:22] + father[22:44]

    return child1, child2

# Função para gerar a próxima geração a partir da população atual
def generate_next_population(population, population_size, mutation_probability = 0.0002):
    new_population = []

    roulette_table = generate_roulette_table(population)

    for _ in range(0, population_size // 2):
        father = choose_random_parent(population, roulette_table)
        mother = choose_random_parent(population, roulette_table)

        c1, c2 = reproduce(father, mother, mutation_probability)

        new_population.extend((c1, c2))

    # Elimina aleatoriamente algum indivíduo da
    # nova geração e o substitui pelo melhor pai
    new_population[random.randint(0, len(new_population) - 1)] = best_solution(population)

    return new_population
