
thick="0.9 0.95 1.05 1.1 1.15 1.2"

for thickness in $thick
do 
   
   cd $thickness/zntuples

    # prints which thickness the simulation is being run with 
   echo "Running simulation start time = "$thickness "mm"

   bash ~/bash/low_energy_muons.sh



   cd ../..

done 