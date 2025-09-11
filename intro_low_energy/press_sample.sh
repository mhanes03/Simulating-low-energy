# !/bin/sh

for pressure in $(seq 20 20 80)
do 
    # makes directory for pressure
    mkdir $pressure

    # coping the input file into the directory corresponds to thickness being run
    cp -r ./high_energy.g4bl ../BEAM_100K.txt ./$pressure

    # moves into the directory for thickness being sampled
    cd $pressure

    # prints the current working directory
    pwd 

    # prints which thickness the simulation is being run with 
    echo "Running simulation for pressure = "$pressure 'mbar'

    # runs simulation in the correct thickness directory
    g4bl high_energy.g4bl Pressure=$pressure/1013 > g4_out.txt

    mkdir zntuples
    mv Z* ./zntuples

    # move to previous directory
    cd ..

done 