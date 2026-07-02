
mkdir in_cell

radius=12

for i in $(seq 10 10 140)
do 
	awk '$1**2+$2**2 <= f"{$radius**2}"' Z$i.txt > ./in_cell/in_cell_Z$i.txt

done 

cd ./in_cell
python3 ~/python/how_many_muons_cell.py
gnuplot ~/gpls/in_cell.gpl