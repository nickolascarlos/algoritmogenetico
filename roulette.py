import random
import genetics

# Função auxiliar para calcular a tabela usada
# no algoritmo da roleta
def generate_roulette_table(population):
    accumulator = 0
    table = []
    
    for s in population:
        accumulator += genetics.solution_fitness(s)
        table.append((s, accumulator))
        
    return table

# Função para escolha de pais
def choose_random_parent(population, roulette_table = None):
    roulette_association = generate_roulette_table(population) if not roulette_table else roulette_table
    random_number = random.uniform(0, max([y for _, y in roulette_association]))
    
    for s, a in roulette_association:
        if  random_number < a:
            return s