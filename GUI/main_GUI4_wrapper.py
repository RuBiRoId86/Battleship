from GUI.main_gui4 import Ui_MainWindow
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

        self.state2 = QtCore.QState()
        self.state2.assignProperty(self.centralwidget, "enabled", True)

        #Transitions
        self.initial_state.addTransition(self.actionStart.triggered, self.state2)

        #State Machine
        self.fsm = QtCore.QStateMachine()

        self.fsm.addState(self.initial_state)
        self.fsm.addState(self.state2)

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
