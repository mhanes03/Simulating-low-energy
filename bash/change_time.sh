# For graphite degrader

time="40 60 80 100 120 200"

for starts in $time
do 

   mkdir $starts

   cp input.g4bl ./$starts
   
   cd $starts

    # prints which thickness the simulation is being run with 
   echo "Running simulation start time = "$starts

   # runs simulation in the correct thickness directory
   apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl start_time=$starts > g4_out

   mkdir zntuples
   mv Z* ./zntuples

   # move to previous directory   
   cd ..

done 