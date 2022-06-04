import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from body import *
from node import *
from quadtree import *
from simulation import *

if __name__ == '__main__':
    #Milky Way parameters (default)
    r0 = 3 #kpc, scale length of galaxy
    m0 = 50.0 #10^9 solar mass, mass of galaxy
    #simulation space
    N = 1000 #number of particles
    s = 15.0 #half length of box, kpc
    #Barnes-Hut simulation resolution
    theta = 1.0
    epsilon = theta*s/np.sqrt(N)
    #time evolution parameters
    dt = 0.1 #10Myr
    T = 10.0 #10Myr
    steps = int(T/dt)
    #generate 1000 masses in 15kpc box
    bodies = generateGalaxy(r0, m0, N, s)
    #generate Barnes-Hut tree on original grid
    tree = Node(Quad(-s,-s,2*s))
    #populate tree with bodies from list
    for body in bodies:
        tree.insert_body(body)
    #calculate force on every body from tree and evolve leapfrog step
    for body in bodies:
        body.resetForce()
        tree.applyForce(body, theta, epsilon)
        #take a half time step
        body.leapFrog(dt)

    #make list of objects for plotting
    images = []
    #plotting setup
    fig = plt.figure()
    ax = plt.axes(xlim=(-s, s), ylim=(-s, s))
    #evolve N-body in time
    for i in range(steps):
        #computation counter
        print("Computing time step "+str(i+1)+"/"+str(steps))
        #generate Barnes-Hut tree on original grid
        tree = Node(Quad(-s,-s,2*s))
        #populate tree with bodies from list
        for body in bodies:
            tree.insert_body(body)
        #calculate force on every body from tree and evolve
        for body in bodies:
            body.resetForce()
            tree.applyForce(body, theta, epsilon)
            #take a time step
            body.update(dt)
        #append to list of objects for plotting
        position = np.array([body.r for body in bodies]).T
        scatter = ax.plot(position[0], position[1], 'k.')
        images.append((scatter))
                
    anim = animation.ArtistAnimation(fig, images, interval=100, blit=True)
    writer = animation.PillowWriter(fps=30)
    anim.save('BH_'+str(N)+'.gif', writer = writer)
    plt.show()
    