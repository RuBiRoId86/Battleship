from GUI.main_gui3 import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
import sys

class BattleShipGUI(Ui_MainWindow):

    def setupUi(self, Window):
        Ui_MainWindow.setupUi(self, Window)

        self.Player1_name.clicked.connect(lambda: self.open_name_dialog(self.Player1_name))
        self.Player2_name.clicked.connect(lambda: self.open_name_dialog(self.Player2_name))

        # Create menu items
        self.printHello = QtWidgets.QAction("&Hello")
        self.printHello.setShortcut("Ctrl+P")
        self.printHello.setStatusTip("This will print \"Hello World!!!\"")
        self.printHello.triggered.connect(lambda: self.statusbar.showMessage("Hello World!"))

        self.startGame = QtWidgets.QAction('&Start')
        self.startGame.setShortcut("Alt+S")
        self.startGame.setStatusTip("Start the game.")
        # self.startGame.triggered.connect(self.start_FSM)
        self.startGame.triggered.connect(lambda: self.open_name_dialog(self.Player1_name))

        self.exitGame = QtWidgets.QAction("&Exit")
        self.exitGame.setShortcut("Alt+F4")
        self.exitGame.setStatusTip("Exit the game.")
        self.exitGame.triggered.connect(lambda: sys.exit())

        #Add menu ites to menu
        self.gameMenu = self.menubar.addMenu('&Game')
        self.gameMenu.addAction(self.startGame)
        self.gameMenu.addAction(self.exitGame)
        self.gameMenu.addAction(self.printHello)

    def retranslateUi(self, Window):
        Ui_MainWindow.retranslateUi(self, Window)
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "BattleShip"))

    def open_name_dialog(self, buttonName):
        name, ok = QtWidgets.QInputDialog.getText(None, "Name", "Enter your name...")
        if ok:
            buttonName.setText(name)

    def start_FSM(self):
        self.fsm = QtCore.QStateMachine()

        self.initial_state = QtCore.QState()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = BattleShipGUI()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
