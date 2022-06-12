import numpy as np

from itertools import chain

from utils import *

if __name__ == '__main__':
    # Milky Way parameters
    r0 = 3 #kpc
    m0 = 50.0 #10^9 solar mass

    # Simulation space
    N = 100
    L = 15.0 #kpc

    # Barnes-Hut simulation resolution
    theta = 1.0
    epsilon = theta*L/np.sqrt(N) 

    dt = 0.1 #10Myr
    T = 100.0 #10Myr
    steps = int(T/dt)

    dir = 'output/'

    thetas = [0.5, 0.7, 0.8, 1.0, 1.5, 2]
    nums = list(chain(range(1,101),range(101,1001,10)))

    comparison(nums, dir, thetas, r0, m0, L, epsilon)


    