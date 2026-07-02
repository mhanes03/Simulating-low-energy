cat Det1.txt Det1_cp.txt > big_det1.txt
cat Det2.txt Det2_cp.txt > big_det2.txt

for i in {1..99..1}
do

    cat Det2_cp.txt >> big_det2.txt
    cat Det1_cp.txt >> big_det1.txt

    echo $i
done 
    
