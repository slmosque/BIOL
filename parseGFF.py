# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO


# this script will parse a GFF file and extract each feature from the genome, repeated in parser object
# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object

parser = argparse.ArgumentParser(description='this script will parse a GFF file and extract each feature from the genome')

# add positional arguments (required, two req gff and fasta file, their order matters)
parser.add_argument("gff", help='name of the gff file')
parser.add_argument("fasta", help='name of the fasta file')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta, 'fasta')
#print(genome.seq)
#print(len(genome.seq))
# http://biopython.org/DIST/docs/tutorial/Tutorial.html
# https://biopython.org/wiki/Seq

# open and read in GFF file
with open(args.gff, 'r') as gff_in:
   # for l in gff_in:
       # columns = l.split('\t')
       # print(columns[3], columns[4])

    # create a csv reader object, you can split in any delimiter, smart about spaces
    reader = csv.reader(gff_in, delimiter = '\t')
    # loop over all the lines in our reader object (i.e., parsed file)
    for line in reader:
        # extract the sequence
        #print(line)
        start  = (line[3]) 
        end    = (line[4]) 
        strand = line[6] 
        #print(start)
        #print(len(genome.seq))
        
      
        
        
        
    



# %%
