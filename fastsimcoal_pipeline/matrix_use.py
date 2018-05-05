from __future__ import print_function
import sys
fh = open(sys.argv[1], "r") 

lines = fh.readlines()
for line in lines:
	column_a = line.strip().split(' ')
	for num in range(1, 101):
		print("%s " % column_a[num-1],end = '')
		if (num % 10 == 0):
			print("")
