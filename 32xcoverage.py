#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

genomesize = int(sys.argv[1]) #make sys.argv positions integers
readnumber = int(sys.argv[2])
readlength = int(sys.argv[3])
genome = [] #create empty list
for i in range(genomesize):
    genome.append(0) #make genome
for j in range(readnumber):
    ran = random.randint(0, genomesize - readlength) #random reads in genome (-readlength bc will go over genome size)
    #print(ran)
    for x in range(ran, ran + readlength): 
        #print(ran, x)
        genome[x] += 1 #count all read
#print(genome)
sum = 0
min = readnumber #don't use 0 because nothing will be less than 0
max = 0
for i, cov in enumerate(genome): #make list into vertical: index and coverage
    if i < readlength: continue #take out the first part of chromosome 
    if i > genomesize - readlength: continue #take out the last past of the chromosome
    if cov < min: min = cov
    if cov > max: max = cov
    sum += cov #sum of coverage
print(min, max, f'{sum/(genomesize-2*readlength):.5f}')

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
