# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:31:24 2019

@author: DHARSHAN
"""

# Read the variable from STDIN
a = int(input())

# Output the variable to STDOUT
list_a = []
i = 0
while (i < a):
    list_a.append(input())
    i = i + 1
for eachString in list_a:
    count = len(eachString)
    if (count > a):
        print (eachString);
