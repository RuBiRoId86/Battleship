import re
from cell import Cell
from ship import Ship
from GUI.main_gui5.main_GUI5_wrapper import BattleShipGUI

class BattleMap:
    "A field with 10x10 cells. Separate instances can be used for positioning of both own and an enemy's ships."

    ship_counter = 0

    def __init__(self):
        field_side_length_in_cells = 10
        self.map = [[None for x in range(field_side_length_in_cells)] for y in range(field_side_length_in_cells)]

    def disposition_of_all_ships(self):
        self.dispose_ship(4)

        # self.dispose_ship(3)
        # self.dispose_ship(3)
        #
        # self.dispose_ship(2)
        # self.dispose_ship(2)
        # self.dispose_ship(2)
        #
        # self.dispose_ship(1)
        # self.dispose_ship(1)
        # self.dispose_ship(1)
        self.dispose_ship(1)

        self.mark_remaining_cells_as_free()

    def force_neighbour_cells_to_be_free(self, ship):
        for ship_cell in ship.cell_tuple:
            for i in range(getattr(ship_cell, "letter_index") - 1, getattr(ship_cell, "letter_index") + 2):
                for j in range(getattr(ship_cell, "number_index") - 1, getattr(ship_cell, "number_index") + 2):
                    #                    print("i = ", i, "j = ", j)
                    if Cell.cell_coordinates_are_valid(i, j):
                        neighbour_cell = Cell(chr(i + 97), j + 1)
                        if neighbour_cell is not None:
                            #                            print("neighbour_cell.letter_index = ", neighbour_cell.letter_index)
                            #                            print("neighbour_cell.number_index = ", neighbour_cell.number_index)
                            if self.get_cell_value(neighbour_cell) is None:
                                self.set_cell_value(neighbour_cell, 0)
#                               print("neighbour_cell marked as 0")

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
