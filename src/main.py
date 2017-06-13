import re
#from battle_map_with_cell import BattleMap
from cell_with_new import Cell
from ship_with_new import Ship
#obm = BattleMap()

#obm.set_cell_value("e", 3, 1)



print("Start ship positioning.")
print("Position the 4 cell battleship.")

battleship1 = None
while battleship1 is None:
    cell_list = []
    for c in range(0,4):
        cell = None
        while cell is None:
            coordinate = input("Input coordinate: ")

            if re.match("^[a-j]([1-9]|10)$", coordinate):
                letter = coordinate[0]
                number = int(coordinate[1:])
            else:
                print("Invalid coordinates. Try again.")
                continue

            cell = Cell(letter, number)
        cell_list.append(cell)
    cell_tuple = tuple(cell_list)
    battleship1 = Ship(cell_tuple)

print("The 4 cell battleship is positioned.")
print("End of input")

print("length : ", len(cell_tuple))

for c in cell_tuple:
    print("The letter_index is: ", getattr(c, "letter_index"))
    print("The number_index is: ", getattr(c, "number_index"))