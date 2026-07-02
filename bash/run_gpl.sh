# For graphite degrader

press="50 500 1000"

for pressure in $press
do 
   
   cd $pressure

   gnuplot ~/gpls/energy_distributions/conditional.gpl

  # gnuplot ~/gpls/gifs/energy_v_time_gif_log.gpl

   
   # move to previous directory   
   cd ..

done 