# !/bin/sh


for electric in $(seq 20 20 100)
do 

    mkdir $electric 
    cd $electric

    pressures="0.5 5 50 100"

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
      echo "Running simulation for pressure and E-field = "$pressure 'mbar' $electric 'kV/m'

      # runs simulation in the correct thickness directory
      apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl Pressure=$pressure/1013 E_field_magnitude=$electric*1e-3 > g4_out.txt

      mkdir zntuples
      mv Z* ./zntuples

      # move to previous directory
      cd ..

    done 

    cd ..

done 