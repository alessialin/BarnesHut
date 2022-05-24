# QuadTree structure + massive body
import matplotlib.pyplot as plt
import numpy as np

class QuadTree:
    """
    Defining a 2D quadrant for Barnes Hut.
    
    Parameters: 
    -----------
        rx : int
            x-axis of left corner of quadrant
        ry : int
            y-axis of left corner of quadrant
        s : float
            quadrant side length
    """
    def __init__(self, rx, ry, s:float):
        self.r = np.array([rx, ry])
        self.s = float(s)
    
    # subquadrants (SW = southwest, NW = northwest, NE = northeast, SE = southeast)
    def SW(self):
        return QuadTree(self.r[0], self.r[1], self.s/2.0)
    
    def NW(self):
        return QuadTree(self.r[0], self.r[1]+self.s/2.0, self.s/2.0)

    def NE(self):
        return QuadTree(self.r[0]+self.s/2.0, self.r[1]+self.s/2.0, self.s/2.0)

    def SE(self):
        return QuadTree(self.r[0]+self.s/2.0, self.r[1], self.s/2.0)

    def plot_Quad(self):
        rx, ry, s = self.r[0], self.r[1], self.s
        plt.plot([rx, rx+s], [ry+ry], c='k')
        plt.plot([rx,rx], [ry,ry+s], c='k')
        plt.plot([rx+s,rx+s], [ry,ry+s], c='k')
        plt.plot([rx,rx+s], [ry+s,ry+s], c='k')

