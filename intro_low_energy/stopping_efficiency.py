# extracts all the parameters from the beamlossntuple
# calculates the stopping efficiency of the muons by finding length 
# of the z array that is extracted from the beamlossntuple and dividing by number of muons

import numpy as np 

# reads in the thickness
initial_muons = 5000

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt('beamloss.txt', skiprows = 2, unpack=True)

# finds the length of z array and this number of stopped muons 
stopped_muons = len(z)
efficiency = stopped_muons/initial_muons
z_avg = np.mean(z)

# prints to screen so that can be written to file
print('Average stopping distance :', z_avg)
print('Stopping efficiency :', efficiency)