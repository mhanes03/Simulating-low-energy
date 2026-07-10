# Purpose : to match before and after values for muons before and after going through the degrader 
#
# Input : two zntuples, one before the degrader and one after 
# Output : Pz values before and after 
# 
# Limitations : 
import numpy as np 

Event_id_100, Pz_100 = np.loadtxt('pz_before_and_after_100.txt',  unpack=True)
Event_id_120, Pz_120 = np.loadtxt('pz_before_and_after_120.txt',  unpack=True)

#open('pz_before_and_After.txt', 'x')

f = open('pz_before_and_After.txt', 'a' )

for i in range (1, 1000, 1):
	
	if Event_id_100[i-1] == i and Event_id_120[i-1] == Event_id_100[i-1]:
	    # the ids match and so the values are the before and after 
		f.write(str(i) + ' ' + str(Pz_100[i-1])+ ' ' + str(i) +' ' + str(Pz_120[i-1]) + '\n')

    elif Event_id_120[i-1] == Event_id_100[i-2]:
    	# the id in 120 is a repeat 
    	f.write(str(i) + ' ' + str(Pz_120[i-1])+ ' ' + str(i) +' ' + str(Pz_120[i-2]) + '\n')
        
    elif Event_id_100[i-1] == Event_id_120[i]:
    	f.write(str(i) + ' ' + str(Pz_100[i-1])+ ' ' + str(i) +' ' + str(Pz_120[i]) + '\n')
    
    else:
    	f.write(str(i) + ' ' + str(Pz_100[i-1])+ ' ' + str(i) +' ' + str(0.00) + '\n')


f.close()
