import core.ga as ga
import core.genotype as gtype
import math
import numpy as np


def fitness_function(chromosome):
    x = 0
    for y in reversed(range(8)):
        if chromosome.genes[7-y] == '1':
                x += pow(2, y)
    y = math.sin(math.pi * (x / 256))
    return y

labels = ['8_bit', '7_bit', '6_bit', '5_bit', '4_bit', '3_bit', '2_bit', '1_bit']
values = [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]
genotype = gtype.Genotype(labels, values)
genetic_algorithm = ga.GeneticAlgorithm(population_size=20, genotype=genotype)

genetic_algorithm.fit(fitness_function=fitness_function, num_generations=5)
generations = genetic_algorithm.populations

for g in generations:
    fitness = []
    for chrom in g:
        fitness.append(chrom.fitness)
    print("Avg fitness = " + str(np.average(fitness)))
    print("Max fitness = " + str(np.max(fitness)))
    print("Fitness std = " + str(np.std(fitness)))
    print("\n")
