# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:48:39 2019

@author: DHARSHAN
"""
def calAvg(Name,Marks):
    #Write your implementation here
    file= open(r"C:\Users\DHARSHAN\.spyder-py3\Assigment Solutions\output.txt", "w")
    fName = open(Name, "r")
    fMarks = open(Marks, "r")
    list_Name = []
    list_Marks = []
    for strName in fName.readlines():
        list_Name.append(strName.rstrip('\n'))
    for strMark in fMarks.readlines():
        strMark = strMark.rstrip('\n');
        Marklist = strMark.split(",")
        for i in range(0, len(Marklist)): 
            Marklist[i] = int(Marklist[i]) 
        list_Marks.append(sum(Marklist) / len(Marklist))
    for i in range(len(list_Name)):
        file.write(list_Name[i])
        file.write(':'),
        file.write(str(list_Marks[i])),
        file.write('\n'),
    

      

Name = r"C:\Users\DHARSHAN\.spyder-py3\Assigment Solutions\Names.txt"
Marks = r"C:\Users\DHARSHAN\.spyder-py3\Assigment Solutions\Marks.txt"
calAvg(Name, Marks)