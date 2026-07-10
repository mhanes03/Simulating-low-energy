# Purpose : sample different degrader thicknesses and running g4bl simulation for each thickness
#
# Input : thickness values want to sample 
# Output : simulations for each thickness 
# 
# Limitations : 
thick="0.9 0.95 1.05 1.1 1.15 1.2"

for thickness in $thick
do 

   mkdir $thickness

   cp input.g4bl ./$thickness
   cp HIFI_2D_symm.BLFieldMap ./$thickness
   
   cd $thickness

    # prints which thickness the simulation is being run with 
   echo "Running simulation start time = "$thickness "mm"

   # runs simulation in the correct thickness directory
   apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl mylar_thickness=$thickness > g4_out

   mkdir zntuples
   mv Z* ./zntuples

   #gnuplot ~/gpls/energy_distributions/energy_distr.gpl 

   #cd zntuples

  # python3 ~/python/energy_no_muon.py
   
   # move to previous directory   
   cd ..

done 
