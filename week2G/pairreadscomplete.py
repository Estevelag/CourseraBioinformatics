def Pairedcomp(k,d,Dna):
    preads=[]
    for i in range(0,len(Dna)-k-d-k):
        preads.append(Dna[i:i+k]+ '|' + Dna[i+k+d:i+k+d+k])
    preads.sort()
    return preads

def presuf(A):
    A=A.split("\n")
    kmers = A
    nodes=[]
    for i in range(0,len(A)):
        nodes.append(A[i].split('|')[0][:-1] + '|' + A[i].split('|')[1][:-1])
    nodes=list(set(nodes))
    nodes.sort()
    adjlist={}
    for i in nodes:
        List=[]
        for j in kmers:
            if i == (j.split('|')[0][:-1] + '|' + j.split('|')[1][:-1]):#[suffix==preffis]
                List.append(j.split('|')[0][1:]+ '|' + j.split('|')[1][1:])
        adjlist[i]=List
    return adjlist            

def out(i,vertex):
    k=len(vertex[i])
    return k

def indeg(i,vertex):
    k=0
    for j in vertex:
        if len(vertex[j])>1:
           if i in vertex[j]:
               y=vertex[j].count(i)
               k=k+y
        else:
            if i in vertex[j]:
                k=k+1
    return k 

def outnum(vertex):
    k=[]
    for j in vertex:
        k.extend(vertex[j])
    return k



def separator(vertex):
    vertexup={}
    vertexdown={}
    for key in vertex.keys():
        if key.split('|')[1] in vertexdown.keys():
            if len(vertex[key])>1:
                m=vertexdown[key.split('|')[1]]
                m.append(vertex[key][0].split('|')[1],vertex[key][1].split('|')[1])
                vertexdown[key.split('|')[1]]=m
            else:
                m=vertexdown[key.split('|')[1]]
                m.append(vertex[key][0].split('|')[1])
                vertexdown[key.split('|')[1]]=m
        else:
            if len(vertex[key])>1:
                vertexdown[key.split('|')[1]]=[vertex[key][0].split('|')[1],vertex[key][1].split('|')[1]]
            else:
                vertexdown[key.split('|')[1]]=[vertex[key][0].split('|')[1]]
        if key.split('|')[0] in vertexup.keys():
            if len(vertex[key])>1:
                m=vertexup[key.split('|')[0]]
                m.append(vertex[key][0].split('|')[0],vertex[key][1].split('|')[0])
                vertexup[key.split('|')[0]]=m
            else:
                m=vertexup[key.split('|')[0]]
                m.append(vertex[key][0].split('|')[0])
                vertexup[key.split('|')[0]]=m
        else:
            if len(vertex[key])>1:
                vertexup[key.split('|')[0]]=[vertex[key][0].split('|')[0],vertex[key][1].split('|')[0]]
            else:
                vertexup[key.split('|')[0]]=[vertex[key][0].split('|')[0]]
    return vertexdown,vertexup




def eulerpath(Dna):
    import random
    vertex=Dna
    location=None
    circuit=[]
    Stack=[]
    nums=[]
    ending=None
    s=0
    for i in vertex:
        if out(i,vertex) - indeg(i,vertex) == 1:
            location=i
        nums.append(i)
    if len(list(set(outnum(vertex))-set(nums))) == 1:
        ending =  list(set(outnum(vertex))-set(nums))[0]
    else: 
        for i in vertex:
            if  indeg(i,vertex) - out(i,vertex) == 1:
                ending=i
    if ending==None:
        location=random.choice(list(vertex.keys()))
        s=1
    else:
        if ending in vertex.keys():
            h=vertex[ending]
            h.append(location)
            vertex[ending]=h
        else:
            vertex[ending]=[location]
    while any(vertex.values())== True:
        if location in vertex.keys():#bool(vertex[location]) == True: 
            Stack.append(location)
            l=location   
            location=random.choice(list(vertex[location]))
            if len(vertex[l])>1:
                m=vertex[l]
                m.remove(location)
                vertex[l]=m
            else:
                vertex.pop(l) 
        else:
            circuit.append(location)
            location=Stack[-1]
            Stack.pop()
            # if len(Stack)>0:
            #     location=Stack[-1]
            #     Stack.pop()
    circuit=circuit+[location]+Stack[::-1]
    A=circuit[::-1]   
    return A,ending,s



#A=Pairedcomp(3,1,'''TAATGCCATGGGATGTT''')
k=3
d=1
D='''ACC|ATA
ACT|ATT
ATA|TGA
ATT|TGA
CAC|GAT
CCG|TAC
CGA|ACT
CTG|AGC
CTG|TTC
GAA|CTT
GAT|CTG
GAT|CTG
TAC|GAT
TCT|AAG
TGA|GCT
TGA|TCT
TTC|GAA'''
A=presuf(D)
h=1
while h==1:
    h=0
    A=presuf(D)
    A,ending,s=eulerpath(A)
    for t in range(0,len(A)-d-k-1):
        if A[t].split('|')[1]!= A[t+d+k].split('|')[0]:
            h=1
B=[A[0].split('|')[0]]
for i in range (1,len(A)-1):
    B.append(A[i].split('|')[0][k-2])
for i in range (len(A)-d-k-1,len(A)-1): 
    B.append(A[i].split('|')[1][k-2])
print(''.join(B),s)

# vertexdown,vertexup=separator(A)
# Aup,endingup=eulerpath(vertexup)
# Bup=[]
# Adown,endingdown=eulerpath(vertexdown)
# Bdown=[]
# while endingup != Aup[len(Aup)-2]:
#     vertexdown,vertexup=separator(A)   
#     Aup,endingup=eulerpath(vertexup)
#     if endingup == None:
#         u=1
#         break
# Bup=[Aup[0]]
# for i in range (1,len(Aup)-1):
#     Bup.append(Aup[i][k-2])
# stringup=str(''.join(Bup))
# while endingdown != Adown[len(Adown)-2]:
#     vertexdown,vertexup=separator(A)   
#     Adown,endingdown=eulerpath(vertexdown)
#     if endingdown == None:
#         u=1
#         break
# Bdown=[Adown[0]]
# for i in range (1,len(Adown)-1):
#     Bdown.append(Adown[i][k-2])
# stringdown=str(''.join(Bdown))
# for i in range(k + d + 1,len(stringup)):
#     if stringup[i]!= stringdown[i-k-d]:
#         print("there is no string spelled by the gapped patterns")
# print(stringup+stringdown)
# print(stringup+stringdown[-k-d:])