#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

def get_args():
    parser = argparse.ArgumentParser(description='this script will parse a GFF file and extract each feature from the genome')

    # add positional arguments (required, two req gff and fasta file, their order matters)
    parser.add_argument("gff", help='name of the gff file')
    parser.add_argument("fasta", help='name of the fasta file')

    # parse the arguments
    args = parser.parse_args()
    return args
    
    genome = SeqIO.read(args.fasta, 'fasta')
    x1 = genome.id
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
            start  = int(line[3]) #start codon
            end    = int(line[4]) #stop codon
            strand = line[6] #strand
                        
            #print(start)
            #x2 = line [8]
            x3 = genome.seq[start:end+1]
            #if strand == "-":
                #rev_com = x3.reverse_complement()
                #print(x1, x2, x3, rev_com)

            def rev_com():
                    reverse = rev(arguments.gff)
                    if strand == "-":
                        x3.reverse_complement()
                        print(reverse)
                        
            arguments = get_args()    

            if __name__ == '__rev_com__':
                    rev_com()