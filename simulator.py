from model import Model
from user import User
import matplotlib.pyplot as plt
import random
import math

class Simulator():

    def __init__(self, model='basic', users=10, steps=10):
        self.number_users = users
        self.users = []
        self.steps = steps

        if(model == 'basic'):
            self.model = Model()
        else:
            raise NameError('Incorrect type of model')

    def init_users(self, p_0=(0, 0), p_1=(10, 10)):
        print("Initialization of users: ")
        for i in range(0, self.number_users):
            new_user = User(i, random.uniform(p_0[0], p_1[0]), random.uniform(p_0[1], p_1[1]))
            self.users.append(new_user)
            new_user.print_position()

    def simulate(self, filename='mobility-simulation.txt'):
        f = open(filename, 'w')

        for s in range(0, self.steps):
            print("# Simulation Step " + str(s) + " #")
            f.write("# Simulation Step " + str(s) + " #\n")
            for user in self.users:
                # Do some simulation stuff
                print("(User " + str(user.get_id()) + ") Do some simulation stuff")

                params = self.model.generate_uniform_parameters()
                x = user.get_x()
                y = user.get_y()
                (new_x, new_y) = self.model.update_position(x, y, params[1], params[0])

                user.update_position(new_x, new_y)

                f.write("(User " + str(user.get_id()) + ")(" + str(user.get_x()) + "," + str(user.get_y()) + ")\n")

        f.close()

    def print_graph(self):
        reg = []
        for user in self.users:
            reg.append(user.get_register())

        for r in reg:
            plt.plot(r[0], r[1])
            plt.plot(r[0][0], r[1][0], 'o')

        plt.show()
