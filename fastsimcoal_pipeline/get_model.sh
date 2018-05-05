#!/bin/bash
for ((i =1;i<=100;i++));
do
cp model2_boot.est  model${i}.est
cp model2_boot.tpl model${i}.tpl
done
