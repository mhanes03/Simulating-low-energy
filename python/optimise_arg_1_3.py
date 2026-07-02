import subprocess 
from scipy.optimize import differential_evolution
import numpy as np
import os

####################### calculating Paschen breakdown voltage ########################

def paschen(a, b, pd):
    # using gamma = 0.01
    V = b * pd / (np.log((a * pd) / np.log(1+1/.01)))
    return V*1e-6

# for Helium 
a = 2.8 
b = 77 

# mbar to Torr 
p = 5*1.333

# cm
d = 100

V_breakdown = paschen(a, b, p*d)
print("Breakdown voltage for p =", p/1.333,"mbar", "and d =", d, "cm is",V_breakdown, "V")

######################## setting up file ################################################

file_name = 'optimisation_trail.txt'
param_to_be_optimised_1 = 'acc_paschen_factor'
param_to_be_optimised_2 = 'density_factor'
param_to_be_optimised_3 = 'volt'

with open(file_name, 'a') as f:
		f.write('#'+ param_to_be_optimised_1 + ' ' + param_to_be_optimised_2 + ' ' + 'volt' + ' ' + 'density' + ' ' + 'pressure' + ' ' + 'N_not_eqm' +  ' ' + 'N_less_eqm' + ' ' + 'N_eqm' + '\r\n')
f.close()

###################### running g4 and calculating number of muons E > 10 keV #############

def func_g4(bounds):
	# runs g4beamline from python
	density = bounds[1]*1.6E-4

	a = 2.8 
	b = 77 
	d = 30 

	R = 82.056
	T = 290
	M = 4.002602

	p = (density*R*T)/M
	p = p*760

	print(bounds[0],paschen(a, b, p*d))
	voltage = bounds[0]*paschen(a, b, p*d)

	# conver to MV/m
	voltage = voltage/(d*1e-2)

	path = fr'/home/mh1163604/low_energy/making_stopping_curves/Sandwich_in_SRIM/trim/1/chris_cooling/moving_decelerating/tuning_time_1/10_ns_reacc/using_python/dc_cell/3keV_eqm/volt_{str(voltage)}_density_{str(density)}'
	path_main = '/home/mh1163604/low_energy/making_stopping_curves/Sandwich_in_SRIM/trim/1/chris_cooling/moving_decelerating/tuning_time_1/10_ns_reacc/using_python/dc_cell/3keV_eqm/'

	if os.path.exists(path) == True :
		os.chdir(path)
	else :
		os.mkdir(path)
		os.chdir(path)

	bash = subprocess.Popen('bash ~/bash/copy_files.sh', shell=True)

	bash.communicate()

	g4_calc = subprocess.Popen(fr'apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl E_field_magnitude={voltage} He_density={density} > g4_out', shell=True)
	print ("g4 running simulation")
	
	# waits for the simulation to be finished 
	g4_calc.communicate()

	# to calculate the energy of all the muons from a chosen zntuple
	file = 'Z300.txt'
	x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight= np.loadtxt(file, unpack=True)
	E = (Px**2 + Py**2 + Pz**2)/(2*105.66)

	plots = subprocess.Popen('bash ~/bash/plots.sh', shell=True)

	plots.communicate()
	
	os.chdir(path_main)

	E_mean = 0.003
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
		f.write(str(bounds[0]) + ' ' + str(bounds[1]) + ' ' + str(voltage) + ' ' + str(density) + ' ' + str(p/760) + ' ' + str(N) + ' ' + str(N_less) + ' ' + str(N_eqm) + '\r\n')
	f.close()

	return N

##################### running optimisation ###############################################

# bound one be the paschen factor voltage/breakdown_voltage
# bound two to be the density factor density/1bardensity

# bounds controls what parameters are optimised 
bounds = [(3,5), (0, 0.05)]

# carries out the optimisation 
result = differential_evolution(func_g4, bounds)


print(result)
