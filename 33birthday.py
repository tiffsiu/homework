#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

people = 25
trial = 100
sharedbirthdays = 0
daysincalendar = 365
calendar = []
for i in range(daysincalendar): 
    calendar.append(0)
for i in range(trial):
    for j in range(people):
        ran = random.randint(0, daysincalendar-1)
    calendar[ran] += 1
for i in calendar:
    if i > 1:
        sharedbirthdays += 1
        break
print(f'{sharedbirthdays/trial:.3f}')
#print(calendar)
"""
python3 33birthday.py
0.571
"""