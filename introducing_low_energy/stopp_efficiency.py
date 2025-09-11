# extracts all the parameters from the zntuple 
# calculates the mean value of magnitude of the momentum and writes them to a text file 
# for plotting 

import numpy as np 

initial_muons = 5000
thickness = 0.88

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt('beamloss.txt', skiprows = 2, unpack=True)

z_avg = np.mean(z)

print('Average stopping distance :', z_avg, 'mm')

# extracts all the parameters from the zntuple 
# calculates the mean value of magnitude of the momentum and writes them to a text file 
# for plotting 

stopped_muons = len(z)
efficiency = stopped_muons/initial_muons

print('Stopping efficiency',efficiency)