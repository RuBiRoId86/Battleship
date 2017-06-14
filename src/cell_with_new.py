class Cell:
    def __new__(cls, letter, number):
        if "a" <= letter <= "j" and 1 <= number <= 10:
            self = super(Cell, cls).__new__(cls)
            self.letter_index = ord(letter) - 97
            self.number_index = number - 1
            print("A cell is valid.")
            return self
        else:
            print("Invalid cell. Coordinates are out of borders.")

    @staticmethod
    def cell_coordinates_are_valid(letter_index, number_index):
        if 0 <= letter_index <= 9 and 0 <= number_index <= 0:
            return True
        else:
            return False