from battle_map import BattleMap

class OwnBattleMap(BattleMap):

    def set_cell_value(self, letter, number, value):

        letter_code = ord(letter)
        letter_index = letter_code - 97

        number_index = number - 1

        self.map[letter_index][number_index] = value

        return