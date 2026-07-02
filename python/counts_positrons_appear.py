import numpy as np 

filename = 'positrons_produced.txt'
with open(filename, 'a') as f:
	f.write('# N' + '\n')
f.close()

beamloss = 'positronsincell.txt'

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(beamloss, unpack=True)

N = len(x)

with open(filename, 'a') as f:
	f.write(str(beamloss) + ' ' + str(N) + '\n')
f.close()

beamloss = 'positrondegrader.txt'

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(beamloss, unpack=True)

N = len(x)

with open(filename, 'a') as f:
	f.write(str(beamloss) + ' ' + str(N) + '\n')
f.close()

beamloss = 'positronsinwalls.txt'

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(beamloss, unpack=True)

N = len(x)

with open(filename, 'a') as f:
	f.write(str(beamloss) + ' ' + str(N) + '\n')
f.close()

beamloss = 'positroninlead.txt'

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(beamloss, unpack=True)

N = len(x)

with open(filename, 'a') as f:
	f.write(str(beamloss) + ' ' + str(N) + '\n')
f.close()

beamloss = 'positrons.txt'

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(beamloss, unpack=True)

N = len(x)

with open(filename, 'a') as f:
	f.write(str(beamloss) + ' ' + str(N) + '\n')
f.close()