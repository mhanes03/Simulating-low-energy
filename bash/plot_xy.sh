
var="2 2.5 3 3.5 4 4.5 5"

for folder in $var
do 
   
   cd $folder

   echo $folder

   gnuplot ~/gpls/x_and_y_restricted.gpl

   # move to previous directory   
   cd ..

done 