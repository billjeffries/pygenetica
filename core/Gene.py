"""
    Gene represents a gene in a chromosome

    Properties:
        values = list of possible values for gene
"""


class Gene:
    def __init__(self, values):
        self._values = values

    @property
    def values(self):
        return self._values
