import re
from cell import Cell
from ship import Ship
from PyQt5 import QtCore, QtWidgets
from time import sleep

from GUI.main_gui5.main_GUI5_wrapper import BattleShipGUI

class BattleMap:
    "A field with 10x10 cells. Separate instances can be used for positioning of both own and an enemy's ships."

    ship_counter = 0

    gui = None

    @classmethod
    def set_gui(cls, gui_object):
        cls.gui = gui_object

    def __init__(self, gui_object):
        field_side_length_in_cells = 10
        self.map = [[None for x in range(field_side_length_in_cells)] for y in range(field_side_length_in_cells)]
        self.set_gui(gui_object)

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

    def dispose_ship(self, ship_length):
        print("Ship disposition")
        cells_are_free = False
        while cells_are_free is False:
            ship = self.ship_construction(ship_length)
            cells_are_free = self.cells_are_free(ship)
            if cells_are_free is False:
                print("There is no room for the ship in the battlemap. Try to place the ship into other coordinates.")
        for cell in ship.cell_tuple:
            self.set_cell_value(cell, 1)
#            print("mark ship cell as 1")
        self.__force_neighbour_cells_to_be_free(ship)
        self.ship_counter += 1
        print("The ship is disposed on the battle map.")

    # @staticmethod
    # def ship_construction(ship_length):
    #     print("Position the", ship_length, "cell", Ship.ship_types[ship_length])
    #
    #     ship = None
    #     while ship is None:
    #         cell_list = []
    #         for c in range(ship_length):
    #             cell = None
    #             while cell is None:
    #                 coordinate = input("Input coordinate: ")
    #
    #                 if re.match("^[a-j]([1-9]|10)$", coordinate):
    #                     letter = coordinate[0]
    #                     number = int(coordinate[1:])
    #                 else:
    #                     print("Invalid coordinates. Try again.")
    #                     continue
    #
    #                 cell = Cell(letter, number)
    #             cell_list.append(cell)
    #         cell_tuple = tuple(cell_list)
    #         ship = Ship(cell_tuple)
    #
    #     print("The", ship_length, "cell", Ship.ship_types[ship_length], "is constructed.")
    #
    #     return ship


    # @staticmethod
    # def ship_construction(ship_length):
    #     print("Position the", ship_length, "cell", Ship.ship_types[ship_length])
    #
    #     ship = None
    #     while ship is None:
    #         cell_list = []
    #         for c in range(ship_length):
    #             cell = None
    #
    #             # position = BattleMap.gui.gridLayout.getItemPosition(BattleMap.gui.gridLayout.indexOf(cell))
    #             # created_cell = Cell.create_cell_from_indexes(position[0] - 1, position[1] - 1)
    #             cell_list.append(cell)
    #         cell_tuple = tuple(cell_list)
    #         ship = Ship(cell_tuple)
    #
    #     print("The", ship_length, "cell", Ship.ship_types[ship_length], "is constructed.")
    #
    #     return ship


    @staticmethod
    def ship_construction(gui, ship_length):
        print("hello ship_constructor")
        while (Cell.cell_constuctor_iterator < ship_length):
            # print(Cell.cell_constuctor_iterator)
            # Cell.cell_constuctor_iterator += 1
            Cell.cell_gui_input(gui)
            print(Cell.cell_constuctor_iterator)
            sleep(0.2)

        else:
            # print(Cell.cell_constuctor_iterator)
            Cell.cell_constuctor_iterator = 0
            print(Cell.cell_constuctor_iterator)
            # gui.buttonGroup.buttonClicked.connect(lambda object : BattleMap.ship_constructor_slot(gui, object))
    #
    # @staticmethod
    # def ship_constructor_slot(gui, object):
    #     position = gui.gridLayout.getItemPosition(gui.gridLayout.indexOf(object))
    #     created_cell = Cell.create_cell_from_indexes(position[0] - 1, position[1] - 1)
    #     print(created_cell.letter_index, created_cell.number_index)
    #     gui.buttonGroup.buttonClicked.disconnect()




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
#                    print("i = ", i, "j = ", j)
                    if Cell.cell_coordinates_are_valid(i, j):
                        neighbour_cell = Cell(chr(i + 97), j + 1)
                        if neighbour_cell is not None:
#                            print("neighbour_cell.letter_index = ", neighbour_cell.letter_index)
#                            print("neighbour_cell.number_index = ", neighbour_cell.number_index)
                            if self.get_cell_value(neighbour_cell) is None:
                                self.set_cell_value(neighbour_cell, 0)
#                                print("neighbour_cell marked as 0")

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
