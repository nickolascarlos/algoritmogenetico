from genetics import *
import statistics
from utils import generate_random_solution, print_generation, worst_solution, best_solution

def main():

    options = {
        
        ## Parâmetros do algoritmo genético

        # Número de gerações
        "generations": 111000,

        # Tamanho da população por geração
        "population": 50,

        # Probabilidade mutação
        "mutation_probability": 0.002,



        ## Opções de saída

        # Imprimir todos os indivíduos da geração
        "print_all_population": False,

        # Imprimir a melhor solução da geração
        "print_best_solution": True,

        # Imprimir a pior solução da geração
        "print_worst_solution": True,

        # Imprimir a aptidão média
        "print_generation_fitness_mean": True,

        # Imprimir a melhor aptidão
        "print_generation_best_fitness": True,

        # Imprimir a pior aptidão
        "print_generation_worst_fitness": True,

        # Intervalo, em gerações, para impressão de detalhes
        "print_interval": 1000 # Imprime detalhes das gerações múltiplas de 1000
    }

    # Executa o algoritmo genético para a função F6
    run_genetic_algorithm(options)

def run_genetic_algorithm(options):
    # Gera população inicial
    population = [generate_random_solution() for _ in range(0, options['population'])]

    for i in range(0, options['generations']):

        # Imprime detalhes da geração a cada 'options['print_interval']'
        # gerações, incluindo a última
        if i % options['print_interval'] == 0 or i == options['generations'] - 1:
            print_generation(i, population, options)

        # Gera a próxima população
        population = generate_next_population(population, options['population'], options['mutation_probability'])

if __name__ == '__main__':
    main()