import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from body import *
from quadtree import *
from node import *
from simulation import *

if __name__ == '__main__':
    #Milky Way parameters (default)
    r0 = 3 #kpc, scale length of galaxy
    mass = 50.0 #10^9 solar mass, mass of galaxy
    #simulation space
    n = 1000 #number of particles
    s = 15.0 #half length of box, kpc
    #Barnes-Hut simulation resolution
    theta = 1.0
    epsilon = theta*s/np.sqrt(n)
    #time evolution parameters
    delta_t = 1 #0.1=10Myr
    T = 10.0 #10Myr
    steps = int(T/delta_t)
    #generate 1000 masses in 15kpc box
    bodies = generateGalaxy(r0, mass, n, s)
    #generate Barnes-Hut tree on original grid
    tree = Node(QuadTree(-s,-s,2*s))
    #populate tree with bodies from list
    for body in bodies[:5]: #only first 5 
        tree.insert_body(body)
    #calculate force on every body from tree and evolve leapfrog step
    #for body in bodies:
        body.resetForce()
        tree.applyForce(body, theta, epsilon)
        #take a half time step
        #body.leapFrog(delta_t)

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
        tree = Node(QuadTree(-s,-s,2*s))
        #populate tree with bodies from list
        for body in bodies:
            tree.insert_body(body)
        #calculate force on every body from tree and evolve
        for body in bodies:
            body.resetForce()
            tree.applyForce(body, theta, epsilon)
            #take a time step
            body.update(delta_t)
        #append to list of objects for plotting
        position = np.array([body.r for body in bodies]).T
        scatter, = ax.plot(position[0], position[1], 'k.')
        images.append((scatter,))
         
    anim = animation.ArtistAnimation(fig, images, interval=100, blit=True)
    anim.save('BH_'+str(n)+'.gif', fps=10)
    plt.show()