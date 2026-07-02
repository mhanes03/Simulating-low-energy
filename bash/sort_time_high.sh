
for i in $(seq 200 1 300)
do 
	awk '$7 == '$i in_cell_times_sorted.txt > T$i.txt 

done 