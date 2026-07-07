import numpy as np 

filename = 'counts.txt'
with open(filename, 'a') as f:
	f.write('# N' + '\n')
f.close()


beamloss = 'all_loss.txt'

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(beamloss, unpack=True)

N = len(x)

with open(filename, 'a') as f:
	f.write(str(beamloss) + ' ' + str(N) + '\n')
f.close()


detector1 = 'Det1.txt'

#x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(detector1, unpack=True)
x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight = np.loadtxt(detector1, unpack=True)

N = len(x)

# writes the values to file
with open(filename, 'a') as f:
	f.write(str(detector1) + ' ' + str(N) + '\n')
f.close()

detector2 = 'Det2.txt'

#x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(detector2, unpack=True)
x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight = np.loadtxt(detector2, unpack=True)

N = len(x)

# writes the values to file
with open(filename, 'a') as f:
	f.write(str(detector2) + ' ' + str(N) + '\n')
f.close()

beamloss = 'positrons.txt'

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(beamloss, unpack=True)

N = len(x)

with open(filename, 'a') as f:
	f.write(str(beamloss) + ' ' + str(N) + '\n')
f.close()


