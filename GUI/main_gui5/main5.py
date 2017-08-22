import sys
from dashboard import Dashboard
from battlemap import BattleMap
from ship import Ship
from cell import Cell
from GUI.main_gui5.main_GUI5_wrapper import BattleShipGUI
from PyQt5 import QtCore, QtWidgets

class mainGUI(BattleShipGUI):

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
                self.user1 = Dashboard(self.Player1_name.text())
            elif buttonName == self.Player2_name:
                self.user2 = Dashboard(self.Player2_name.text())
            print(self.user1.username, " - ", self.user2.username)

    def cell_selection(self):
        self.buttonGroup.buttonClicked.connect(lambda object : self.cell_selection_slot(object))

    def cell_selection_slot(self, object):
        created_cell = Cell.gui_cell_input(self, object)
        self.cell_list.append(created_cell)
        print(self.cell_list[-1].letter_index, self.cell_list[-1].number_index)
        self.buttonGroup.disconnect()
        self.custom_signal.cell_created.emit()


    def varify_ship_length(self, length):
        print("Varifying ship length.")
        if (len(self.cell_list) < length):
            print("There are", len(self.cell_list), "cells in the ship")
            pass
        else:
            print("The ship is constructed.")
            self.cell_list = []
            print("There are", len(self.cell_list), "cells in the ship")


    def ship_construction(self, length):
        self.ship_construction_FSM(length)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = mainGUI()
    ui.setupUi(Window)
    ui.start_FSM()
    Window.show()
    sys.exit(app.exec_())
