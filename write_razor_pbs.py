#! /usr/bin/env python3

# This script generates a PBS file for the AHPCC razor cluster

# define some variables
Name = 'slmosque.$PBS_JOBID'
queue = 'tiny16core'
N = 1
P = 1

wall = 3 # this is in hours

# This section prints the header/required info for the PBS script
print('#PBS -N', Name) # job name
print('#PBS -q', queue) # which queue to use
print('#PBS -j oe') # join the STDOUT and STDERR into a single file
print('#PBS -o', Name) # set the name of the job output file
print('#PBS -l nodes=' + str(N) + ':' + 'ppn=' + str(P)) # how many resources to ask for (nodes = num nodes, ppn = num processors)
print('#PBS -l walltime=' + str(wall) + ':00:00') # set the walltime (default to 1 hr)
print()

# cd into working directory
print('cd $PBS_O_WORKDIR')
print()

# load the necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1')
print()

# commands for this job
print('# insert commands here')

