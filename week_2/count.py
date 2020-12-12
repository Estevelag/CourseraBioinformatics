
def skew(Genome):
    count=0
    skewi=[0]
    for i in range(0,len(Genome)):
        if "C" == Genome[i]:
            count=count -1
        elif "G" == Genome[i]:
            count=count +1
        skewi.append(count)
    return skewi

def mins(Genome):
    skewi=skew(Genome)
    mini=[]
    for i in range(1,len(skewi)-1):
        if skewi[i]<skewi[i-1] and skewi[i]<skewi[i+1]:
            mini.append(i)
    return mini

def minimum(Genome):
    skewi=skew(Genome)
    mini=min(skewi)
    minim=[]
    for i in range(0,len(skewi)):
        if skewi[i]==mini:
            minim.append(i)
    return minim

import math

# Profile is provided on slide #4 in 1.3 Scoring Motifs

profile = {
        'A': [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
        'C': [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
        'G': [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
        'T': [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
}

# 1. Take each number in dictionary and calculate Pn * Log2(Pn)
# 2. Add all the numbers from step 1

total_enthropy = 0.0
for key, values in profile.items():
    for value in values:
        if value > 0:
            total_enthropy += abs(value * math.log(value, 2))
        else:
            continue
print(total_enthropy)
