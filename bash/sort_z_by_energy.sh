
awk '$1**2+$2**2 <= 40**2 && ' time_output.txt > in_cell_times.txt


sort -k 7n in_cell_times.txt > in_cell_times_sorted.txt



for i in $(seq 0 5 2500)
do 
	awk '$7 == '$i in_cell_times_sorted.txt > T$i.txt 

done 