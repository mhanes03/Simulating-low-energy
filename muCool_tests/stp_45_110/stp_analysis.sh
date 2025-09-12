# !/bin/bash

for sp in $(seq 45 5 110)
do

    # moves into the directory for stopping power being sampled
    cd $sp

    # prints the current working directory
    pwd 

    # prints which radiusthe simulation is being run with 
    echo "Running analysis for stopping power = "$sp 

    gnuplot ../../kinetic_energy.gpl

    # move to previous directory
    cd ..
done