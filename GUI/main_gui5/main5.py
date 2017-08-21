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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = mainGUI()
    ui.setupUi(Window)
    ui.start_FSM()
    Window.show()
    sys.exit(app.exec_())
