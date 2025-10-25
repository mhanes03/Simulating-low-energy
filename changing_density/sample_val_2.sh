# !/bin/sh


for electric in $(seq 0.02 0.02 0.1)
do 

    mkdir $electric 
    cd $electric

    pressures="6 60 18 42"

   for pressure in $pressures
   do 
      # makes directory for pressure
      mkdir $pressure

      # coping the input file into the directory corresponds to thickness being run
      cp ../input.g4bl ./$pressure

      # moves into the directory for thickness being sampled
      cd $pressure

      # prints the current working directory
      pwd 

      # prints which thickness the simulation is being run with 
      echo "Running simulation for pressure and E-field = "$pressure 'mbar' $electric 'MV/m'

      # runs simulation in the correct thickness directory
      apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl Pressure=$pressure/1013 E_field_magnitude=$electric > g4_out

      mkdir zntuples
      mv Z* ./zntuples

      # move to previous directory
      cd ..

    done 

    cd ..

done 