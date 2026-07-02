for i in $(seq 15 1 30)
do 
   
   cd $i/zntuples

   echo $i >> ../../by_hand_optimum.txt

   awk '$1 == 500' E_mean_no_muons_z.txt >> ../../by_hand_optimum.txt 

   cd ../..

done 
