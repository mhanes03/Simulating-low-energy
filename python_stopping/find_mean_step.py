# extracts all the parameters from the zntuple 
# calculates the mean value of magnitude of the momentum and writes them to a text file 
# for plotting 

import numpy as np 

# parameters of the cell ran by simulation 
cell_length = 500
cell_start = 10
step = 0.1
N = 100 

# opens new file for data to be written to 
open('P_mean_versus_z.txt', 'x')

# loops over each of the zntuples files and extracts the momentum and finds the mean
for i in range (0, 51, 1):
  file = 'Z' + str(int(cell_start + 10*i)) + '.txt'
  x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(file, skiprows = 2, unpack=True)
  
  # finds the mean and the average value 
  P = np.sqrt(Px**2 + Py**2 + Pz**2)
  P_mean = np.mean(P)
  z = np.mean(z)

  # writes the values to file
  with open('P_mean_versus_z.txt', 'a') as f:
  	f.write(str(z) + ' ' + str(P_mean)+'\n')


f.close()
