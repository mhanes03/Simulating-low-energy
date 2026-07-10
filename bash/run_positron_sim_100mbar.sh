# Purpose : samples different field values for the 100 mbar pressure cell for Paschen factors 0.5 to 0.9 for positron simulation 
#
# Input : field values  
# Output : simulations for each electric field value
# 
# Limitations : 
# 0.5 0.6 0.7 0.8 0.85 0.9 paschen factors 
field="0.0555 0.0665 0.0778 0.0888 0.1"

for E in $field
do 

   cd $E
   mkdir run

   cp ../other_input/input.g4bl ./run
   cp ../HIFI_2D_symm.BLFieldMap ./run

   #python3 ~/python/make_beam__file_distr.py
   python3 ~/python/make_beam__file_rev.py

   cp beam.txt ./run 

   cd run 

   echo 'running simulation'

   g4bl input.g4bl > g4_out

   bash ~/bash/remove_le_positrons.sh

   # move to previous directory   
   cd ../..

done 
