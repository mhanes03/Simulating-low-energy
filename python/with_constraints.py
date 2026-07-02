import subprocess 
from scipy.optimize import differential_evolution, LinearConstraint, Bounds
import numpy as np

####################### calculating Paschen breakdown voltage ########################

def paschen(a, b, pd):
    # using gamma = 0.01
    V = b * pd / (np.log((a * pd) / np.log(1+1/.01)))
    return V

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
param_to_be_optimised = 'ez2'

with open(file_name, 'a') as f:
		f.write('#'+ param_to_be_optimised + ' ' + 'N' + '\r\n')
f.close()

###################### running g4 and calculating number of muons E > 10 keV #############

def func_g4(ez):
	# runs g4beamline from python
	g4_calc = subprocess.Popen(fr'apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 cooling.g4bl ez2={ez[0]} > g4_out', shell=True)
	print ("g4 running simulation")
	
	# waits for the simulation to be finished 
	g4_calc.communicate()
	
	# to calculate the energy of all the muons from a chosen zntuple
	file = 'Z1000.txt'
	x,y,z,Px,Py,Pz,t,PDGid,EventID,TrackID,ParentID,Weight= np.loadtxt(file, unpack=True)
	E = (Px**2 + Py**2 + Pz**2)/(2*105.66)

    # finding number with energy greater than 10 keV
	N = (E > 0.01).sum()

	# to keep track of the parameter and number of muons
	with open(file_name, 'a') as f:
		f.write(str(ez[0]) + ' ' + str(N) + '\r\n')
	f.close()

	return N

##################### running optimisation ###############################################

# bounds controls what parameters are optimised 
bounds = [(-2,-1)]

# carries out the optimisation 
result = differential_evolution(func_g4, bounds)

print(result)
