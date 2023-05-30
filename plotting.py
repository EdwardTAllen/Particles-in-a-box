# Here the 3D plot will be generated

# imports
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation
import random
import pandas as pd

class Plot():
    '''
    A class which allows a 3D animated plot to be generated when
    a given dataframe of a list of particles each with their own 
    position which is updated at each time.
    '''
    def __init__(self, dataframe):
        '''
        Here the perameters are initialised.
        '''
        self.fig = plt.figure()
        self.dataframe = dataframe
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.var=self.dataframe[self.dataframe['time']==0]
        self.l = len(self.var.x)
        self.colour = np.arange(self.l)
        self.graph = self.ax.scatter(self.var.x, self.var.y, self.var.z, marker="o",
            depthshade = False, c = self.colour)
        self.title = self.ax.set_title('3D Test')
        self.ani = matplotlib.animation.FuncAnimation(self.fig, init_func=self.create_boundaries,
            func = self.update_graph, frames = int(self.dataframe['time'].max()), interval=1, blit=False)
        
        plt.show()

    def create_boundaries(self):
        '''
        boundaries need to be generated in this function so that
        the simulation can be confined to a box.
        '''
        maxdist = float(self.dataframe[['x','y','z']].min(axis =1).min())
        mindist = float(self.dataframe[['x','y','z']].max(axis = 1).max())

        self.ax.set_xlim(mindist, maxdist)
        self.ax.set_ylim(mindist, maxdist)
        self.ax.set_zlim(mindist, maxdist)
        return self.graph

    def update_graph(self, num):
        '''
        This function allows the animation to occur as it updates
        the plot for each time in the data frame.
        '''
        var=self.dataframe[self.dataframe['time']==num]
        self.graph._offsets3d = (var.x, var.y, var.z)
        return self.graph