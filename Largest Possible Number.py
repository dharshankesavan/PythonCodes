# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 23:55:40 2019

@author: DHARSHAN
"""

X = input("Please enter the number: ")
K = input("Please enter count: ")
count = 0
for c in map(int, X):
    if (c < 9):
        count = count + 1
        X = X.replace(str(c),"9",1)
    if count == int(K):
        break;

print (X)