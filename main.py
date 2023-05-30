# the plot is rendered in this module

# imports
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation
import random
import pandas as pd
from gas_molecules import molecule
from plotting import Plot

# the data frame is opended and read here
dframe = pd.read_excel('dataframe.xlsx')

# the data frame is plotted here
plot1 = Plot(dframe)