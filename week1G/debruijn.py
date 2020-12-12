
def Stringrec(Dna,k):
    suffix =	{}
    prefix =    {}
    pairs =     {}
    for i in range(0,len(Dna)-k+1):
        if Dna[i:i+k-1] in prefix.keys():
            if isinstance(prefix[Dna[i:i+k-1]],list):
                m=prefix[Dna[i:i+k-1]]
                m.append(Dna[i:i+k])
                prefix[Dna[i:i+k-1]]=m
            else:
                m=[prefix[Dna[i:i+k-1]]]
                m.append(Dna[i:i+k])
                prefix[Dna[i:i+k-1]]=m
        else:
            prefix[Dna[i:i+k-1]] = Dna[i:i+k]
    for i in range(0,len(Dna)-k+1):
        if Dna[i+1:i+k] in suffix.keys():
            if isinstance(suffix[Dna[i+1:i+k]],list):
                m=suffix[Dna[i+1:i+k]]
                m.append(Dna[i:i+k])
                suffix[Dna[i+1:i+k]]=m
            else:
                m=[suffix[Dna[i+1:i+k]]]
                m.append(Dna[i:i+k])
                suffix[Dna[i+1:i+k]]=m
        else:
            suffix[Dna[i+1:i+k]] = Dna[i:i+k]
    for key in suffix:
        print(suffix)
        if isinstance(key,list):#sufijo es una lista
            for key2 in key:
               for key1 in prefix:
                   if isinstance(key1,list):
                       for key3 in key1:
                           if  key2 == key3:  
                                if key in pairs.keys():
                                    if isinstance(pairs[prefix[key3]],list):
                                        m=pairs[key3]
                                        m.append(list(prefix.keys())[list(prefix.values()).index(suffix[key2])])
                                        key
                                        pairs[key3]=m
                                    else:    
                                        m=[pairs[key3]]
                                        m.append(list(prefix.keys())[list(prefix.values()).index(suffix[key2])])
                                        pairs[key3]=m
                                else:
                                    pairs[key3]=list(prefix.keys())[list(prefix.values()).index(suffix[key2])]
                   else:
                        if  key2 == key1:  
                            if key in pairs.keys():
                                if isinstance(pairs[prefix[key1]],list):
                                    m=pairs[key1]
                                    m.append(list(prefix.keys())[list(prefix.values()).index(suffix[key2])])
                                    key
                                    pairs[key1]=m
                                else:    
                                    m=[pairs[key1]]
                                    m.append(list(prefix.keys())[list(prefix.values()).index(suffix[key2])])
                                    pairs[key1]=m
                            else:
                                    pairs[key1]=list(prefix.keys())[list(prefix.values()).index(suffix[key2])]       
        else:#sufijo no es una lista entonces se utiliza key
            print('a')
            for key1 in prefix:
                if isinstance(key1,list):
                    for key3 in key1:
                        if  key == key3:  
                            if key in pairs.keys():
                                if isinstance(pairs[prefix[key3]],list):
                                    m=pairs[key3]
                                    m.append(list(prefix.keys())[list(prefix.values()).index(suffix[key])])
                                    key
                                    pairs[key3]=m
                                else:    
                                    m=[pairs[key3]]
                                    m.append(list(prefix.keys())[list(prefix.values()).index(suffix[key])])
                                    pairs[key3]=m
                            else:
                                pairs[key3]=list(prefix.keys())[list(prefix.values()).index(suffix[key])]
                else:
                    if  key == key1:  
                            if key in pairs.keys():
                                if isinstance(pairs[prefix[key1]],list):
                                    m=pairs[key1]
                                    m.append(list(prefix.keys())[list(prefix.values()).index(suffix[key])])
                                    key
                                    pairs[key1]=m
                                else:    
                                    m=[pairs[key1]]
                                    m.append(list(prefix.keys())[list(prefix.values()).index(suffix[key])])
                                    pairs[key1]=m
                            else:
                                    pairs[key1]=list(prefix.keys())[list(prefix.values()).index(suffix[key])]
            return(pairs)

