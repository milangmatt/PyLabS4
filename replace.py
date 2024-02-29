"""
Name : Milan George Mathew
Class : S4 DS
Roll No : 39
Experiment : 4 - Replace words in a String
Date : 14 - 02 -2024
"""

instr = input("Enter a string: ")
dele = input("Enter a string to be replaced: ")
rep = input("Enter a string to replace: ")

inarr= instr.split()
repcount = 0
for i in range (0,len(inarr)):
    if inarr[i] == dele:
        inarr[i] = rep
        repcount+=1

print(f"replaced string ({repcount} replaces of {len(inarr)} words): \n{' '.join(inarr)}")
