from battle_map_with_cell import BattleMap
from cell import Cell
obm = BattleMap()

#obm.set_cell_value("e", 3, 1)
cell = Cell('b', 8)
print(obm.get_cell_value(cell))
cell = Cell('c', 7)
print(obm.get_cell_value(cell))
cell = Cell('z', 15)
print(obm.get_cell_value(cell))
