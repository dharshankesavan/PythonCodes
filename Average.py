# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 21:23:33 2019

@author: DHARSHAN
"""

noOfElements = int(input())
i = 0
list_Elements = []
average = 0
while (i < noOfElements):
    list_Elements.append(int(input()))
    i = i + 1

average = sum(list_Elements) / len(list_Elements)
print (average);