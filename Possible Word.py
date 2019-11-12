# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 22:27:11 2019

@author: DHARSHAN
"""

MainString = "edurekaedurekaas"
SmallString ="edureka"
subStrLen = len(SmallString)
count = 0
for i in range(len(MainString)):
    for j in range(i+1,len(MainString)):
        subMainString = MainString[i:j+1]        
        if (subMainString == SmallString):
            count = count +1
print (count);
    