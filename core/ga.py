"""
    GeneticAlorithm operates over populations of chromosomes

    Properties:
        population_size: # chromosomes in populations
        genotype: structure of each chromosome
        generations: list of successive populations

    Methods:
        fit: runs the genetic algorithm, using selection, crossover, and mutation operations
"""
import core.selectors as sel
import core.crossover as xo
import core.chromosome as chrom
import random


class GeneticAlgorithm:
    def __init__(self, population_size, genotype):
        self._population_size = population_size
        self._genotype = genotype
        self._generations = []

    def fit(self, fitness_function, num_generations=10, selector=sel.RankSelector(threshold=10), crossover_op=xo.OnePointCrossover(), crossover_rate=.6, mutation_rate=.01):
        # initialize population
        population = []
        for x in range(self._population_size):
            chromosome = self._genotype.create_random_instance()
            population.append(chromosome)

        # process each generation
        for g in range(num_generations):
            # track generations
            self._generations.append(population)
            next_population = []

            # calculate fitness function
            for c in population:
                c.fitness = fitness_function(c)

            # select parents for next generation
            parents = selector.select_pairs(population=population)

            # perform crossover
            for parent in parents:
                do_crossover = random.random() < crossover_rate
                if do_crossover:
                    child_1, child_2 = crossover_op.recombine(parent[0].genes, parent[1].genes)
                    chrom_child_1 = chrom.Chromosome(genes=child_1)
                    chrom_child_2 = chrom.Chromosome(genes=child_2)

                    # add new children to next population
                    next_population.append(chrom_child_1)
                    next_population.append(chrom_child_2)
                else:
                    # no crossover, add parents as is
                    next_population.append(parent[0])
                    next_population.append(parent[1])

            # mutate

            population = next_population

    @property
    def populations(self):
        return self._generations