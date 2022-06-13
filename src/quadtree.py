import numpy as np
import matplotlib.pyplot as plt

#Quadrant in 2D space
class Quad:

    def __init__(self, rx, ry, L):
        self.r = np.array([rx,ry]) #anchor lower left corner
        self.L = L  #quadrant side length

    # 4 Subquadrants
    def SW(self):
        #northwest quadrant
        return Quad(self.r[0], self.r[1], self.L/2.0)
    def SE(self):
        #southwest quadrant
        return Quad(self.r[0]+self.L/2.0, self.r[1], self.L/2.0)
    def NW(self):
        #northwest quadrant
        return Quad(self.r[0], self.r[1]+self.L/2.0, self.L/2.0)
    def NE(self):
        #northeast quadrant
        return Quad(self.r[0]+self.L/2.0, self.r[1]+self.L/2.0, self.L/2.0)

    def plot(self):
        rx, ry, L = self.r[0], self.r[1], self.L
        plt.plot([rx, rx+L], [ry, ry], c='b')
        plt.plot([rx, rx], [ry, ry+L], c='b')
        plt.plot([rx+L, rx+L], [ry, ry+L], c='b')
        plt.plot([rx, rx+L], [ry+L, ry+L], c='b')
