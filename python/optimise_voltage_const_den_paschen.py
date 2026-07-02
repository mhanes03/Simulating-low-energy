import subprocess 
from scipy.optimize import differential_evolution
import numpy as np
import os

####################### calculating Paschen breakdown voltage ########################

def paschen(a, b, pd):
    # using gamma = 0.01
    V = b * pd / (np.log((a * pd) / np.log(1+1/.01)))
    return V*1e-6

######################## setting up file ################################################

file_name = 'optimisation_trail.txt'
param_to_be_optimised_1 = 'paschen_factor'

with open(file_name, 'a') as f:
		f.write('#'+ param_to_be_optimised_1 + ' ' + 'volt' + ' ' + 'N_eqm' +  ' ' + 'N_less' + ' ' + 'N_high' +  '\r\n')
f.close()

###################### running g4 and calculating number of muons E > 10 keV #############

def func_g4(bounds):
	# runs g4beamline from python

	# for Helium 
	a = 2.8 
	b = 77 

	# mbar to Torr
	p = 100/1.333

	# cm
	d = 4

	V_breakdown = paschen(a, b, p*d)

	# convert to MV/m
	V_breakdown = V_breakdown/(d*1e-2)

	volt = bounds[0]*V_breakdown

	path = fr'/home/mh1163604/experiment/new_layout/100_mbar/volt_{str(volt)}'
	path_main = '/home/mh1163604/experiment/new_layout/100_mbar/'

	if os.path.exists(path) == True :
		os.chdir(path)
	else :
		os.mkdir(path)
		os.chdir(path)

	bash = subprocess.Popen('bash ~/bash/copy_files.sh', shell=True)

	bash.communicate()

	g4_calc = subprocess.Popen(fr'apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl E_field_magnitude={volt} > g4_out', shell=True)
	print ("g4 running simulation")
	
	# waits for the simulation to be finished 
	g4_calc.communicate()

	file = 'Z0.txt'

	if os.path.getsize(fr'/home/mh1163604/experiment/new_layout/100_mbar/volt_{str(volt)}/{file}') == 121 :
		N = 0 
		N_eqm = 0 
		N_less = 0
		os.chdir(path_main)
	else: 
		file = 'Z0.txt'
		x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight= np.loadtxt(file, unpack=True)
		E = (Px**2 + Py**2 + Pz**2)/(2*105.66)
		plots = subprocess.Popen('bash ~/bash/plots.sh', shell=True)

		plots.communicate()
		os.chdir(path_main)

		E_mean = 0.0002
		spread = 0.14 
		std = E_mean*spread

		E_low = E_mean - 3*std
		E_high = E_mean + 3*std 

		N_less = (E < E_low).sum()
		N_high = (E > E_high).sum()

		N = N_less + N_high

		# captured muons 
		N_eqm = len(E) - N

	with open(file_name, 'a') as f:
		f.write(str(bounds[0]) + ' ' + str(volt) + ' ' + str(N_eqm) + ' ' +  str(N_less) + ' ' + str(N_high) + '\r\n')
	f.close()

	return N

##################### running optimisation ###############################################

# bounds controls what parameters are optimised 
bounds = [(0.65,0.85)]

# carries out the optimisation 
result = differential_evolution(func_g4, bounds)


print(result)
