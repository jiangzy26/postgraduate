#!/bin/bash
for i in $(find /disk5/jiangzy/fsc_sam/redothefsc/sfs/sfs/step1/*)
do
awk 'NR==3{$1="d1_0"}NR==4{$1="d1_1"}NR==5{$1="d1_2"}NR==6{$1="d1_3"}NR==7{$1="d1_4"}NR==8{$1="d1_5"}NR==9{$1="d1_6"}NR==10{$1="d1_7"}NR==11{$1="d1_8"}NR==12{$1="d1_9"}{print}' $i > ${i}_use.sfs
done
