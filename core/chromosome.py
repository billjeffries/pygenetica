"""

    Chromosome represents an individual

    Properties:
        genes = list of gene values
        fitness = fitness score

"""


class Chromosome:
    def __init__(self, genes):
        self._genes = genes
        self._fitness = 0

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, fitness):
        self._fitness = fitness

    @property
    def genes(self):
        return self._genes


