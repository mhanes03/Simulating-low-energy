import numpy as np 


def paschen(a, b, pd):
    # using gamma = 0.01
    V = (b * pd) / (np.log((a * pd) / np.log(1+1/.01)))
    return V

# for Helium 
a = 2.8 
b = 77 

# mbar to Torr 
p = 100/1.333

# cm
d = 4

V_breakdown = paschen(a, b, p*d)
print("Breakdown voltage for helium at a pressure p =", p*1.333,"mbar", "and d =", d, "cm is",V_breakdown*1e-6, "MV", "whic