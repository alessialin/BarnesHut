import numpy as np
import sys

sys.path.append('PATH_TO_SRC_FOLDER')

from itertools import chain
from utils import *


if __name__ == '__main__':
    r0 = 3 #kpc
    m0 = 50.0 #10^9 solar mass

    # Simulation space
    L = 15.0 #length of box, kpc

    # Barnes-Hut parameters
    N = 1000
    theta = 1.0
    epsilon = theta*L/np.sqrt(N) #softening length

    # Time parameters
    dt = 0.1 #10Myr
    T = 100.0 #10Myr
    steps = int(T/dt)

    dir = 'output/benchmark/'
    nums = list(chain(range(1,101),range(101,1001,10)))

    # Test Brute Force computation speed
    BruteForce_eval_plot(nums, r0, m0, L, epsilon, dir)