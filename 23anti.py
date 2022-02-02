#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
blank = ''
for i in range(len(dna)): 
    if dna[i] == 'A': blank += 'T'
    elif dna[i] == 'T': blank += 'A'
    elif dna[i] == 'C': blank += 'G'
    else: blank += 'C'
print(blank[::-1])

#worked with Thomas

"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""