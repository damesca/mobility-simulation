from model import Model
import matplotlib.pyplot as plt
from simulator import Simulator

#m = Model(100)
#m.simulate()

s = Simulator(users=50, steps=1000)
s.init_users((0, 0), (1000, 1000))
s.simulate()
s.print_graph()
