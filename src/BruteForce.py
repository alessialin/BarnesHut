#essential modules
import numpy as np
import matplotlib.pyplot as plt
from time import process_time
from itertools import chain

#essential imports
from body import Body
from quadtree import Quad
from node import BHTree
from simulation import generateGalaxy

#function: main
if __name__ == '__main__':
    #Milky Way parameters
    r0 = 3 #kpc, scale length of galaxy
    m0 = 50.0 #10^9 solar mass, mass of galaxy
    #simulation space
    L = 15.0 #length of box, kpc
    #Barnes-Hut simulation resolution
    N = 1000
    theta = 1.0
    epsilon = theta*L/np.sqrt(N) #softening length
    #time evolution parameters
    dt = 0.1 #10Myr
    T = 100.0 #10Myr
    steps = int(T/dt)
    #generate 1000 masses in 15kpc box
    #bodies = generateGalaxy(r0, m0, N, L)
    
    #plot galactic bodies, initial distribution
    # for body in bodies:
    #     body.plot()
    # plt.xlim([-L,L])
    # plt.ylim([-L,L])
    # plt.show()

    #test BH tree construction/traversal speed
    nums = list(chain(range(1,101),range(101,1001,10)))
    timesForce = []
    for i in range(len(nums)):
        num = nums[i]
        print ("Computing number "+str(num)+"/{steps}")
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
    plt.savefig(f'simulations/BruteForce_time.png')
    plt.show()