import numpy as np 
import matplotlib.pyplot as plt


x,y,z,Px,Py,Pz,t_1,PDGid,EventID,TrackID,ParentID,Weight = np.loadtxt(Det1, unpack=True)
x,y,z,Px,Py,Pz,t_2,PDGid,EventID,TrackID,ParentID,Weight = np.loadtxt(Det2, unpack=True)


plt.hist(t_1, bins=10)
plt.save()