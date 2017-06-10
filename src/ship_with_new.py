from cell import Cell

class Ship:

    def __new__(cls,cell_tuple):
        if 1 <= len(cell_tuple) <= 4:
            if cls.__are_cells_valid(cell_tuple):
                self = super(Ship, cls).__new__(cls)
                self.cell_tuple = cell_tuple
                print("The ship is constructed")
                return self

            else:
                print("A ship must be linear either horizontally or vertically. Ship cells must be sequential.")
        else:
            print("A ship must have at least 1 and not more than 4 cells.")

    @classmethod
    def __are_cells_valid(cls, cell_tuple):
        "Checks if the ship cells are disposed linearly and sequentially."

        ship_type = cls.__is_ship_linear(cell_tuple, "horizontal")

        if ship_type is None:
            ship_type = cls.__is_ship_linear(cell_tuple, "vertical")
        if ship_type is not None:

            ########################################
            # A check for sequentiality starts here

            coord_array = cls.__get_array_of_indexes(cell_tuple, ship_type)
            coord_array.sort()

            for i in range(1, len(coord_array)):
                if coord_array[i] - coord_array[i - 1] != 1:
                    print("Ship construction failed. Ship cells are not sequential.")
                    return 0
            return 1

        else:
            print("Ship construction failed. Ship cells are not linear.")
            return 0

    @staticmethod
    def __is_ship_linear(cell_tuple, type):
        "Checks if the ship cells are disposed linearly."

        flag = 1
        fixed_coordinate = None
        if type == "horizontal":
            fixed_coordinate = "letter_index"
        elif type == "vertical":
            fixed_coordinate = "number_index"

        for x in range(1, len(cell_tuple)):
            flag = flag and getattr(cell_tuple[x], fixed_coordinate) == getattr(cell_tuple[x - 1], fixed_coordinate)
            if flag == 0:
                break

        if flag == 1:
            return type

    @staticmethod
    def __get_array_of_indexes(cell_tuple, type):
        "Returns a list of cell coordinates, which are changing along the ship."

        if type == "horizontal":
            coordinate = "number_index"
        elif type == "vertical":
            coordinate = "letter_index"

        index_array = []
        for cell in cell_tuple:
            if coordinate == "letter_index":
                index_array.append(cell.letter_index)
            elif coordinate == "number_index":
                index_array.append(cell.number_index)
        return index_array
