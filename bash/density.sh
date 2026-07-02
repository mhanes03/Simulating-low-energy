pressure="5 1000 5000"

for press in $pressure
do 
   mkdir $press

   cp input.g4bl ./$press

   cd $press

   atm_press=$press/1013

   rho=$atm_press*4/23780
   
   apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl He_density=$rho Pressure=$atm_press > g4_out

   mkdir zntuples
   mv Z* zntuples

   gnuplot ~/gpls/energy_distributions/energy_distr.gpl

   cd ..

done 