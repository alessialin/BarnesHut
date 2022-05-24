# info on huge ass celestial body 
import matplotlib.pyplot as plt
import numpy as np

G = 1 #6.674e-11 #N/m^2/kg^2

class Body:
    # f = force, v = velocity
    def __init__(self, mass, rx, ry, vx=0, vy=0, fx=0, fy=0, s=0, color='k'):
        self.mass = mass
        self.r = np.array([rx, ry])
        self.velocity = np.array([vx, vy])
        self.force = np.array([fx, fy])
        self.s = s #side
        self.color = color

    def distance(self, body):
        #distance self to body
        dr = self.r - body.r
        return np.sqrt(dr.dot(dr))

    def resetForce(self):
        self.force = np.array([0,0])
    
    def addForce(self, body, epsilon=1e-5):
        #add force contribution to self (this is the F formula)
        dr = self.r - body.r
        d = np.sqrt(dr.dot(dr) + epsilon**2)
        delta_f = -G * self.mass * body.mass * dr/d**3
        self.force = self.force + delta_f
    
    def updateForce(self, delta_f):
        self.force = self.force + delta_f
    
    def update(self, delta_t):
        self.velocity += delta_t * self.force / self.mass
        self.r += self.velocity * delta_t

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
