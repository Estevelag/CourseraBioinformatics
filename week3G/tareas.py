
def prottrans(Dna):
    start=len(Dna)
    prot=[]
    translate={"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    for i in range(0,len(Dna)):
        if translate[Dna[i:i+3]]=="M":
            start=i
            coding=1
            break
    for i in range(start,len(Dna)-3,3):
        if translate[Dna[i:i+3]]=="STOP":
            break
        else:
            prot.append(translate[Dna[i:i+3]])
    return prot

def transcribe(Dna):
    DNA=""
    for i in range(0,len(Dna)):
        if Dna[i]=="T":
            DNA=DNA+"U"
        else:
            DNA=DNA+Dna[i]
    return DNA


D="ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
A=prottrans(transcribe(D))
B=''.join(A)
C=''.join(prottrans(transcribe(D)[::-1])) 
K=C+B
print(''.join(K))
