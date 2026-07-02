
press="75 100 150 200 250 300 350 400 450"

for pressure in $press
do 

   mkdir $pressure

   cp input.g4bl ./$pressure
   
   cd $pressure

    # prints which thickness the simulation is being run with 
   echo "Running simulation start time = "$pressure "mbar"

   # runs simulation in the correct thickness directory
   apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl Pressure=$pressure/1013 > g4_out

   mkdir zntuples
   mv Z* ./zntuples

   cd zntuples

   gnuplot ~/gpls/energy_distributions/energy_distr.gpl 
   
   # move to previous directory   
   cd ../..

done 