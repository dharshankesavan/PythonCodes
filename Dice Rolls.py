# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:25:25 2019

@author: DHARSHAN
"""
DiceNumber = "3662123"
#DiceNumber = "15616"
count = 0
for number in range(len(DiceNumber)):
    if (DiceNumber[number] == "6"):
        if (number + 1 == len(DiceNumber)):
            count = -1
            break;
        if (DiceNumber[number +1] == None):
            count = -1
            break;
    else:
        count = count + 1
print (count);        