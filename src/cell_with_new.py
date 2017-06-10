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
