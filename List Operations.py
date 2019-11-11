# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:06:37 2019

@author: DHARSHAN
"""

def add_list(list_a, list_b):
    # Write your implementation here
    return (list_a + list_b)


def sub_list(list_a, list_b):
    # Write your implementation here
    return list(set(list_a) - set(list_b))


def max_list(list_a):
    # Write your implementation here
    maxNum = 0
    for i in list_a:
        if (i > maxNum):
            maxNum = i
    return maxNum


def sort_list(list_a):
    # Write your implementation here
    print(sorted(list_a, reverse=False));
            
        

list_a = [4, 3, 2]
list_b = [3, 5, 6]

print(add_list(list_a, list_b));
print(sub_list(list_a, list_b));
print(max_list(list_a));
print(sort_list(list_a));