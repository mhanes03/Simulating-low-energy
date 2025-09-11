# !/bin/sh

for length in $(seq 200 100 1000)
do
    pressure=60

    # makes directory for length
    mkdir $length

    # coping the input file into the directory corresponds to length being run
    cp -r ./high_energy.g4bl ../BEAM_100K.txt ./$length

    # moves into the directory for thickness being sampled
    cd $length

    # prints the current working directory
    pwd 

    # prints which length the simulation is being run with 
    echo "Running simulation for length = "$length 'mm'

    # runs simulation in the correct thickness directory
    g4bl high_energy.g4bl cell_length=$length Pressure=$pressure/1013 > g4_out.txt

    mkdir zntuples
    mv Z* ./zntuples

    # move to previous directory
    cd ..

done 