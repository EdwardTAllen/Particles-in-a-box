#this allows the generation of the data frame of all the particle postions over time

#imports
import random 
import numpy as np
from gas_molecules import molecule
#from membrane import Membrane_junction
import pandas as pd

#lists of data
membrane_section_list = []
molecule_list = [] #list of all the particle objects
data = [] # list of all the atributes of the particles in list particle

# key variables for the data generation
intervals = 500
number_of_molecules = 150
number_of_membrane_sections = 50
#functions to generate all the data:
#def generate_membrane():
#    '''
#    Function producing the seperate membrane physical sections.
#    '''
#    for k in range(number_of_membrane_sections):
#        m = Membrane_junction()
#        membrane_section_list.append()

def generate_particle_list():
    '''
    This fucntion produces a list of particles and names each one
    a corisponding number so that when evaluating the forces, a particle
    won't generate force on its self.
    '''
    for k in range(number_of_molecules):
        p = molecule(label = k, mass = 1, radius = 0.5)
        molecule_list.append(p)

def generate_data_list():
    '''
    The function here updates all the particles postions and velocities and
    adds each stage of update per time to a data base.
    '''
    for i in range(intervals):
        for p in molecule_list:
            p.update(molecules = molecule_list)
            data.append(np.array([p.pos[0],p.pos[1], p.pos[2], i, p.momentum, p.Ek], dtype = float))
            loading = 'loading...', round((i/intervals)*100, 0), '%' #this generates a loading update to see the progress of the data
            print(loading)

# data producing functions are returned here            
generate_particle_list()
generate_data_list()

# Here a data frame of the particles data is generated
dframe = pd.DataFrame(data, columns=['x', 'y', 'z', 'time', 'p', 'Ek'])

# This saves the data of the particles to an excel sheet
dframe.to_excel('dataframe.xlsx', sheet_name='new_sheet_name')

print('complete')
