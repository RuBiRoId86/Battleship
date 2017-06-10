#from battle_map_with_cell import BattleMap
from cell_with_new import Cell
#obm = BattleMap()

#obm.set_cell_value("e", 3, 1)

cell = None

print("Start of input")
while not cell:
    letter = input("Input letter: ")
    number = int(input("Input number: "))
    cell = Cell(letter, number)

print("End of input")
print("The letter_index of the cell is: ", cell.letter_index)
print("The number_index of the cell is: ", cell.number_index)