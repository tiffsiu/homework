#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

#print(sys.argv)
genomesize = int(sys.argv[1])
readnumber = int(sys.argv[2])
readlength = int(sys.argv[3])
list = []
for i in range(genomesize):
    list.append(0)
for j in range(readnumber):
    ran = random.randint(0, 999)
    for i in range(ran):
        list[i] += 1
list.sort()
print(f'{list[0]} {list[999]} {sum(list)/readlength:.5f}')
#print(sum(list))
"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
