from GUI.main_gui4.main_gui4 import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
import sys

class BattleShipGUI(Ui_MainWindow):

    def setupUi(self, Window):
        Ui_MainWindow.setupUi(self, Window)

        self.Player1_name.clicked.connect(lambda: self.open_name_dialog(self.Player1_name))
        self.Player2_name.clicked.connect(lambda: self.open_name_dialog(self.Player2_name))

        # Menu items
        self.actionExit.setShortcut("Alt+F4")
        self.actionExit.triggered.connect(lambda: sys.exit())
        self.actionAbout_us.triggered.connect(lambda: self.show_help())

        self.start_FSM()

    def retranslateUi(self, Window):
        Ui_MainWindow.retranslateUi(self, Window)
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "BattleShip"))

    def open_name_dialog(self, buttonName):
        self.statusbar.showMessage("Set the new name of " + buttonName.text() + ".")
        name, ok = QtWidgets.QInputDialog.getText(None, buttonName.text(), "Enter your name...")
        if (ok and len(name) > 0):
            print("The name of", buttonName.text(), "is changed to", name)
            buttonName.setText(name)

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


    def start_FSM(self):

        #States
        self.initial_state = QtCore.QState()
        self.initial_state.assignProperty(self.centralwidget, "enabled", False)
        self.initial_state.entered.connect(lambda: print("initial_state"))
        self.initial_state.entered.connect(lambda: self.label.setStyleSheet("color : #555555;"))
        self.initial_state.entered.connect(lambda: self.statusbar.showMessage("To start the game press Game->Start."))

        self.set_player_names = QtCore.QState()
        self.set_player_names.entered.connect(lambda: print("set_player_names"))
        self.set_player_names.entered.connect(lambda: self.label.setStyleSheet("color : #5500FF;"))
        self.set_player_names.entered.connect(lambda: self.player_names_dialogs())

        self.start_playing = QtCore.QState()
        self.start_playing.entered.connect(lambda: print("start_playing"))
        self.start_playing.assignProperty(self.centralwidget, "enabled", True)
        self.start_playing.entered.connect(lambda: self.statusbar.showMessage("Start ship positioning."))
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
