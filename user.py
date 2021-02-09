class User():

    def __init__(self, id=0, x=0, y=0):
        self.__id = id
        self.__x = x
        self.__y = y
        self.__register = [[x],[y]]

    def get_id(self):
        return self.__id

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_register(self):
        return self.__register

    def update_position(self, x, y):
        self.__x = x
        self.__y = y
        self.__register[0].append(x)
        self.__register[1].append(y)

    def reset_register(self):
        self.__register = [[],[]]

    def print_position(self):
        print("(User " + str(self.__id) + ")Position: (" + str(self.__x) + ", " + str(self.__y) + ")")
