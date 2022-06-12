from body import Body

#2D Node in Barnes-Hut with 4 child trees
class Node:

    def __init__(self, quad):
        self.quad = quad
        
    def insertBody(self, body):
        #node is not empty
        if hasattr(self, 'body'):
            if self.external:
                #if node is external node (to the quadrant), make into internal node
                self.external = False
                #create 4 child trees
                self.SW = Node(self.quad.SW())
                self.SE = Node(self.quad.SE())
                self.NW = Node(self.quad.NW())
                self.NE = Node(self.quad.NE())
                #sort node body into child trees
                if self.body.inQuad(self.quad.SW()):
                    self.SW.insertBody(self.body)
                if self.body.inQuad(self.quad.SE()):
                    self.SE.insertBody(self.body)
                if self.body.inQuad(self.quad.NW()):
                    self.NW.insertBody(self.body)
                if self.body.inQuad(self.quad.NE()):
                    self.NE.insertBody(self.body)
            #sort new body into child trees
            if body.inQuad(self.quad.SW()):
                self.SW.insertBody(body)
            if body.inQuad(self.quad.SE()):
                self.SE.insertBody(body)
            if body.inQuad(self.quad.NW()):
                self.NW.insertBody(body)
            if body.inQuad(self.quad.NE()):
                self.NE.insertBody(body)
            #add to node body aggregate mass - center of mass (com)
            com_R, com_M = self.body.r, self.body.m
            r, m = body.r, body.m
            com_R = (com_M*com_R + m*r)/(com_M + m) #center of mass location
            com_M += m #aggregate mass
            self.body = Body(com_M, com_R[0], com_R[1])
            
        else:
            #if node is empty, add body and the node external
            self.body = body
            self.external = True
        

    def applyForce(self, body, theta, epsilon): #epsilon = softening length
        """
        theta: float
            Barnes-Hut resolution parameter 
        epsilon : numpy.float64
            softening length, to avoid excessive accelerations in astrophysics
        """
        #not an empty node
        if hasattr(self, 'body'):
            #if it's not a self force
            if (self.body.r != body.r).any():
                d = body.distanceTo(self.body)

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
            self.quad.plot()
            if not self.external:
                #plot quadrants in every child node
                self.SW.plot()
                self.SE.plot()
                self.NW.plot()
                self.NE.plot()