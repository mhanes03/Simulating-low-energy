import numpy as np 

filename = 'muon_counts_loss.txt'
with open(filename, 'a') as f:
	f.write('# N' + '\n')
f.close()

beamloss = 'beamlossincell.txt'

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(beamloss, unpack=True)

N = len(x)

with open(filename, 'a') as f:
	f.write(str(beamloss) + ' ' + str(N) + '\n')
f.close()

beamloss = 'in_degrader.txt'

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(beamloss, unpack=True)

N = len(x)

with open(filename, 'a') as f:
	f.write(str(beamloss) + ' ' + str(N) + '\n')
f.close()

beamloss = 'beamlossinwalls.txt'

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(beamloss, unpack=True)

N = len(x)

with open(filename, 'a') as f:
	f.write(str(beamloss) + ' ' + str(N) + '\n')
f.close()

beamloss = 'in_lead.txt'

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(beamloss, unpack=True)

N = len(x)

with open(filename, 'a') as f:
	f.write(str(beamloss) + ' ' + str(N) + '\n')
f.close()

beamloss = 'all_loss.txt'

x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(beamloss, unpack=True)

N = len(x)

with open(filename, 'a') as f:
	f.write(str(beamloss) + ' ' + str(N) + '\n')
f.close()