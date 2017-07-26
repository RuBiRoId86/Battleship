from GUI.main_gui4.main_gui4 import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
import sys

class BattleShipGUI(Ui_MainWindow):

    def setupUi(self, Window):
        Ui_MainWindow.setupUi(self, Window)

        self.Player1_name.clicked.connect(lambda: self.open_name_dialog(self.Player1_name))
        self.Player2_name.clicked.connect(lambda: self.open_name_dialog(self.Player2_name))

        # Menu items
        # self.actionStart.triggered.connect(lambda: self.open_name_dialog(self.Player1_name))

        self.actionExit.setShortcut("Alt+F4")
        self.actionExit.triggered.connect(lambda: sys.exit())

        self.start_FSM()

    def retranslateUi(self, Window):
        Ui_MainWindow.retranslateUi(self, Window)
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "BattleShip"))

    def open_name_dialog(self, buttonName):
        name, ok = QtWidgets.QInputDialog.getText(None, "Name", "Enter your name...")
        if ok:
            buttonName.setText(name)

    def start_FSM(self):

        #States

        self.initial_state = QtCore.QState()
        self.initial_state.assignProperty(self.centralwidget, "enabled", False)
        self.initial_state.entered.connect(lambda: print("initial_state"))
        self.initial_state.entered.connect(lambda: self.label.setStyleSheet("color : #555555;"))

        # self.set_player_names = QtCore.QState()
        # self.set_player_names.entered.connect(lambda: self.label.setStyleSheet("color : #5500FF;"))
        # self.set_player_names.entered.connect(lambda: print("set_player_names"))


        # self.set_player1_name = QtCore.QState(self.set_player_names)
        self.set_player1_name = QtCore.QState()
        self.set_player1_name.entered.connect(lambda: print("set_player1_name"))
        self.set_player1_name.entered.connect(lambda: self.open_name_dialog(self.Player1_name))


        # self.set_player_names.setInitialState(self.set_player1_name)

        # self.set_player2_name = QtCore.QFinalState(self.set_player_names)
        self.set_player2_name = QtCore.QState()
        self.set_player2_name.entered.connect(lambda: print("set_player2_name"))
        self.set_player2_name.entered.connect(lambda: self.open_name_dialog(self.Player2_name))

        self.start_playing = QtCore.QState()
        self.start_playing.entered.connect(lambda: print("start_playing"))
        self.start_playing.assignProperty(self.centralwidget, "enabled", True)
        self.start_playing.entered.connect(lambda: self.statusbar.showMessage("Start ship positioning."))

        #Transitions
        # self.initial_state.addTransition(self.actionStart.triggered, self.set_player_names)
        self.initial_state.addTransition(self.actionStart.triggered, self.set_player1_name)
        # self.set_player_names.addTransition(self.set_player_names.entered, self.set_player1_name)
        self.set_player1_name.addTransition(self.set_player1_name.exited, self.set_player2_name)
        self.set_player2_name.addTransition(self.set_player2_name.exited, self.start_playing)

        #State Machine
        self.fsm = QtCore.QStateMachine()

        self.fsm.addState(self.initial_state)
        # self.fsm.addState(self.set_player_names)
        self.fsm.addState(self.set_player1_name)
        self.fsm.addState(self.set_player2_name)
        self.fsm.addState(self.start_playing)

        self.fsm.setInitialState(self.initial_state)

        self.fsm.start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = BattleShipGUI()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
