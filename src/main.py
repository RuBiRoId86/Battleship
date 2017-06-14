import re
from battle_map_with_cell import BattleMap
from cell_with_new import Cell
from ship_with_new import Ship

own_bm = BattleMap()

def ship_construction(ship_length):
    print("Position the", ship_length, "cell", Ship.ship_types[ship_length])

    ship = None
    while ship is None:
        cell_list = []
        for c in range(ship_length):
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
        ship = Ship(cell_tuple)
        own_bm.dispose_ship(ship)

    print("The", ship_length, "cell", Ship.ship_types[ship_length], "is positioned.")

    return ship


print("Start ship positioning.")
# battleship1 = ship_construction(4)
# cruiser1 = ship_construction(3)
# cruiser2 = ship_construction(3)
destroyer1 = ship_construction(2)
# destroyer2 = ship_construction(2)
# destroyer3 = ship_construction(2)
# submarine1 = ship_construction(1)
# submarine2 = ship_construction(1)
# submarine3 = ship_construction(1)
# submarine4 = ship_construction(1)

print("End of input")



print("length : ", len(getattr(destroyer1, "cell_tuple")))

for c in getattr(destroyer1, "cell_tuple"):
    print("The letter_index is: ", getattr(c, "letter_index"))
    print("The number_index is: ", getattr(c, "number_index"))