def ComputingFrequencies1(A,B):
    FrequencyArray=[0]*(4**B)
    for i in range(0,len(A)-B+1):
        Pattern=A[i:i+B]
        j=Pattern2num(Pattern)
        FrequencyArray[j]=FrequencyArray[j]+1
    return (FrequencyArray)

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

A="CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
Text=Frequentpat=[]
B=5
D=50
Clump=[0]*(4**B)
Text=A[0:D+1]
FreqArray=ComputingFrequencies1(Text,B)
C=4
for j in range(0,4**B):
        if int(FreqArray[j])>=C:
            Clump[j]=1
i=1

FirstPattern=A[i-1:i+B-1]
print(FirstPattern)
index=Pattern2num(FirstPattern)
print(index)
FreqArray[index]=FreqArray[index]-1
LastPattern=A[i+D-B:i+D]
print(LastPattern)
index=Pattern2num(LastPattern)