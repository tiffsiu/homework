#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

numbers = []
for thing in sys.argv[1:]:
    numbers.append(float(thing))
sum = 0
std = 0
print('Count:', len(numbers))
numbers.sort()
print(f'Minimum: {numbers[0]:.1f}')
print(f'Maximum: {numbers[-1]:.1f}')
for i in range(len(numbers)):
    sum += numbers[i]
for j in range(len(numbers)):
    std += math.sqrt((numbers[j]-sum/(len(numbers)))**2)
print(f'Mean: {sum/(len(numbers)):.3f}')
print(f'Std. dev: {std/len(numbers):.3f}')
#if odd than the median is the middle number in the list
#if even than the median is the average of the two middle numbers in the list
mid = len(numbers)//2
if len(numbers)%2 == 1: #odd
    median = numbers[mid]
else: #even
    median = (numbers[mid] + numbers[mid-1])/2
print(f'Median: {median}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
