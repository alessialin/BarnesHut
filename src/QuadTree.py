#essential modules
import numpy as np
import matplotlib.pyplot as plt

#class: a quadrant in space
class Quad:
    """definition of a quadrant in 2D space"""
    def __init__(self, rx, ry, L):
        #anchor lower left corner
        self.r = np.array([rx,ry])
        #side length
        self.L = L

    #return subquadrants
    def SW(self):
        #return northwest quadrant
        return Quad(self.r[0], self.r[1], self.L/2.0)
    def SE(self):
        #return northwest quadrant
        return Quad(self.r[0]+self.L/2.0, self.r[1], self.L/2.0)
    def NW(self):
        #return northwest quadrant
        return Quad(self.r[0], self.r[1]+self.L/2.0, self.L/2.0)
    def NE(self):
        #return northwest quadrant
        return Quad(self.r[0]+self.L/2.0, self.r[1]+self.L/2.0, self.L/2.0)

    def plot(self):
        #plot quadrant
        rx, ry, L = self.r[0], self.r[1], self.L
        plt.plot([rx, rx+L], [ry, ry], c='b')
        plt.plot([rx, rx], [ry, ry+L], c='b')
        plt.plot([rx+L, rx+L], [ry, ry+L], c='b')
        plt.plot([rx, rx+L], [ry+L, ry+L], c='b')