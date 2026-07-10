# Purpose : to separate the time values in the timentuple into separate files for each time
#
# Input : timentuple 
# Output : individual files for each time value  
# 
# Limitations : 
mkdir tntuples

cp time_output.txt tntuples

cd tntuples 

awk '$1**2+$2**2 <= 500**2 && $3 >= 0 && $3 <= 1000' time_output.txt > in_cell_times.txt

sort -k 7n in_cell_times.txt > in_cell_times_sorted.txt

for i in $(seq 0 10 2000)
do 
	awk '$7 == '$i in_cell_times_sorted.txt > T$i.txt 

done 
