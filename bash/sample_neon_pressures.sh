pressure="5 10 100 500 1000"

for press in $pressure
do 

   mkdir $press

   cp input.g4bl ./$press
   cp HIFI_2D_symm.BLFieldMap ./$press
   
   cd $press

    # prints which thickness the simulation is being run with 
   echo "Running simulation start pressure = "$press "mbar"

   # runs simulation in the correct thickness directory
   g4bl input.g4bl Ne_press=$press > g4_out

   # move to previous directory   
   cd ..

done 