# info on huge ass celestial body 
import matplotlib.pyplot as plt
import numpy as np

G = 1 #6.674e-11 #N/mass^2/kg^2
G = 0.449 #kpc^3/[kMs]/[10Myr]^2

class Body:
    # f = force, s = box boundary
    def __init__(self, mass, rx, ry, vx=0, vy=0, fx=0, fy=0, s=0, color='k'): 
        self.mass = mass
        self.r = np.array([rx, ry])
        self.velocity = np.array([vx, vy])
        self.force = np.array([fx, fy])
        self.s = s #side
        self.color = color

    def update(self, delta_t):
        #update position velocity using Euler-Cromer
        self.velocity = self.velocity + (self.force/self.mass)*delta_t
        self.r = np.mod(self.r + self.velocity*delta_t + self.s, 2*self.s) - self.s

    def leapFrog(self, delta_t):
        #take symplectic step with velocity half step
        self.velocity = self.velocity + (self.force/self.mass)*0.5*delta_t
        self.r = np.mod(self.r + self.velocity*delta_t + self.s, 2*self.s) - self.s

    def vHalfStep(self, delta_t):
        #take velocity half step to match with position time
        return self.velocity + (self.force/self.mass)*0.5*delta_t

    def distance_to(self, body):
        #distance self to body
        dr = self.r - body.r
        return np.sqrt(dr.dot(dr))

    def resetForce(self, fx=0, fy=0):
        self.force = np.array([fx,fy])
    
    def addForce(self, body, epsilon=1e-5):
        #add force contribution to self (this is the F formula)
        dr = self.r - body.r
        d = np.sqrt(dr.dot(dr) + epsilon**2)
        delta_f = -G * self.mass * body.mass * dr/d**3
        self.force = self.force + delta_f

    def Kenergy(self, dt):
        #compute kinetic energy
        v = self.vHalfStep(dt)
        return 0.5*self.mass*np.sqrt(v.dot(v))
        
    def Uinteract(self, body):
        #compute interaction potential
        return -G*self.mass*body.mass/self.distance_to(body)

    def inQuad(self, quadrant):
        #checking if self is in the quadrant
        rx, ry = self.r[0], self.r[1]
        inX = rx >= quadrant.r[0] and rx < quadrant.r[0]+quadrant.s
        inY = ry >= quadrant.r[1] and ry < quadrant.r[1]+quadrant.s

        if inX and inY:
            return True
        else:
            return False
    
    def plot(self):
        rx, ry = self.r[0], self.r[1]
        plt.scatter(rx, ry, color=self.color)
