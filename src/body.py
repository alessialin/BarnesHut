import numpy as np
import matplotlib.pyplot as plt


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
    elif kpc:
        G = 0.449 
    return G

# Massive cloud of points with mass in space
class Body:
    def __init__(self, mass, rx, ry, vx=0, vy=0, fx=0, fy=0, L=0, color='k'):
        self.m = mass
        self.r = np.array([rx,ry])
        self.v = np.array([vx,vy])
        self.f = np.array([fx,fy])
        self.L = L
        self.c = color
    
    def update(self, dt): #update position velocity using Euler-Cromer
        self.v = self.v + (self.f/self.m)*dt
        self.r = np.mod(self.r + self.v*dt + self.L, 2*self.L) - self.L
        
    def distanceTo(self, body): #distance from self to other body
        return np.sqrt((self.r[1]-body.r[1])**2 + (self.r[0]-body.r[0])**2)

    def resetForce(self, fx=0, fy=0):
        self.f = np.array([fx, fy])
        
    def addForce(self, body, epsilon): #force from self to body
        dr = self.r-body.r
        d = np.sqrt(dr.dot(dr) + epsilon**2)
        df = -gravity()*self.m*body.m*dr/d**3
        #add force contribution from body
        self.f = self.f + df

    def inQuad(self, quad):
        rx, ry = self.r[0], self.r[1]
        qx, qy, qL = quad.r[0], quad.r[1], quad.L
        #heck if self is already in quadrant
        inX = rx >= qx and rx < qx+qL
        inY = ry >= qy and ry < qy+qL
        if inX and inY:
            return True
        else:
            return False

    def plot_body(self):
        rx, ry = self.r[0], self.r[1]
        plt.scatter(rx, ry, c=self.c)
    
    def plot_velocity(self):
        rx, ry = self.r[0], self.r[1]
        vx, vy = self.v[0], self.v[1]
        v = np.sqrt(self.v[0]**2+self.v[1]**2)
        #plot body as point
        plt.scatter(rx, ry, c=self.c)
        #plot velocity as direction
        plt.plot([rx,rx+vx/v], [ry,ry+vy/v], c='r')