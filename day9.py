#! /usr/bin/python3

import fileinput
import sys

stream = ''
for line in fileinput.input():
    stream += line.strip()

sum = 0
depth = 0
i = 0
garbage_count = 0
garbage = False

while i < len(stream):
    ch = stream[i]

    if garbage and ch == '!':
        i += 1
    elif ch == '>':
        garbage = False
    elif garbage:
        garbage_count += 1
    elif ch == '<':
        garbage = True
    elif ch == '{':
        depth += 1
    elif ch == '}':
        sum += depth
        depth -= 1
    
    i += 1
    
print(garbage_count)