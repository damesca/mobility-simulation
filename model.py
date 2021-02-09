from user import User
import random
import math
import matplotlib.pyplot as plt

class Model():

    def __init__(self, max_steps=10):
        #self.angle = ('up', 'down', 'right', 'left')
        self.angle = (0, 2 * math.pi)
        self.length = (0, 5)    #[max, min]
        self.speed = (1, 2)     #[max, min]
        self.pause = (0, 1)     #[max, min]

    def generate_uniform_parameters(self):
        angle = random.uniform(self.angle[0], self.angle[1])
        length = random.uniform(self.length[0], self.length[1])
        speed = random.uniform(self.speed[0], self.speed[1])
        pause = random.uniform(self.pause[0], self.pause[1])
        return (angle, length, speed, pause)

    def update_position(self, x, y, length, angle):
        xx = x + length * math.cos(angle)
        yy = y + length * math.sin(angle)
        return (xx, yy)
