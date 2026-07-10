# Purpose : separates the Paschen factor values into different files 
#
# Input : optimisation trails   
# Output : Paschen files 
# 
# Limitations : 
python3 ~/python/round.py

for i in $(seq 1 0.1 5)
do 
	awk '$1 == '$i optimisation_trail_rounded.txt > P$i.txt
	sort -k 5n P$i.txt > Paschen$i.txt 

done 
