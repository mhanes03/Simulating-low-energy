for energies in $(seq 2.25E-3 0.25E-3 4E-3)
do 

    mkdir $energies 
    cd $energies

    thickness="0.001 0.01 0.1"

   for thickness_val in $thickness
   do 
      # makes directory for pressure
      mkdir $thickness_val

      # coping the input file into the directory corresponds to thickness being run
      cp ../input.g4bl ./$thickness_val

      # moves into the directory for thickness being sampled
      cd $thickness_val

      # prints the current working directory
      pwd 

      # prints which thickness the simulation is being run with 
      echo "Running simulation for thickness and energy = "$thickness_val 'mm' $energies 'MeV'

      # runs simulation in the correct thickness directory
      apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl degrader_thickness=$thickness_val Ek=$energies > g4_out

      mkdir zntuples
      mv Z* ./zntuples

      # move to previous directory
      cd ..

    done 

    cd ..

done 