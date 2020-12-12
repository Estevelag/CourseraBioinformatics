
def Stringcomp(DNA):
    DNA=DNA.split("\n")
    suffix={}
    for i in range (0,len(DNA)-1):
        suffix[i]=(equal(DNA[i],DNA))
    for x, y in suffix.items():
        if len(y)>0:
            print(x, y) 
    

def equal(pattern,DNA):
    diction=[]
    DNA.remove(pattern)
    k=len(DNA[1])
    for i in DNA:
        if pattern[1:k]==i[0:k-1]:
            diction.append(i)
    return diction



Stringcomp('''AAAT
AATG
ACCC
ACGC
ATAC
ATCA
ATGC
CAAA
CACC
CATA
CATC
CCAG
CCCA
CGCT
CTCA
GCAT
GCTC
TACG
TCAC
TCAT
TGCA''')

