# !/bin/sh

ez2="-0.0 -0.5 -1.0 -1.5 -2.0"

for ez in $ez2
do 
    # makes directory for thickness
    mkdir negative_$ez

    # coping the input file into the directory corresponds to thickness being run
    cp -r cooling.g4bl beam.bltrk ./negative_$ez

    # moves into the directory for thickness being sampled
    cd negative_$ez

    # prints the current working directory
    pwd 

    # prints which thickness the simulation is being run with 
    echo "Running simulation for field = "$ez

    # runs simulation in the correct thickness directory
    g4bl cooling.g4bl ez2=$ez > g4_out

    # move to previous directory
    cd ..

done 