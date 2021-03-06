#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments


#isolate genome from data file
filename = sys.argv[1]
refrag = sys.argv[2]
genome = ''
with open(filename) as fp:
    for line in fp.readlines():
        line = line.rstrip() #make into continuous line
        if 'ORIGIN' in line: #genome starts after the word origin
            genome = ''
        else:
            line = line.split()[1:]
            genome += ''.join(line)
#look for all of the restriction patterns 'gaattc' in genome
before = 0
for match in re.finditer(refrag, genome):
    size = match.start() - before
    before = match.start()
    print(size)
"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
