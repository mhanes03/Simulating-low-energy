
for energy in $(seq 1 0.5 2.5)
do 

  cd $energy

  rm values.txt
  
  for thickness in $(seq 0.01 0.01 0.1)
  do 


      # moves into the directory for thickness being sampled
      cd $thickness

      # prints the current working directory
      pwd 

      cd zntuples

      python3 ~/python/energy_no_muon.py

     (echo $thickness ; sed '1!d' E_mean_no_muons_z.txt ) >> ../../values.txt


      cd ../..

  done 

  cd ..

done 