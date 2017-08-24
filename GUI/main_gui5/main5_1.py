import sys
from dashboard import Dashboard
from battlemap import BattleMap
from ship import Ship
from cell import Cell
from GUI.main_gui5.main_GUI5_1_wrapper import BattleShipGUI
from PyQt5 import QtCore, QtWidgets

class BattleMapGUI(BattleMap):

    @staticmethod
    def ship_construction(ship_length, gui):
        print("Position the", ship_length, "cell", Ship.ship_types[ship_length])

        ship = None
        while ship is None:
            cell_list = []
            for c in range(ship_length):
                cell = None
                while cell is None:
                    # coordinate = input("Input coordinate: ")
                    #
                    # if re.match("^[a-j]([1-9]|10)$", coordinate):
                    #     letter = coordinate[0]
                    #     number = int(coordinate[1:])
                    # else:
                    #     print("Invalid coordinates. Try again.")
                    #     continue
                    # cell = Cell(letter, number)
                    print("AAAAAAAAAA")

                    gui.input_cell_gui()
                    print("BBBBBBBBBBBBB")
                    cell = gui.created_cell
                    # print(cell.letter_index, cell.number_index)

                # cell_list.append(cell)
            # cell_tuple = tuple(cell_list)
            # ship = Ship(cell_tuple)

        print("The", ship_length, "cell", Ship.ship_types[ship_length], "is constructed.")

        return ship

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
                self.user1.username = self.Player1_name.text()
            elif buttonName == self.Player2_name:
                self.user2.username = self.Player2_name.text()
            print(self.user1.username, " - ", self.user2.username)

    def cell_selection(self):
        self.buttonGroup.buttonClicked.connect(lambda object : self.cell_selection_slot(object))

    def cell_selection_slot(self, object):
        self.created_cell = Cell.gui_cell_input(self, object)
        print(self.created_cell.letter_index, self.created_cell.number_index)
        self.buttonGroup.disconnect()
        self.custom_signal.cell_created.emit()

    def ship_construction(self, length):
        BattleMapGUI.ship_construction(length, self)

    def input_cell_gui(self):
        print("Hello")
        self.input_cell_FSM()


    def input_cell_FSM(self):

        # States
        self.input_cell = QtCore.QState()
        self.input_cell.entered.connect(lambda: print("CCCCCCCCCCCCCC"))
        self.input_cell.entered.connect(lambda: self.cell_selection())
        self.input_cell.entered.connect(lambda: print("cell is inputted."))

        self.finalState = QtCore.QFinalState()
        self.finalState.entered.connect(lambda: print("Finish"))

        # Transitions
        self.input_cell.addTransition(self.custom_signal.cell_created, self.finalState)

        # State Machine
        self.cell_inputting = QtCore.QStateMachine()

        self.cell_inputting.addState(self.input_cell)
        self.cell_inputting.addState(self.finalState)

        self.cell_inputting.setInitialState(self.input_cell)

        self.cell_inputting.start()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = mainGUI()
    ui.setupUi(Window)
    ui.start_FSM()
    Window.show()
    sys.exit(app.exec_())
