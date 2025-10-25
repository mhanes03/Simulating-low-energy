# !/bin/sh

for i in $(seq 20 20 100)
do 

   cd $i 
	
   sed 's/change_this/'"$i"'/g' ../../avg_energy.py > ./avg_energy.py 

   pressures="0.2 2 0.6 1.5"

   for pressure in $pressures
   do  

      cd $pressure

      sed 's/and_this/'"$pressure"'/g' ../avg_energy.py > ./avg_energy.py

      python3 avg_energy.py >> ../../energy.txt

      cd ..

    done 

    cd ..

done 

awk '$3 == 0.2' energy.txt > 0.2.txt 

awk '$3 == 2' energy.txt > 2.txt 

awk '$3 == 0.6' energy.txt > 0.6.txt 

awk '$3 == 1.5' energy.txt > 1.5.txt 