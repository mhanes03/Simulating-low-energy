variable="0.9 0.8 0.7 0.6 0.5"

for var in $variable
do 
   mkdir $var

   cp input.g4bl ./$var

   cd $var

   V_breakdown=1.02

   volt=$var*$V_breakdown

   apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl E_field_magnitude=$volt > g4_out

   mkdir zntuples
   mv Z* zntuples

   gnuplot ~/gpls/energy_distributions/energy_distr.gpl
   gnuplot ~/gpls/gifs/stills.gpl

   cd ..

done 