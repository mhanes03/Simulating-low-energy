
time="40 60 80 100 120 200"

for starts in $time
do 
   
   cd $starts

    # prints which thickness the simulation is being run with 
   echo "Running simulation start time = "$starts

   gnuplot ~/gpls/energy_v_time_gif_log.gpl

   bash ~/bash/sort_time.sh

   gnuplot ~/gpls/energy_v_z_gif_log.gpl


   # move to previous directory   
   cd ..

done 