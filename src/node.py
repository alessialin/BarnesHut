#essential modules
#import numpy as np
#import matplotlib.pyplot as plt

#essential imports
from body import Body
#from quadtree import Quad

#class: node of Barnes-Hut tree
class BHTree:
    """definition of node of Barnes-Hut tree"""
    def __init__(self, quad):
        self.quad = quad
        
    def insertBody(self, body):
        #add body to Barnes-Hut node
        if hasattr(self, 'body'):
            #node is not empty
            if self.external:
                #node is external node, make into internal node
                self.external = False
                #create 4 child trees
                self.SW = BHTree(self.quad.SW())
                self.SE = BHTree(self.quad.SE())
                self.NW = BHTree(self.quad.NW())
                self.NE = BHTree(self.quad.NE())
                #sort node body into child trees
                if self.body.inQuad(self.quad.SW()):
                    #new body in SW quadrant node
                    self.SW.insertBody(self.body)
                if self.body.inQuad(self.quad.SE()):
                    #new body in SW quadrant node
                    self.SE.insertBody(self.body)
                if self.body.inQuad(self.quad.NW()):
                    #new body in SW quadrant node
                    self.NW.insertBody(self.body)
                if self.body.inQuad(self.quad.NE()):
                    #new body in SW quadrant node
                    self.NE.insertBody(self.body)
            #sort new body into child trees
            if body.inQuad(self.quad.SW()):
                #new body in SW quadrant node
                self.SW.insertBody(body)
            if body.inQuad(self.quad.SE()):
                #new body in SW quadrant node
                self.SE.insertBody(body)
            if body.inQuad(self.quad.NW()):
                #new body in SW quadrant node
                self.NW.insertBody(body)
            if body.inQuad(self.quad.NE()):
                #new body in SW quadrant node
                self.NE.insertBody(body)
            #add to node body aggregate mass
            R, M = self.body.r, self.body.m
            r, m = body.r, body.m
            R = (M*R + m*r)/(M + m)
            M += m
            self.body = Body(M, R[0], R[1])
        else:
            #if node is empty, add body and make external node
            self.body = body
            self.external = True

    def applyForce(self, body, theta, epsilon):
        #evaluate force on body from tree with resolution theta
        if hasattr(self, 'body'):
            #not an empty node
            if (self.body.r != body.r).any():
                #not self force
                d = body.distanceTo(self.body) #distance of node body to body
                if self.quad.L/d < theta or self.external:
                    #box sufficiently far away for its size, compute force
                    body.addForce(self.body, epsilon)
                else:
                    #box too close, compute forces from children instead
                    self.SW.applyForce(body, theta, epsilon)
                    self.SE.applyForce(body, theta, epsilon)
                    self.NW.applyForce(body, theta, epsilon)
                    self.NE.applyForce(body, theta, epsilon)

    def plot(self):
        if hasattr(self, 'body'):
            #not an empty node
            self.quad.plot()
            if not self.external:
                #plot quadrants in every child node
                self.SW.plot()
                self.SE.plot()
                self.NW.plot()
                self.NE.plot()