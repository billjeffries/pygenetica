"""
    Crossover operators take 2 parent gene lists and return two child gene lists

    Input: 2 lists
    Output: 2 lists

"""
import random


"""
    Base class, not to be used

"""
class CrossOver:
    def recombine(self, list_1, list_2):
        return list_1, list_2


"""
    OnePointCrossover:
    - swaps list elements to right of randomized crossover point

"""
class OnePointCrossover(CrossOver):
    def recombine(self, list_1, list_2):
        # determine crossover point
        max = len(list_1)
        crossover_point = random.randint(1, max-1)

        # perform crossover
        child_1 = list_1[0:crossover_point] + list_2[crossover_point:]
        child_2 = list_2[0:crossover_point] + list_1[crossover_point:]

        return child_1, child_2

