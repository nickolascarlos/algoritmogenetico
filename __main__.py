from genetics import *
import statistics

if __name__ == '__main__':
    # Gera população inicial
    population = [generate_solution() for _ in range(0, 40)]

    for i in range(0, 10000):
        print('Geração #%d: [MÉDIA: %f]' % (i, statistics.mean([solution_fitness(x) for x in population])))
        print('\t', end='')
        print([solution_to_humans(x) for x in population])
        print()
        print()
        population = generate_next_population(population, 10)