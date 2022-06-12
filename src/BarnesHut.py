import numpy as np

from body import *
from node import *
from quadtree import *
from utils import *


if __name__ == '__main__':
    
    # Galaxies parameters
    r0 = 3 #kpc, scale length of galaxy
    m0 = 50.0 #10^9 solar mass, mass of galaxy 1
    m1 = 3.0
    shift = np.array([10.,10.]) #shift of initial location of galaxy
    c_vel = np.array([-.5,-.5]) #velocity vector of center of galaxies

    # Simulation space
    N = 800 #number of particles
    L = 50.0 #half length of box, kpc

    # Barnes-Hut simulation parameters
    theta = 1
    epsilon = theta*L/np.sqrt(N)

    # Time evolution parameters
    dt = 0.1 #10Myr
    T = 20.0 #10Myr
    steps = int(T/dt)
    
    # Generating two galaxies
    tree = Node(Quad(-L,-L,2*L))
    bodies = two_galaxies(r0=r0, m0=m0, m1=m1, N=N, L=L, c_vel=c_vel, shift=shift)
    
    plot_bh(steps, bodies, tree, L, theta, epsilon, dt, N, version='0')
    #nohup python3 ./src/BarnesHut.py &