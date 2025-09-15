# !/bin/sh

for length in $(seq 200 100 1000)
do

    # moves into the directory for thickness being sampled
    cd $length

    # prints the current working directory
    pwd 

    # prints which length the simulation is being run with 
    echo "Finding average stopping for = "$length 'mm'

    sed 's/change_this/'"$length"'/g' ../../avg_stop.py > ./avg_stop.py 
    python3 avg_stop.py >> ../avg_stop.txt

    # move to previous directory
    cd ..

done 