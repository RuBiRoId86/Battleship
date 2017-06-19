from battlemap import BattleMap
from cell import Cell

class Dashboard:

    def __init__(self, username):
        self.myMap = BattleMap()
        self.rivalMap = BattleMap()
        self.username = username

    def shoot(self, other_user, target_cell):
        change_turn = False
        if self.rivalMap.get_cell_value(target_cell) is None:
            self.rivalMap.set_cell_value(target_cell, other_user.myMap.get_cell_value(target_cell))
            if self.rivalMap.get_cell_value(target_cell) == 0:
                change_turn = True
                print("{name}, your shot missed the targets" .format(name=self.username))
            elif self.rivalMap.get_cell_value(target_cell) == 1:
                for i in range(target_cell.letter_index - 1, target_cell.letter_index + 2):
                    for j in range(target_cell.number_index - 1, target_cell.number_index + 2):
                        if Cell.cell_coordinates_are_valid(i, j):
                            neighbour_cell = Cell.create_cell_from_indexes(i, j)
                            if neighbour_cell != target_cell and other_user.myMap.get_cell_value(neighbour_cell) == 1:
                                if self.rivalMap.get_cell_value(neighbour_cell) is None:
                                    print("{name}, your shot was on target, but the ship is still alive." .format(name=self.username))
                                else:
                                    print("{name}, your shot was on target and the ship is destroyed." .format(name=self.username))
        elif self.rivalMap.get_cell_value(target_cell) == 1:
            print("Choose a better target. A strict shot has been already made on this cell.")
        elif self.rivalMap.get_cell_value(target_cell) == 0:
            print("Choose a better target. A miss has been already made on this cell.")
        else:
            print("Invalid target cell value.")

        return change_turn