def Stringrec2(Dna,k):
    prefix=     {}
    pairs =     {}
    for i in range(0,len(Dna)-k+1):
        if Dna[i:i+k-1] in prefix.keys():
            if isinstance(prefix[Dna[i:i+k-1]],list):
                m=prefix[Dna[i:i+k-1]]
                m.append(Dna[i:i+k])
                prefix[Dna[i:i+k-1]]=m
            else:
                m=[prefix[Dna[i:i+k-1]]]
                m.append(Dna[i:i+k])
                prefix[Dna[i:i+k-1]]=m
        else:
            prefix[Dna[i:i+k-1]] = Dna[i:i+k]
    for j in range(0,len(Dna)-k+1):
        for i in range(0,len(Dna)-k+1):
            if i==j:
                pass
            else:
                if Dna[i:i+k-1]==Dna[j+1:j+k]:#prefix suffix
                    if Dna[j:j+k-1] in pairs.keys():
                        if isinstance(pairs[Dna[j:j+k-1]],list):
                            m=pairs[Dna[j:j+k-1]]
                            m.append(Dna[i:i+k-1])
                            pairs[Dna[j:j+k-1]]=m
                        else:    
                            m=[pairs[Dna[j:j+k-1]]]
                            m.append(Dna[i:i+k-1])
                            pairs[Dna[j:j+k-1]]=m
                    else:
                        pairs[Dna[j:j+k-1]]=Dna[i:i+k-1]
    return(pairs)
    
def Stringrec3(Dna,k):
    nodes =	[]
    kmers = []
    for i in range(0,len(Dna)-k+1):
        nodes.append(Dna[i:i+k-1])
    for i in range(0,len(Dna)-k+1):
        kmers.append(Dna[i:i+k])
    nodes=list(set(nodes))
    nodes.sort()
    adjlist={}
    for i in nodes:
        List=[]
        for j in kmers:
            if i==j[:len(j)-1]:
                List.append(j[1:])
        adjlist[i]=List
    return adjlist            
