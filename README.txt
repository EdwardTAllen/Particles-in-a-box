README

This project provides a simulation of N-body particles in a closed box used
model gas molecules in a container or closed system. These particles interact
with each other and the wall of the box. At each collision the velocities
of the particles swap direction and momentum is conserved.

FILES CONTAINED IN THIS PROJECT
- 'gas_molecules.py' this is where a class is contained which allows the production
  of gas molecules each having position velocity and momentum as well as 
  methods to update these perameters.
- 'generating_data.py' is where the main loops of the simulation are held
  creating the data frames from all the particle interactions at any given time.
  producing data of all the particles perameters at every time. This data is then
  saved with pandas into an excel file.
- 'plotting.py' contains a plotting class which utilises the 3D animate function of
  matplotlib and allows inputed particle position data and allow a 3D animated plot
  to me visulaised from this showing the particles progression over time.
- 'main.py' runs the data through the plotting class and allows the simulation to be
  run and shown.
- 'p_and_ek.py' extracts the momentum and energy data from the data frame and produces
  a plot shwoing the momentum and kinetic energy over time using matplotlib. 

