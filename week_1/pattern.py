def pattern(A,B):
    count=[]
    for i in range(0,len(A)):
        if B == A[i:i+len(B)]:
            count.append(i)
    for i in range(len(count)):
        print(count[i])

pattern("CAGATTTTCAGATTTTCAGATTTCAGATTTCATCCCAGATTTGATTTGCCAGATTTCAGATTTTACACGAACAGACAGATTTCCAGATTTAACAGATTTGTACAGATTTCAGATTTGACAGATTTACAGATTTCAGATTTCCAGTTTTTTGACCAGATTTTTATCGGTCAGATTTCCCGCGAATGCAGATTTGCTCAGATTTCAGATTTACCCAGATTTGCCAGATTTGCAGATTTCAGATTTGCGCAGATTTCGCAGATTTATTCAGATTTGTCGTCCAGATTTTCAGATTTCAGATTTCAGATTTCAGATTTCAGATTTTGCATCCAGATTTCGCAGATTTCAGATTTGCCCGTGCTGTCAGATTTACAGATTTCGCAGATTTCTCAGATTTCAGATTTTTCAGATTTGAGGGAGTCAGATTTGGCCAGATTTCAGATTTCAGATTTCGCCAGATTTTCGGCAGATTTCGTGTATAAAGAGCAGATTTAACAGATTTACAGATTTGCAGATTTCAGATTTACAGATTTTGGCTAGAACAGATTTCAGATTTTCCCAGATTTCAGATTTATACGCAGATTTTCAGATTTGCAGATTTTCAGATTTTTCAGCAGATTTCAGATTTCAGATTTCTCCAGATTTCAGATTTCAGATTTTCGTCAGATTTGCAGATTTTCTGCAGATTTAGGCCAGATTTTCGTGCCAGATTTCGACCTTCAGATTTGGCCAGATTTCCTAGACGTCAGATTTCGGTCAGATTTCCAGATTTATCCAGATTTTGCACTGGACGACTACAGATTTTTGTAGCAGATTTAAACAGATTTGTCCTCAGATTTTAACCATCAGATTTTACCAGGGTAGCAGATTTTATGGCGCAGATTTATCTCCCCAGATTTCCAGATTTTACAGATTTCAGATTTCAGATTTTGACCAGATTTCAGATTTCAGATTTTCAGGCAGATTTGCGTGAGGCAGATTTCGAGGTCCCAGATTTGCGGTACAGATTTACTTGGCAGATTTCAGATTTCAGATTTCCATTTCCCAGATTTGGCTCGACAGATTTACCAGATTTTGATCAGATTTACAGATTTCAGATTTCAGATTTTCAGATTTGCAGATTTCACACAGATTTGTGTTCAGATTTCAGCAGATTTGCAGATTTCTGTTCAGATTTCAGATTTGCGGATCAGATTTCACAGATTTCAGATTTACTCTCAGATTTTAACAGATTTACAGATTTCCTGCCGCCAGATTTGCAGCAGATTTCCATAGCAGATTTCAGATTTCCAGATTTGTCAGATTTGATTCAGATTTCAGATTTCAGATTTCAGATTTGGCAGATTTAGTTATTCAGATTTCAGATAACAGATTTATGATCTGCAGATTTCAGATTTACAGATTTCAGATTTCATCGCAGATTTGTACTGCTAGCCAGATTTTCAGATTTATACAGATTTATAACAGATTTATAAACTACAGATTTTAAGATGGTCCAGATTTGATAGACAGATTTCAGATTTTTGTACAGATTTACAGATTTCAGATTTTCAGATTTCCAGATTTTTGGCACGTCAGATTTGTGTATCAGATTTCCAGATTTCGGTCGATGTTCAGATTTACTCCAGATTTTACAGATTTACGTCAGATTTCAGATTTCAGATTTCAGATTTTCTGATCTCAGATTTTTTTTATCAGATTTTGCAGATTTCGCAGATTTAGTCAGATTTCAGATTTCAGTTCCCAGATTTATACAGATTTAGCAGATTTTTACAGATTTCCAGATTTCAGATTTCAGATTTCAGATTTCCCCCAGATTTGCGCAGATTTGTCTCACCCAACGTACGACACAGATTTTCCAGATTTCAGATTTCAGATTTTAACAGATTTTAGACAGATTTCAGATTTCTCAGATTTGCAGATTTCAGATTTCAGATTTGCAGATTTTCAGATTTAGCGGCAGATTTCAGATTTCGCAGCAGATTTCAGATTTCCCAGATTTTACAGACAGATTTACAGATTTTCCCCAGATTTACGCTCAAGCCCGTCAGATTTCAGATTTCACAGATTTACCAGATTTACAGATTTCAGATTTTCACAGATTTAACAGATTTAAAATTACACAGATTTCAGATTTCAGATTTCAGATTTCCAGATTTCAGATTTCAGATTTTATAGGCACAGATTTGCGCCCAGATTTTTACAGATTTCCGAAACAGATTTCCAGATTTGTCAGATTTTGCAGATTTCCCAGATTTCACAGATTTACAGATTTACTGTGGCAGATTTACCGCAGATTTGTCAGATTTCAGATTTCAGATTTCACAGATTTCACCAGATTTTTCCAGCAGATTTATTAATTCAGATTTCAGATTTCAGATTTTCAGATTTATAGTCTCAGATTTCAGATTTTCCTACAGATTTTAACAGATTTTCCAGATTTCCAGATTTCGCAGATTTCCCAGATTTCCTGACGCAGATTTGCAGATTTCAGATTTCCCAGATTTCAGATTTCCCAGATTTCAGATTTTGCAGATTTGTCAGATTTCAGATTTTGCAGATTTACAGATTTCACTTTAGCCAGATTTTGCAGAGTATGCAGATTTACAGCCGCGAACAGATTTGCAGATTTTACCACCATCAGATTTCAGATTTCCAGATTTCAGATTTCACGGTCAGATTTTCAGATTTACCAAATAACAGATTTCAGATTTCTGCCCAGATTTAGGCAGATTTCTCAGATTTGCAGGGGTCGGTACAGATTTCAGATTTCGCAGATTTGGGTTCAGATTTCCAGATTTCCCAGATTTTCAGATTTGTACCAGATTTCCAGATTTTTCACTCCGCATAAAAGGTGAGGCAGATTTAACAGATTTCAGATTTCAGATTTCCTCAGATTTACCTGCAGATTTCAGATTTACCGCACAGATTTGGCAGATTTTGCCGTAGTGCTCATCAGATTTCAGATTTACAGATTTCTAGCGCAGATTTCAGATTTTTGCAGATTTCAGATTTTCGCAGATTTGAAGCTCCAGATTTTACAGATTTGTCCTCAGATTTCACTGCAGATTTCAGATTTGTCTACGTGCCAGATTTCAGATTTACTTCAGATTTAAGCCAGATTTCAGATTTACAGATTTCAGATTTACAGATTTGCAGATTTCCTCCCTGTTATTCCTTACGCACCACAGATTTCAGATTTCAGATTTCACATCCAGATTTCAGATTTACATTCAGATTTCAGATTTAGCAGATTTCAGATTTGCAGATTTCGCAGATTTCAGATTTCAGATTTAGTCAGATTTCAGATTTCTTATTCAGATTTCAGATTTAGCGCAGATTTGCAGATTTTCCCCCAGATTTCAGATTTCACAGATTTCAGATTTCAGATTTCAGATTTACCTCAGATTTCAGATTTACAGATTTGCAGATTTGGTGCAGATTTCAGATTTCAGATTTCGTGACAGATTTACTTCCCCCAGATTTGCATCCAGATTTAATTTAGGCAGATTTATCAGATTTGGCAGGCAGATTTAAGGCAGATTTGCATTCGTGGTAAGTGCAGATTTGACCAGATTTCAGATTTACCTACAGATTTGGTTGCAGATTTTATTCCCAGATTTCCCAGATTTAAGAATGGTTATTCAGATTTCCCAGATTTCAGATTTCAGATTTGGCACTAAATCAGATTTCAGATTTGCCCTCGGACAGATTTTAGAAATTAGTATCCGCCCAGATTTGTTCAGATTTGCAGATTTGGCAGATTTCAGATTTCCCAGATTTGGTCAGATTTGGCAGATTTCGGGACAGATTTGCCCAGATTTGTCAGATTTGCTACTCAGCGGTCGCAGATTTGCAGATTTCACAGATTTGCAGATTTGGGCAGATTTCAGATTTTACCGCAGATTTCTCCCAGATTTGACAGATTTGTACAGATTTCAGATTTTTTCAGATTTCCTTATCCTTCGCAGATTTACAGATTTAGGCAGCAGATTTCAGATTTGGATGTACAGATTTACAGATTTCAGATTTCTCCAGATTTGTCAGATTTTCAGATTTCAGATTTCAGATTTATACAGATTTCAGATTTCAGATTTAACTCCAGATTTTGTCAGATTTTTCCGGACAGATTTATGGCAGATTTCTTCAGATTTAATCTAACAGATTTCAGATTTCAGATTTACACAGATTTGCTCAGATTTCAGATTTGCAGATTTCTGGCCCGACCACAGATTTCACCAGATTTACTCAGATTTCGCCAGATTTGCCACAGATTTCAGATTTCAGATTTCAGATTTCCAGATTTTCAGATTTACCAGATTTGGAGCTCGAGCAGATTTCAGATTTCTGCAGATTTACAGATTTTCAGATTTAGCAATACAGATTTTCAGATTTCAGATTTTAGCCTAACAGATTTCTCAGATTTTGTAGTTCCAGATTTTCTACCACAGATTTGCAGATTTCAGATTTTGCGGGCAGATTTACAGATTTCAGATTTTACAGATTTTCAGATTTACAGATTTGCCGCAGATTTACAGATTTCAGATTTGACCCTCAGATTTTATACAGATTTATCAGATTTCAGATTTCCAACGCAGATTTCAGATTTGCAGATTTCAGATTTATCAGATTTACAGATTTCGCAGATTTGGGTCAGATTTTCTGCCCAGATTTCGGCCAAGTACAGATTTCACAGATTTACAGATTTGAGCAGATTTACCGCAGATTTGACCAGATTTGCAAGTACTGTTAGGGGACGCAGATTTAACAGATTTCCAGATTTATGCAGATTTATCAGATTTTCCCAGATTTCAGATTTTTAACAGATTTCGTCAGATTTCTAGCAGATTTTCAGATTTTCAGATTTCATCAGATTTCCAGATTTCAGATTTCAGATTTCCAGATTTCAGATTTCAGATTTCTCCCAGATTTATCAGATTTCAGATTTAACGTCGCAACTCACAACAGATTTACAGATTTCAGATTTCTCAGATTTGAACTGAACCAGATTTCTCGATACGGCAGATTTTCAGATTTAAGGCACAGATTTTCTGCACAGATTTCAGATTTCTCGCAGATTTGTCCCCAGATTTTAACAGATTTCATCAGATTTTCAGATTTGACAGCAGATTTCGTATCAGATTTCAGATTTGAGCAGATTTTACAGATTTTCAGATTTGCAGATTTCAGATTTAACAGATTTCCAGATTTCCCAGATTTGTGCAGATTTGCTCAGATTTAGCTTCAGATTTCAGATTTCACCAGATTTGTCCAGATTTTACAGATTTCAGATTTCAGATTTCAGATTTAGTTTCAGATTTCCAGATTTACAGATTTCAGATTTGCAGATTTTAAAGCCAGATTTACCAGATTTCATTCATCCCAGTGGACAGATTTCAGATTTTCCAGATTTGGTCTCAGATTTACCAGATTTCAGGTATATCAGATTTAAGGAGTCAGATTTCAGATTTCACAGATTTGCCAGCCAGATTTTTTCCCTCCCAGATTTTGGCGCTCAGATTTAGCAGATTTCCAGATTTCAGATTTCAGATTTACCAGATTTTCAGATTTTTGCAGATTTAGGAAGCAGATTTTTCAGATTTTCAGATTTGCCAGATTTTCAACTGTTGCCAGATTTCAGATTTGGGGTTTCCAGATTTTTCAGATTTTATGACAGATTTGTTCAGCTGCCGTCAGATTTGCAGATTTGCAGATTTCAGATTTCACCAGATTTCAGATTTTCAGATTTTAGCAGATTTCAGATTTGCAGATTTTATACAGATTTTCCCAGATTTTCAGATTTAAGTCAGATTTATCAGATTTCAGATTTCAGATTTTCAGATTTACAGCAGATTTTCGCGCAGATTTTCAGATTTGGTCAGATTTCAGATTTCAGATTTTACAGATTTAATCGATCCAGATTTCCCAGATTTGTCGGTGCAGATTTAGTTCGCAGATTTCTGCCACAGATTTTCAGATTTACAGATTTTCAGATTTATTCACAGATTTATCAGATTTCAGATTTCCAGATTTCGACGAAAACACAGATTTGTCAGATTTCAGATTTCAGATTTCAGATTTACAGATTTACAGATTTCCAGATTTGTCAGATTTCAGATTTTAGGACAGATTTACAGATTTCTCAGATTTCTCCCCCAGATTTGCATAGGTAATATGCCAGATTTTGGAACATTACAGATTTGAACAGATTTTCAGATTTCCTCGCAGATTTTCAGATTTCAGATTTTGGGGTGAGACATTCAGATTTCAGATTTCAGCAGATTTCCCCCCAGATTTATTTCAGATTTAAGGCAGATTTCCGTCAGATTTCAGATTTACAGATTTTGGCCAGATTTTCCAGATTTCCGCAGATTTGACCAGATTTTACTTGCAGATTTTCAGATTTCAGATTTCCAGATTTTTACAGATTTTATCAGATTTCAGATTTTCAGATTTCCAGATTTCAGATTTCAGATTTATTCGTCAAAGGCCAGATTTGAGTGCGCAGATTTGTGGCAGATTTCGCCAGATTTCAGATTTCAGATTTACAGATTTCAGATTTCAGATTTAATCGGTGTTTTCATCCAGATTTCAGATTTGCAGATTTCAGATTTAGTCAGATTTTGCAGATTTCCAGATTTCCAGATTTTTCTGGGCGTAATCTTAGACAGATTTCCACAACGTGCTTTTGAACGACCTCAGATTTGCCAGATTTCGACATGCCGCAGATTTCCAGATTTCAGATTTATGTAGTGCAGATTTAACAGATTTCTCAGATTTTACTTTCCAGACCAGATTTCTAACAGATTTCAGATTTGCAGATTTCGACAGATTTCAGATTTCAGATTTGCAGATTTCCAGATTTGACAGATTTTACAGATTTAACAGATTTCAGATTTACAAGGCAGATTTCAGATTTGGGGAACCGTCAGATTTTACATCAGATTTACAGAGCCAGATTTCCAGATTTCAGATTTTCAGATTTTACAGATTTTCAGATTTCAGATTTTACAGATTTCAGATTTCAGATTTTGAGTCTGCAGATTTTTGCAGAACAGATTTGCAGATTTAGTACTCAGATTTACAGATTTGCCAGATTTCATCGGCAGATTTGGGCGCAGATTTTAGCCGGCGGCAGATTTTGCAGATTTCAGATTTTCACAGATTTCAGATTTGTAACTCACAGATTTCAGATTTACAGATTTCACAGATTTTATGGCCAGATTTGTGCAGATTTCAGATTTCAGATTTTCAGATTTCACAGATTTCCAGATTTGGTCAGATTTATGCAGATTTCTAACACAGATTTTTCTGATGCAGATTTCAGATTTCACAGATTTGACGACAGATTTTTCAGATTTCCAGATTTCAGATTTTTCAGATTTTAACCAATTAGGGCAGATTTCAGATTTAGCAGATTTGGCGTACCAGATTTGCAGATTTGGCCCAGATTTGTCAGATTTCAGATTTAAGCAGATTTACAGATTTGTCAGATTTCAGATTTTCATGGCCAGATTTGGCCCAGATTTTCTCAGATTTCAGATTTACACAGATTTCAGATTTCAGATTTTCAGACAGATTTTTGGTACAGCAGATTTCCAGATTTGCAGATTTCAGATTTCTCCAGATTTATACCAGATTTTACAGATTTACCAGATTTTAGCAGATTTAGGTCTATACAGATTTCGCAGATTTCAGATTTCAGATTTTACAGGATTTCAGATTTTGAGGGCCAGATTTCACAGATTTTCACAGATTTAGTCAGATTTCTCAGATTTCCCAGATTTCCAGATTTCCAGATTTTGTCGACAGATTTTCCAGATTTCCCCCCGTCCAGATTTGATTCAGATTTAGCAGATTTCACAGTAGACCCATCCAGATTTGCACAGATTTCAGATTTGCAAAAATAAACAGATTTGACAGATTTGGTCAGATTTCTACCCCCAGATTTCAGATTTCAGATTTCTCCCCGATACAGATTTAGCGTGGGGCAGATTTAACAGATTTTCGCAGATTTGGGGCAGATTTAGCAGATTTGCAGATTTCCCAGATTTACCCAGATTTCCAGATTTCGAGCAGATTTTGGCAGATTTTCGTCAGATTTCAGATTTCAGATTTAGCCAGATTTTACATCAGATTTCAGATTTCAGATTTCAGATTTCAGATTTGATCCAGATTTGTTCGTACCCAGATTTTAAAGTACAGATTTTCAGATTTTCAGATTTGCGACAGATTTACAGATTTAGACAGATTTCGGCCACAGATTTTAGCTCGCGGCAGATTTGCAGATTTTCAGATTTTATGCAGATTTCAGATTTACAGATTTGCAGATTTTCCAGATTTTCCAGATTTTGCAGATTTGTCAGATTTTTCAGCAGATTTCCACAGATTTAACATCAGATTTATACCAGATTTCTTACAGATTTAACGCAGATTTCTCCAGATTTTGCGTACGTGATCCAGATTTACAGATTTGAAGTCAGATTTCAGATTTCAGATTTAACAGATTTGTAGCAGATTTCAGATTTCCAGATTTCCAGATTTGGCCAGATTTTTTCAGATTTCCCAGATTTCGCCCTGGCAGATTTATTAGGCAGATTTCCGGCAGATTTAATCCAGATTTCAGATTTCAGATTTAGCAGATTTGGTCTCCCAGATTTTTTCTCAGATTTATGCAGATTTATGGCAGATTTGCAGATTTTTTCGACAGATTTCCCAGATTTCTGCAGATTTCAGATTTGCAGATTTGACAGATTTTTCAGATTTATCAGATTTGCAGATTTCAGATTTGCCAGATTTCACAGATTTCAGATTTACAGATTTACCAGATTTGCGTGGGATACAGATTTCAGATTTCACCAGATTTTCCAGATTTCAGATTTGCAGATTTGCAGATTTCAGATTTACCAACACAGATTTGACCAGATTTATCCTTGCAGATTTGTAGTCTGTGAACAGATTTACCAGATTTAACCAGATTTGCAGATTTAGCAGATTTAACAGATTTCTGCCAGATTTCAGATTTCAGATTTACAGATTTCCTTCAGATTTCAGATTTATTTCAGATTTCAGCGCAGATTTTATGTGGGCAGATTTTTCCAGATTTCCCAGATTTTTACAGATTTGACCAGTCAGATTTACCGGCAGATTTCAGATTTCGCAGATTTCACCAGCAGATTTGCAGATTTCAGATTTCAGATTTCAGATTTCGACCAGATTTCTTGAGAAACTGGCTTCCAGATTTACCTTACAGATTTGTGCAGATTTACAGATTTCAGATTTGTCAGATTTAGCAGATTTTACAGATTTTGAGGCCCAGATTTAACAGATTTCCAGATTTACCAGATTTAGAAACAGATTTGGCCGCAGATTTGAGCAGATTTCAGATTTCAGATTTGTTCAGATTTAGCAGATTTGGAAAAGACAGATTTCCAGATTTTGCAGATTTGTCAGATTTCAGATTTACAGATTTGTACGAGGCAGATTTCAGATTTCCAGATTTCAGATTTCAGATTTCTGCACAGATTTCTATCCAGATTTGCAGATTTCCGCATCAGATTTACAGATTTTCCCAGATTTACCACAGATTTCGCAGATTTCCCGAACCTTGCACTCAGATTTCCAGATTT","CAGATTTCA")