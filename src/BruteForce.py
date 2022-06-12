import numpy as np
import matplotlib.pyplot as plt

from itertools import chain
from time import process_time
from tqdm import tqdm

from utils import *

def BruteForce_evaluation(nums, r0, m0, num, L, epsilon, dir):
    timesForce = []
    for i in tqdm(range(len(nums))):
        num = nums[i]
        bodies = generateGalaxy(r0, m0, num, L)
        #compute all forces between pairs
        t_start = process_time() 
        for body in bodies:
            #pick a body
            body.resetForce()
            for other in bodies:
                #pick any other body
                if (body.r != other.r).any():
                    #don't compute self forces
                    body.addForce(other, epsilon)
        t_end = process_time()
        timesForce.append(t_end - t_start)
    plt.plot(nums, timesForce)
    plt.xlabel("N-bodies")
    plt.ylabel("Time")
    plt.title("Brute Force - Time to compute N^2 forces")
    plt.savefig(dir+'BruteForce_time.png')

#function: main
if __name__ == '__main__':
    # Milky Way parameters
    r0 = 3 #kpc, scale length of galaxy
    m0 = 50.0 #10^9 solar mass, mass of galaxy

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

    dir = 'output/'
    nums = list(chain(range(1,101),range(101,1001,10)))

    # Test Brute Force computation speed
    BruteForce_evaluation(nums, r0, m0, nums, L, epsilon, dir)