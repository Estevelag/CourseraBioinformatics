def out(i,vertex):
    k=len(vertex[i])
    return k
import random
def indeg(i,vertex):
    k=0
    for j in vertex:
        if isinstance(vertex[j],list):
           if i in vertex[j]:
               k=k+1
        else:
            if i in [vertex[j]]:
                k=k+1
    return k 
def outnum(vertex):
    k=[]
    for j in vertex:
        k.extend(vertex[j])
    return k
vertex={'A': ['G', 'T', 'A', 'T'], 'G': ['A', 'G', 'T'], 'T': ['A', 'G', 'T']}
location=None
circuit=[]
Stack=[]
nums=[]
k=0
for j in vertex:
    if isinstance(vertex[j],list):
        if 'T' in vertex[j]:
            y=vertex[j].count('T')
            k=k+y
    else:
        if 'T' in [vertex[j]]:
            k=k+1
print(k)
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
if ending in vertex.keys():
    h=vertex[ending]
    h.extend(location)
    vertex[ending]=h
else:
    vertex[ending]=[location]
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
A=circuit[::-1]   
if ending==A[-2]:
    p=1
