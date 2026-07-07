import numpy as np 

# opens new file for data to be written to 
open('number_of_entries.txt', 'x')

file = 'less_1keV_800.txt'
x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(file, unpack=True)
  

number_of_muons = len(x)
with open('number_of_entries.txt', 'a') as f:
  f.write('#z' + ' ' + 'entries' + '\n')

# writes the values to file
with open('number_of_entries.txt', 'a') as f:
  f.write(str(z[0]) + ' ' + str(number_of_muons) + '\n')

f.close()
