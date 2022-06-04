from body import *
from quadtree import *

class Node: #BHTree or QuadTree
    """Definition of Node based on Barnes Hut"""
    def __init__(self, quadrant=Quad):
        self.quadrant = quadrant
    
    def insert_body(self, body=Body):
        if hasattr(self, 'body'): #node is not empty
            if self.external: #node is external node, so make it internal
                #create 4 children nodes
                self.SW = Node(self.quadrant.SW())
                self.NW = Node(self.quadrant.NW())
                self.NE = Node(self.quadrant.NE())
                self.SE = Node(self.quadrant.SE())

                # sort node into child trees
                if self.body.inQuad(self.quadrant.SW()):
                    self.SW.insert_body(self.body)
                elif self.body.inQuad(self.quadrant.NW()):
                    self.NW.insert_body(self.body)
                elif self.body.inQuad(self.quadrant.NE()):
                    self.NE.insert_body(self.body)
                elif self.body.inQuad(self.quadrant.SE()):
                    self.SE.insert_body(self.body)
                self.external = False
            # sorting the new body into child trees
            if body.inQuad(self.quadrant.SW()):
                self.SW.insert_body(body)
            if body.inQuad(self.quadrant.NW()):
                self.NW.insert_body(body)
            if body.inQuad(self.quadrant.NE()):
                self.NE.insert_body(body)
            if body.inQuad(self.quadrant.SE()):
                self.SE.insert_body(body)
            
            #adding to node body aggregate of mass
            R, M = self.body.r, self.body.mass
            r, m = body.r, body.mass
            R = (M*R + m*r) / (M+m)
            M += m 
            self.body = Body(M, R[0], R[1]) #big ass body with all the masses and positions r
        else:
            self.body = body
            self.external = True
    
    def applyForce(self, body, theta=0.5, epsilon=1e-5):
        if hasattr(self, 'body'):
            if (self.body.r != body.r).any():
                d = body.distance(self.body) #distance of node body to body 
                if self.quadrant.s/d < theta or self.external:
                    body.addForce(self.body)
                else:
                    #box too close, compute forces from children instead
                    self.SW.applyForce(body, theta, epsilon)
                    self.SE.applyForce(body, theta, epsilon)
                    self.NW.applyForce(body, theta, epsilon)
                    self.NE.applyForce(body, theta, epsilon)

    def plot(self):
        if hasattr(self, 'body'):
            self.quadrant.plot()
            if not self.external: #plot quadrants in every child node
                self.SW.plot()
                self.NW.plot()
                self.NE.plot()
                self.SE.plot()