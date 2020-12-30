def LinearSpectrum(Peptide, Aminoacid, AminoAcidMass):
    PrefixMass=[0]*(len(Peptide))
    for i  in range(0,len(Peptide)):
        for j in range(0,18):
            if Aminoacid[j] == Peptide[i]:
                PrefixMass[i]=PrefixMass[i-1] + AminoAcidMass[Aminoacid[j]]
    null=[0]
    null.extend(PrefixMass)
    PrefixMass=null
    LinearSpectrum = [0]
    for i in range(0,len(PrefixMass)-1): 
        for j in range(i + 1, len(PrefixMass)):
            LinearSpectrum.append(PrefixMass[j]-PrefixMass[i])
    LinearSpectrum.sort()
    return LinearSpectrum
Aminoacid = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'I', 'N', 'D', 'K', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
aminoAcidMass = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'E': 129,
    'M': 131,
    'H': 137,
    'F': 147,
    'R': 156,
    'Y': 163,
    'W': 186
}

def cyclopeptide(peptide):
    A=LinearSpectrum(peptide[1:],Aminoacid,aminoAcidMass)
    peptidemass=(LinearSpectrum(peptide,Aminoacid,aminoAcidMass)[-1])
    diffspec=[]
    for i in A:
        diffspec.append(peptidemass-i)
    A.extend(diffspec)
    A.sort()
    return(A)

def expand(candidatePeptides,Spectrum,aminoAcidMass,Aminoacid):
    canpep=[]
    Bnew=[]
    for i in Spectrum:
        Bnew.append(int(i)) 
    for i in candidatePeptides:
        for j in Aminoacid:
            if aminoAcidMass[j] in Bnew:
                canpep.append(i+j)
    return canpep

def Mass(peptide):
    listed=[]
    for i in peptide:
        listed.append(aminoAcidMass[i])
    return sum(listed)

def consistent(peptide,Spectrum):
    spec=LinearSpectrum(peptide,Aminoacid,aminoAcidMass)
    Bnew=[]
    for i in Spectrum:
        Bnew.append(int(i)) 
    spectrum=set(spec)
    for l in spectrum:
        if spec.count(int(l)) <= Bnew.count(int(l)):
            pass
        else:
            return False
    return True

def singlepep(Spectrum):
    peptides=[]
    for i in aminoAcidMass:
        if Spectrum.count(str(aminoAcidMass[i]))>0:
            peptides.append(i)
    return peptides

def equal(A,B):
    Bnew=[]
    for i in B:
        Bnew.append(int(i)) 
    A1=set(A)
    Bnew1=set(Bnew)
    if A1==Bnew1:
        return True
    else:
        return False

import math
def CyclopeptideSequencing(Spectrum):
    Spectrum=Spectrum.split(' ')
    CandidatePeptides=singlepep(Spectrum)
    FinalPeptides = []
    n=0
    while n < ((1+math.sqrt(1+4*(len(Spectrum)*(len(Spectrum)-1)-2)))/2)-1:
        CandidatePeptides = expand(CandidatePeptides,Spectrum,aminoAcidMass,Aminoacid)
        temppep=CandidatePeptides[:]
        for i in temppep: 
            if int(Mass(i)) == int(Spectrum[-1]):
                if equal(cyclopeptide(i),Spectrum) :
                    if i in FinalPeptides:
                        pass
                    else:                     
                        FinalPeptides.append(i)
                CandidatePeptides.remove(i) 
            else: 
                peptide=i
                if  consistent(peptide,Spectrum)==True:
                    pass
                else:
                    CandidatePeptides.remove(peptide)
        n=n+1
    Ultpep=[]
    for i in FinalPeptides:
        Finalepeptides=[]
        for j in i:
            Finalepeptides.append(str(aminoAcidMass[j]))
        Ultpep.append('-'.join(Finalepeptides))          
    return Ultpep 
n='0 71 97 99 103 113 113 114 115 131 137 196 200 202 208 214 226 227 228 240 245 299 311 311 316 327 337 339 340 341 358 408 414 424 429 436 440 442 453 455 471 507 527 537 539 542 551 554 556 566 586 622 638 640 651 653 657 664 669 679 685 735 752 753 754 756 766 777 782 782 794 848 853 865 866 867 879 885 891 893 897 956 962 978 979 980 980 990 994 996 1022 1093'
n=n.split(' ')

