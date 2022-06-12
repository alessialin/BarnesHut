import matplotlib.pyplot as plt

from time import process_time
from tqdm import tqdm


# from src.body import *
from ..node import Node
from ..quadtree import Quad
from ..utils import generateGalaxy

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
        for body in bodies:
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