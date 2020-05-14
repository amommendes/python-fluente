import copy


class Cell:
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class Cloner:
    def __init__(self, mitochondria, ribosomes, cell):
        self.mitochondria = mitochondria
        self.ribosomes = ribosomes
        self.cell = cell

    def __copy__(self):
        ribosomes = copy.copy(self.ribosomes)
        cell = copy.copy(self.cell)

        new = self.__class__(self.mitochondria, ribosomes, cell)
        new.__dict__.update(self.__dict__)

        return new

    def __deepcopy__(self, memodict={}):
        ribosomes = copy.deepcopy(self.ribosomes, memodict)
        cell = copy.deepcopy(self.cell, memodict)

        new = self.__class__(self.mitochondria, ribosomes, cell)
        new.__dict__.update(self.__dict__)
        return new