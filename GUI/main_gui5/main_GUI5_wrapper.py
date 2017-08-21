from GUI.main_gui5.main_gui5 import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
import sys

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

    def ship_positioning(self):
        pass


    def start_FSM(self):

        # States
        self.initial_state = QtCore.QState()
        self.initial_state.assignProperty(self.centralwidget, "enabled", False)
        self.initial_state.entered.connect(lambda: print("initial_state"))
        self.initial_state.entered.connect(lambda: self.label.setStyleSheet("color : #555555;"))
        self.initial_state.entered.connect(lambda: self.statusbar.showMessage("To start the game press Game->Start."))
        self.initial_state.entered.connect(lambda: print("Test"))
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
        self.start_playing.entered.connect(lambda: self.start_positioning_FSM())

        self.end = QtCore.QState()
        self.end.assignProperty(self.centralwidget, "enabled", False)
        self.end.entered.connect(lambda: print("End of the game!!!"))
        self.end.entered.connect(lambda: self.label.setStyleSheet("color : #555555;"))
        self.end.entered.connect(lambda: self.statusbar.showMessage("Game Over!!!!!"))

        # Transitions
        self.initial_state.addTransition(self.actionStart.triggered, self.set_player_names)
        self.set_player_names.addTransition(self.set_player_names.entered, self.start_playing)
        self.start_playing.addTransition(self.end_shortcut.activated, self.end)

        # State Machine
        self.fsm = QtCore.QStateMachine()

        self.fsm.addState(self.initial_state)
        self.fsm.addState(self.set_player_names)
        self.fsm.addState(self.start_playing)
        self.fsm.addState(self.end)

        self.fsm.setInitialState(self.initial_state)

        self.fsm.start()


    def start_positioning_FSM(self):

        # States
        self.input_cell = QtCore.QState()
        self.input_cell.entered.connect(lambda: print("cell is inputted."))
        self.input_cell.entered.connect(lambda: self.ship_positioning())

        self.check_ship = QtCore.QState()
        self.check_ship.entered.connect(lambda: print("check ship."))

        # Transitions
        self.input_cell.addTransition(self.buttonGroup.buttonClicked, self.check_ship)
        self.check_ship.addTransition(self.check_ship.entered, self.input_cell)

        # State Machine
        self.positioning = QtCore.QStateMachine()

        self.positioning.addState(self.input_cell)
        self.positioning.addState(self.check_ship)

        self.positioning.setInitialState(self.input_cell)

        self.positioning.start()
