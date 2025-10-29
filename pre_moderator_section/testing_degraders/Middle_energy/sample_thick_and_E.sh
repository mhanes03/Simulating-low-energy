# !/bin/sh
# this bash script samples the thickness of the degrader between 0.01 mm and 1 mmm in
# steps of 0.01 mm

for energy in $(seq 1 0.5 2.5)
do 

  mkdir $energy
  cd $energy

  for thickness in $(seq 0.01 0.01 0.1)
  do 
      # makes directory for thickness
      mkdir $thickness

      # coping the input file into the directory corresponds to thickness being run
      cp -r ../input.g4bl ./$thickness

      # moves into the directory for thickness being sampled
      cd $thickness

      # prints the current working directory
      pwd 

      # prints which thickness the simulation is being run with 
      echo "Running simulation for thickness = "$thickness 'mm'

      # runs simulation in the correct thickness directory
      apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl degrader_thickness=$thickness Ek=$energy > g4_out.txt

      mkdir zntuples
      mv Z* ./zntuples

      cd zntuples
      bash ~/sort_by_energy.sh

      cd ..

      gnuplot ~/gpls/energy_plot.gpl

      # move to previous directory
      cd ..

  done 

  cd ..

done 