#!/usr/bin/env python3
# 50kmers.py

import sys

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k


filename = sys.argv[1]
def readfasta(filename):
    protein = [] #create emppty list to put in seq
    seq = '' #create empty for seq
    name = '' #create empty for name
    with open(filename) as fp: #open file
        for line in fp.readlines():
            line = line.rstrip() #making it one continous line
            if line[0] == '>': #chr starts with >
                name = line[1:].split() #split name from seq, name is first line
                seq = ''
            else: 
                seq += line #seq is every other line than the first
        protein.append((name, seq))
    return protein
    
count = {} 
k = 2
all = 0
for name, seq in readfasta(filename):
    for aa in range(len(seq)-k+1):
        kmer = seq[aa:aa+k] #account for length of kmer
        if kmer not in count: count[kmer] = 0 #remove if not in range
        count[kmer] += 1
        all += 1 #add each kmer 
    #print(count)

for kmer in sorted(count.keys()):
    print(f'{kmer}  {count[kmer]:<8} {count[kmer]/all:.4f}')

"""
python3 50kmers.py ../Data/chr1.fa 2
AA	33657	0.1106
AC	15836	0.0520
AG	18244	0.0600
AT	27223	0.0895
CA	18965	0.0623
CC	10517	0.0346
CG	8147	0.0268
CT	18142	0.0596
GA	19994	0.0657
GC	9673	0.0318
GG	10948	0.0360
GT	16348	0.0537
TA	22344	0.0734
TC	19744	0.0649
TG	19624	0.0645
TT	34869	0.1146
"""
