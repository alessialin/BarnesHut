import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from matplotlib.animation import FFMpegWriter #brew install ffmpeg prerequisites
from time import process_time
from tqdm import tqdm

from body import *
from node import *
from quadtree import *

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

def plot_bh(steps, galaxy, tree, L, theta, epsilon, dt, N, version='0', two_galaxies=True):
    images = []
    marker = ['k.', 'g.']

    fig = plt.figure()
    ax = plt.axes(xlim=(-L, L), ylim=(-L, L))

    if two_galaxies: #if there are two galaxies
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

    else: #if it's only one galaxy
        for i in tqdm(range(steps), desc='Computing time progression'):
            #computation counter
            galaxy = barnes_hut(galaxy, tree, theta, epsilon, dt)

            #appending galaxies to list for plotting
            position = np.array([body.r for body in galaxy]).T 
            scatter_body = ax.plot(position[0], position[1], marker[0]) 
            ax.set_title('Barnes-Hut: Milky Way')
            images.append(scatter_body)
        
        anim = animation.ArtistAnimation(fig, images, interval=100, blit=True)
        writer = FFMpegWriter(fps=30)
        anim.save(f'./output/BH_GalaxySimulation_'+str(N)+'_v'+version+'.mp4', writer=writer)
        #plt.show()


def BarnesHut_evaluation(nums, r0, m0, L, theta, epsilon):
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
            body.resetForce()
            tree.applyForce(body, theta, epsilon)
        t_end = process_time()
        timesTree.append(t_end - t_start)
    return timesTree

def BruteForce_evaluation(nums, r0, m0, L, epsilon):
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
    
    return timesForce

def BruteForce_eval_plot(nums, r0, m0, L, epsilon, dir):
    timesForce = BruteForce_evaluation(nums, r0, m0, L, epsilon)
    plt.plot(nums, timesForce)
    plt.xlabel("N-bodies")
    plt.ylabel("Time")
    plt.title("Brute Force - Time to compute N^2 forces")
    plt.savefig(dir+'BruteForce_time.png')

def BarnesHut_eval_plot(r0, m0, nums, L, theta, epsilon, dir):
    timesTree = BarnesHut_evaluation(nums, r0, m0, L, theta, epsilon)
    plt.plot(nums, timesTree)
    plt.xlabel("N-bodies")
    plt.ylabel("Time")
    plt.title("Time to compute forces with Barnes-Hut quadtree for N bodies")
    plt.savefig(dir+'BarnesHut_time.png')

def comparison(nums, dir, thetas, r0, m0, L, epsilon):
    bh_all = {}
    bf = BruteForce_evaluation(nums, r0, m0, L, epsilon)
    for theta in thetas:
        bh = BarnesHut_evaluation(nums, r0, m0, L, theta, epsilon)
        bh_all[theta] = bh
    for key, value in bh_all.items():
        plt.plot(nums, value, label='Barnes-Hut: theta='+str(key))
        

    plt.plot(nums, bf, label='Brute Force')
    plt.xlabel("N-bodies")
    plt.ylabel("Time")
    plt.title("Time to compute forces for N bodies - Comparisons")
    plt.legend()
    plt.savefig(dir+'Comparison_time.png')
    plt.show()

def plot_Quadtree(bodies, tree, theta, epsilon, dir):
    for body in bodies:
        tree.insertBody(body)
        body.resetForce()
        body.plot_body()
        tree.applyForce(body, theta, epsilon)

    tree.plot()
    plt.savefig(dir+'BH_Quad.png')
    #plt.show()