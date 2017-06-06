from own_battle_map import OwnBattleMap

obm = OwnBattleMap()

obm.set_cell_value("e", 3, 1)

print(obm.get_cell_value("e", 2))
print(obm.get_cell_value("e", 3))
