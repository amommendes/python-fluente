import copy
from design_patterns.prototype.cells.cell import Cell, Cloner

if __name__ == "__main__":
    mitochondria = ["mitochondria"]
    ribosomes = [{10}]
    cell = Cell()
    cloner = Cloner(mitochondria, ribosomes, cell)
    cell.set_parent(cloner)
    new_cell = copy.copy(cloner)

    # The new cell DNA was changed, more ribosomes were produced
    new_cell.ribosomes.append(2)

    if cloner.ribosomes[-1] == 2:
        print("The change in the DNA of new cell, affect the cloner itself")

    # The cloner genetically modified the cell, adding more ribosomes

    cloner.ribosomes[0].add(4)
    if 4 in new_cell.ribosomes[0]:
        print("Cloner succeed in modifying the clone")

    # Cloning the cloner (deepcopy)
    deep_clone_cell = copy.deepcopy(cloner)
    deep_clone_cell.mitochondria.append("modified")

    if cloner.mitochondria == ["mitochondria", "modified"]:
        print("The deepclone mdified the parent mitochondria")

    # Changing original cell
    cell.parent.ribosomes[0].add(12)
    if 12 in new_cell.ribosomes[0] and 12 in deep_clone_cell.ribosomes[0]:
        print("Changing original cell, changes child cells")


