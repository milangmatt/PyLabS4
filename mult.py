"""
Name : Milan George Mathew
Class : S4 DS
Roll No : 39
Experiment : 2 - Multiplication Table
Date : 31 - 01 -2024
"""
num = int(input("Enter a number: "))
limit = int(input("Enter a limit: "))
for i in range (1, limit+1):
	print(f"{num} x {i} = {num*i}")
