import numpy as np

from itertools import chain

from utils import *

if __name__ == '__main__':
    # Milky Way parameters
    r0 = 3 #kpc, scale length of galaxy
    m0 = 50.0 #10^9 solar mass, mass of galaxy

    # Simulation space
    N = 100
    L = 15.0 #kpc

    # Barnes-Hut simulation resolution
    theta = 1.0
    epsilon = theta*L/np.sqrt(N) #softening length

    # Time evolution parameters
    dt = 0.1 #10Myr
    T = 100.0 #10Myr
    steps = int(T/dt)

    dir = 'output/evaluation/'
    nums = list(chain(range(1,101),range(101,1001,10)))

    BarnesHut_eval_plot(r0, m0, nums, L, theta, epsilon, dir)