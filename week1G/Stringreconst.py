def Stringrecons(DNA):
    DNA=DNA.split("\n")
    k=len(DNA[1])
    n=len(DNA)
    reads=DNA[:]
    Genome=[]
    for i in reads:
        DNA.remove(i)
        Genome.append(i)
        for j in DNA:
            if i[1:k]==j[0:k-1]:
                Genome.append(j)
                i=j
        if len(Genome)==n:
            news=Genome[0][0:k]
            for z in range(1,len(DNA)+1):
                news=news+Genome[z][k-1]
            return news
        else:
            Genome=[]
            DNA=reads[:]

def strgen(DNA):
    DNA=DNA.split("\n")
    k=len(DNA[1])
    news=DNA[0][0:k]
    for z in range(1,len(DNA)+1):
        news=news+DNA[z][k-1]
    return news

print(Stringrecons('''CTTA
ACCA
TACC
GGCT
GCTT
TTAC'''))

#f = open('data.txt','w')
#f.write(A)
#f.close()