# !/bin/sh

for var in $(seq 0.01 0.01 1)
do 
    # makes directory for thickness
    mkdir $var

    # coping the input file into the directory corresponds to thickness being run
    cp input.g4bl ./$var

    # moves into the directory for thickness being sampled
    cd $var

    # prints the current working directory
    pwd 

    # runs simulation in the correct thickness directory
    apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl  degrader_thickness=$var > g4_out

    # prints which thickness the simulation is being run with 
    echo "Running simulation for variable = "$var

    # move to previous directory
    cd ..

done 
