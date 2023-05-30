# In this module a class describes the atributes of every gas molecule created inside the box

# Imports
import random
import numpy as np

x_up = 10
x_low = 5

class molecule():
    '''
    A class to allow the genration of molecules, giving them multiple 
    atributes: mass, radius, label, position, velocity, momentum,
    kinetic energy. The molecules all have the same mass, so their
    elastic collsions.
    '''
    def __init__(self, mass, radius, label):
        self.mass = mass
        self.radius = radius
        self.label = label
        self.pos = np.array([random.uniform(5,10),random.uniform(5,10) , random.uniform(5,10)])
        self.vel = np.array([random.uniform(-2,2), random.uniform(-2,2), random.uniform(-2,2)])
        self.momentum = 0
        self.Ek = 0 # kinetic energy

    def update(self, molecules):
        '''
        This fucntion updates all the atributes of the particles by
        thier interaction with the walls and the other particles.
        '''
        # colisions with other molecules
        dt = 0.01 # time interval
        for m in molecules:
            if self.label != m.label:
                if -self.radius < np.linalg.norm(m.pos - self.pos) < self.radius:
                    temp = m.vel # swapping the values of the velocities
                    m.vel = self.vel
                    self.vel = temp
    
        # colisions witht the wall
        if not x_low < self.pos[0] < x_up:
            self.vel[0] = -self.vel[0]
        if not x_low < self.pos[1] < x_up:
            self.vel[1] = -self.vel[1]   
        if not x_low < self.pos[2] < x_up:
            self.vel[2] = -self.vel[2] 

        self.pos += self.vel*dt

        # updating the momentum
        vel_sclr = np.linalg.norm(self.vel)
        self.momentum = vel_sclr*self.mass

        #updating the kinetic energy
        self.Ek = 0.5*self.mass*vel_sclr**2

        return self.pos