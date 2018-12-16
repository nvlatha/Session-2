# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:10:32 2018

@author: Latha NV
"""
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:10:32 2018

@author: Latha NV
"""

# 1. Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.
getsequence = input ("Input numbers with comma separated :" )
ListNumber= getsequence.split(',')
print("Answer 1" )
print(ListNumber)

# End#

"""
#2. Create the below pattern using nested for loop in Python.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
print("Answer 2")
print("* " * 1 )
print("* " * 2)
print("* " * 3)
print("* " * 4)
print("* " * 5)
print("* " * 4)
print("* " * 3)
print("* " * 2)
print("* " * 1)


#3.3.  Write a Python program to reverse a word after accepting the input from the user. 
 #Sample Output: 
 #Input word: AcadGild 
 #Output: dilGdacA 
 

wordreverse=input("Enter any word for reversing: ")
print("Answer 3")
print("Reversed Word:"+ wordreverse[::-1])


#
#4.4.  Write a Python Program to print the given string in the format specified in the â€‹sample output. 
 
#WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens 
 
#Sample Output: 
print("Answer 4")
print("WE, THE PEOPLE OF INDIA")
print("    having solemnly resolved to constitute India into a SOVEREIGN, !")
print("        SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC ")
print("        and to secure to all its citizens")
    