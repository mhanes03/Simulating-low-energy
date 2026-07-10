# extracts all the parameters from the zntuple 
# calculates the mean value of magnitude of the momentum and writes them to a text file 
# for plotting 

import numpy as np 

initial_muons = 5000
thickness = change_this

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt('0.001.txt', skiprows = 2, unpack=True)

z_avg = np.mean(z)

print(thickness, z_avg)
