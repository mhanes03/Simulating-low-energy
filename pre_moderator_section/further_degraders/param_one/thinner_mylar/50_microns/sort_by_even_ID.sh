
for event_id in $(seq 1 1 10000)
do 
	awk -v id=$event_id '{if ($9 == id) print $9,$6} ' Z100.txt >> pz_before_and_after_100.txt
	awk -v id=$event_id '{if ($9 == id) print $9,$6} ' Z120.txt >> pz_before_and_after_120.txt


done


for event_id in $(seq 1 1 10000)
do 
	awk -v id=$event_id '{if ($9 == id) print $9,$6} ' Z210.txt >> pz_before_and_after_210.txt
	awk -v id=$event_id '{if ($9 == id) print $9,$6} ' Z220.txt >> pz_before_and_after_220.txt


done


