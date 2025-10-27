# !/bin/sh
# this bash script samples the thickness of the degrader between 0.01 mm and 1 mmm in
# steps of 0.01 mm

for field in $(seq 15 1 30)
do 

    # moves into the directory for thickness being sampled
    cd $field

    # prints the current working directory
    pwd 

    # prints which thickness the simulation is being run with 
    echo "Running python for field = "$field 'kV/m'

    gnuplot ~/gpls/energy_v_time_gif_log.gpl

    cd ..

done