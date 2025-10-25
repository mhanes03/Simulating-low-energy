# !/bin/sh

for i in $(seq 20 20 100)
do 

   cd $i 
	
   sed 's/change_this/'"$i"'/g' ../../avg_energy.py > ./avg_energy.py 

   pressures="0.5 5 50 100"

   for pressure in $pressures
   do  

      cd $pressure

      sed 's/and_this/'"$pressure"'/g' ../avg_energy.py > ./avg_energy.py

      python3 avg_energy.py >> ../../energy.txt

      cd ..

    done 

    cd ..

done 

awk '$3 == 0.5' energy.txt > 0.5.txt 

awk '$3 == 5' energy.txt > 5.txt 

awk '$3 == 50' energy.txt > 50.txt 

awk '$3 == 100' energy.txt > 100.txt 