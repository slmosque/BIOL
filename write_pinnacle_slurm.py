#! /usr/bin/env python3

#!/bin/bash

# This script generates a PBS file for the AHPCC pinnacle cluster

# define some variables
Name = 'slmosque.$SLURM_JOBID'
queue = 'partition comp06'
N = 1
P = 1
wall = 3 # this is in hours

print('#SBATCH -J', Name)
print('#SBATCH --', queue)
print('#SBATCH -o Trinity_%j.txt')
print('#SBATCH -e Trinity_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=slmosque@uark.edu')  
print('#SBATCH --nodes=' + str(N))
print('#SBATCH --ntasks-per-node=' + str(P))
print('#SBATCH --time=' + str(wall) + ':00:00')
print()

print('export', Name)
print()
 
print('# load required modules')
print('module load samtools')
print('module load jellyfish')
print('module load bowtie2')
print('module load salmon/0.8.2')
print('module load java')
print()
 
# cd into the directory where you're submitting this script from
print('cd $SLURM_SUBMIT_DIR')
print()

# copy files from storage to scratch
print('rsync -av RNA-R*.fastq.gz /scratch/$SLURM_JOB_ID')
print()

# cd onto the scratch disk to run the job
print('cd /scratch/$SLURM_JOB_ID/')
print()

# run the Trinity assembly
print('/share/apps/bioinformatics/trinity/trinityrnaseq-v2.11.0/Trinity --seqType fq --left RNA-R1.fastq.gz --right RNA-R2.fastq.gz --CPU 48 --max_memory 250G --trimmomatic --no_normalize_reads --full_cleanup --output trinity_Run2 ')
print()

# copy output files back to storage
print('rsync -av trinity_Run2 $SLURM_SUBMIT_DIR')