#! /usr/bin/env python3

# This script is used to calculate DNA bases composition

# %%
# set the name of input DNA sequence file
filename = 'dna.txt'


# %%
# open the input file, assign to file handle called 'infile'
infile = open(filename, 'r')

#print(infile)


# %%
#read the file
dna_sequence = infile.read()
dna_sequence = dna_sequence.rstrip()


# %%
# print the dna sequence
print(dna_sequence)


# %%
# close the file
infile.close()


# %%
print(dna_sequence)


# %%
seqlen = len(dna_sequence)


# %%
print("Length of DNA sequence", seqlen)


# %%
print(dna_sequence.count('A'))
numA = dna_sequence.count('A')


# %%
print("The number of A's in", filename + ":", numA)


# %%
frequencyofA = numA / seqlen
print("The frequency of A's in", filename + ":", frequencyofA )


# %%
print(dna_sequence.count('C'))
numC = dna_sequence.count('C')


# %%
frequencyofC = numC / seqlen
print("The frequency of C's in", filename + ":", frequencyofC)


# %%
print(dna_sequence.count('G'))
numG = dna_sequence.count('G')


# %%
frequencyofG = numG / seqlen
print("The frequency of G's in", filename + ":", frequencyofG)


# %%
print(dna_sequence.count('T'))
numT = dna_sequence.count('T')


# %%
frequencyofT = numT / seqlen
print("The frequency of T in", filename + ":", frequencyofT)


# %%
GC = (numG + numC) /seqlen 
print(GC)


# %%
frequencytotal = frequencyofA + frequencyofC + frequencyofG + frequencyofT
print(frequencytotal)


# %%
outfile = open('nucleotide_composition.py', 'w')


# %%
outfile.write('DNA sequence:' + dna_sequence + '\n')
outfile.write('Sequence length:' + str(seqlen) + 'nt' + '\n')
outfile.write("Number of A's:" + str(numA) + '\n')
outfile.write("Frequency of A's:" + str(frequencyofA) + '\n')
outfile.write("Number of C's:" + str(numC) + '\n')
outfile.write("Frequency of C's:" + str(frequencyofC) + '\n')
outfile.write("Number of G's:" + str(numG) + '\n')
outfile.write("Frequency of G's:" + str(frequencyofG) + '\n')
outfile.write("Number of T's:" + str(numT) + '\n')
outfile.write("Frequency of T's:" + str(frequencyofT) + '\n')
outfile.write("G+C content:" + str(GC) + '\n')
outfile.write("Frequency Total:" + str(frequencytotal) + '\n')


# %%
outfile.close()


