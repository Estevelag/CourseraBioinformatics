def Vcholera(A,B):

    count=[]
    for i in range(0,len(A)-len(B)+1):
        if B == A[i:i+len(B)]:
            count.append(i)
    print(*count)

f = open("Vibrio_cholerae.txt", "r")
Vc=f.readline()
print(Vcholera(Vc,"CTTGATCAT"))
