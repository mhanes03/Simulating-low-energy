import numpy as np 

mass_density = change_mass_density
thickness = change_thickness
input_energy = change_energy
initial_muons = 10000

# opens new file for data to be written to 
open('stopping_power.txt', 'x')

file = 'Z10.txt'
x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(file, unpack=True)
  
# finds the mean and the average value 
P = (Px**2 + Py**2 + Pz**2)

P = P[~np.isnan(P)]
#P_mean = np.mean(P)

P_mean = np.sum(P)/initial_muons
E_mean = P_mean/(2*105.66)


#z = z[~np.isnan(z)]
number_of_muons = len(P)

dE = input_energy - E_mean

stopping_power = dE/(mass_density*(thickness/10))

# writes the values to file
with open('stopping_power.txt', 'a') as f:
  f.write(str(input_energy) + ' ' + str(E_mean) + ' ' + str(stopping_power) + ' ' + str(number_of_muons) + '\n')

f.close()