A=Stringrec3('CCGGAAACGTAGCGCAATCAGTGGAGTAGCCTACGACGCGCGAGGCAGAGCGCTGGAGTAAGTACAGTCTGAATCATAATCCCTTGACATCTTCGCACTGCATATTGTCTTCCACGTGCCGCAGGGCCTCCTGGCCAAAAAGGCTTTAATTCTCAAGTTGCGGTCGCCCCTCAGAGGCTGGGCCTCTTCTAAGGCACAATCTAGAAGCGGTGACCGGCTCGTGTATCACAATCGAATAGCCCTTTTCACAACTGTCGGAAATGCCAGGGATAAGATCGTCGTTAGCCCTGGCCTGTCGATTAGTTCCGATACAGTAGTGTAAGAGCAGAGGACGCCTTGGGTATTGTGGATGTGAATACATAATGATCCTGCGCTAGGGTACTAGTGTGTACTTCGGGCTTAAGCCATACCGGTCATTTCCCGCCTCCAGAACCCCTAGAGCTTCGGGGGCCGTTCGACCCATTCCCGCCCTCAGATGCTGGTATGCGGGGATAATCCCTTATAAACAAACCAATATGATCCTAGCTTAGTGAAAAAATACCTGGACTGCAATATTGTACGAATACTTGTGGCGGACATACAGAAGTACAACCGGGATGCTAGGGCGTACTATTTGGTCCCCCTCCCCGGAGTGGGTTCAATTCTACCTAGATGGCGTGACAGCGGCCAACTCTGAGGTAATGGACATAAATTGATCAGTTTATGTTATGCGTTGCGTCTGGAGACAATTATCTTACAAGGCAACCCAGGTGGCCTCGGCGGGTAATACGCATGTATCATGGCTACTAAACTACTTACGGAGCTTCCTTTGTGGTTCGTTTATAGGCGAAATGGCGAGTTCCTCCTTTCCTATGTCGTTATCGTCCGGTGCGGCAGTAGGGTCCATGGTGAAGAACCACTATACTCGGACGAAGCATGCCTTCATAATGGGACTTCAGTAGCTCTTGGGGATATGGCGGTTATGGTTCACGCCCTTGCTAGTCTATATTATACTCTCTTAACGGTTGTCAAATCTCCAACCTCGATGTTATTTCTTCACAGTCCCACCAGCGGGCGGCAGAAACCGGGGGCCGTTGGTGACCTTAGACTGTGAGTGCGAGATTTCCTCATGTATGTAGACACTTGCTAGGTGAAGGCGCTTGACTACTAGGTTACCAATGTATTCACCTCACTCTTAACGTGGAGTTACCCCCGGAGACCTGATAGCGAGTAGAGGTCATAGTCTTGGTGCGCAGTGGTCTGAGTTTGAATAAGGAAGTCGATTTGCAACAGATAGGCTAGCGTCCTACCATTAATGGCAGGATTCCGACCGTGTGAAAGCCGTAGTGGCCCTGACCGGTAGTCCCGATGATGGATTTTTCTCTCTCCTGCCGACCGCTTATAGCGCTGTTGGCGTGCTAATTGCCCATGGCGACGTATATGTTATAACACTTCAGTTAGGTCATTCTACGTTCGGCCCTATAGAGACTGAATGTACGGACCGTTCCTGCACTAGCAATATCTTTAGCGATGACCTCGAACCACGGAATATTGTTTCTACAGTGAACGCGTCTATTGACCATCTATTGGGCAGGAGGACTTCATATACCGGGGTAATCCGTGTCAATTGGACCACCAAATACAACGCTAGTTTCGTAAGTTAGGCGTTGATATCTGATCACTAAGCGAGGTAGGTTCGCTCAGATCAGCTAACGGGTTGATCGCCGAAACTTTGTACAGAATACAGATTGGGCATTCGGAACACTAGGTTAAGACAAGGAACTGAATTCGTCGTGATGACAGTGTGTAATATTCCTCCTGCGAGTAGCTTTTTTCTAACCTCTGTCGCCCTGTTGATAGAAGACCGCTCAACACGACTGAAGACTTGTATTGAGTCCAATTAAATTTCGAAAGCCTGGCTCCCGGACCTATTTATTTCAACTGAGAGGGGTGTGGGAGTAATAATGAACGGGGGCCCACGTAGATTATCCCCATAATATCTGTTAGACATGTTCGCTCCC',12)
print(A)
for key, value in A.items():
    print(key + ' -> ' + ','.join(map(str, value)))
with open('dict.txt', 'w') as f:
    for key in A:
        if isinstance(A[key], list):
            f.write(''.join(key+' -> '+','.join(A[key])))
        else:
            f.write(''.join(key+' -> '+A[key]))
        f.write("\n")
'''
    for key in suffix:
        for key1 in prefix:
            if  suffix[key] == prefix[key1]:  
                if prefix[key] in pairs.keys():
                    if isinstance(pairs[prefix[key]],list):
                        m=pairs[prefix[key]]
                        m.append(prefix[key1])
                        pairs[prefix[key]]=m
                    else:    
                        m=[pairs[prefix[key]]]
                        m.append(prefix[key1])
                        pairs[prefix[key]]=m
                else:
                     pairs[prefix[key]]=prefix[key1]
                     '''

'''for i in range(0,len(Dna)-k+1):
        for j in range(0,len(Dna)-k+1):
            if suffix[Dna[i:i+k]]==prefix[Dna[j:j+k]]:
                if prefix[Dna[i:i+k]] in pairs.keys():
                    if isinstance(pairs[prefix[Dna[i:i+k]]],list):
                        m=pairs[prefix[Dna[i:i+k]]]
                        m.append(prefix[Dna[j:j+k]])
                        pairs[prefix[Dna[i:i+k]]]=m
                    else:    
                        m=[pairs[prefix[Dna[i:i+k]]]]
                        m.append(prefix[Dna[j:j+k]])
                        pairs[prefix[Dna[i:i+k]]]=m
                else:
                     pairs[prefix[Dna[i:i+k]]]=prefix[Dna[j:j+k]]'''