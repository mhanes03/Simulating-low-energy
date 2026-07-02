
thick="1 1.32 1.34 1.36 1.38"

for thickness in $thick
do 
   cd $thickness/zntuples

   echo $thickness >> ../../summary.txt

   head -2 number_of_entries.txt >> ../../summary.txt

   cd ../..

done 