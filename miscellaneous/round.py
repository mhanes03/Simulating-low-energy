# Purpose : to round the Paschen factors from the optimisations to one decimal place, done so that plots for particular Paschen factors could be produced 
#
# Input : optimisation trail file from the differential evolution optimiser 
# Output : optimisation trail with rounded Paschen factors 
#
# Limitations : 

import numpy as np 

file_name = 'optimisation_trail.txt'

acc_paschen_factor,density_factor,volt,density,pressure,N_not_eqm,N_less_eqm,N_eqm= np.loadtxt(file_name, unpack=True)

acc_paschen_factor = np.round(acc_paschen_factor, 1)

with open(file_name, 'a') as f:
		f.write('#'+ 'acc_paschen_factor' + ' ' + 'density_factor' + ' ' + 'volt' + ' ' + 'density' + ' ' + 'pressure' + ' ' + 'N_not_eqm' +  ' ' + 'N_less_eqm' + ' ' + 'N_eqm' + '\r\n')
f.close()

file = 'optimisation_trail_rounded.txt'

for i in range (0, len(acc_paschen_factor)):
	with open(file, 'a') as f:
		f.write(str(acc_paschen_factor[i]) + ' ' + str(density_factor[i]) + ' ' + str(volt[i]) + ' ' + str(density[i]) + ' ' + str(pressure[i]) + ' ' + str(N_not_eqm[i]) +  ' ' + str(N_less_eqm[i]) + ' ' + str(N_eqm[i]) + '\r\n')


f.close()
