# !/bin/bash

for sp in $(seq 45 5 110)
do

    # makes directory for stopping power
    mkdir $sp

    # moves into the directory for stopping power being sampled
    cd $sp

    # coping the input file into the directory corresponds to stopping power being run
    cp ../muon_drift_He_test.g4bl .

    # prints the current working directory
    pwd 

    # prints which radiusthe simulation is being run with 
    echo "Running simulation for stopping power = "$sp 

    # runs simulation in the correct radius directory
    apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 muon_drift_He_test.g4bl stp=$sp > g4_out

    # move to previous directory
    cd ..
done