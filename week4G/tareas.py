
We say that a DNA string Pattern encodes an amino acid string Peptide if the RNA string transcribed from either Pattern or its reverse complement Pattern translates into Peptide. For example, the DNA string GAAACT is transcribed into GAAACU and translated into ET. The reverse complement of this DNA string, AGTTTC, is transcribed into AGUUUC and translated into SF. Thus, GAAACT encodes both ET and SF.

Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.

    Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
    Output: All substrings of Text encoding Peptide (if any such substrings exist).

Code Challenge: Solve the Peptide Encoding Problem. Click here for the RNA codon table corresponding to the array GeneticCode.

Note: The solution may contain repeated strings if the same string occurs more than once as a substring of Text and encodes Peptide.

Extra Dataset

Sample Input:

ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
MA

Sample Output:

ATGGCC
GGCCAT
ATGGCC

##########
The Cyclopeptide Sequencing Problem

For now, we will assume for simplicity that the mass spectrometer breaks the copies of a cyclic peptide at every possible two bonds, so that the resulting experimental spectrum contains the masses of all possible linear fragments of the peptide, which are called subpeptides. For example, the cyclic peptide NQEL has 12 subpeptides: N, Q, E, L, NQ, QE, EL, LN, NQE, QEL, ELN, and LNQ. We will also assume that subpeptides may occur more than once if an amino acid occurs multiple times in the peptide (e.g., ELEL also has 12 subpeptides: E, L, E, L, EL, LE, EL, LE, ELE, LEL, ELE, and LEL.

Exercise Break: How many subpeptides does a cyclic peptide of length n have?

Sample Input:

31315

Sample Output:

980597910

######

The theoretical spectrum of a cyclic peptide Peptide, denoted Cyclospectrum(Peptide), is the collection of all of the masses of its subpeptides, in addition to the mass 0 and the mass of the entire peptide, with masses ordered from smallest to largest. We will assume that the theoretical spectrum can contain duplicate elements, as is the case for NQEL (shown below), where NQ and EL have the same mass.

Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.

    Input: An amino acid string Peptide.
    Output: Cyclospectrum(Peptide).

Code Challenge: Solve the Generating Theoretical Spectrum Problem.

Extra Dataset

Note: An obvious approach for solving the Generating Theoretical Spectrum Problem would be to construct a list containing all subpeptides of Peptide, and then find the mass of each subpeptide by adding the integer masses of its constituent amino acids. This approach will work, but you may like to check out Charging Station: Generating the Theoretical Spectrum of a Peptide to see a more elegant algorithm that applies to both linear and cyclic peptides.

Sample Input:

LEQN

Sample Output:

0 113 114 128 129 227 242 242 257 355 356 370 371 484

########
Counting Peptides with Given Mass Problem: Compute the number of peptides of given mass.

    Input: An integer m.
    Output: The number of linear peptides having integer mass m.

Exercise Break (Optional): Solve the Counting Peptides with Given Mass Problem. The integer mass table is reproduced below; recall that we assume that peptides are formed from only 18 amino acid masses. That is, I/L are considered the same and K/Q are considered the same, so we would count AIKD and ALQD as just one peptide, not two.

[Image: http://bioinformaticsalgorithms.com/images/Antibiotics/integer_mass_table.png]

Suggestion: This exercise is optional because you may have difficulty solving this problem; if so, please return to it after learning more about dynamic programming algorithms in a future lesson.

Extra Dataset

Sample Input:

1024

Sample Output:

14712706211
#######
More generally, brute force algorithms that enumerate all candidate solutions but discard large subsets of hopeless candidates by using various consistency conditions are known as branch-and-bound algorithms. Each such algorithm consists of a branching step to increase the number of candidate solutions, followed by a bounding step to remove hopeless candidates. In our branch-and-bound algorithm for the Cyclopeptide Sequencing Problem, the branching step will extend each candidate peptide of length k into 18 peptides of length k + 1, and the bounding step will remove inconsistent peptides from consideration.

Note that the spectrum of a linear peptide does not contain as many masses as the spectrum of a cyclic peptide with the same amino acid sequence. For instance, the theoretical spectrum of the cyclic peptide NQEL contains 14 masses (corresponding to "", N, Q, E, L, LN, NQ, QE, EL, ELN, LNQ, NQE, QEL, and NQEL). However, the theoretical spectrum of the linear peptide NQEL, shown below, does not contain masses corresponding to LN, LNQ, or ELN, since these subpeptides “wrap around” the end of the linear peptide.

Exercise Break: How many subpeptides does a linear peptide of given length n have? (Include the empty peptide and the entire peptide.)

    Input: An integer n.
    Output: The number of subpeptides of a linear peptide of length n.

Sample Input:

4

Sample Output:

11

#########
Code Challenge: Implement CyclopeptideSequencing (pseudocode reproduced below).

Note: After the failure of the first brute-force algorithm we considered, you may be hesitant to implement CyclopeptideSequencing for fear that its runtime will be prohibitive. The potential problem with CyclopeptideSequencing is that it may generate incorrect k-mers at intermediate stages (i.e., k-mers that are not subpeptides of a correct solution). In practice, however, this is not a concern. See Charging Station: How fast is CyclopeptideSequencing?

    CyclopeptideSequencing(Spectrum)
        CandidatePeptides ← a set containing only the empty peptide
        FinalPeptides ← empty list of strings
        while CandidatePeptides is nonempty
            CandidatePeptides ← Expand(CandidatePeptides)
            for each peptide Peptide in CandidatePeptides
                if Mass(Peptide) = ParentMass(Spectrum)
                    if Cyclospectrum(Peptide) = Spectrum and Peptide is not in ﻿FinalPeptides
                        append Peptide to FinalPeptides
                    remove Peptide from CandidatePeptides
                else if Peptide is not consistent with Spectrum
                    remove Peptide from CandidatePeptides
        return FinalPeptides

Extra Dataset

Sample Input:

0 113 128 186 241 299 314 427

Sample Output:

186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186

#######

The following pseudocode assumes that we have a string or list of symbols Alphabet containing the 20 symbols of the amino acid alphabet, and a dictionary AminoAcidMass whose keys are the symbols of ﻿Alphabet and whose values are the the integer masses of each symbol.

LinearSpectrum(Peptide, Alphabet, AminoAcidMass)
    PrefixMass(0) ← 0
    for i ← 1 to |Peptide|
        for every symbol s in Alphabet
            if s = i-th amino acid in Peptide
                PrefixMass(i) ← PrefixMass(i − 1) + AminoAcidMass[s]
    LinearSpectrum ← a list consisting of the single integer 0
    for i ← 0 to |Peptide| − 1
        for j ← i + 1 to |Peptide|
            add PrefixMass(j) − PrefixMass(i) to LinearSpectrum
    return sorted list LinearSpectrum

Code Challenge: Implement LinearSpectrum.

    Input: An amino acid string Peptide.
    Output: The linear spectrum of Peptide.

Extra Dataset

Sample Input:

NQEL

Sample Output:

0 113 114 128 129 242 242 257 370 371 484

######
Let me show you an insanely easy approach [Prerquisites - Implement LinearSpectrum(Peptide)]:

    Let's suppose the given peptide is ABCD
    It's Circular_Spectrum will consist of mass of these substrings - [0, A, B, C, D, AB, BC, CD, DA, ABC, BCD, CDA, DAB, ABCD]. This is essentially what we need to calculate.

Do this to calculate Circular_Spectrum(Peptide).

    Calculate Linear Spectrum for the Prefix of Peptide i.e. ABC which returns the mass of these substrings [0, A, B, C, AB, BC, ABC]
    Find the Total_Mass of original peptide i.e. ABCD. You can use LinearSpectrum(Peptide) and return the last element of the spectrum which is equal to Total_Mass. 
    Now, for each element of LinearSpectrum of ABC, calculate the difference between mass of ABCD (Total_Mass) and each element. This results in mass of these substrings [ABCD , BCD , CDA, DAB, CD, DA, D].
    Combine both the PrefixSpectrum and the difference one. Sort it. What you get is  [0, A, B, C, D, AB, BC, CD, DA, ABC, BCD, CDA, DAB, ABCD] which is what you require.

Cheers !

Thanks to @Zhixia_Liu for this awesome approach.