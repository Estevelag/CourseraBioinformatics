def univstr(k):
    import itertools
    A=list(itertools.product('01', repeat=k))
    B=[]
    for i in A:
        B.append(''.join(i))
    C=str("\n".join(B))
    return C
    
def out(i,vertex):
    k=len(vertex[i])
    return k

def indeg(i,vertex):
    k=0
    for j in vertex:
        if isinstance(vertex[j],list):
           if i in vertex[j]:
               y=vertex[j].count(i)
               k=k+y
        else:
            if i in [vertex[j]]:
                k=k+1
    return k 
def outnum(vertex):
    k=[]
    for j in vertex:
        k.extend(vertex[j])
    return k
def eulerpath(Dna):
    import random
    vertex=Dna
    location=None
    circuit=[]
    Stack=[]
    location=random.choice(list(vertex.keys()))
    while any(vertex.values())== True:
        if bool(vertex[location]) == True: 
            Stack.append(location)
            l=location   
            location=random.choice(list(vertex[location]))
            if isinstance(vertex[l],list):
                m=vertex[l]
                m.remove(location)
                vertex[l]=m
            else:
                vertex.pop(l) 
        else:
            circuit.append(location)
            location=Stack[-1]
            Stack.pop()
    circuit=circuit+[location]+Stack[::-1]
    return circuit[::-1]    

def Stringrec3(Dna,k):
    Dna=Dna.split("\n")
    nodes =	[]
    kmers = []
    for i in range(0,len(Dna)):
        nodes.append(Dna[i][:k-1])
    for i in range(0,len(Dna)):
        kmers.append(Dna[i][:k])
    nodes=list(set(nodes))
    nodes.sort()
    adjlist={}
    for i in nodes:
        List=[]
        for j in kmers:
            if i==j[:len(j)-1]:
                List.append(j[1:])
        adjlist[i]=List
    return adjlist 


def assembly(k,Dna):
    dbg=Stringrec3(Dna,k)
    A=eulerpath(dbg)
    B=[A[0]]
    for i in range (1,len(A)-k+1):
        B.append(A[i][k-2])
    return ''.join(B)
print((assembly(8,univstr(8))))
