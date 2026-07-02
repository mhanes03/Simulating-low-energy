
T="0.005 0.01 0.02 0.03 0.04 0.05"

for energy in $T
do 
   mkdir $energy

   cp input.g4bl ./$energy

   cd $energy

   efield="0.024 0.032 0.0456 0.076"

    for elec in $efield
    do 

       mkdir $elec

       cp input.g4bl ./$elec

       cd $elec

        # prints which thickness the simulation is being run with 
       echo "Running simulation start time = "$elec "MV/m"

       # runs simulation in the correct thickness directory
       apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl Ek=$energy E_field_magnitude_back=$elec*-1.0 > g4_out

       mkdir zntuples
       mv Z* ./zntuples

       cd ..

    done 
done 