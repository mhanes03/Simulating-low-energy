import numpy as np 
import os

optimise_file = 'optimisation_trail.txt'

acc_paschen_factor,density_factor,volt,density,pressure,N_great,N_less = np.loadtxt(optimise_file, unpack=True)

file_name = 'mean_std_spread.txt'

with open(file_name, 'a') as f:
		f.write('#'+ 'volt' + ' ' 'Paschen_fac' + ' ' + 'density' + ' ' + 'pressure' + ' ' + 'mean' + ' ' + 'standard_deviation' +  ' ' + 'spread' + ' ' + 'N_less' + '\r\n')
f.close()

for i in volt :
	index = next(j for j, x in enumerate(volt) if x == i)
	path = fr'/home/mh1163604/low_energy/making_stopping_curves/Sandwich_in_SRIM/trim/1/chris_cooling/moving_decelerating/tuning_time_1/10_ns_reacc/using_python/dc_cell/vary_density_volt_2/volt_{str(i)}_density_{str(density[index])}'
	path_main = '/home/mh1163604/low_energy/making_stopping_curves/Sandwich_in_SRIM/trim/1/chris_cooling/moving_decelerating/tuning_time_1/10_ns_reacc/using_python/dc_cell/vary_density_volt_2/'

	os.chdir(path)

	file = 'Z300.txt'

	x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight= np.loadtxt(file, unpack=True)
	E = (Px**2 + Py**2 + Pz**2)/(2*105.66)
	E = E[~np.isnan(E)]

	os.chdir(path_main)

	mean = np.mean(E)
	standard_deviation = np.std(E)
	spread = standard_deviation/mean

	with open(file_name, 'a') as f:
		f.write(str(i) + ' ' + str(acc_paschen_factor[index]) + ' ' + str(density[index]) + ' ' + str(pressure[index]) + ' ' + str(mean) + ' ' + str(standard_deviation) + ' ' +  str(spread) +  ' ' +  str(N_less[index]) + '\r\n')
	f.close()

