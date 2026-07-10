# Purpose : removes the low energy positrons from the detector file, by looking at their initial energy 
#
# Input : detector files  
# Output : detector files without the low energy positrons 
# 
# Limitations : 
awk '$28 > 26' Det1.txt > Det1_remove_le.txt

awk '$28 > 26' Det2.txt > Det2_remove_le.txt
