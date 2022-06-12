import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from matplotlib.animation import FFMpegWriter #brew install ffmpeg prerequisites
from tqdm import tqdm

from body import *
from node import *
from quadtree import *

def gravity(newton=False, kpc=True):
    """
    newton : bool
        if the unit of measure used is N/m^2/kg^2
    kpc : bool
        if the unit of measure used is kpc^3/[kMs]/[10Myr]^2

    -------
    returns gravitational force definition
    """
    if newton:
        G = 6.674e-11
    if kpc:
        G = 0.449 
    return G

def generateGalaxy(r0, m0, N, L, c_vel=[0.,0.], shift=[0.,0.]):
    bodies = []
    m = m0/N #divide mass of galaxy among N masses

    for i in range(N):
        #position from normalized distribution p(R) = (1/r0)exp(-r/r0)
        r = -r0*np.log(1.0-np.random.rand())

        if r < L:
            theta = 2.0*np.pi*np.random.rand()
            rx = shift[0] + r*np.cos(theta)
            ry = shift[1] + r*np.sin(theta)
            #velocity from naive estimate v ~ sqrt(GMgalaxy/r)
            v = 4.738*np.exp(-r0/r)/np.sqrt(r)
            vx = -v*np.sin(theta) + c_vel[0]
            vy = v*np.cos(theta) +c_vel[1]
            #generate bodies
            bodies.append(Body(m, rx, ry, vx=vx, vy=vy, L=L+shift[0]))

    return bodies

def two_galaxies(r0, m0, m1, N, L, c_vel, shift=[0.,0.]):
    galaxy1 = generateGalaxy(r0, m0, N//2, L, shift=shift*-1)
    galaxy = generateGalaxy(r0, m1, N//2, L, c_vel=c_vel, shift=shift)
    for i in galaxy1:
        galaxy.append(i)
    return galaxy

def barnes_hut(galaxy, tree:Node(Quad), theta, epsilon, dt):
    for body in galaxy:
            tree.insertBody(body)
        #calculate force on every body from tree and evolve
            body.resetForce()
            tree.applyForce(body, theta, epsilon)
            #take a time step
            body.update(dt)
    return galaxy

def plot_bh(steps, galaxy, tree, L, theta, epsilon, dt, N, version='0'):
    images = []
    marker = ['k.', 'g.']

    fig = plt.figure()
    ax = plt.axes(xlim=(-L, L), ylim=(-L, L))

    for i in tqdm(range(steps), desc='Computing time progression'):
        #computation counter
        galaxies = barnes_hut(galaxy, tree, theta, epsilon, dt)

        #appending galaxies to list for plotting
        position = np.array([body.r for body in galaxies]).T 
        scatter_body1 = ax.plot(position[0][:N//2], position[1][:N//2], marker[0]) 
        scatter_body2 = ax.plot(position[0][N//2:], position[1][N//2:], marker[1])
        ax.set_title('Barnes-Hut Galaxies Collision')
        images.append(scatter_body1+scatter_body2)

    anim = animation.ArtistAnimation(fig, images, interval=100, blit=True)
    writer = FFMpegWriter(fps=30)
    anim.save(f'./output/BH_GalaxyCollision_'+str(N)+'_v'+version+'.mp4', writer=writer)
    #plt.show()
