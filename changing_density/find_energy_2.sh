# !/bin/sh

for i in $(seq 20 20 100)
do 

   cd $i 
	
   sed 's/change_this/'"$i"'/g' ../../avg_energy.py > ./avg_energy.py 

   pressures="6 60 18 42"

   for pressure in $pressures
   do  

      cd $pressure

      sed 's/and_this/'"$pressure"'/g' ../avg_energy.py > ./avg_energy.py

      python3 avg_energy.py >> ../../energy.txt

      cd ..

    done 

    cd ..

done 

awk '$3 == 6' energy.txt > 6.txt 

awk '$3 == 60' energy.txt > 60.txt 

awk '$3 == 18' energy.txt > 18.txt 

awk '$3 == 42' energy.txt > 42.txt 