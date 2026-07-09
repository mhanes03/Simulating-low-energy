# Purpose : For each zntuple the mean energy and time value with the number of muons at these values 
#
# Input : zntuples 
# Output : file that holds the number of muons, mean energy and time 
#
# Limitations : The number of entries does not take into account double counts this can be done using the unique command on the EventID

import numpy as np 

# parameters of the cell ran by simulation 
cell_length = 1000
cell_start = 10
step = 0.1
N = 100 

# opens new file for data to be written to 
open('energy_and_number.txt', 'x')

# loops over each of the zntuples files and extracts the momentum and finds the mean
for i in range (10, 1010, 10):
  file = 'Z' + str(int(i)) + '.txt'
  #x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(file, unpack=True)
  x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight = np.loadtxt(file, unpack=True)
  
  # finds the mean and the average value 
  P = (Px**2 + Py**2 + Pz**2)
  #np.delete(P, np.where(P == nan))

  P = P[~np.isnan(P)]
  P_mean = np.mean(P)
  E_mean = P_mean/(2*105.66)

  z = z[~np.isnan(z)]
  number_of_muons = len(z)
  z = np.mean(z)

  t = t[~np.isnan(t)]
  time = np.mean(t)

  # writes the values to file
  with open('energy_and_number.txt', 'a') as f:
  	f.write(str(z) + ' ' + str(E_mean)+ ' ' + str(number_of_muons) +' ' + str(time) + '\n')

  f.close()
