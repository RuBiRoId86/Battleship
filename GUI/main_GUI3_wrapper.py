from GUI.main_gui3 import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets

class BattleShipGUI(Ui_MainWindow):

    def setupUi(self, Window):
        Ui_MainWindow.setupUi(self, Window)

        self.Player1_name.clicked.connect(lambda: self.open_name_dialog(self.Player1_name))
        self.Player2_name.clicked.connect(lambda: self.open_name_dialog(self.Player2_name))

        self.statusbar.showMessage("Hello World!!!")

    def retranslateUi(self, Window):
        Ui_MainWindow.retranslateUi(self, Window)
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "BattleShip"))

    def open_name_dialog(self, buttonName):
        name, ok = QtWidgets.QInputDialog.getText(None, "Name", "Enter your name...")
        if ok:
            buttonName.setText(name)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = BattleShipGUI()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())
