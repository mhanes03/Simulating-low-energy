# !/bin/sh

#mkdir zntuples
mkdir analysis

#mv Z* ./zntuples

echo 'plotting momentum plots'

gnuplot ~/gpls/momentum_v_z.gpl

mv ./zntuples/*.pdf ./analysis
mv ./zntuples/*gif ./analysis

echo 'plotting z stopping distribution'

gnuplot ~/gpls/stopping_distr.gpl

mv *.pdf ./analysis

echo 'calculating stopping efficiency and average stopping distance'

python3 ../../stopp_efficiency.py > stop_eff_values.txt

