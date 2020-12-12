#print((0.25**9)*992*500)
def Hammingdist(seq1,seq2):
    dist=0
    for i in range(0,len(seq1)):
        if seq1[i]!= seq2[i]:
            dist=dist+1
    return dist

def neighboors(Pattern,d):
    if d==0:
        return{Pattern}
    if len(Pattern)==1:
        return {"A","C","T","G"}
    neilist=set()
    Suffixneighbors=neighboors(Pattern[1:],d)
    for i in Suffixneighbors:
        if Hammingdist(Pattern[1:],i) < d:
            for x in "ACTG":
                neilist.add(x+i)
        else:
            neilist.add(Pattern[0]+i)
    return list(neilist)

def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return True 
    else: 
        return False
    
def motifenum(Dna,k,d):
    Patterns=set()
    Dna=Dna.split("\n")
    for a in range(0,len(Dna[0])-k+1):
        neighbours=neighboors(Dna[0][a:a+k],d)
        for w in neighbours: 
            m=0
            for j in range(1,len(Dna)):
                elems=[]
                for i in range(0,len(Dna[j])-k+1):
                    elems.append(Dna[j][i:i+k])
                neigbours2=neighboors(w,d)
                if common_member(elems,neigbours2)==True:
                    m=m+1  
            if m ==(len(Dna)-1):
                Patterns.add(w)
            
    return list(Patterns)

def get_motifs(pattern, dnas):
    dnas=Dnas.split(' ')
    k = len(pattern)
    n = len(dnas[0])  # <== assuming  same length
    motifs_loc = []
    for string in dnas:
        distance = None
        min_distance = None
        min_kmer_loc = None
        for i in range(n - k +1):
            if i == 0:
                min_distance = Hammingdist(pattern, string[i:i+k])  
                min_kmer_loc = i
            else:
                distance = Hammingdist(pattern, string[i:i+k])
                if min_distance >= distance:
                    min_distance = distance
                    min_kmer_loc = i
        motifs_loc.append(min_kmer_loc)
    motifs = [dnas[i][motifs_loc[i] : motifs_loc[i]+k] for i in range(len(motifs_loc))]

    return motifs

def get_minscore(pattern, dnas):
    k = len(pattern)
    n = len(dnas[0])  # <== assuming  same length
    dist=0
    motifs_loc = []
    for string in dnas:
        distance = None
        min_distance = None
        min_kmer_loc = None
        for i in range(n - k +1):
            if i == 0:
                min_distance = Hammingdist(pattern, string[i : i+k])  
                min_kmer_loc = i
            else:
                distance = Hammingdist(pattern, string[i : i+k])
                if min_distance > distance:
                    min_distance = distance
                    min_kmer_loc = i
        motifs_loc.append(min_kmer_loc)
        dist=dist+min_distance
    motifs = [dnas[i][motifs_loc[i] : motifs_loc[i]+k] for i in range(len(motifs_loc))]
    return dist

def Num2Patt(A,B):
    l=[None]*B
    for i in range(0,B):
        l[i]=A%4
        A=A//4 
    for i in range(0,len(l)):
        if l[i]==0:
            l[i]="A"
        elif l[i]==1:
            l[i]="C"    
        elif l[i]==2:
            l[i]="G"    
        elif l[i]==3:
            l[i]="T" 
    l=l[::-1]   
    return ''.join(l)

def median_string(Dna,k):
    Dna=Dna.split("\n")
    distance=999999
    for i in range(0,(4**k)):
        Pattern=Num2Patt(i,k)
        currentdist = get_minscore(Pattern, Dna)
        if distance > currentdist:
            distance = currentdist
            Median = Pattern
    return Median

print(median_string("""CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG""",7))
