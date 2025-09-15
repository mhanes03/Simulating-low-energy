# !/bin/sh

for length in $(seq 200 100 1000)
do
    pressure=20

    # moves into the directory for thickness being sampled
    cd $length

    # prints the current working directory
    pwd 

    # prints which length the simulation is being run with 
    echo "Finding stopping efficiency for = "$length 'mm'

    sed 's/change_this/'"$length"'/g' ../../efficiency_len.py > ./efficiency_len.py 
    python3 efficiency_len.py >> ../efficiency.txt

    # move to previous directory
    cd ..

done 