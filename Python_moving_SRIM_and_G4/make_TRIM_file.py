# Purpose : to produce a TRIM.dat file so that a momentum spread can be put on the muons 
#
# Input : Setting of the mean energy value and spread 
# Output : TRIM.dat file 
#
# Limitations : TRIM.dat file can only have 9999 entries 

import numpy as np 

# for the gaussian distribution, energy in eV
mean = 4E6
sigma = 0.02*4E6
samples = 10000

# For the TRIM.dat file column to specify hydrogen
atom_number = 1

# depth values
X = 0 
Y = 0 
Z = 0 

# cosx,y and z for atom direction 
x_direction = 1
y_direction = 0 
z_direction = 0 

# creates gaussian 
gauss = np.random.normal(mean, sigma, samples)

open('TRIM.dat', 'x')

for event_name in range(1, samples, 1):

	with open('TRIM.dat', 'a') as f:
		f.write('H    ' + ' ' + str(atom_number) + ' ' + str(int(gauss[event_name])) + ' ' + str(X) + ' ' + str(Y) + ' ' + str(Z) + ' ' + str(x_direction) +  ' ' + str(y_direction) + ' ' + str(z_direction) + '\r\n')

f.close()
