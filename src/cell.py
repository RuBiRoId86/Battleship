class Cell:
    def __init__(self, letter, number):
        self.letter_index = ord(letter)-97
        self.number_index = number - 1
