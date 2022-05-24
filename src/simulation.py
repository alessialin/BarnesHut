import math
import matplotlib.pyplot as plt
import numpy as np

from body import *

def gravitational_constant():
    return 4.302e-3  # pc(M_solar)^-1 (km/s)^2

def generateGalaxy(r0, mass, n, s):
    """n = number of celestial bodies in the galaxy"""
    m = mass/n

    #Generate n bodies 
    bodies = []
    for i in range(n):
        r = -r0 * np.log(1.0-np.random.rand())
        if r < s:
            theta = 2.0*math.pi*np.random.rand()
            rx = r*np.cos(theta)
            ry = r*np.sin(theta)
            v = gravitational_constant()*np.exp(-r0/r)/np.sqrt(r)
            vx = -v*np.sin(theta)
            vy = v*np.cos(theta)
            bodies.append(Body(m, rx, ry, vx=vx, vy=vy, s=s))
    return bodies