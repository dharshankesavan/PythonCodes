# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 23:17:02 2019

@author: DHARSHAN
"""
def listPrime(N):
    #Write your implementation here
    listPrime = []
    if N > 0:
        for num in range(2, N): #Loop through all numbers from 2 to the given Numbers
            if num > 1:
                # Loop through from 2 to the current outer loop variable
                for i in range(2, num): 
                    if (num % i) == 0:
                        break
                else:
                    listPrime.append(num);
        return listPrime
    else:
        return "Invalid Parameter";
    
            
    
NoOfTimes = -1
print(listPrime(NoOfTimes));