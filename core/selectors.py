"""

    Selectors choose candidate parents from a given population

    input: population of chromosomes
    output: pairs of selected parent chromosomes

"""
import random

"""
    Base class, not to be used

"""
class SelectionOperator:
    def select_pairs(self, population):
        pass

"""
    RankSelector:
    - only selects parents with fitness rank above specified threshold

"""
class RankSelector(SelectionOperator):
    def __init__(self, threshold):
        self._threshold = threshold

    def select_pairs(self, population):
        pop_size = len(population)
        parent_size = pop_size / 2

        # sort population by rank
        population.sort(key=lambda x: x.fitness, reverse=True)

        # take individuals above threshold
        parent_pool = population[0:self._threshold]

        # pair off
        parents = []
        while len(parents) < parent_size:
            random_1 = random.randint(0, len(parent_pool)-1)
            random_2 = random.randint(0, len(parent_pool)-1)
            parent_1 = parent_pool[random_1]
            parent_2 = parent_pool[random_2]
            parents.append([parent_1, parent_2])

        return parents
