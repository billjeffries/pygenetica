"""
    Genotype defines the structure of a chromosome

    Properties:
        labels: user friendly label for each gene
        values: possible values for each gene
        formatter: function that takes chromosome instance and returns a string
    Methods:
        describe: tuple with genotype info
        num_genes: # genes in genotype
        create_random_instance: creates chromosome with randomized gene values
        get_label: label from gene position
        get_pos: gene position from label
"""
import random
import core.chromosome as chrom


class Genotype:
    def __init__(self, labels, values):
        self._labels = labels
        self._values = values
        self._formatter = None

    @property
    def formatter(self):
        return self._formatter

    @formatter.setter
    def formatter(self, f_function):
        self._formatter = f_function

    def describe(self):
        description = (len(self._values), self._labels, self._values)
        return description

    def num_genes(self):
        return len(self._values)

    def create_random_instance(self):
        instance = []
        for v in self._values:
            num = len(v) - 1
            index = random.randint(0, num)
            gene_value = str(v[index])
            instance.append(gene_value)

        chromosome = chrom.Chromosome(genes=instance)
        return chromosome

    def print_instance(self, instance):
        c_string = ""
        if self._formatter is None:
            for gene in instance.genes:
                c_string += str(gene)
        else:
            c_string = self._formatter(instance)

        return c_string

    def get_label(self, pos):
        return self._labels[pos]

    def get_pos(self, label):
        index = self._labels.index(label)
        return index

