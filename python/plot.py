import numpy as np 
import os
import subprocess

optimise_file = 'max_N_eqm_entries.txt'

acc_paschen_factor,density_factor,volt,density,pressure,N_not_eqm,N_less_eqm,N_eqm = np.loadtxt(optimise_file, unpack=True)

for i in volt :
	index = next(j for j, x in enumerate(volt) if x == i)
	path = fr'/home/mh1163604/low_energy/making_stopping_curves/Sandwich_in_SRIM/trim/1/chris_cooling/moving_decelerating/tuning_time_1/10_ns_reacc/using_python/dc_cell/1keV_eqm/volt_{str(i)}_density_{str(density[index])}'
	path_main = '/home/mh1163604/low_energy/making_stopping_curves/Sandwich_in_SRIM/trim/1/chris_cooling/moving_decelerating/tuning_time_1/10_ns_reacc/using_python/dc_cell/1keV_eqm/'

	os.chdir(path)

	plots = subprocess.Popen('bash ~/bash/best_plots.sh', shell=True)

	plots.communicate()

	move = subprocess.Popen('bash ~/bash/move_plots.sh', shell=True)

	move.communicate()

	os.chdir(path_main)
