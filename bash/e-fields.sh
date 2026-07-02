efield="1.38 1.36 1.34 1"

for elec in $efield
do 

   mkdir $elec

   cp input.g4bl ./$elec

   cp beam.txt ./$elec
   
   cd $elec

    # prints which thickness the simulation is being run with 
   echo "Running simulation start time = "$elec "MV/m"

   # runs simulation in the correct thickness directory
   apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl E_field_magnitude_back=$elec*-1.0 > g4_out

   mkdir zntuples
   mv Z* ./zntuples

   cd ..

done 