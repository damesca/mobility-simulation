
class Grid():

    def __init__(self, rows=10, columns=10):
        self.__rows=rows
        self.__columns=columns
        self.matrix = [[0 for i in range(self.__rows)] for j in range(self.__columns)]
        print("Grid: ")
        for x in range(0, self.__rows):
            print(self.matrix[x])

    def get_number_rows(self):
        return self.__rows

    def get_number_columns(self):
        return self.__columns

    def add_element(self, x, y, val):
        self.matrix[x][y] = val

    def remove_element(self, x, y):
        self.matrix[x][y] = 0

    def print_matrix(self):
        print("Grid: ")
        for x in range(0, self.__rows):
            print(self.matrix[x])
