from cell import Cell
from ship_with_new import Ship

c0 = Cell.create_valid_cells('a', 1)
c1 = Cell('b', 1)
c2 = Cell('c', 1)
c3 = Cell('d', 1)
c4 = Cell('e', 1)
c5 = Cell.create_valid_cells('m', 1)

# c0 = Cell('b', 6)
# c1 = Cell('b', 5)
# c2 = Cell('b', 4)


cell_tuple = (c1, c0, c2, c4)

ship1 = Ship(cell_tuple)
#print(getattr(ship1.cell_tuple[2], "number_index"))
#print(getattr(ship1.cell_tuple[2], "letter_index"))
print(ship1 is None)

# a = []
# a.append(3)
# a.append(6)
# a.append(9)
#
# print(a)

# if c5 is None:
#     print("There is no c5")
# else:
#     print("Hello c5")
# print(c5.letter_index)
# print(c5.number_index)

