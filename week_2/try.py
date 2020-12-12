def Hammingdist(seq1,seq2):
    dist=0
    for i in range(0,len(seq1)):
        if seq1[i]!= seq2[i]:
            dist=dist+1
    return dist



def Profilemostprob1(Text,k,A):
    diction={'A': [0],
    'C': [1],
    'G': [2],
    'T': [3]}
    prob=[]
    for i in range(0,len(Text)-k+1):
        B=diction[Text[i]][0]
        P=float(A[B][0])
        D=Text[i+1:i+k]
        for c in range(0,len(D)):
            H=diction[D[c]][0]
            P=P*float(A[H][c+1])
        prob.append(P)
    pos=int(prob.index(max(prob)))
    return Text[pos:pos+k]
#print(Profilemostprob("GAGATCTCAGGTACTCCTAGAATACAAACTCCAGAATGTCCGAGCAGCAATACGTTGGGTGAGGTAACTCGTAGATATGGAACAATTACGGCCTTCGGCGCCTTATGTGGCGCAGCCCTCATACCTGTTACCTGGCAGTGCAATTCGCGAAAGCTGCTGCGGTTCCATGAGTGATGCGGGGACCGTGCTTGCTCGGTATACGACACGCACCGGCCGGGAGCGTCCCACGATCTGGACACTGTTCCAGAGGTATAATTGCATCAGGGCCAATTGCGCCCTGACTTAGGCTAAGGCAATCCGGTTCTATCGGTACACTCACGAGAATCCCCCAGTATGTCATAGTTGATGTTGCCTACTTCTCCATTTACGAAACCGTTGGTCTTACGGGCCACACCCCGTGCAGAACTGAACGCATATGACGTACAATAGGATTCCACCCATTCACTTTTTTGGCAGAGTCACCTTAGCACTCTTAACCCTAAATGGTAGATCACCTGCACTCCGTTCGGTAATTTCGACCATGATTAAGTCAGGTTTATGTTGTTGAGGCTGAATCGGAAGCAGAAGGGCAGAAATATTCGTCAACTAATATATAGGACTCTTTAGGGAATGTAAGGGGTCGCACGAGGCTGGTATCATCGCGTGGTTAGTCAGGGGAGCGTTCAAGCTAAGTCAGACCGCCAGGTCACATTGGTTAATTAATACTCTGTACTAACGACAACTCCCGGGCTCACTGGCAGAAATTCCGGCATAAAAATGATGAACCCTAATTCAGTTGCGGTGCTCTCTGCAGATGGAGGGATAAGCAATTACGATCCCATTACCCGGCAGAAATAGGTATATCGGGTTCCTCCTTGGGTCTCGGTATCTCTCGCTAGGCCCCCCCAAACTCCGATCACACTTGCGTCGGGTGTGACGGTCCGGTTATAGATAGGAGGGGGTCCTAAGGGCTATCCATGGGCTCGCAGGTTTGCAATTCTTGAGCCCGACCTCGATCATG",12,"""0.289 0.253 0.349 0.169 0.229 0.241 0.193 0.277 0.181 0.313 0.253 0.241

def createprofilemat(motifs):
    diction={'A': [0],
    'C': [1],
    'G': [2],
    'T': [3]}
    Matrix = [[0 for x in range(len(motifs[0]))] for y in range(4)]
    for i in motifs:
        for j in range(0,len(i)):
            fila=diction[i[j]][0]
            Matrix[fila][j]= Matrix[fila][j] + 1
    return Matrix


def normprofmat(Matrix): 
    Sum=[]
    for i in range(0,len(Matrix[0])):
        Sum.append(Matrix[0][i]+Matrix[1][i]+Matrix[2][i]+Matrix[3][i])
    for i in range(0,len(Matrix)):
        for j in range(0,len(Matrix[0])):
            Matrix[i][j]=Matrix[i][j]/Sum[j]
    return Matrix

def scorematrix(Matrix):
    score=[]
    Sum=[]
    for i in range(0,len(Matrix[0])):
        Sum.append(Matrix[0][i]+Matrix[1][i]+Matrix[2][i]+Matrix[3][i])
    Max=[]
    for i in range(0,len(Matrix[0])):
        Max.append(max([Matrix[0][i],Matrix[1][i],Matrix[2][i],Matrix[3][i]]))
    for i in range(0,len(Max)):
        score.append(Sum[i]-Max[i])
    return sum(score)


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
def Hammingdist(seq1,seq2):
    dist=0
    for i in range(0,len(seq1)):
        if seq1[i]!= seq2[i]:
            dist=dist+1
    return dist


def MedianString(Dna, k):
    distance=999999
    for i in range(0,(4**k)):
        Pattern=Num2Patt(i,k)
        currentdist = get_minscore(Pattern, Dna)
        if distance > currentdist:
            distance = currentdist
            Median = Pattern
    return Median

print(MedianString("""CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG""",7))