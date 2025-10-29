# !/bin/sh
# this bash script samples the thickness of the degrader between 0.01 mm and 1 mmm in
# steps of 0.01 mm

for energy in $(seq 1.0 0.5 2.5)
do 

  cd $energy

  for thickness in $(seq 0.01 0.01 0.1)
  do 
      
      # moves into the directory for thickness being sampled
      cd $thickness

      # prints the current working directory
      pwd 

      gnuplot ~/gpls/pz_avg.gpl

      # move to previous directory
      cd ..

  done 

  cd ..

done 