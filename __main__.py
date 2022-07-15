from genetics import *
import statistics

if __name__ == '__main__':
    # Teste
    # solucao = "10000000000000000000001000000000000000000000"
    # print(solution_fitness(solucao))
    # print(solution_to_humans(solucao))

    # exit(0)
    # Gera população inicial
    population = [generate_solution() for _ in range(0, 40)]

    for i in range(0, 1000):
        print('Geração #%d: [MÉDIA: %f]' % (i, statistics.mean([solution_fitness(x) for x in population])))
        # print('\t', end='')
        # print([solution_to_humans(x) for x in population])
        # print()
        # print()
        population = generate_next_population(population, 40)
