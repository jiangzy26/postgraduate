with open('/disk-1/song/NHT130112/releaseData/re_call/sliding_win/f4.vcf') as fh:
    with open('/disk-1/song/NHT130112/releaseData/re_call/sliding_win/f4.vcfchangeChr1Chr2','w') as fw:
        lines = fh.readlines()
        for line in lines:
            column_a = line.strip().split('\t')
            if len(column_a[0]) == 4:
                #print(column_a[0])
               

                if str(column_a[0]) == 'chr1':
                    column_a[0] = 'chr100'
                    fw.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(column_a[0],column_a[1],column_a[2],column_a[3],column_a[4],column_a[5],column_a[6],column_a[7],column_a[8],column_a[9],column_a[10],column_a[11],column_a[12],column_a[13],column_a[14],column_a[15],column_a[16],column_a[17],column_a[18],column_a[19],column_a[20],column_a[21],column_a[22],column_a[23],column_a[24],column_a[25],column_a[26],column_a[27],column_a[28],column_a[29],column_a[30],column_a[31],column_a[32],column_a[33],column_a[34],column_a[35],column_a[36],column_a[37],column_a[38],column_a[39],column_a[40],column_a[41],column_a[42],column_a[43],column_a[44],column_a[45],column_a[46],column_a[47]))
                elif column_a[0] == 'chr2':
                    column_a[0] = 'chr200'
                    fw.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(column_a[0],column_a[1],column_a[2],column_a[3],column_a[4],column_a[5],column_a[6],column_a[7],column_a[8],column_a[9],column_a[10],column_a[11],column_a[12],column_a[13],column_a[14],column_a[15],column_a[16],column_a[17],column_a[18],column_a[19],column_a[20],column_a[21],column_a[22],column_a[23],column_a[24],column_a[25],column_a[26],column_a[27],column_a[28],column_a[29],column_a[30],column_a[31],column_a[32],column_a[33],column_a[34],column_a[35],column_a[36],column_a[37],column_a[38],column_a[39],column_a[40],column_a[41],column_a[42],column_a[43],column_a[44],column_a[45],column_a[46],column_a[47]))
                else: 
                    fw.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(column_a[0],column_a[1],column_a[2],column_a[3],column_a[4],column_a[5],column_a[6],column_a[7],column_a[8],column_a[9],column_a[10],column_a[11],column_a[12],column_a[13],column_a[14],column_a[15],column_a[16],column_a[17],column_a[18],column_a[19],column_a[20],column_a[21],column_a[22],column_a[23],column_a[24],column_a[25],column_a[26],column_a[27],column_a[28],column_a[29],column_a[30],column_a[31],column_a[32],column_a[33],column_a[34],column_a[35],column_a[36],column_a[37],column_a[38],column_a[39],column_a[40],column_a[41],column_a[42],column_a[43],column_a[44],column_a[45],column_a[46],column_a[47]))
  
            else: 
                fw.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' %(column_a[0],column_a[1],column_a[2],column_a[3],column_a[4],column_a[5],column_a[6],column_a[7],column_a[8],column_a[9],column_a[10],column_a[11],column_a[12],column_a[13],column_a[14],column_a[15],column_a[16],column_a[17],column_a[18],column_a[19],column_a[20],column_a[21],column_a[22],column_a[23],column_a[24],column_a[25],column_a[26],column_a[27],column_a[28],column_a[29],column_a[30],column_a[31],column_a[32],column_a[33],column_a[34],column_a[35],column_a[36],column_a[37],column_a[38],column_a[39],column_a[40],column_a[41],column_a[42],column_a[43],column_a[44],column_a[45],column_a[46],column_a[47]))
            	
