# Purpose : create beam file for the positron simulation for the experiment, removing the entries with a Nan and changing the z value of those outside the cell. Introducing an x and y distribution to the values outside the cell
# this is specifically for the negative field simulations because the z value that determines outside the cell changed to the previous file
# 
# Input : beamlossntuple from the muon simulation of the experiment 
# Output : beam file for positron simulation, and file to hold all the Nan entries 
#
# Limtiation :
import numpy as np 

with open('beam.txt', 'a') as f:
		f.write('#x' + ' ' + 'y' + ' ' + 'z' + ' ' + 'Px' + ' ' + 'Py' + ' ' + 'Pz' + ' ' + 't' +  ' ' + 'PDGid' + ' ' + 'EventNum' + ' ' + 'TRACKID' + ' ' + 'Parent' + ' ' + 'Weight' +  ' ' + 'Bx' + ' ' + 'By' + ' ' +  'Bz' + ' ' + 'Ex' + ' ' + 'Ey' + ' ' + 'Ez' + ' ' + 'ProperTime' + ' ' + 'PathLength' + ' ' + 'PolX' + ' ' + 'PolY' + ' ' + 'PolZ'  + ' ' + 'InitX' + ' ' + 'InitY' + ' ' + 'InitZ' + ' ' + 'InitT' + ' ' + 'InitKE' + '\r\n')

f.close()

with open('nan_outside.txt', 'a') as f:
		f.write('#x' + ' ' + 'y' + ' ' + 'z' + ' ' + 'Px' + ' ' + 'Py' + ' ' + 'Pz' + ' ' + 't' +  ' ' + 'PDGid' + ' ' + 'EventNum' + ' ' + 'TRACKID' + ' ' + 'Parent' + ' ' + 'Weight' +  ' ' + 'Bx' + ' ' + 'By' + ' ' +  'Bz' + ' ' + 'Ex' + ' ' + 'Ey' + ' ' + 'Ez' + ' ' + 'ProperTime' + ' ' + 'PathLength' + ' ' + 'PolX' + ' ' + 'PolY' + ' ' + 'PolZ'  + ' ' + 'InitX' + ' ' + 'InitY' + ' ' + 'InitZ' + ' ' + 'InitT' + ' ' + 'InitKE' + '\r\n')

f.close()

filename = 'all_loss.txt'
x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE = np.loadtxt(filename, unpack=True)

print('phew')

N = (z < -40).sum()

mean = 0
sigma = 5

samples = N

x_dist = np.random.normal(mean, sigma, samples)
y_dist = np.random.normal(mean, sigma, samples)

j = 0 

for i in range(0, len(Px), 1):


	if np.isnan(Px[i]) or np.isnan(Py[i]) or np.isnan(Pz[i]) or np.isnan(t[i]) or np.isnan(x[i]) or np.isnan(y[i]) or np.isnan(z[i]) :
		print('got one')
		with open('nan_outside.txt', 'a') as g:
			g.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')
	else:
		if z[i] < -40 :
			z[i] = -40
			with open('beam.txt', 'a') as f:
				f.write(str(x_dist[j]) + ' ' + str(y_dist[j]) + ' ' + str(z[i]) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')
			j = j + 1
		else :
			with open('beam.txt', 'a') as f:
				f.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')

f.close()
g.close()
