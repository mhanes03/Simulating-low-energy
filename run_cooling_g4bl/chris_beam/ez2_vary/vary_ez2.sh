# !/bin/sh

for ez2 in $(seq 0 0.5 2)
do 
    # makes directory for thickness
    mkdir $ez2

    # coping the input file into the directory corresponds to thickness being run
    cp -r cooling.g4bl beam.bltrk ./$ez2

    # moves into the directory for thickness being sampled
    cd $ez2

    # prints the current working directory
    pwd 

    # prints which thickness the simulation is being run with 
    echo "Running simulation for field = "$ez2

    # runs simulation in the correct thickness directory
    g4bl cooling.g4bl ez2=$ez2 > g4_out

    # move to previous directory
    cd ..

done 