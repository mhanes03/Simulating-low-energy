import numpy as np 

# parameters of the cell ran by simulation 
cell_length = 130
cell_start = 10
radius = 12

step = 10
N = 100 

filename = 'in_cell_2.txt'
with open(filename, 'a') as f:
	f.write('# z' + ' ' + 'N_eqm' + ' ' + 'N_less' + ' ' + 'N_high' + '\n')
f.close()

# loops over each of the zntuples files and extracts the momentum and finds the mean
for i in range (cell_start, cell_length+2*step, step):
  file = 'in_cell_Z' + str(int(i)) + '.txt'
  #file = 'Z' + str(int(i)) + '.txt'
  x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(file, unpack=True)
  #x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight = np.loadtxt(file, unpack=True)
  E = (Px**2 + Py**2 + Pz**2)/(2*105.66)

  E_mean = 0.0002
  spread = 0.14 
  std = E_mean*spread

  #E_low = E_mean - 3*std
  #E_high = E_mean + 3*std 

  E_low = 10*1e-6
  E_high = 600*1e-6

  N_less = (E < E_low).sum()
  N_high = (E > E_high).sum()

  N = N_less + N_high

  # captured muons 
  N_eqm = len(E) - N

  # writes the values to file
  with open(filename, 'a') as f:
  	f.write(str(i) + ' ' + str(N_eqm) + ' ' + str(N_less) + ' ' + str(N_high) + '\n')

  f.close()
