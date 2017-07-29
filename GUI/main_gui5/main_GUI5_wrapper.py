from GUI.main_gui5.main_gui5 import Ui_MainWindow
from GUI.main_gui5.cell import Cell
from GUI.main_gui5.dashboard import Dashboard
from GUI.main_gui5.battlemap import *
from PyQt5 import QtCore, QtWidgets
import sys

class BattleShipGUI(Ui_MainWindow):

    def setupUi(self, Window):
        Ui_MainWindow.setupUi(self, Window)

        self.Player1_name.clicked.connect(lambda: self.open_name_dialog(self.Player1_name))
        self.Player2_name.clicked.connect(lambda: self.open_name_dialog(self.Player2_name))

        self.buttonGroup.setExclusive(False)
        self.buttonGroup_2.setExclusive(False)

        # self.buttonGroup.buttonClicked.connect(lambda object: self.cell_clicked_slot(object))

        # Menu items
        self.actionExit.setShortcut("Alt+F4")
        self.actionExit.triggered.connect(lambda: sys.exit())
        self.actionAbout_us.triggered.connect(lambda: self.show_help())

        self.start_FSM()


    def retranslateUi(self, Window):
        Ui_MainWindow.retranslateUi(self, Window)
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "BattleShip"))

    def user_dashboard_initialization(self):
        self.user1 = Dashboard(self.Player1_name.text())
        self.user2 = Dashboard(self.Player2_name.text())

    def cell_clicked_slot(self, cell):
        if isinstance(cell, QtWidgets.QCheckBox):

            # user1.myMap.disposition_of_all_ships()
            # print("{name}, you ships are disposed.".format(name=user1.username))

            print(self.gridLayout.getItemPosition(self.gridLayout.indexOf(cell)))
            position = self.gridLayout.getItemPosition(self.gridLayout.indexOf(cell))
            created_cell = Cell.create_cell_from_indexes(position[0]-1, position[1]-1)
            print(created_cell.letter_index, created_cell.number_index)
        elif isinstance(cell, int):
            print(cell)

    def open_name_dialog(self, buttonName):
        self.statusbar.showMessage("Set the new name of " + buttonName.text() + ".")
        name, ok = QtWidgets.QInputDialog.getText(None, buttonName.text(), "Enter your name...")
        if (ok and len(name) > 0):
            print("The name of", buttonName.text(), "is changed to", name)
            buttonName.setText(name)
            if buttonName == self.Player1_name:
                self.user1 = Dashboard(self.Player1_name.text())
                print(self.user1.username, " - ", self.user2.username)
            elif buttonName == self.Player2_name:
                self.user2 = Dashboard(self.Player2_name.text())
                print(self.user1.username, " - ", self.user2.username)


    def player_names_dialogs(self):
        buttons = (self.Player1_name, self.Player2_name)
        for button in buttons:
            self.open_name_dialog(button)

    def show_help(self):
        print("Show help.")
        QtWidgets.QMessageBox.information(None, "About us", """\
This application is developed by Ruben Sargsyan.
Contacts:
Email: ruben86@rambler.ru
Phone: 095461767""")


    def cell_gui_input(self):
        self.buttonGroup.buttonClicked.connect(lambda object: self.cell_clicked_slot(object))


    def start_FSM(self):

        #States
        self.initial_state = QtCore.QState()
        self.initial_state.assignProperty(self.centralwidget, "enabled", False)
        self.initial_state.entered.connect(lambda: print("initial_state"))
        self.initial_state.entered.connect(lambda: self.label.setStyleSheet("color : #555555;"))
        self.initial_state.entered.connect(lambda: self.statusbar.showMessage("To start the game press Game->Start."))
        self.initial_state.entered.connect(lambda: self.user_dashboard_initialization())
        self.initial_state.entered.connect(lambda: print(self.user1.username, " - ", self.user2.username ))

        self.set_player_names = QtCore.QState()
        self.set_player_names.entered.connect(lambda: print("set_player_names"))
        self.set_player_names.entered.connect(lambda: self.label.setStyleSheet("color : #5500FF;"))
        self.set_player_names.entered.connect(lambda: self.player_names_dialogs())

        self.start_playing = QtCore.QState()
        self.start_playing.entered.connect(lambda: print("start_playing"))
        self.start_playing.assignProperty(self.centralwidget, "enabled", True)
        for button in self.buttonGroup_2.buttons():
            self.start_playing.assignProperty(button, "enabled", False)
        self.start_playing.entered.connect(lambda: self.statusbar.showMessage("{player1}, start ship positioning." .format(player1=self.Player1_name.text())))
        self.start_playing.entered.connect(lambda: self.cell_gui_input())

        # self.start_playing.entered.connect(lambda: print("Position of checkbox is", self.gridLayout.getItemPosition(self.gridLayout.indexOf(self.checkBox_3))[0]))


        #Transitions
        self.initial_state.addTransition(self.actionStart.triggered, self.set_player_names)
        self.set_player_names.addTransition(self.set_player_names.entered, self.start_playing)

        #State Machine
        self.fsm = QtCore.QStateMachine()

        self.fsm.addState(self.initial_state)
        self.fsm.addState(self.set_player_names)
        self.fsm.addState(self.start_playing)

        self.fsm.setInitialState(self.initial_state)

        self.fsm.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = BattleShipGUI()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
