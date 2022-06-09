import numpy as np
import matplotlib.pyplot as plt

#essential imports
from body import Body

#function: initialize array of bodies in a galaxy
def generateGalaxy(r0, m0, N, L, c_vel=[0.,0.], center=[0.,0.], color='k'):
    #divide mass of galaxy among N masses
    m = m0/N
    #generate N bodies
    bodies = []
    for i in range(N):
        #position from normalized distribution p(R) = (1/r0)exp(-r/r0)
        r = -r0*np.log(1.0-np.random.rand())
        if r < L:
            theta = 2.0*np.pi*np.random.rand()
            rx = center[0] + r*np.cos(theta)
            ry = center[1] + r*np.sin(theta)
            #velocity from naive estimate v ~ sqrt(GMgalaxy/r)
            v = 4.738*np.exp(-r0/r)/np.sqrt(r)
            vx = -v*np.sin(theta) + c_vel[0]
            vy = v*np.cos(theta)+ c_vel[1]
            #generate body
            bodies.append(Body(m, rx, ry, vx=vx, vy=vy, L=L+center[0], color=color))
    return bodies

# #function: initialize array of bodies in uniform box
# def generateUniform(m0, c_vel:np.array, N, L):
#     #divide total among N masses
#     m = m0/N
#     a=0.5
#     b=0.6
#     #generate N bodies randomly distributed in box
#     bodies = []
#     for i in range(N):
#         theta = np.random.rand(N)
#         r = a*np.exp(b*theta)
#         if r < L:
#             vx, vy = np.sin(theta)*29791.032 + c_vel[0], -np.cos(theta)*29791.032 + c_vel[1]
#             rx, ry = r*np.cos(theta+np.pi), r*np.sin(theta+np.pi)
#             #generate body
#             bodies.append(Body(m, rx, ry, vx=vx, vy=vy, L=L))
#     return bodies 

