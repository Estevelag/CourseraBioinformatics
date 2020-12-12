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



def ComputingFrequencies(A,B):
    FrequencyArray=[0]*(4**B)
    for i in range(0,len(A)-B+1):
        Pattern=A[i:i+B]
        j=Pattern2num(Pattern)
        FrequencyArray[j]=FrequencyArray[j]+1
    return (' '.join(map(str, FrequencyArray)))

def ComputingFrequencies1(A,B):
    FrequencyArray=[0]*(4**B)
    for i in range(0,len(A)-B+1):
        Pattern=A[i:i+B]
        j=Pattern2num(Pattern)
        FrequencyArray[j]=FrequencyArray[j]+1
    return (FrequencyArray)

def ClumpFind(A,B,C,D):#k,l,t
    Frequentpat=[]
    Clump=[0]*(4**B)
    for i in range(0,len(A)-C+1):
        Text=A[i:i+C]
        FreqArray=ComputingFrequencies1(Text,B)
        for j in range(0,4**B):
            if FreqArray[j]>=D:
                Clump[j]=1
    for i in range(0,4**B):
        if Clump[i]==1:
            Pattern=Num2Patt(i,B)  
            Frequentpat.append(Pattern) 
    return Frequentpat     

def Betterclump(A,B,C,D): #k,L,t  k,t,L is how its done here
    Frequentpat=set()
    Clump=[0]*(4**B)
    Text=A[0:D]
    FreqArray=ComputingFrequencies1(Text,B)
    for j in range(0,4**B):
        if int(FreqArray[j])>=C:
            Clump[j]=1
    for i in range(1,len(A)-D+1):
        FirstPattern=A[i-1:i+B-1]
        index=Pattern2num(FirstPattern)
        FreqArray[index]=FreqArray[index]-1
        LastPattern=A[i+D-B:i+D]
        index=Pattern2num(LastPattern)
        FreqArray[index]=FreqArray[index]+1
        if FreqArray[index]>=C:
            Clump[index]=1
    for i in range(0,4**B):
        if Clump[i]==1:
            Pattern=Num2Patt(i,B)
            Frequentpat.add(Pattern)        
    return (list(Frequentpat))    

#f = open("E_coli.txt", "r")
#Vc=f.readline()
#count=0
#for i in range(500,len(Vc),500):
    #if ClumpFind(Vc, 9, i, 3):
        #count=count+1
#print(count)
    
print(Betterclump("CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA", 5, 4, 50))
#print(Pattern2num("TCTGAGAGTTCGCAATG"))
#print(Num2Patt(5031,8))
#print(ComputingFrequencies1("CTCAAAAAGCTAGCGGCACTACAGCTGCTCGTGGGGAAGCTGTAAGAAGACCTGAAAGGGTCTACGAGTCAATCGAGAAACACTTCGAGTTCAATACGGGTTCGGTTCATCAAAACGGTGAAACAGCCTACGCCGCTATTCTGAAGTGCGACTGATTTCAATCATTATTTTCAAGTGATGGTAGAAGTCAGACGCCGCGCAGAGGGGTCTCGGTCTGCCAATAAGAGTTTGGTCATTTTAGTCCCAGCAAATCTCGATAACTCGTCTGCAATTAGTCCATCCAGGCATGAAACCCGGGCTCTGTAATCCCCGCAGTACGCACAAATGCAGTCACATGCGACCAAACCATAGTCGACTGAGAGCAACGGGCCAGTTAAGAGCTAAGGGCCACTGTAACCGCACTCACCGGACAAGCGATGTTGTCTGATTCCAGCTAACATCGTGCGCGTAAGCGCGGGCTTACGGCCCGCAGTGGGAGTAATCCTGCGTCTGGACCCGAATATGATCATCTTGCCATGATTATCCCTCGGGAGCCTGTATTGGGGGTCGAACTAATTCGTTCTGCCGACGCCGTAGAAGGATGTTCGTCCCGGCTTCGTCCGAGAGACTAAAGACAGAGATACATCTGAAGCGCGTTTTGGCACTTTAGTGGTCGAAGATCAATGACGG",5))
