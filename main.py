from model import Model
import matplotlib.pyplot as plt
from simulator import Simulator

#m = Model(100)
#m.simulate()

s = Simulator(steps=100)
s.init_users(10, (0, 0), (0.001, 0.001))
#s.init_users(2, (-50, -50), (-30, -30))
s.simulate()
s.print_graph()
