# Purpose : attempt to make the beam file for the muons taken from the beamloss file, and introduces an x and y distribution 
#
# Input : beamloss files for each part of the cell
# Output : beam file
# 
# Limitations : it needs to load a lot of files in, because each of the beamloss files are separate 
import numpy as np

filename = 'outside_cell.txt'
x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE = np.loadtxt(filename, unpack=True)

z = 142 

mean = 0
sigma = 5

samples = len(x)

x_dist = np.random.normal(mean, sigma, samples)
y_dist = np.random.normal(mean, sigma, samples)

with open('beam.txt', 'a') as f:
		f.write('#x' + ' ' + 'y' + ' ' + 'z' + ' ' + 'Px' + ' ' + 'Py' + ' ' + 'Pz' + ' ' + 't' +  ' ' + 'PDGid' + ' ' + 'EventNum' + ' ' + 'TRACKID' + ' ' + 'Parent' + ' ' + 'Weight' +  ' ' + 'Bx' + ' ' + 'By' + ' ' +  'Bz' + ' ' + 'Ex' + ' ' + 'Ey' + ' ' + 'Ez' + ' ' + 'ProperTime' + ' ' + 'PathLength' + ' ' + 'PolX' + ' ' + 'PolY' + ' ' + 'PolZ'  + ' ' + 'InitX' + ' ' + 'InitY' + ' ' + 'InitZ' + ' ' + 'InitT' + ' ' + 'InitKE' + '\r\n')

f.close()

with open('nan_outside.txt', 'a') as f:
		f.write('#x' + ' ' + 'y' + ' ' + 'z' + ' ' + 'Px' + ' ' + 'Py' + ' ' + 'Pz' + ' ' + 't' +  ' ' + 'PDGid' + ' ' + 'EventNum' + ' ' + 'TRACKID' + ' ' + 'Parent' + ' ' + 'Weight' +  ' ' + 'Bx' + ' ' + 'By' + ' ' +  'Bz' + ' ' + 'Ex' + ' ' + 'Ey' + ' ' + 'Ez' + ' ' + 'ProperTime' + ' ' + 'PathLength' + ' ' + 'PolX' + ' ' + 'PolY' + ' ' + 'PolZ'  + ' ' + 'InitX' + ' ' + 'InitY' + ' ' + 'InitZ' + ' ' + 'InitT' + ' ' + 'InitKE' + '\r\n')

f.close()


for i in range(0, len(Px), 1):


	if np.isnan(Px[i]) or np.isnan(Py[i]) or np.isnan(Pz[i]) or np.isnan(t[i]) :
		print('got one')
		with open('nan_outside.txt', 'a') as g:
			g.write(str(x_dist[i]) + ' ' + str(y_dist[i]) + ' ' + str(z) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')
	else:
		with open('beam.txt', 'a') as f:
			f.write(str(x_dist[i]) + ' ' + str(y_dist[i]) + ' ' + str(z) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')

f.close()
g.close()

filename = 'in_lead.txt'
x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE = np.loadtxt(filename, unpack=True)


for i in range(0, len(Px), 1):


	if np.isnan(Px[i]) or np.isnan(Py[i]) or np.isnan(Pz[i]) or np.isnan(t[i]) or np.isnan(x[i]) or np.isnan(y[i]) or np.isnan(z[i]) :
		print('got one')
		with open('nan_outside.txt', 'a') as g:
			g.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')
	else:
		with open('beam.txt', 'a') as f:
			f.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')

f.close()
g.close()

filename = 'in_degrader.txt'
x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE = np.loadtxt(filename, unpack=True)


for i in range(0, len(Px), 1):


	if np.isnan(Px[i]) or np.isnan(Py[i]) or np.isnan(Pz[i]) or np.isnan(t[i]) or np.isnan(x[i]) or np.isnan(y[i]) or np.isnan(z[i]) :
		print('got one')
		with open('nan_outside.txt', 'a') as g:
			g.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')
	else:
		with open('beam.txt', 'a') as f:
			f.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')

f.close()
g.close()

filename = 'beamlossinwalls.txt'
x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE = np.loadtxt(filename, unpack=True)


for i in range(0, len(Px), 1):


	if np.isnan(Px[i]) or np.isnan(Py[i]) or np.isnan(Pz[i]) or np.isnan(t[i]) or np.isnan(x[i]) or np.isnan(y[i]) or np.isnan(z[i]) :
		print('got one')
		with open('nan_outside.txt', 'a') as g:
			g.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')
	else:
		with open('beam.txt', 'a') as f:
			f.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')

f.close()
g.close()

filename = 'beamlossincell.txt'
x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE = np.loadtxt(filename, unpack=True)


for i in range(0, len(Px), 1):


	if np.isnan(Px[i]) or np.isnan(Py[i]) or np.isnan(Pz[i]) or np.isnan(t[i]) or np.isnan(x[i]) or np.isnan(y[i]) or np.isnan(z[i]) :
		print('got one')
		with open('nan_outside.txt', 'a') as g:
			g.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')
	else:
		with open('beam.txt', 'a') as f:
			f.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')

f.close()
g.close()
