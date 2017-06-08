class BattleMap:
    "A field with 10x10 cells. Separate instances can be used for positioning of both own and an enemy's ships."

    def __init__(self):
        field_side_length_in_cells = 10
        self.map = [[0 for x in range(field_side_length_in_cells)] for y in range(field_side_length_in_cells)]

    def get_cell_value(self, letter, number):

        letter_code = ord(letter)
        letter_index = letter_code - 97

        number_index = number - 1

        result = 0

        try:
            result = self.map[letter_index][number_index]
        except IndexError:
            print ("The coodrinates are incorrect.")

        return result

