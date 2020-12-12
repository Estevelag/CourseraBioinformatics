
def Hammingdist(seq1,seq2):
    dist=0
    for i in range(0,len(seq1)):
        if seq1[i]!= seq2[i]:
            dist=dist+1
    return dist

#print(Hammingdist("CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA","CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"))
def Aproxxpatternmissmatch(Pattern,genome,d):
    pos=[]
    for i in range(0,len(genome)-len(Pattern)+1):
        di = Hammingdist(Pattern,genome[i:i+len(Pattern)])
        if di <= d:
            pos.append(i)
    return pos

def Aproxxpatterncount(Pattern,genome,d):
    count=0
    for i in range(0,len(genome)-len(Pattern)+1):
        Patt = genome[i:i+len(Pattern)]
        if Hammingdist(Pattern,Patt)<= d:
            count=count+1
    return count

#print(Aproxxpatterncount("CCC","CATGCCATTCGCATTGTCCCAGTGA",2))
#print(len(Aproxxpatternmissmatch("AAAAA","AACAAGCTGATAAACATTTAAAGAG",2)))

def Pattern2num(A):
    l=[None]*len(A)
    a=0
    for i in range(0,len(A)):
        if A[i]=="A":
            l[i]=0
        elif A[i]=="C":
            l[i]=1    
        elif A[i]=="G":
            l[i]=2  
        elif A[i]=="T":
            l[i]=3
    for i in range(0,len(l)):
        a=a+int(l[len(l)-i-1])*(4**i)          
    return(a)  

def Inmediateneighbours(Pattern):
    neighbour=set()
    for i in range(0,len(Pattern)):
        for x in "ACTG":
            neighbor=list(Pattern)
            neighbor[i]=x
            neighbour.add(''.join(map(str, neighbor)))
    neighbour.remove(Pattern)
    return list(neighbour)        

#print(Inmediateneighbours("ACG"))

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

print(len(neighboors("ACGT",3)))
#outF = open("myOutFile.txt", "w")
#for line in A:
#  outF.write(line)
#  outF.write("\n")
#outF.close()

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

def computingfreqmiss(Text,k,d):
    FrequencyArray=[0]*(4**k)
    for i in range(0,len(Text)-k+1):
        Pattern=Text[i:i+k]
        Neighboorhod=neighboors(Pattern,d)
        for i in Neighboorhod:
            j=Pattern2num(i)
            FrequencyArray[j]=FrequencyArray[j]+1
    maxim=max(FrequencyArray)
    Patterns=[]
    for i in range(0,len(FrequencyArray)):
        if FrequencyArray[i]==maxim:
            Patterns.append(Num2Patt(i,k))
    return Patterns

def reversecom(A):
    A=list(A)
    for i in range(0,len(A)):
        if A[i]=="A":
            A[i]="T"
        elif A[i]=="C":
            A[i]="G"
        elif A[i]=="G":
            A[i]="C"
        elif A[i]=="T":
            A[i]="A"
    return("".join(A[::-1]))

def computfreqmissrev(Text,k,d):
    FrequencyArray=[0]*(4**k)
    for i in range(0,len(Text)-k+1):
        Pattern=reversecom(Text[i:i+k])
        Neighboorhod=neighboors(Pattern,d)
        for i in Neighboorhod:
            j=Pattern2num(i)
            FrequencyArray[j]=FrequencyArray[j]+1
    for i in range(0,len(Text)-k+1):
        Pattern=Text[i:i+k]
        Neighboorhod=neighboors(Pattern,d)
        for i in Neighboorhod:
            j=Pattern2num(i)
            FrequencyArray[j]=FrequencyArray[j]+1
    maxim=max(FrequencyArray)
    Patterns=[]
    for i in range(0,len(FrequencyArray)):
        if FrequencyArray[i]==maxim:
            Patterns.append(Num2Patt(i,k))
    return Patterns

#print(*computfreqmissrev("CTCTCTCGCTTGTTGTTGGCACGCGCACGCCTCTTTGGCAGCATTGCGCTTGCGCCTCTGCCGCCTCGCGCCTCTCTCTTTGGCGCAGCATTGCGCCGCTTGCGCCTGCAGCACGCCTCTCTTTGGCACTGCACGCCTCGCGCGCCTTTGGCACTGCATTGCTGCTTGCGCTTGCTTTGTTGCGCGCGCGCGCAGCGCTTGGCTTGCGC",7,3))



#print(*computingfreqmiss("CGCTGTCCGCTTTACATACGCTGTCCCACATACGCTCATACGCTCATACCACCAGTCCATATTACGCTGTCGTCTTAGTCGTCCCACCATTACGCTCCACCACATACGCTCCATTACATACCACCACCACATATTACATACGCTTTATTACGCTCGCTCGCTCCAGTCCATACATACATACATACCACATACATAGTCCATACCATTACATATTACGCTCCACGCTCCAGTCGTCCGCTCCACCACCACCAGTCCATAGTCCCACCATTAGTCCATAGTCCCACCATTACATATTACGCTTTACCATTACATACATACCACGCTTTACATAGTCCATACATAGTCCCACGCT",7,3))
