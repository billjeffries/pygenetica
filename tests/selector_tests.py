import core.selectors as selector
import core.chromosome as chrom
import random


"""Test RankSelector

Create population of 100 individuals with random fitness levels
Verify that RankSelector selects the top 50

"""
def test_rank_selector():
    print("Testing RankSelector")
    # initialize population
    pop_size = 100
    population = []
    for p in range(pop_size):
        c = chrom.Chromosome(genes=[])
        fitness = random.randint(0, 100)
        c.fitness = fitness
        population.append(c)

    # get parents using RankSelector
    rank_selector = selector.RankSelector(threshold=50)
    parents = rank_selector.select_pairs(population=population)

    # verify 50 parents returned
    assert len(parents) == pop_size/2

    # verify top 50 returned
    population.sort(key=lambda x: x.fitness, reverse=True)
    fitness_threshold = population[int(pop_size/2)-1].fitness
    for p in parents:
        for c in p:
            assert c.fitness >= fitness_threshold
    print("RankSelector passed")

""" Test RouletteSelector
Create population of 100 individuals with random fitness levels

"""
def test_roulette_selector():
    print("Testing RouletteSelector")
    # initialize population
    pop_size = 100
    population = []
    for p in range(pop_size):
        c = chrom.Chromosome(genes=[])
        fitness = random.randint(0, 100)
        c.fitness = fitness
        population.append(c)

    # get parents using RouletteSelector
    rank_selector = selector.RouletteSelector()
    parents = rank_selector.select_pairs(population=population)

    # verify 50 parents returned
    assert len(parents) == pop_size/2

    print("RouletteSelector passed")


#test_rank_selector()
test_roulette_selector()