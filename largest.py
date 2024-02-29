"""
Name : Milan George Mathew
Class : S4 DS
Roll No : 39
Experiment : 1 -  Largest of Three
Date : 31 - 01 -2024
"""
a = int(input("Enter variable a: "))
b = int(input("Enter variable b: "))
c = int(input("Enter variable c: "))
if a > b:
	if a > c:
		print ( f" variable a ={a} is largest " ) 
	else:
		print ( f" variable c ={c} is largest " )
		 
else:
	if b > c:
		print ( f" variable b ={b} is largest " ) 
	else:
		print (f" variable c ={c} is largest " )		
