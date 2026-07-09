# Purpose : attempts to calculate the asymmetry from the detector 
#
# Input : the detector files 
# Output : asymmetry as a function of time 
#
# Limitations : should use the in built histogram function to bin the time values 

import numpy as np 
import pandas as pd

filename = 'counts_asym.txt'
with open(filename, 'a') as f:
	f.write('# t' + ' ' + 'N_B' +  ' ' + 'N_F' + ' ' + 'A' + '\n')
f.close()

Det1 = 'Det1.txt'
Det2 = 'Det2.txt'

#df = pd.read_csv(filename, sep=' ', header=1)
#print(df.head())

x,y,z,Px,Py,Pz,t_1,PDGid,EventID,TrackID,ParentID,Weight = np.loadtxt(Det1, unpack=True)
x,y,z,Px,Py,Pz,t_2,PDGid,EventID,TrackID,ParentID,Weight = np.loadtxt(Det2, unpack=True)

t_1 = t_1.round()
t_2 = t_2.round()

print(t_1)


for t in range(0, 5000, 1):
	N_F = (t_1 == t).sum()
	N_B = (t_2 == t).sum()

	alpha = 1

	if N_B == 0 and N_F == 0 : 
		A = 0 
	else: 
		A = (N_F - (alpha*N_B))/(N_F + (alpha*N_B))

	with open(filename, 'a') as f:
		f.write(str(t) + ' ' + str(N_B) + ' ' + str(N_F) + ' ' + str(A) + '\n')
	f.close()

filename = 'counts_asym_binned.txt'
with open(filename, 'a') as f:
	f.write('# t' + ' ' + 'N_B' +  ' ' + 'N_F' + ' ' + 'A' + '\n')
f.close()


for t in range(0, 5000, 10):
	N_F_higher = (t_1 > t).sum()
	N_F_lower = (t_1 < t).sum()

	N_F = len(t_1) - (N_F_lower + N_F_higher)

	N_B_higher = (t_2 > t).sum()
	N_B_lower = (t_2 < t).sum()

	N_B = len(t_2) - (N_B_lower + N_B_higher)

	alpha = 1

	if N_B == 0 and N_F == 0 : 
		A = 0 
	else: 
		A = (N_F - (alpha*N_B))/(N_F + (alpha*N_B))

	with open(filename, 'a') as f:
		f.write(str(t) + ' ' + str(N_B) + ' ' + str(N_F) + ' ' + str(A) + '\n')
	f.close()
