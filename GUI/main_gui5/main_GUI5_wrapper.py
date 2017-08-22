from GUI.main_gui5.main_gui5 import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
import sys

class CustomSignals(QtCore.QObject):
    cell_created = QtCore.pyqtSignal()

class BattleShipGUI(Ui_MainWindow):

    def setupUi(self, Window):
        Ui_MainWindow.setupUi(self, Window)

        self.Player1_name.clicked.connect(lambda: self.open_name_dialog(self.Player1_name))
        self.Player2_name.clicked.connect(lambda: self.open_name_dialog(self.Player2_name))

        self.buttonGroup.setExclusive(False)
        self.buttonGroup_2.setExclusive(False)

        # Menu items
        self.actionExit.setShortcut("Alt+F4")
        self.actionExit.triggered.connect(lambda: sys.exit())
        self.actionAbout_us.triggered.connect(lambda: self.show_help())

        # Signals
        self.custom_signal = CustomSignals()

        # Shortcuts
        self.end_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+E"), Window)

    def retranslateUi(self, Window):
        Ui_MainWindow.retranslateUi(self, Window)
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "BattleShip"))

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

    def cell_selection(self):
        pass

    def varify_ship_length(self, length):
        pass

    cell_counter = 0

    def ship_construction(self, length):
        pass

    def start_FSM(self):

        # States
        self.ParentStateToEnd = QtCore.QState()



        self.initial_state = QtCore.QState(self.ParentStateToEnd)
        self.initial_state.assignProperty(self.centralwidget, "enabled", False)
        self.initial_state.entered.connect(lambda: print("initial_state"))
        self.initial_state.entered.connect(lambda: self.label.setStyleSheet("color : #555555;"))
        self.initial_state.entered.connect(lambda: self.statusbar.showMessage("To start the game press Game->Start."))
        self.initial_state.entered.connect(lambda: print("Test"))
        self.initial_state.entered.connect(lambda: self.user_dashboard_initialization())
        self.initial_state.entered.connect(lambda: print(self.user1.username, " - ", self.user2.username ))

        self.ParentStateToEnd.setInitialState(self.initial_state)

        self.set_player_names = QtCore.QState(self.ParentStateToEnd)
        self.set_player_names.entered.connect(lambda: print("set_player_names"))
        self.set_player_names.entered.connect(lambda: self.label.setStyleSheet("color : #5500FF;"))
        self.set_player_names.entered.connect(lambda: self.player_names_dialogs())

        self.start_playing = QtCore.QState(self.ParentStateToEnd)
        self.start_playing.entered.connect(lambda: print("start_playing"))
        self.start_playing.assignProperty(self.centralwidget, "enabled", True)
        for button in self.buttonGroup_2.buttons():
            self.start_playing.assignProperty(button, "enabled", False)
        self.start_playing.entered.connect(lambda: self.statusbar.showMessage("{player1}, start ship positioning." .format(player1=self.Player1_name.text())))
        # self.start_playing.entered.connect(lambda: self.start_positioning_FSM())
        self.start_playing.entered.connect(lambda: self.ship_construction(4))

        self.end = QtCore.QState()
        self.end.assignProperty(self.centralwidget, "enabled", False)
        self.end.entered.connect(lambda: print("End of the game!!!"))
        self.end.entered.connect(lambda: self.label.setStyleSheet("color : #555555;"))
        self.end.entered.connect(lambda: self.statusbar.showMessage("Game Over!!!!!"))

        # Transitions
        self.initial_state.addTransition(self.actionStart.triggered, self.set_player_names)
        self.set_player_names.addTransition(self.set_player_names.entered, self.start_playing)
        self.ParentStateToEnd.addTransition(self.end_shortcut.activated, self.end)

        # State Machine
        self.fsm = QtCore.QStateMachine()

        self.fsm.addState(self.ParentStateToEnd)
        self.fsm.addState(self.initial_state)
        self.fsm.addState(self.set_player_names)
        self.fsm.addState(self.start_playing)
        self.fsm.addState(self.end)

        self.fsm.setInitialState(self.ParentStateToEnd)

        self.fsm.start()


    def ship_construction_FSM(self, length):

        self.cell_list = []

        # States
        self.input_cell = QtCore.QState()
        self.input_cell.entered.connect(lambda: print("cell is inputted."))
        self.input_cell.entered.connect(lambda: self.cell_selection())

        self.ship_length_varification = QtCore.QState()
        self.ship_length_varification.entered.connect(lambda: print("ship_length_varification."))
        self.ship_length_varification.entered.connect(lambda: self.varify_ship_length(length))

        # Transitions
        self.input_cell.addTransition(self.custom_signal.cell_created, self.ship_length_varification)
        self.ship_length_varification.addTransition(self.ship_length_varification.entered, self.input_cell)

        # State Machine
        self.positioning = QtCore.QStateMachine()

        self.positioning.addState(self.input_cell)
        self.positioning.addState(self.ship_length_varification)

        self.positioning.setInitialState(self.input_cell)

        self.positioning.start()
