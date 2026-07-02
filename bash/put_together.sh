energy="0.0020 0.0019 0.0018 0.0017 0.0016 0.0015 0.0014 0.0013 0.0012 0.0011 0.00100 0.00090 0.00080 0.00075 0.00070 0.00065 0.00060 0.00055 0.00050 0.00045 0.00040 0.000375 0.000350 0.000325 0.000300 0.000275 0.000250 0.000225 0.00020 0.00019 0.00018 0.00017 0.00016 0.00015 0.00014 0.00013 0.00012 0.00011 0.00010"

touch 0.1
touch 0.01
touch 0.001

for energies in $energy
do 
    cd $energies

    thickness="0.001 0.01 0.1"

   for thickness_val in $thickness
   do 

      # moves into the directory for thickness being sampled
      cd $thickness_val

      # prints the current working directory
      pwd 

      cd zntuples

      cat stopping_power_2.txt >> ../../../$thickness_val

      # move to previous directory
      cd ../..

    done 

    cd ..

done 