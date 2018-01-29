#!/bin/python
fw_lines1 = open('/disk-1/song/NHT130112/releaseData/re_call/sliding_win/No1.blast','w')
fw_lines2 = open('/disk-1/song/NHT130112/releaseData/re_call/sliding_win/No2.blast','w')
with open('/disk-1/song/NHT130112/releaseData/re_call/sliding_win/blast.sort2')as fh:
	for line in fh:
	    key = line.split('	')[0]
	    chr = line.split('	')[1]
	    q1 = line.split('	')[6]
	    q2 = line.split('	')[7]
	    t1 = line.split('	')[8]
	    t2 = line.split('	')[9]    
	    if int(t1) < int(t2):
	        value = int(t1) - int(q1) + 1
	        fw_lines1.write('%s\t%s\t%s\n' % (key,chr,value))
	    else:
	        value = int(t1) + int(q1)
	        fw_lines2.write('%s\t%s\t%s\n' % (key,chr,value))

fw_lines1.close()
fw_lines2.close()