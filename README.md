pygenetica
==========

pygenetica is a genetic algorithms library.

The intent is to make the library as Pythonic and straightforward as possible.  Another goal is to make the library feel familiar to those with scikit-learn experience.

```
import core.ga as ga
import core.genotype as gtype
import math
import numpy as np

''' Define fitness function '''
def fitness_function(chromosome):
    x = 0
    for y in reversed(range(8)):
        if chromosome.genes[7-y] == '1':
                x += pow(2, y)
    y = math.sin(math.pi * (x / 256))
    return y

''' Define genotype
labels = ['8_bit', '7_bit', '6_bit', '5_bit', '4_bit', '3_bit', '2_bit', '1_bit']
values = [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]
genotype = gtype.Genotype(labels, values)

''' Configure genetic algorithm '''
genetic_algorithm = ga.GeneticAlgorithm(population_size=20, genotype=genotype)

''' Run genetic algorithm '''
genetic_algorithm.fit(fitness_function=fitness_function, num_generations=5)

''' Inspect generations
generations = genetic_algorithm.populations
```

