class Cell:
    def __init__(self, letter, number):
        self.letter_index = ord(letter) - 97
        self.number_index = number - 1

    @classmethod
    def create_valid_cells(cls, letter, number):
        if "a" <= letter <= "j" and 1 <= number <= 10:
            return cls(letter, number)
        else:
            print("Invalid cell. Coordinates are out of borders.")
            return None
