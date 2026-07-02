# 0.5 0.6 0.7 0.8 0.85 0.9 paschen factors 
field="0.0665 0.0798 0.093 0.107 0.113 0.120"

for E in $field
do 

   mkdir $E

   cp input.g4bl ./$E
   cp HIFI_2D_symm.BLFieldMap ./$E
   
   cd $E

    # prints which thickness the simulation is being run with 
   echo "Running simulation start field = "$E "kV"

   # runs simulation in the correct thickness directory
   apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl E_field_magnitude=$E > g4_out

   bash ~/bash/low_energy_muons.sh

   # move to previous directory   
   cd ..

done 