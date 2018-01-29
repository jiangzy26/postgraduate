#the output of blastn may contain scafforlds, so we need to delete these lines include scafforlds
with open('/disk-1/song/NHT130112/releaseData/re_call/sliding_win/DeleteGi.blast', 'w') as f:
    f.write(''.join([line for line in open('/disk-1/song/NHT130112/releaseData/re_call/sliding_win/12.fil.contigs.fa.blast').readlines() if 'gi' not in line]))
