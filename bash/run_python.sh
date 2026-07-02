
press="50 100 250 500 750 1000"

for pressure in $press
do 
   
   cd $pressure/zntuples

   if test -f energy_and_number.txt ; then 
      rm energy_and_number.txt
   fi 
   
   python3 ~/python/energy_no_muon.py

   
   # move to previous directory   
   cd ../..

done 