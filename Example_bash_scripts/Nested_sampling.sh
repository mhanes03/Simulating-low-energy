for var1 in $(seq 0.02 0.02 0.1)
do 

    mkdir $var1
    cd $var1

    variables="6 60 18 42"

   for var2 in $variables
   do 
      # makes directory for variable 2
      mkdir $var2

      # copying the input file into the directory corresponds to thickness being run
      cp ../input.g4bl ./$var2

      # moves into the directory for thickness being sampled
      cd $var2

      # prints the current working directory
      pwd 

      # prints which thickness the simulation is being run with 
      echo "Running simulation for pressure and E-field = "$var2 'mbar' $var1 'MV/m'

      # runs simulation in the correct thickness directory
      apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl Pressure=$var2/1013 E_field_magnitude=$var1 > g4_out

      # puts zntuple data together
      mkdir zntuples
      mv Z* ./zntuples

      # move to previous directory
      cd ..

    done 

    cd ..

done 
