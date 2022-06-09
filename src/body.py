import numpy as np
import matplotlib.pyplot as plt
#gravitational force definition
G = 6.674e-11 #N/m^2/kg^2
G = 0.449 #kpc^3/[kMs]/[10Myr]^2

#class: massive objects in space
class Body:
    """definition for object with mass"""
    def __init__(self, mass, rx, ry, vx=0, vy=0, fx=0, fy=0, L=0, color='k'):
        self.m = mass
        self.r = np.array([rx,ry])
        self.v = np.array([vx,vy])
        self.f = np.array([fx,fy])
        self.L = L
        self.c = color
    
    def update(self, dt):
        #update position velocity using Euler-Cromer
        self.v = self.v + (self.f/self.m)*dt
        self.r = np.mod(self.r + self.v*dt + self.L, 2*self.L) - self.L
    # def leapFrog(self, dt):
    #     #take symplectic step with velocity half step
    #     self.v = self.v + (self.f/self.m)*0.5*dt
    #     self.r = np.mod(self.r + self.v*dt + self.L, 2*self.L) - self.L
    # def vHalfStep(self, dt):
    #     #take velocity half step to match with position time
    #     return self.v + (self.f/self.m)*0.5*dt
        
    def distanceTo(self, body):
        #distance from self to body
        dr = self.r-body.r
        return np.sqrt(dr.dot(dr))

    def resetForce(self, fx=0, fy=0):
        #reset force to zero
        self.f = np.array([fx, fy])
    def addForce(self, body, epsilon):
        #force on self from body
        dr = self.r-body.r
        d = np.sqrt(dr.dot(dr) + epsilon**2)
        df = -G*self.m*body.m*dr/d**3
        #add force contribution from body
        self.f = self.f + df

    # def Kenergy(self, dt):
    #     #compute kinetic energy
    #     v = self.vHalfStep(dt)
    #     return 0.5*self.m*np.sqrt(v.dot(v))
    # def Uinteract(self, body):
    #     #compute interaction potential
    #     return -G*self.m*body.m/self.distanceTo(body)

    def inQuad(self, quad):
        rx, ry = self.r[0], self.r[1]
        qx, qy, qL = quad.r[0], quad.r[1], quad.L
        #check if self in in quadrant
        inX = rx >= qx and rx < qx+qL
        inY = ry >= qy and ry < qy+qL
        if inX and inY:
            return True
        else:
            return False

    def plot(self):
        rx, ry = self.r[0], self.r[1]
        #vx, vy = self.v[0], self.v[1]
        #v = np.sqrt(self.v[0]**2+self.v[1]**2)
        #plot body as point
        plt.scatter(rx, ry, c=self.c)
        #plot velocity as direction
        #plt.plot([rx,rx+vx/v], [ry,ry+vy/v], c=self.c)