#!/bin/bash
for x in $(find /disk5/jiangzy/fsc_sam/redothefsc/sfs/sfs10/*.sfs)
do
python matrix_use.py ${x} > ${x}_new.sfs
done
