# extracts all the parameters from the zntuple 
# calculates the mean value of magnitude of the momentum and writes them to a text file 
# for plotting 

import numpy as np 

# parameters of the cell ran by simulation 
cell_end = 300
cell_start = 10
step = 0.1
N = 100 

filename = 'captured.txt'

# writes the values to file
with open(filename, 'a') as f:
  f.write('# z' + ' ' + 'Energy limit (MeV)' + ' ' + 'Number of muons' + '\n')

  f.close()

# loops over each of the zntuples files and extracts the momentum and finds the mean
for i in range (cell_start, cell_end+cell_start, 10):
  file = 'Z' + str(int(i)) + '.txt'
  x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(file, unpack=True)
  #x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight = np.loadtxt(file, unpack=True)
  
  # finds the mean and the average value 
  P = (Px**2 + Py**2 + Pz**2)

  P = P[~np.isnan(P)]
  E = P/(2*105.66)
  E_limit = 0.001

  N = (E<=E_limit).sum()

  Z = np.mean(z)

  # writes the values to file
  with open(filename, 'a') as f:
  	f.write(str(Z) + ' ' + str(E_limit)+ ' ' + str(N) + '\n')

  f.close()