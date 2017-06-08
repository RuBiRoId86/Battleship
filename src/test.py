from cell import Cell
from ship import Ship

c0 = Cell('a', 1)
c1 = Cell('b', 1)
c2 = Cell('c', 1)
c3 = Cell('d', 1)
c4 = Cell('e', 1)

# c0 = Cell('b', 6)
# c1 = Cell('b', 5)
# c2 = Cell('b', 4)


cell_tuple = (c1, c0, c2, c3)

ship1 = Ship(cell_tuple)
#print(getattr(ship1.cell_tuple[2], "number_index"))

# a = []
# a.append(3)
# a.append(6)
# a.append(9)
#
# print(a)