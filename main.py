from model import Model
import matplotlib.pyplot as plt
from simulator import Simulator

#m = Model(100)
#m.simulate()

s = Simulator(steps=500)
s.init_users(10, (36.713447, -4.502069), (36.721978, -4.487821))
s.init_users(5, (36.717330, -4.479766), (36.724165, -4.473174))
s.simulate()
s.print_graph()
