import numpy as np
import matplotlib.pyplot as plt

from itertools import chain
from time import process_time
from tqdm import tqdm

from quadtree import Quad
from node import BHTree

from utils import *

def BarnesHut_evalutation(r0, m0, nums, L, theta, epsilon, dir):
    timesTree = []
    for i in tqdm(range(len(nums))):
        num = nums[i]
        
        bodies = generateGalaxy(r0, m0, num, L)
        #tree construction
        t_start = process_time()
        tree = Node(Quad(-L,-L,2*L))
        for body in bodies:
            tree.insertBody(body)

        #tree traversal
        for body in bodies:
            body.resetForce()
            tree.applyForce(body, theta, epsilon)
        t_end = process_time()
        timesTree.append(t_end - t_start)
    plt.plot(nums, timesTree)
    plt.xlabel("N-bodies")
    plt.ylabel("Time")
    plt.title("Time to compute forces with Barnes-Hut quadtree for N bodies")
    plt.savefig(dir+'BarnesHut_time.png')


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

    dir = 'output/'
    nums = list(chain(range(1,101),range(101,1001,10)))

    BarnesHut_evalutation(r0, m0, nums, L, theta, epsilon, dir)