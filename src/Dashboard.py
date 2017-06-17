from battlemap import BattleMap
from cell import Cell

class Dashboard:

    def __init__(self, username):
        self.myMap = BattleMap()
        self.rivalMap = BattleMap()
        self.username = username

    def shoot(self, other_user):
        while True:
            target_cell = Cell.cell_input()
            if self.rivalMap.get_cell_value(target_cell) is None:
                self.rivalMap.set_cell_value(target_cell, shooting_result = other_user.myMap.get_cell_value(target_cell))
                if self.rivalMap.get_cell_value(target_cell) == 0:
                    print("{name}, your shot missed the targets" .format(name=self.username))
                elif self.rivalMap.get_cell_value(target_cell) == 1:
                    print("{name}, your shot was on target" .format(name=self.username))
                return
            elif self.rivalMap.get_cell_value(target_cell) == 1:
                print("Choose a better target. A strict shot has been already made on this cell.")
            elif self.rivalMap.get_cell_value(target_cell) == 0:
                print("Choose a better target. A miss has been already made on this cell.")
            else:
                print("Invalid target cell value.")
