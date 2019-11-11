# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:37:28 2019

@author: DHARSHAN
"""
def stringCase(string_list):
    #Write your implementation here
    modified_String = ""
    for temp_String in string_list:
        res = len(temp_String.split())
        if (res == 1):
            temp_String = temp_String.upper()
            print(temp_String);
        if (res == 2):
            print(temp_String.capitalize());
        if (res > 2):
            for i in range(len(temp_String)):
                if(temp_String[i] >= 'a' and temp_String[i] <= 'z'): 
                    modified_String = modified_String + chr((ord(temp_String[i]) - 32))
                elif(temp_String[i] >= 'A' and temp_String[i] <= 'Z'):
                    modified_String = modified_String + chr((ord(temp_String[i]) + 32))
                else:
                    modified_String = modified_String + temp_String[i]
            print (modified_String);
    
list_temp_Strings = ["Hello","My name is","adam smith"]
stringCase(list_temp_Strings)