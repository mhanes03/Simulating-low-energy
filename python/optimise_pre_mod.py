import subprocess 
from scipy.optimize import differential_evolution
import numpy as np
import os

######################## setting up file ################################################

file_name = 'optimisation_trail.txt'
param_to_be_optimised_1 = 'density_Factor'

with open(file_name, 'a') as f:
		f.write('#'+ param_to_be_optimised_1 + ' ' + 'density' +  ' ' + 'N_not_eqm' +  ' ' + 'N_less_eqm' + ' ' + 'N_eqm' + '\r\n')
f.close()

###################### running g4 and calculating number of muons E > 10 keV #############

def func_g4(bounds):
	# runs g4beamline from python
	density = bounds[0]*1.6E-4

	path = fr'/home/mh1163604/low_energy/optimising_pre_mod/density_{str(density)}'
	path_main = '/home/mh1163604/low_energy/optimising_pre_mod/'

	if os.path.exists(path) == True :
		os.chdir(path)
	else :
		os.mkdir(path)
		os.chdir(path)

	bash = subprocess.Popen('bash ~/bash/copy_files.sh', shell=True)

	bash.communicate()

	g4_calc = subprocess.Popen(fr'apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl He_density={density} > g4_out', shell=True)
	print ("g4 running simulation")
	
	# waits for the simulation to be finished 
	g4_calc.communicate()

	# to calculate the energy of all the muons from a chosen zntuple
	file = 'Z250.txt'
	x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight= np.loadtxt(file, unpack=True)
	E = (Px**2 + Py**2 + Pz**2)/(2*105.66)

	plots = subprocess.Popen('bash ~/bash/plots.sh', shell=True)

	plots.communicate()
	
	os.chdir(path_main)

	E_mean = 0.01
	spread = 0.3 
	std = E_mean*spread

	E_low = E_mean - 3*std
	E_high = E_mean + 3*std 

	N_less = (E < E_low).sum()
	N_high = (E > E_high).sum()

	N = N_less + N_high

	N_eqm = len(E) - N

	with open(file_name, 'a') as f:
		f.write(str(bounds[0]) + ' ' + str(density) +  ' ' + str(N) + ' ' + str(N_less) + ' ' + str(N_eqm) + '\r\n')
	f.close()

	return N

##################### running optimisation ###############################################

# bound one be the paschen factor voltage/breakdown_voltage
# bound two to be the density factor density/1bardensity

# bounds controls what parameters are optimised 
bounds = [(0.05, 1)]

# carries out the optimisation 
result = differential_evolution(func_g4, bounds)


print(result)
