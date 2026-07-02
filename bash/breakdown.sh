field="50 500 1000"

for E in $field
do 

   mkdir $E

   cp input.g4bl ./$E
   
   cd $E

    # prints which thickness the simulation is being run with 
   echo "Running simulation for field = "$E "MV/m"

   # runs simulation in the correct thickness directory
   apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl cell_length=100 E_field_magnitude_for=$E > g4_out

   mkdir zntuples
   mv Z* ./zntuples

   # move to previous directory   
   cd ..

done 