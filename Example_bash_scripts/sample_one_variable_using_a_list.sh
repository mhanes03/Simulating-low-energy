variable="6 60 18 42"

for var in $variable
do 
  # makes directory for pressure
  mkdir $var

  # copying the input file into the directory corresponds to thickness being run
  cp ../input.g4bl ./$var

  # moves into the directory for thickness being sampled
  cd $var

  # prints the current working directory
  pwd 

  # prints which thickness the simulation is being run with 
  echo "Running simulation for variable = "$var

  # runs simulation in the correct thickness directory
  apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl Pressure=$var > g4_out

  # puts zntuple data together
  mkdir zntuples
  mv Z* ./zntuples

  # move to previous directory
  cd ..
  
done 
