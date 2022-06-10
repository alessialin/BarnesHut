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
    N=100
    L = 15.0 #length of box, kpc
    #Barnes-Hut simulation resolution
    theta = 1.0
    epsilon = theta*L/np.sqrt(N) #softening length
    #time evolution parameters
    dt = 0.1 #10Myr
    T = 100.0 #10Myr
    steps = int(T/dt)
    #generate 1000 masses in 15kpc box
    #bodies = generateGalaxy(r0, m0, N, L)
    
    # #plot galactic bodies, initial distribution
    # for body in bodies:
    #     body.plot()
    # plt.xlim([-L,L])
    # plt.ylim([-L,L])
    # plt.show()

    #generate Barnes-Hut tree on original grid
    # tree = BHTree(Quad(-L,-L,2*L))
    # #populate tree with bodies from list
    # for body in bodies:
    #     tree.insertBody(body)
    # #calculate force on every body from tree and evolve leapfrog step
    # for body in bodies:
    #     body.resetForce()
    #     tree.applyForce(body, theta, epsilon)
    #     #take a half time step
    #     body.leapFrog(dt)
    
    # #test energy conservation over evolution
    # t = np.linspace(0,steps*dt,steps)
    # E = np.zeros(len(t))
    # #sum kinetic
    # for body in bodies:
    #     E[0]+=body.Kenergy(dt)
    # #sum potential
    # for j in range(len(bodies)):
    #     for k in range(j+1,len(bodies)):
    #         E[0]+=bodies[j].Uinteract(bodies[k])
    # #evolve N-body in time
    # for i in range(steps):
    #     #computation counter
    #     print ("Computing time step "+str(i+1)+"/"+str(steps))
    #     #generate Barnes-Hut tree on original grid
    #     tree = BHTree(Quad(-L,-L,2*L))
    #     #populate tree with bodies from list
    #     for body in bodies:
    #         tree.insertBody(body)
    #     #calculate force on every body from tree and evolve
    #     for body in bodies:
    #         body.resetForce()
    #         tree.applyForce(body, theta, epsilon)
    #         #take a time step
    #         body.update(dt)
    #     #calculate energy at time
    #     for body in bodies:
    #         E[i]+=body.Kenergy(dt)
    #     for j in range(len(bodies)):
    #         for k in range(j+1,len(bodies)):
    #             E[i]+=bodies[j].Uinteract(bodies[k])
    # plt.plot(t, E)
    # plt.title("Energy conservation")
    # plt.ylabel("Energy [kMs*kpc^2/(10Myr)^2]")
    # plt.show()

    #test BH tree construction/traversal speed
    nums = list(chain(range(1,101),range(101,1001,10)))
    timesTree = []
    for i in range(len(nums)):
        num = nums[i]
        print ("Computing number "+str(num)+"/{steps}")
        bodies = generateGalaxy(r0, m0, num, L)
        #tree construction
        t_start = process_time()
        tree = BHTree(Quad(-L,-L,2*L))
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
    plt.savefig(f'simulations/BarnesHut_time.png')
    #plt.show()