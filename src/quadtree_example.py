import numpy as np

from body import *
from node import *
from quadtree import *
from utils import *

if __name__ == '__main__':

    dir = '/output'

    N = 15 #number of bodies
    L = 20
    m = 10
    epsilon = 0.1
    theta = 0.5

    bodies = []
    tree = Node(Quad(-L,-L,2*L))

    for i in range(N):
        body = Body(m, np.random.uniform(-L+3, L-3),np.random.uniform(-L+3, L-3), L=L)
        bodies.append(body)

    plot_Quadtree(bodies, tree, theta, epsilon, dir)





