# !/bin/bash

electric_fields="1.445 28.891"

for electric in $electric_fields
do

    # makes directory for stopping power
    mkdir $electric

    # moves into the directory for stopping power being sampled
    cd $electric

    # coping the input file into the directory corresponds to stopping power being run
    cp -r ../low_energy.g4bl ../BEAM_100K.txt .

    # prints the current working directory
    pwd 

    # prints which radiusthe simulation is being run with 
    echo "Running simulation for electric field = "$electric 

    # runs simulation in the correct radius directory
    apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 low_energy.g4bl E_field_magnitude=$electric > g4_out

    # move to previous directory
    cd ..
done