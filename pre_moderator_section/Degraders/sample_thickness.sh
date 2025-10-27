# !/bin/sh
# this bash script samples the thickness of the degrader between 0.01 mm and 1 mmm in
# steps of 0.01 mm

for thickness in $(seq 0.1 0.1 1.5)
do 
    # makes directory for thickness
    mkdir $thickness

    # coping the input file into the directory corresponds to thickness being run
    cp -r ./input.g4bl ./$thickness

    # moves into the directory for thickness being sampled
    cd $thickness

    # prints the current working directory
    pwd 

    # prints which thickness the simulation is being run with 
    echo "Running simulation for thickness = "$thickness 'mm'

    # runs simulation in the correct thickness directory
    apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl degrader_thickness=$thickness > g4_out.txt

    mkdir zntuples
    mv Z* ./zntuples

    # move to previous directory
    cd ..

done 