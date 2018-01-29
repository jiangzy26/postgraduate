#!/bin/python
with open('/disk-1/song/NHT130112/releaseData/re_call/sliding_win/blast.sort1')as fh:
	with open('/disk-1/song/NHT130112/releaseData/re_call/sliding_win/blast.sort2','w')as fw:
		L = set()
		lines = fh.readlines()
		for line in lines:
			column = line.strip().split('\t')
			
			if column[0] not in L:
			    fw.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n'%(column[0],column[1],column[2],column[3],column[4],column[5],column[6],column[7],column[8],column[9],column[10],column[11]))
			    L.add(column[0])

			     