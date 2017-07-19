from GUI.main_gui2 import Ui_Form
from PyQt5 import QtCore, QtWidgets

class BattleShipGUI(Ui_Form):

    def setupUi(self, Form):
        Ui_Form.setupUi(self, Form)

        self.Player1_name.clicked.connect(lambda: self.open_name_dialog(self.Player1_name))
        self.Player2_name.clicked.connect(lambda: self.open_name_dialog(self.Player2_name))

    def retranslateUi(self, Form):
        Ui_Form.retranslateUi(self, Form)
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "BattleShip"))

    def open_name_dialog(self, buttonName):
        name, ok = QtWidgets.QInputDialog.getText(None, "Name", "Enter your name...")
        if ok:
            buttonName.setText(name)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = BattleShipGUI()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
