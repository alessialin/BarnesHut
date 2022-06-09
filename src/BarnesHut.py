#essential modules
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from itertools import cycle
from matplotlib.animation import FFMpegWriter #brew install ffmpeg prerequisites

#essential imports
from body import *
from quadtree import *
from node import *
from simulation import *


#function: main
if __name__ == '__main__':
    #Milky Way parameters (default)
    r0 = 3 #kpc, scale length of galaxy
    m0 = 50.0 #10^9 solar mass, mass of galaxy 
    m1 = 30.0
    #simulation space
    N = 1000 #number of particles
    L = 30.0 #half length of box, kpc

    #Barnes-Hut simulation resolution
    theta = 1.0
    epsilon = theta*L/np.sqrt(N)
    #time evolution parameters
    dt = 0.1 #10Myr
    T = 1.0 #10Myr
    steps = int(T/dt)
    center = [10.,10.]
    c_vel = [-5000.,1000.]
    #generate 1000 masses in 15kpc box
    bodies2 = generateGalaxy(r0, m0, N//2, L)
    bodies = generateGalaxy(r0, m1, N//2, L, center=center, color='g')
    #print(type(bodies))
    for i in bodies2:
        bodies.append(i)
    #print(type(bodies))
    #bodies = generateUniform( m0, c_vel, N, L)
    #generate Barnes-Hut tree on original grid
    #tree = BHTree(Quad(-L,-L,2*L))
    # #populate tree with bodies from list
    #for body in bodies:
    #    tree.insertBody(body)
    # #calculate force on every body from tree and evolve leapfrog step
    # for body in bodies:
    #     body.resetForce()
        #tree.applyForce(body, theta, epsilon)
        #take a half time step
        #body.leapFrog(dt)

    #make list of objects for plotting
    images = []
    images1 = []
    #plotting setup
    fig = plt.figure()
    ax = plt.axes(xlim=(-L, L), ylim=(-L, L))
    #evolve N-body in time
    for i in range(steps):
        #computation counter
        print("Computing time step "+str(i+1)+"/"+str(steps))
        #generate Barnes-Hut tree on original grid
        tree = BHTree(Quad(-L,-L,2*L))
        #populate tree with bodies from list
        for body in bodies:
            tree.insertBody(body)
        #calculate force on every body from tree and evolve
        for body in bodies:
            body.resetForce()
            tree.applyForce(body, theta, epsilon)
            #take a time step
            body.update(dt)
        # for body in bodies2:
        #     tree.insertBody(body)
        # #calculate force on every body from tree and evolve
        # for body in bodies2:
        #     body.resetForce()
        #     tree.applyForce(body, theta, epsilon)
        #     body.update(dt)

        #append to list of objects for plotting
        position = np.array([body.r for body in bodies]).T 
        #colors = cycle([body.c+'.' for body in bodies])
        marker = ['k.', 'g.']
        scatter = ax.plot(position[0][:N//2], position[1][:N//2], marker[0]) 
        scatter1 = ax.plot(position[0][N//2:], position[1][N//2:], marker[1])
        images.append(scatter+scatter1)

    anim = animation.ArtistAnimation(fig, images, blit=True)
    writer = FFMpegWriter(fps=60)
    anim.save('BH_'+str(N)+'_v2.mp4') #, writer=writer)
    plt.show()

    
    
    

