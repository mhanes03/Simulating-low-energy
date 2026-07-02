import numpy as np 

with open('new_outside_cell', 'a') as f:
		f.write('#x' + ' ' + 'y' + ' ' + 'z' + ' ' + 'Px' + ' ' + 'Py' + ' ' + 'Pz' + ' ' + 't' +  ' ' + 'PDGid' + ' ' + 'EventNum' + ' ' + 'TRACKID' + ' ' + 'Parent' + ' ' + 'Weight' +  ' ' + 'Bx' + ' ' + 'By' + ' ' +  'Bz' + ' ' + 'Ex' + ' ' + 'Ey' + ' ' + 'Ez' + ' ' + 'ProperTime' + ' ' + 'PathLength' + ' ' + 'PolX' + ' ' + 'PolY' + ' ' + 'PolZ'  + ' ' + 'InitX' + ' ' + 'InitY' + ' ' + 'InitZ' + ' ' + 'InitT' + ' ' + 'InitKE' + '\r\n')

f.close()

with open('nan_outside.txt', 'a') as f:
		f.write('#x' + ' ' + 'y' + ' ' + 'z' + ' ' + 'Px' + ' ' + 'Py' + ' ' + 'Pz' + ' ' + 't' +  ' ' + 'PDGid' + ' ' + 'EventNum' + ' ' + 'TRACKID' + ' ' + 'Parent' + ' ' + 'Weight' +  ' ' + 'Bx' + ' ' + 'By' + ' ' +  'Bz' + ' ' + 'Ex' + ' ' + 'Ey' + ' ' + 'Ez' + ' ' + 'ProperTime' + ' ' + 'PathLength' + ' ' + 'PolX' + ' ' + 'PolY' + ' ' + 'PolZ'  + ' ' + 'InitX' + ' ' + 'InitY' + ' ' + 'InitZ' + ' ' + 'InitT' + ' ' + 'InitKE' + '\r\n')

f.close()

filename = 'outside_cell.txt'
x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE = np.loadtxt(filename, unpack=True)

for i in range(0, len(Px), 1):


	if np.isnan(Px[i]) or np.isnan(Py[i]) or np.isnan(Pz[i]) or np.isnan(t[i]) or np.isnan(x[i]) or np.isnan(y[i]) or np.isnan(z[i]) :
		print('got one')
		with open('nan_outside.txt', 'a') as g:
			g.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')
	else:
		with open('new_outside_cell.txt', 'a') as f:
			f.write(str(x[i]) + ' ' + str(y[i]) + ' ' + str(z[i]) + ' ' + str(Px[i]) + ' ' + str(Py[i]) + ' ' + str(Pz[i]) + ' ' + str(t[i]) +  ' ' + str(PDGid[i]) + ' ' + str(EventID[i]) + ' ' + str(TrackID[i]) + ' ' + str(ParentID[i])+ ' ' + str(Weight[i]) + ' ' + str(Bx[i]) + ' ' + str(By[i]) + ' ' + str(Bz[i]) + ' ' + str(Ex[i]) + ' ' + str(Ey[i]) + ' ' + str(Ez[i]) + ' ' + str(ProperTime[i]) + ' ' + str(PathLength[i]) + ' ' + str(PolX[i]) + ' ' + str(PolY[i]) + ' ' + str(PolZ[i]) + ' ' + str(InitX[i]) + ' ' + str(InitY[i]) + ' ' + str(InitZ[i]) + ' ' + str(InitT[i]) + ' ' + str(InitKE[i]) + '\n')

f.close()
g.close()