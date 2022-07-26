import random
import statistics
import genetics

# Função para calcular x, y a partir
# da solução (string)
def solution_x_y(solution):
    x = int(solution[0:22], 2) 
    x *= 200/(2**22 - 1)
    x -= 100

    y = int(solution[22:44], 2)
    y *= 200/(2**22 - 1)
    y -= 100

    return x, y

# Função geradora de soluções aleatórias
def generate_random_solution():
    bits = ''
    for _ in range(0, 44):
        bits += '0' if random.random() > 0.5 else '1'
    return bits

# Função que retorna a melhor solução de uma população
def best_solution(population):
    best = population[0]

    for solution in population[1:]:
        if genetics.solution_fitness(solution) > genetics.solution_fitness(best):
            best = solution

    return best

# Função que retorna a pior solução de uma população
def worst_solution(population):
    worst = population[0]

    for solution in population[1:]:
        if genetics.solution_fitness(solution) < genetics.solution_fitness(worst):
            worst = solution

    return worst

def print_generation(i, population, options):
    print("Geração #%d:\n" % i)

    if options['print_generation_fitness_mean'] or options['print_generation_best_fitness'] or options['print_generation_worst_fitness']:
        print('\tAptidão: %s %s %s\n' % (
            "[Média: %f]" % (statistics.mean([genetics.solution_fitness(x) for x in population])) if options['print_generation_fitness_mean'] else "",
            "[Melhor: %f]" % (genetics.solution_fitness(best_solution(population))) if options['print_generation_best_fitness'] else "",
            "[Pior: %f]" % (genetics.solution_fitness(worst_solution(population))) if options['print_generation_worst_fitness'] else "",
        ))

    if options['print_best_solution']:
        print("\tMelhor solução:")
        best = best_solution(population)
        print("\t\t%s" % str(solution_x_y(best)))
        # print("\t\t%s" % best)
        if not options['print_generation_best_fitness']:
            print("\t\tAptidão: %s" % genetics.solution_fitness(best))
        print()
    
    if options['print_worst_solution']:
        print("\tPior solução:")
        worst = worst_solution(population)
        print("\t\t%s" % str(solution_x_y(worst)))
        # print("\t\t%s" % worst)
        if not options['print_generation_worst_fitness']:
            print("\t\tAptidão: %s" % genetics.solution_fitness(worst))
        print()

    if options['print_all_population']:
        print("\tIndivíduos: ")
        print([solution_x_y(p) for p in population])
        print()
    
    print('\n\n')