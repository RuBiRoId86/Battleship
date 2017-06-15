import re
from cell_with_new import Cell
from ship_with_new import Ship

class BattleMap:
    "A field with 10x10 cells. Separate instances can be used for positioning of both own and an enemy's ships."

    def __init__(self):
        field_side_length_in_cells = 10
        self.map = [[None for x in range(field_side_length_in_cells)] for y in range(field_side_length_in_cells)]

    def disposition_of_all_ships(self):
        self.dispose_ship(4)

        self.dispose_ship(3)
        self.dispose_ship(3)

        self.dispose_ship(2)
        self.dispose_ship(2)
        self.dispose_ship(2)

        self.dispose_ship(1)
        self.dispose_ship(1)
        self.dispose_ship(1)
        self.dispose_ship(1)

        self.mark_remaining_cells_as_free()

    def dispose_ship(self, ship_length):
        cells_are_free = False
        while cells_are_free is False:
            ship = self.ship_construction(ship_length)
            cells_are_free = self.cells_are_free(ship)
            if cells_are_free is False:
                print("There is no room for the ship in the battlemap. Try to place the ship into other coordinates.")
        for cell in ship.cell_tuple:
            self.set_cell_value(cell, 1)
            print("mark ship cell as 1")
        self.__force_neighbour_cells_to_be_free(ship)
        print("The ship is disposed on the battle map.")

    @staticmethod
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

        print("The", ship_length, "cell", Ship.ship_types[ship_length], "is constructed.")

        return ship

    def cells_are_free(self, ship):
        cells_are_free = True
        for cell in ship.cell_tuple:
            if self.get_cell_value(cell) is not None:
                cells_are_free = False
                print("used cell found")
                break
        return cells_are_free

    def __force_neighbour_cells_to_be_free(self, ship):
        for ship_cell in ship.cell_tuple:
            for i in range(getattr(ship_cell, "letter_index") - 1, getattr(ship_cell, "letter_index") + 2):
                for j in range(getattr(ship_cell, "number_index") - 1, getattr(ship_cell, "number_index") + 2):
                    print("i = ", i, "j = ", j)
                    if Cell.cell_coordinates_are_valid(i, j):
                        neighbour_cell = Cell(chr(i + 97), j + 1)
                        if neighbour_cell is not None:
                            print("neighbour_cell.letter_index = ", neighbour_cell.letter_index)
                            print("neighbour_cell.number_index = ", neighbour_cell.number_index)
                            if self.get_cell_value(neighbour_cell) is None:
                                self.set_cell_value(neighbour_cell, 0)
                                print("neighbour_cell marked as 0")

    def set_cell_value(self, cell, value):

        if value == 0 or value == 1 or value is None:
            letter_index = cell.letter_index
            number_index = cell.number_index
            self.map[letter_index][number_index] = value
        else:
            print("Value is invalid. Should be either 0, 1 or None.")

    def get_cell_value(self, cell):
        try:
            return self.map[cell.letter_index][cell.number_index]
        except IndexError:
            print ("The coodrinates are incorrect.")

    def mark_remaining_cells_as_free(self):
        for i in range(10):
            for j in range(10):
                cell = Cell(chr(i + 97), j + 1)
                if self.get_cell_value(cell) is None:
                    self.set_cell_value(cell, 0)
