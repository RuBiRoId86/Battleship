from battlemap import BattleMap
from cell import Cell
bm = BattleMap()

cell1 = Cell("a", 7)

cell2 = Cell("b", 8)
print(bm.get_cell_value(cell1))

bm.set_cell_value(cell1, 1)

print(bm.get_cell_value(cell1))

print(bm.get_cell_value(cell2))

bm.mark_remaining_cells_as_free()

print(bm.get_cell_value(cell2))

print(bm.get_cell_value(cell1))
