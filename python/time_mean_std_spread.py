import numpy as np 
import os

optimise_file = 'optimisation_trail.txt'

volt,N_great,N_less = np.loadtxt(optimise_file, unpack=True)

file_name = 'mean_std_spread_time.txt'

with open(file_name, 'a') as f:
		f.write('#'+ 'volt' + ' ' + 'mean' + ' ' + 'standard_deviation' +  ' ' + 'spread' + '\r\n')
f.close()

for i in volt :
	path = fr'/home/mh1163604/low_energy/making_stopping_curves/Sandwich_in_SRIM/trim/1/chris_cooling/moving_decelerating/tuning_time_1/10_ns_reacc/using_python/dc_cell/over_300mm/5_mbar/volt_{str(i)}'
	path_main = '/home/mh1163604/low_energy/making_stopping_curves/Sandwich_in_SRIM/trim/1/chris_cooling/moving_decelerating/tuning_time_1/10_ns_reacc/using_python/dc_cell/over_300mm/5_mbar/'

	os.chdir(path)

	file = 'Z300.txt'

	x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight= np.loadtxt(file, unpack=True)
	t = t[~np.isnan(t)]

	os.chdir(path_main)

	mean = np.mean(t)
	standard_deviation = np.std(t)
	spread = standard_deviation/mean

	with open(file_name, 'a') as f:
		f.write(str(i) + ' ' + str(mean) + ' ' + str(standard_deviation) + ' ' +  str(spread) + '\r\n')
	f.close()

