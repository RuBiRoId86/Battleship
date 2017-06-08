from cell import Cell

class BattleMap:
    "A field with 10x10 cells. Separate instances can be used for positioning of both own and an enemy's ships."

    def __init__(self):
        field_side_length_in_cells = 10
        self.map = [[None for x in range(field_side_length_in_cells)] for y in range(field_side_length_in_cells)]

    def get_cell_value(self, cell):

        try:
            return self.map[cell.letter_index][cell.number_index]
        except IndexError:
            print ("The coodrinates are incorrect.")

    def dispose_ships(self):
        pass



