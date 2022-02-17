#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

numbers = [] 
sum = 0
p = 0
for i in range(1, len(sys.argv[1:])):
    numbers.append(float(sys.argv[i]))
    sum += float(sys.argv[i])
for probability in numbers:
    p += float(sys.argv[i]) * -math.log2(float(sys.argv[i])) 
print(f'{p:.3f}')

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
