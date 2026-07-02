for energies in $(seq 1E-3 0.25E-3 4)
do 

    pressure=50/1013

    mkdir $energies 
    cd $energies

    # prints which thickness the simulation is being run with 
    echo "Running simulation for energy = "$energies 'MeV'

    pwd 

    cp ../input.g4bl .

    # runs simulation in the correct thickness directory
    apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl Pressure=$pressure Ek=$energies > g4_out

    mkdir zntuples
    mv Z* ./zntuples

    cd ..

done 