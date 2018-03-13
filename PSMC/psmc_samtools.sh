#!/bin/bash

for bam in $(find /disk5/jiangzy/j/samtools/rmdup/*_rmdup.bam)
do

samtools mpileup -C 50 -Q 30 -q 20 -t DP,AD,INFO/AD -m 2 -uf /disk5/jiangzy/BGI_jiangzy_humilis/BGI_j_humilis.fa $bam | bcftools call -c - | vcfutils.pl vcf2fq -d 1 -D 100 | gzip > ${bam}.psmc.fq.gz

done

