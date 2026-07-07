import numpy as np 

for j in range(10, 31, 1):
	paschen = float(j)/10
	file = fr'Paschen{str(paschen)}.txt'
	acc_paschen_factor,density_factor,volt,density,pressure,N_not_eqm,N_less_eqm,N_eqm= np.loadtxt(file, unpack=True)

	max_in_range = np.argmax(N_eqm)

	file_2 = 'max_N_eqm_entries.txt'

	with open(file_2, 'a') as f:
		f.write(str(acc_paschen_factor[max_in_range]) + ' ' + str(density_factor[max_in_range]) + ' ' + str(volt[max_in_range]) + ' ' + str(density[max_in_range]) + ' ' + str(pressure[max_in_range]) + ' ' + str(N_not_eqm[max_in_range]) +  ' ' + str(N_less_eqm[max_in_range]) + ' ' + str(N_eqm[max_in_range]) + '\r\n')
	f.close()

file = 'Paschen3.0.txt'
acc_paschen_factor,density_factor,volt,density,pressure,N_not_eqm,N_less_eqm,N_eqm= np.loadtxt(file, unpack=True)

max_in_range = np.argmax(N_eqm)
print(max_in_range, pressure[max_in_range], volt[max_in_range])
