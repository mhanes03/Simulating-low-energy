import numpy as np 

# for the gaussian distribution for time, in ns 
mean = 100
sigma = 0.02*100

# rest mass of muon 
m = 105.66

# g4 variables 
PDGID = -13 
TRACKID = 0
Parent = 0 
weight = 1

file = 'new_TRANSMIT.txt'

ion_num,atomic_num,E_k,x,y,z,cosine_x,cosine_y,cosine_z= np.loadtxt(file, unpack=True, skiprows=12)

# length of the file to determine number of samples 
samples = len(x)
time = np.random.normal(mean, sigma, samples)

# convert units 

# Angstrom to mm 
x = x*1E-7
y = y*1E-7
z = z*1E-7

# eV to MeV
E_k = E_k*1E-6

with open('beam.txt', 'a') as f:
		f.write('#x' + ' ' + 'y' + ' ' + 'z' + ' ' + 'Px' + ' ' + 'Py' + ' ' + 'Pz' + ' ' + 't' +  ' ' + 'PDGid' + ' ' + 'EventNum' + ' ' + 'TRACKID' + ' ' + 'Parent' + ' ' + 'Weight' + '\r\n')

f.close()

for i in range(1, samples, 1):

	with open('beam.txt', 'a') as f:
		f.write(str(z[i]) + ' ' + str(y[i]) + ' ' + str(x[i]) + ' ' + str((np.sqrt((m+E_k[i])**2 - m**2))*cosine_z[i]) + ' ' + str((np.sqrt((m+E_k[i])**2 - m**2))*cosine_y[i]) + ' ' + str((np.sqrt((m+E_k[i])**2 - m**2))*cosine_x[i]) + ' ' + str(0) +  ' ' + str(PDGID) + ' ' + str(i) + ' ' + str(TRACKID) + ' ' + str(Parent)+ ' ' + str(weight) + '\r\n')

f.close()