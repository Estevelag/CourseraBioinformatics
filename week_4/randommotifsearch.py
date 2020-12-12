import random
def createprofilematL(motifs):
    diction={'A': [0],
    'C': [1],
    'G': [2],
    'T': [3]}
    Matrix = [[0 for x in range(len(motifs[0]))] for y in range(4)]
    for i in motifs:
        for j in range(0,len(i)):
            fila=diction[i[j]][0]
            Matrix[fila][j]= Matrix[fila][j] + 1
    for i in range(0,len(Matrix)):#Laplace correction
        for j in range(0,len(Matrix[i])):
            Matrix[i][j]=Matrix[i][j]+1
    return Matrix



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

def normprofmat(Matrix): 
    Sum=[]
    for i in range(0,len(Matrix[0])):
        Sum.append(Matrix[0][i]+Matrix[1][i]+Matrix[2][i]+Matrix[3][i])
    for i in range(0,len(Matrix)):
        for j in range(0,len(Matrix[0])):
            Matrix[i][j]=Matrix[i][j]/Sum[j]
    return Matrix

# profile=normprofmat(createprofilematL(["CCA","CCT","CTT","TTG"]))
# motif=[]
# Dna="""AAGCCAAA
# AATCCTGG
# GCTACTTG
# ATGTTTTG"""
# Dna=Dna.split("\n")
# print(Dna)
# for i in range(0,len(Dna)):
#     motif.append(Profilemostprob1(Dna[i],3,profile))
# print(motif)

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

def RandomizedMotifSearch(Dna,k,t):
    Dna=Dna.split("\n")
    motifs=[]
    for i in range(0,len(Dna)):
        r = random.randrange(0, len(Dna[0])-k,1)
        motifs.append(Dna[i][r:r+k])
    i=1
    while i != 0:
        Motifs=[]
        profile=normprofmat(createprofilematL(motifs))
        for j in range(0,len(Dna)):
            Motifs.append(Profilemostprob1(Dna[j],k,profile))
        if scorematrix(createprofilematL(Motifs)) < scorematrix(createprofilematL(motifs)):
            motifs=Motifs[:]
        else:
            return motifs

def looprandom(Dna,k,t):
    lastmotifs = RandomizedMotifSearch(Dna,k,t)
    i=0
    while (i < 1000):
        bestmotifs = RandomizedMotifSearch(Dna,k,t)
        if scorematrix(createprofilematL(bestmotifs)) < scorematrix(createprofilematL(lastmotifs)):
            lastmotifs = bestmotifs[:]
        i += 1
    return lastmotifs

#print(*looprandom("""""",15,20),sep='\n')        

    





