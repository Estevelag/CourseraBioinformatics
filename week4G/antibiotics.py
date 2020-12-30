
# def prottrans(Dna):
#     start=len(Dna)
#     prot=[]
#     translate={"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
#     "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
#     "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
#     "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
#     "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
#     "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
#     "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
#     "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
#     "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
#     "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
#     "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
#     "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
#     "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
#     "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
#     "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
#     "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
#     for i in range(0,len(Dna)):
#         if translate[Dna[i:i+3]]=="M":
#             start=i
#             coding=1
#             break
#     for i in range(start,len(Dna)-3,3):
#         if translate[Dna[i:i+3]]=="STOP":
#             break
#         else:
#             prot.append(translate[Dna[i:i+3]])
#     return prot,start

def transcribe(Dna):
    DNA=""
    for i in range(0,len(Dna)):
        if Dna[i]=="T":
            DNA=DNA+"U"
        else:
            DNA=DNA+Dna[i]
    return DNA

# D="ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
# A,start=prottrans(transcribe(D))
# B=''.join(A)
# C,startrev=prottrans(transcribe(D)[::-1])
# E=''.join(C)
# pattern="MA"
# import re
# index=re.finditer(pattern,B)
# pos=[]
# for match in re.finditer(pattern,B):
#     phrase = match.group(0)
#     pos.append(match.start())
# posrev=[]
# for match in re.finditer(pattern,E):
#     phrase = match.group(0)
#     posrev.append(match.start())
def reversecom(A):
    A=list(A)
    for i in range(0,len(A)):
        if A[i]=="A":
            A[i]="U"
        elif A[i]=="C":
            A[i]="G"
        elif A[i]=="G":
            A[i]="C"
        elif A[i]=="U":
            A[i]="A"
    return("".join(A))

def prottrans1(Dna,pattern):
    start=len(Dna)
    length=len(pattern)
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
            start=0
            coding=1
            break
    seq=[]
    for i in range(start,len(Dna)-3):
        A=""
        B=""
        seq1=""
        seq2=""
        j=i
        while j < i+3*(length):
            if j>len(Dna)-3:
                break
            else:
                A=A+translate[Dna[j:j+3]]
                seq1=seq1+Dna[j:j+3]
                Rna=Dna[j:j+3]
                Rna=reversecom(Rna)
                B=B+translate[Rna[::-1]]
                seq2=seq2+Dna[j:j+3]
                j=j+3
        if A==pattern:
            seq.append(seq1)
        if B[::-1]==pattern:
            seq.append(seq2)
    return seq
D=""
pattern="VKLFPWFNQY"
sequences=prottrans1(transcribe(D),pattern)
for i in range (0,len(sequences)): 
     sequences[i]=sequences[i].replace("U", "T")
print("\n".join(sequences))
