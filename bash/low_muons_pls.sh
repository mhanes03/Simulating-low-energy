# 0.5 0.6 0.7 0.8 0.85 0.9 paschen factors 
field="0.0555 0.0665 0.0778 0.0888 0.1"

for E in $field
do 

   cd $E

   echo 'running simulation'

   bash ~/bash/low_energy_muons.sh

   # move to previous directory   
   cd ..

done 