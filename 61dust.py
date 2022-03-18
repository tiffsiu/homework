#!/usr/bin/env python3
# 61dust.py
# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library
import argparse
import mcb185
import sys

parser = argparse.ArgumentParser(description='Finds and Masks low entropy seq')
# required arguments
parser.add_argument('--seqfile', required=True, type=str,
	metavar='<str>', help='input fastafile')
parser.add_argument('--winsize', required=True, type=int,
	metavar='<int>', help='window size for entropy calculation')
parser.add_argument('--entropy', required=True, type=float,
	metavar='<float>', help='threshold for entropy')

# switches
parser.add_argument('--lowercase', action='store_true',
	help='turn on lowercase masking')
arg = parser.parse_args()

for name, seq in mcb185.read_fasta(arg.seqfile):
    #print(name, seq[:25], mcb185.entropycal(seq[:25]))
    #sys.exit()
    newseq = list(seq)
    #print(newseq[:25])
    #sys.exit()
    for i in range(len(seq)-arg.winsize+1):
        win = seq[i:i+arg.winsize]
        entropy = mcb185.entropycal(win)
        #print(entropy)
        #sys.exit()
        if entropy < arg.entropy:
            #print(i, win, entropy)
            #sys.exit()
            if arg.lowercase:
                #print(i, win.lower(), entropy)
                newseq[i:i+arg.winsize] = list(win.lower())
                #sys.exit()
            else:
                #print(i, 'N'*arg.winsize, entropy)
                newseq[i:i+arg.winsize] = ['N']*arg.winsize
                #sys.exit()
    print(f'>{name}')
    print(''.join(newseq))
