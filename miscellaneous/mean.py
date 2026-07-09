# Purpose : find the mean energy at a certain z value 
#
# Input : zntuple for a particular z value 
# Output : the mean energy 
#
# Limtiations : 

import numpy as np 

file = 'Z200.txt'

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight= np.loadtxt(file, unpack=True)
E = (Px**2 + Py**2 + Pz**2)/(2*105.66)
E = E[~np.isnan(E)]
mean = np.mean(E)

print('mean at 200 mm', mean)


file = 'Z500.txt'

#x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight= np.loadtxt(file, unpack=True)
#E = (Px**2 + Py**2 + Pz**2)/(2*105.66)
#E = E[~np.isnan(E)]
#mean = np.mean(E)

#print('mean at 500 mm', mean)
