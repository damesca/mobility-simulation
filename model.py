from user import User
from grid import Grid
import random
import matplotlib.pyplot as plt

class Model():

    def __init__(self, max_steps=10):
        self.angle = ['up', 'down', 'right', 'left']
        self.length = [0, 2]    #[max, min]
        self.speed = [1, 2]     #[max, min]
        self.pause = [0, 1]     #[max, min]

        self.max_steps = max_steps
        self.actual_step = 0

        self.grid = Grid(20, 20)
        self.max_rows = self.grid.get_number_rows() - 1
        self.max_columns = self.grid.get_number_columns() - 1

        self.user = User(4, 4)      # Just one user for the moment
        self.user.print_position()

        self.registry_x = []
        self.registry_y = []

    def update_user(self):
        x = self.user.get_x()
        y = self.user.get_y()
        dir = random.choice(self.angle)
        print("Dir: " + dir)
        if(dir == 'up' and y < self.max_rows):
            self.user.set_y(y + 1)
        elif(dir == 'down' and y > 0):
            self.user.set_y(y - 1)
        elif(dir == 'right' and x < self.max_columns):
            self.user.set_x(x + 1)
        elif(dir == 'left' and x > 0):
            self.user.set_x(x - 1)

        if(random.randint(0, 1) == 1):
            self.update_user()


    def simulate(self):
        for step in range(0, self.max_steps):
            print("Step: " + str(self.actual_step))

            self.grid.remove_element(self.user.get_x(), self.user.get_y())
            self.update_user()
            self.user.print_position()
            self.grid.add_element(self.user.get_x(), self.user.get_y(), 5)
            self.registry_x.append(self.user.get_x())
            self.registry_y.append(self.user.get_y())

            self.grid.print_matrix()

            ##
            self.actual_step += 1

        print("Movement: ")
        print(self.registry_x)
        print(self.registry_y)
        plt.plot(self.registry_x, self.registry_y)
        plt.xlim([0, self.grid.get_number_columns()])
        plt.ylim([0, self.grid.get_number_rows()])
        plt.show()
