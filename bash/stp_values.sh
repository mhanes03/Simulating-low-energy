# Purpose : to match electric field value with different stopping power values for constant pressure
#
# Input : pressure value and stopping power values 
# Output : simulations for each electric field valule  
# 
# Limitations : 
S="80 70 60 50 40 30 20"

for stp in $S
do 
   mkdir $stp

   cp input.g4bl ./$stp

   cd $stp

   atm_press=5/1013

   rho=8.2152e-7

   efield=$stp*$rho*100

   echo "density"$rho "e field"$efield

   apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl E_field_magnitude=$efield He_density=$rho > g4_out

   mkdir zntuples
   mv Z* zntuples

   gnuplot ~/gpls/energy_distributions/energy_distr.gpl

   cd ..

done 
