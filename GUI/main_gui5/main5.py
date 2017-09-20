import sys
from dashboard import Dashboard
from battlemap import BattleMap
from ship import Ship
from cell import Cell
from GUI.main_gui5.main_GUI5_wrapper import BattleShipGUI
from PyQt5 import QtCore, QtWidgets
import traceback

class mainGUI(BattleShipGUI):

    current_ship = None

    def user_dashboard_initialization(self):
        Dashboard.set_gui(self)
        self.user1 = Dashboard(self.Player1_name.text())
        self.user2 = Dashboard(self.Player2_name.text())

    def open_name_dialog(self, buttonName):
        self.statusbar.showMessage("Set the new name of " + buttonName.text() + ".")
        name, ok = QtWidgets.QInputDialog.getText(None, buttonName.text(), "Enter your name...")
        if (ok and len(name) > 0):
            print("The name of", buttonName.text(), "is changed to", name)
            buttonName.setText(name)
            if buttonName == self.Player1_name:
                self.user1.username = self.Player1_name.text()
            elif buttonName == self.Player2_name:
                self.user2.username = self.Player2_name.text()
            print(self.user1.username, " - ", self.user2.username)

    def cell_selection(self):
        self.buttonGroup.buttonClicked.connect(lambda object : self.cell_selection_slot(object))

    def cell_selection_slot(self, object):
        created_cell = Cell.gui_cell_input(self, object)
        self.cell_list.append(created_cell)
        print(self.cell_list[-1].letter_index, self.cell_list[-1].number_index)
        self.buttonGroup.disconnect()
        self.custom_signal.cell_created.emit()

    def varify_ship(self):
        print("Varify")
        self.current_ship = Ship(self.cell_tuple)
        for c in self.current_ship.cell_tuple:
            print("Letter Index is", c.letter_index, " - ", "Number index is" , c.number_index)
            BattleMap.set_cell_value(self.user1.myMap, c, 1)
            print("mark ship cell as 1")
        print("Mark Neighbours!!!!!!!!!!!")
        BattleMap.force_neighbour_cells_to_be_free(self.user1.myMap, self.current_ship)
        print("Iterate Counters")
        BattleMap.ship_counter += 1
        print("The ship is disposed on the battle map.")
        print("Test::", self.user1.myMap.map)
        self.custom_signal.valid_ship.emit()
        print("ship_position signal emitted")

    def mark_remaining_cells_as_free(self, battlemap):
        print("Start marking all unmarked cells!!!!!!!!!!!")
        BattleMap.mark_remaining_cells_as_free(battlemap)
        print("End marking all unmarked cells!!!!!!!!!!!")
        self.custom_signal.all_ships_constructed.emit()
        print("all_ships_constructed signal emitted!!!")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = mainGUI()
    ui.setupUi(Window)
    ui.start_FSM()
    Window.show()
    sys.exit(app.exec_())
