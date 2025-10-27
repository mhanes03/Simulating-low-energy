# !/bin/sh


for electric in $(seq 1 0.5 3)
do 

   mkdir $electric 
   cd $electric

   cp ../input.g4bl . 

   # prints which thickness the simulation is being run with 
   echo "Running simulation for an E-field =" $electric 'kV/m'

   pwd 

   apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl E_field_magnitude=$electric > g4_out.txt

   mkdir zntuples
   mv Z* zntuples

   cd ..

done 
