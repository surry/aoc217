#! /usr/bin/python3

import fileinput
import sys

captcha = ''
for line in fileinput.input():
    captcha += line.strip()
    
sum = 0
i = 0

size = len(captcha)
while i < size:
    if captcha[i] == captcha[(i + size//2) % size]:

        sum += ord(captcha[i]) - ord('0')
    i += 1

print(sum)