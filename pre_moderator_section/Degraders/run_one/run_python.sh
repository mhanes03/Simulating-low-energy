# !/bin/sh
# this bash script samples the thickness of the degrader between 0.01 mm and 1 mmm in
# steps of 0.01 mm

for thickness in $(seq 0.1 0.1 1.5)
do 

    # moves into the directory for thickness being sampled
    cd $thickness

    # prints the current working directory
    pwd 

    # prints which thickness the simulation is being run with 
    echo "Running python for thickness = "$thickness 'mm'

    cd zntuples

    python3 ~/python/energy_no_muon.py

    cd ../..

done 