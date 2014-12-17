pygenetica
==========

pygenetica is a genetic algorithms library.

The intent is to make the library as Pythonic and straightforward as possible.  Another goal is to make the library feel familiar to those with scikit-learn experience.

The library will do the heavy lifting in terms of randomizing populations, implementing selection operators, implementing crossover operators, and overall managing each generation until convergence.

But, as with all good Python machine learning libraries, you can also customize each component of the GA

###Usage###
- Define a Genotype, consisting of gene labels and possible values
- Implement a fitness function that the GA will use to evaluate each individual in population
- Create a GeneticAlgorithm object with Genotype and population size
- "Fit" the GeneticAlgorithm with settings for number of generations, selection operator, crossover operator, crossover rate, mutation rate, and your fitness function

