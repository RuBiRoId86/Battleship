from GUI.main_gui5.main_gui5 import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
import traceback
import sys

class CustomSignals(QtCore.QObject):
    cell_created = QtCore.pyqtSignal()
    need_more_cells = QtCore.pyqtSignal()
    enough_cells = QtCore.pyqtSignal()
    invalid_ship = QtCore.pyqtSignal()
    valid_ship = QtCore.pyqtSignal()
    ship_constructed = QtCore.pyqtSignal()
    ship_positioned = QtCore.pyqtSignal()
    all_ships_constructed = QtCore.pyqtSignal()

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

############### Methods for ship construction FSM ####################
    def varify_ship_length(self, length):
        print("Varifying ship length.")
        if (len(self.cell_list) < length):
            print("There are", len(self.cell_list), "cells in the ship")
            self.custom_signal.need_more_cells.emit()
        else:
            print("The ship is constructed. There are", len(self.cell_list), "cells in the ship.")
            self.cell_tuple = tuple(self.cell_list)
            self.cell_list = []
            print("cell_list is flushed. There are", len(self.cell_list), "cells in the ship")
            self.custom_signal.enough_cells.emit()

    def ship_construction(self, length):
        pass
        # self.ship_construction_FSM(length)


############# Main State Machine #################################
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

        # self.start_playing = QtCore.QState(self.ParentStateToEnd)
        # self.start_playing.entered.connect(lambda: print("start_playing"))
        # self.start_playing.assignProperty(self.centralwidget, "enabled", True)
        # for button in self.buttonGroup_2.buttons():
        #     self.start_playing.assignProperty(button, "enabled", False)
        # self.start_playing.entered.connect(lambda: self.statusbar.showMessage("{player1}, start ship positioning." .format(player1=self.Player1_name.text())))
        # self.start_playing.entered.connect(lambda: self.ship_construction_FSM(4))

        self.player1_ship_positioning = QtCore.QState(self.ParentStateToEnd)
        self.player1_ship_positioning.entered.connect(lambda: print("player1_ship_positioning"))
        self.player1_ship_positioning.assignProperty(self.centralwidget, "enabled", True)
        for button in self.buttonGroup_2.buttons():
            self.player1_ship_positioning.assignProperty(button, "enabled", False)
        self.player1_ship_positioning.entered.connect(lambda: self.statusbar.showMessage("{player1}, start ship positioning." .format(player1=self.Player1_name.text())))
        self.player1_ship_positioning.entered.connect(lambda: self.positioning_of_all_ships_FSM())

        self.end = QtCore.QState()
        self.end.assignProperty(self.centralwidget, "enabled", False)
        self.end.entered.connect(lambda: print("End of the game!!!"))
        self.end.entered.connect(lambda: self.label.setStyleSheet("color : #555555;"))
        self.end.entered.connect(lambda: self.statusbar.showMessage("Game Over!!!!!"))

        # Transitions
        self.initial_state.addTransition(self.actionStart.triggered, self.set_player_names)
        self.set_player_names.addTransition(self.set_player_names.entered, self.player1_ship_positioning)
        self.player1_ship_positioning.addTransition(self.custom_signal.all_ships_constructed, self.end)
        self.ParentStateToEnd.addTransition(self.end_shortcut.activated, self.end)

        # State Machine
        self.fsm = QtCore.QStateMachine()

        self.fsm.addState(self.ParentStateToEnd)
        self.fsm.addState(self.initial_state)
        self.fsm.addState(self.set_player_names)
        self.fsm.addState(self.player1_ship_positioning)
        self.fsm.addState(self.end)

        self.fsm.setInitialState(self.ParentStateToEnd)

        self.fsm.start()

####################### Ship construction State Machine ############################
    def ship_construction_FSM(self, length):

        self.cell_list = []

        # States
        self.input_cell = QtCore.QState()
        self.input_cell.entered.connect(lambda: print("cell is inputted."))
        self.input_cell.entered.connect(lambda: self.cell_selection())

        self.ship_length_varification = QtCore.QState()
        self.ship_length_varification.entered.connect(lambda: print("ship_length_varification."))
        self.ship_length_varification.entered.connect(lambda: self.varify_ship_length(length))

        self.varify_ship_state = QtCore.QState()
        self.varify_ship_state.entered.connect(lambda: self.varify_ship())

        self.finalState = QtCore.QFinalState()
        self.finalState.entered.connect(lambda: print("Finish"))
        self.finalState.entered.connect(lambda: self.custom_signal.ship_constructed.emit())

        # Transitions
        self.input_cell.addTransition(self.custom_signal.cell_created, self.ship_length_varification)
        self.ship_length_varification.addTransition(self.custom_signal.need_more_cells, self.input_cell)
        self.ship_length_varification.addTransition(self.custom_signal.enough_cells, self.varify_ship_state)
        self.varify_ship_state.addTransition(self.custom_signal.valid_ship, self.finalState)

        # State Machine
        self.positioning = QtCore.QStateMachine()

        self.positioning.started.connect(lambda: print("Is ship construction running:", self.positioning.isRunning()))


        self.positioning.addState(self.input_cell)
        self.positioning.addState(self.ship_length_varification)
        self.positioning.addState(self.varify_ship_state)
        self.positioning.addState(self.finalState)

        self.positioning.setInitialState(self.input_cell)

        self.positioning.start()



