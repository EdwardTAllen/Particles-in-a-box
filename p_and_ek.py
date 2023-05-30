# This module will be used to plot the total energy and momentum over time in the model

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#creating subplots
fig,ax = plt.subplots()

#reading the data frame 
dframe = pd.read_excel('dataframe.xlsx')

max_time = dframe['time'].max() # find the total amount of iterations

# all plottable x and y lists
Energy_list = []
momentum_list = []
time = list(range(max_time))


def generate_yvalues():
    '''
    The function here extracts the data of total kinetic energy and
    total momentum for each time interval.
    '''
    for i in range(0, max_time):
        times = dframe[dframe['time'] == i]
        ek = times['Ek'].sum()
        mo = times['p'].sum()
        Energy_list.append(ek)
        momentum_list.append(mo)

generate_yvalues()

#plotting the data
#plotting the kinetic energy
ax.plot(time, Energy_list)
ax.set_xlabel('Time')
ax.set_ylabel('Kinetic Energy')
ax.tick_params(axis='x', direction='in') # x ticks point in 
ax.tick_params(axis='y', direction='in') # y ticks point in
ax.plot(time, momentum_list)

#plotting the momnetum
ax2 = ax.twinx() # a second axis is generated here
ax2.plot(time, momentum_list)
ax2.set_ylabel('momentum')
ax2.tick_params(axis='x', direction='in') # x ticks point in 
ax2.tick_params(axis='y', direction='in') # y ticks point in

#render the plot
plt.show()