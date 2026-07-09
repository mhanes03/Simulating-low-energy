# Purpose : to remove the T from the TRANSMIT file and remove the white space in the first column, and run the python script to produce the beam file
#
# Input : TRANSMIT file from SRIM 
# Output : the new TRANSMIT file that removes the first column, and then beam file from the python file 
awk '{OFS=" " ; $1=""; gsub(/[[:space:]]+/, " "); print $0}' TRANSMIT.txt > new_TRANSMIT.txt

python3 ~/python/convert_to_BLTtrack.py