######################################All_Ship_Positionning#########################################################

    def positioning_of_all_ships_FSM(self):



        # States

        self.battleship = QtCore.QState()
        self.battleship.entered.connect(lambda: self.ship_construction_FSM(4))

        self.cruiser1 = QtCore.QState()
        self.cruiser1.entered.connect(lambda: self.ship_construction_FSM(3))

        self.cruiser2 = QtCore.QState()
        self.cruiser2.entered.connect(lambda: self.ship_construction_FSM(3))

        self.destroyer1 = QtCore.QState()
        self.destroyer1.entered.connect(lambda: self.ship_construction_FSM(2))

        self.destroyer2 = QtCore.QState()
        self.destroyer2.entered.connect(lambda: self.ship_construction_FSM(2))

        self.destroyer3 = QtCore.QState()
        self.destroyer3.entered.connect(lambda: self.ship_construction_FSM(2))

        self.submarine1 = QtCore.QState()
        self.submarine1.entered.connect(lambda: self.ship_construction_FSM(1))

        self.submarine2 = QtCore.QState()
        self.submarine2.entered.connect(lambda: self.ship_construction_FSM(1))

        self.submarine3 = QtCore.QState()
        self.submarine3.entered.connect(lambda: self.ship_construction_FSM(1))

        self.submarine4 = QtCore.QState()
        self.submarine4.entered.connect(lambda: print("Hello submarine4"))
        self.submarine4.entered.connect(lambda: self.ship_construction_FSM(1))


        self.mark_all_unmarked_cells = QtCore.QState()
        self.mark_all_unmarked_cells.entered.connect(lambda: self.mark_remaining_cells_as_free(self.user1.myMap))

        self.finish_positioning = QtCore.QFinalState()
        self.finish_positioning.entered.connect(lambda: print("Test::", self.user1.myMap.map))

        # Transitions

        # self.battleship.addTransition(self.custom_signal.ship_constructed, self.mark_all_unmarked_cells)
        self.battleship.addTransition(self.custom_signal.ship_constructed, self.submarine4)
        # self.battleship.addTransition(self.custom_signal.ship_positioned, self.cruiser1)
        # self.cruiser1.addTransition(self.custom_signal.ship_positioned, self.cruiser2)
        # self.cruiser2.addTransition(self.custom_signal.ship_positioned, self.destroyer1)
        # self.destroyer1.addTransition(self.custom_signal.ship_positioned, self.destroyer2)
        # self.destroyer2.addTransition(self.custom_signal.ship_positioned, self.destroyer3)
        # self.destroyer3.addTransition(self.custom_signal.ship_positioned, self.submarine1)
        # self.submarine1.addTransition(self.custom_signal.ship_positioned, self.submarine2)
        # self.submarine2.addTransition(self.custom_signal.ship_positioned, self.submarine3)
        # self.submarine3.addTransition(self.custom_signal.ship_positioned, self.submarine4)
        self.submarine4.addTransition(self.custom_signal.ship_constructed, self.mark_all_unmarked_cells)

        self.mark_all_unmarked_cells.addTransition(self.custom_signal.all_ships_constructed, self.finish_positioning)

        # State Machine

        self.all_ship_positioning = QtCore.QStateMachine()

        self.all_ship_positioning.addState(self.battleship)
        self.all_ship_positioning.addState(self.cruiser1)
        self.all_ship_positioning.addState(self.cruiser2)
        self.all_ship_positioning.addState(self.destroyer1)
        self.all_ship_positioning.addState(self.destroyer2)
        self.all_ship_positioning.addState(self.destroyer3)
        self.all_ship_positioning.addState(self.submarine1)
        self.all_ship_positioning.addState(self.submarine2)
        self.all_ship_positioning.addState(self.submarine3)
        self.all_ship_positioning.addState(self.submarine4)
        self.all_ship_positioning.addState(self.mark_all_unmarked_cells)
        self.all_ship_positioning.addState(self.finish_positioning)

        self.all_ship_positioning.setInitialState(self.battleship)

        self.all_ship_positioning.start()