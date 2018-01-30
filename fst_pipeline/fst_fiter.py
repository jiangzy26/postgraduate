#!/bin/python
with open('/disk-1/song/NHT130112/releaseData/re_call/sliding_win/fst/aToe/ABCDE100000.windowed.weir.fst') as fh:
	with open('/disk-1/song/NHT130112/releaseData/re_call/sliding_win/fst/aToe/ABCDE100000.windowed.weir.fst.filter','w') as fw:
		lines = fh.readlines()
		for line in lines:
			column = line.strip().split('\t')
			if int(column[3]) >= 10:
				fw.write('%s\t%s\t%s\t%s\t%s\t%s\n' % (column[0],column[1],column[2],column[3],column[4],column[5]))