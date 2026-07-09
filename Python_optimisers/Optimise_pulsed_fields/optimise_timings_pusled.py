# Purpose : using differential evolution optimiser to optimise the cell for timings of pulsed fields 
#
# Input : bounds for the timings 
# Output : optimisation trail file 
# 
# Limitations :
import subprocess 
from scipy.optimize import differential_evolution
import numpy as np
import os

####################### calculating Paschen breakdown voltage ########################

######################## setting up file ################################################

file_name = 'optimisation_trail.txt'
param_to_be_optimised_1 = 'turning_on_forward'

with open(file_name, 'a') as f:
		f.write('#'+ param_to_be_optimised_1 + ' ' + 'N_not_eqm' +  ' ' + 'N_less_eqm' + ' ' + 'N_eqm' + ' ' + 'less_500eV_unique_event' '\r\n')
f.close()

###################### running g4 and calculating number of muons E > 10 keV #############

def func_g4(bounds):

	path = fr'/home/mh1163604/looking_at_pulsed_detail/01_07_2026/timed_fields/optimiser/timings_{bounds[0]}'
	path_main = '/home/mh1163604/looking_at_pulsed_detail/01_07_2026/timed_fields/optimiser/'

	if os.path.exists(path) == True :
		os.chdir(path)
	else :
		os.mkdir(path)
		os.chdir(path)

	bash = subprocess.Popen('bash ~/bash/copy_files.sh', shell=True)

	bash.communicate()

	g4_calc = subprocess.Popen(fr'apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl neg_flatop={bounds[0]} > g4_out', shell=True)
	print ("g4 running simulation")
	
	# waits for the simulation to be finished 
	g4_calc.communicate()

	file = 'Z1000.txt'

	if os.path.getsize(fr'/home/mh1163604/looking_at_pulsed_detail/01_07_2026/timed_fields/optimiser/timings_{str(bounds[0])}/{file}') == 121 :
		N = 0 
		N_eqm = 0 
		N_less = 0
		os.chdir(path_main)

		unique = []
	else: 
		# to calculate the energy of all the muons from a chosen zntuple
		file = 'Z1000.txt'
		#x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight= np.loadtxt(file, unpack=True)
		x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(file, unpack=True)
		E = (Px**2 + Py**2 + Pz**2)/(2*105.66)

		plots = subprocess.Popen('bash ~/bash/plots.sh', shell=True)
		plots.communicate()

		E_mean = 0.0002
		spread = 0.14 
		std = E_mean*spread

		E_low = E_mean - 3*std
		E_high = E_mean + 3*std 

		N_less = (E < E_low).sum()
		N_high = (E > E_high).sum()

		N = N_less + N_high

		N_eqm = len(E) - N

		file_two = 'zntuples/Z1000_less_500.txt'
		x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight,Bx,By,Bz,Ex,Ey,Ez,ProperTime,PathLength,PolX,PolY,PolZ,InitX,InitY,InitZ,InitT,InitKE= np.loadtxt(file_two, unpack=True)
		unique = len(np.unique(EventID))

		os.chdir(path_main)

		with open(file_name, 'a') as f:
			f.write(str(bounds[0]) + ' ' + str(N) + ' ' + str(N_less) + ' ' + str(N_eqm) +  ' ' + str(unique) + '\r\n')
		f.close()

	return N

##################### running optimisation ###############################################

# bound one be the paschen factor voltage/breakdown_voltage
# bound two to be the density factor density/1bardensity

# bounds controls what parameters are optimised 
bounds = [(100, 1000)]

# carries out the optimisation 
result = differential_evolution(func_g4, bounds)


print(result)
