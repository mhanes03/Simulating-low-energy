
awk '{OFS=" " ; $1=""; gsub(/[[:space:]]+/, " "); print $0}' TRANSMIT.txt > new_TRANSMIT.txt

python3 ~/python/convert_to_BLTtrack.py