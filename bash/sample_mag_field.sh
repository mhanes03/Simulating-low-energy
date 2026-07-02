
B_field="2.5 4.5 3.5 1.5"

for B in $B_field
do 

   mkdir $B

   cp input.g4bl ./$B
   cp HIFI_2D_symm.BLFieldMap ./$B
   
   cd $B

    # prints which thickness the simulation is being run with 
   echo "Running simulation start field = "$B "T"

   # runs simulation in the correct thickness directory
   apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl current_val=$B > g4_out

   bash ~/bash/low_energy_muons.sh

   # move to previous directory   
   cd ..

done 