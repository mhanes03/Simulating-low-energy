# Purpose : runs the python file and runds g4bl simulation 
#
# Input : python script and input file for g4bl  
# Output : beam file from the python script 
# 
# Limitations : 
python3 ~/python/make_beam__file_distr.py

g4bl input.g4bl > g4_out
