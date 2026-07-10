# Purpose : match the electric field for different densities for a stopping power of 20 MeV cm^2 /g 
#
# Input : pressure values and the stopping power value wanted 
# Output : simulations for these parameters 
# 
# Limitations : 
pressure="50 100 150 200 250 500 750 1000"

for press in $pressure
do 
   mkdir $press

   cp input.g4bl ./$press

   cd $press

   atm_press=$press/1013

   rho=$atm_press*4/23780

   S=20
   efield=$S*$rho*100

   apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl E_field_magnitude=$efield He_density=$rho Pressure=$atm_press > g4_out

   mkdir zntuples
   mv Z* zntuples

   gnuplot ~/gpls/energy_distributions/energy_distr.gpl

   cd ..

done 
