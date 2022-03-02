#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

numbers = [] 
for item in sys.argv[1:]:
    numbers.append(float(item))
    
print(numbers)
H = 0

H += numbers[0] * math.log2(numbers[0])
H += numbers[1] * math.log2(numbers[1])
H += numbers[2] * math.log2(numbers[2])
H += numbers[3] * math.log2(numbers[3])
print(-H)

H = 0
for i in range(len(numbers)):
    H += numbers[i] * math.log2(numbers[i])
print(H)

H = 0
for p in numbers:
    H += p * math.log2(p)
print(-H)

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
