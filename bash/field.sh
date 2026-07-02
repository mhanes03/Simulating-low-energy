
for i in $(seq 0 10 1000)
do 
	awk '$3 == '$i field.txt > F$i.txt 

done 

mkdir fieldntuples
mv F* fieldntuples