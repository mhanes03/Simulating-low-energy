
mkdir three_runs_2

cp -r HIFI_2D_symm.BLFieldMap input.g4bl ./three_runs_2

cd ./three_runs_2

for i in $(seq 1 3 1)
do 
	mkdir $i 

	cp -r HIFI_2D_symm.BLFieldMap input.g4bl ./$i

	cd $i 

	apptainer run --app g4blmpi ~/g4blmpi_muoncooling_20250821.sif 16 input.g4bl > g4_out

	cd ..

done