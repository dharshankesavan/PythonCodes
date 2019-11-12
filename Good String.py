# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:53:32 2019

@author: DHARSHAN
"""

def CreateWord (MainString):
    possibleWords = []
    for i in range(len(MainString)):
        for j in range(i+1,len(MainString)):
            possibleWords.append(MainString[i:j+1])
    return (possibleWords);

def CheckRepeat (CheckString):
    count = 0
    for x in range(0, len(CheckString)):
        for y in range(x+1, len(CheckString)):
            if CheckString[x] == CheckString[y]:
                count = count + 1
    return count;
                
    

MainString = "abcdeefghij"
WordsList = CreateWord(MainString)
maxValue = 0
GoodString = ""
for eachWord in WordsList:
    if (CheckRepeat(eachWord) == 0):
        if (len (eachWord) > maxValue):
            maxValue = len(eachWord)
            GoodString = eachWord
print ("Good String is:-%s and it's length is:-%s" %(GoodString,maxValue));
        
        
