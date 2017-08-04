import re
class Cell:
    def __new__(cls, letter, number):
        if "a" <= letter <= "j" and 1 <= number <= 10:
            self = super(Cell, cls).__new__(cls)
            self.letter_index = ord(letter) - 97
            self.number_index = number - 1
            return self
        else:
            print("Invalid cell. Coordinates are out of borders.")

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @classmethod
    def create_cell_from_indexes(cls, letter_index, number_index):
        if Cell.cell_coordinates_are_valid(letter_index, number_index):
            self = super(Cell, cls).__new__(cls)
            self.letter_index = letter_index
            self.number_index = number_index
            return self
        else:
            print("Invalid cell. Coordinates are out of borders.")

    @staticmethod
    def cell_coordinates_are_valid(letter_index, number_index):
        if 0 <= letter_index <= 9 and 0 <= number_index <= 9:
            return True
        else:
            return False

    @classmethod
    def cell_input(cls):
        while True:
            coordinate = input("Input coordinate: ")

            if re.match("^[a-j]([1-9]|10)$", coordinate):
                letter = coordinate[0]
                number = int(coordinate[1:])
                return cls(letter, number)
            else:
                print("Invalid coordinates. Try again.")
                continue

    cell_constuctor_iterator = 0

    @classmethod
    def cell_gui_input(cls, gui):
        gui.buttonGroup.buttonClicked.connect(lambda object: cls.cell_gui_input_slot(gui, object))

    @staticmethod
    def cell_gui_input_slot(gui, object):
        position = gui.gridLayout.getItemPosition(gui.gridLayout.indexOf(object))
        created_cell = Cell.create_cell_from_indexes(position[0] - 1, position[1] - 1)
        print(created_cell.letter_index, created_cell.number_index)
        gui.buttonGroup.buttonClicked.disconnect()
        Cell.cell_constuctor_iterator += 1
