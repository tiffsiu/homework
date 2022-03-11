#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix

#create KD library using the hydrophobicity link


protein = [] #create empty list

with open(sys.argv[1]) as fp: #open at prots file
    seq = '' #create empty seq
    name = ''
    for line in fp.readlines(): #for each line in at prots file
        line = line.rstrip()
        #print(line)
        if len(line) == 0: continue
        if line[0] == '>':
            protein.append((name,seq))
            name = line[1:].split('|')[0]
            seq = ''
        else: 
            seq += line
#print(protein[:3])            
protein = protein[1:]
protein.append((name, seq))
#print(protein[:3])

#sys.exit()

def kd(protein): #create KD library
    hydrophobicity = 0
    #print(protein, len(protein))
    for aa in protein:
        if aa == "I": hydrophobicity += 4.5
        elif aa == "V": hydrophobicity += 4.2
        elif aa == "L": hydrophobicity += 3.8
        elif aa == "F": hydrophobicity += 2.8
        elif aa == "C": hydrophobicity += 2.5
        elif aa == "M": hydrophobicity += 1.9
        elif aa == "A": hydrophobicity += 1.8
        elif aa == "G": hydrophobicity += -0.4
        elif aa == "T": hydrophobicity += -0.7
        elif aa == "S": hydrophobicity += -0.8
        elif aa == "W": hydrophobicity += -0.9
        elif aa == "Y": hydrophobicity += -1.3
        elif aa == "P": hydrophobicity += -1.6
        elif aa == "H": hydrophobicity += -3.2
        elif aa == "E": hydrophobicity += -3.5
        elif aa == "Q": hydrophobicity += -3.5
        elif aa == "D": hydrophobicity += -3.5
        elif aa == "N": hydrophobicity += -3.5
        elif aa == "K": hydrophobicity += -3.9
        elif aa == "R": hydrophobicity += -4.5
        else: return 0
    return hydrophobicity/len(protein)

def kd_scoring(window, threshold, protein):
    for i in range(len(protein)-window+1):
        kmer = protein[i:i+window]
        score = kd(kmer)
        #print(kmer, score)
        if score > threshold: return True
    return False

for id, seq in protein:
    if kd_scoring(8, 2.5, seq[:30]) and kd_scoring(11, 2.0, seq[30:-1]):
        print(id)
    #else: 
        #print(id, kd_scoring(8, 2.5, seq[:30]), kd_scoring(11, 2.0, seq[30:-1]))

#if kd_scoring(8, 2.5, seq[:30]):

#if kd_scoring(11, 2.0, seq[30:]):


"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
