""" 
Name : Milan George Mathew
Class : S4 DS
Roll No : 39
Experiment : 6 - Remove Duplicates
Date : 28 - 02 - 2024
"""


n = int(input("Enter Number of Elements: "))
print("Enter Elements: ")
intarr=list()
for i in range(0,n):
    num=int(input(f"[{i+1}]: "))
    intarr.append(num)
ndp=1
print(f"Entered list is {intarr}\n\n")
for i in range(1,n):
    if intarr[i] not in intarr[:ndp]:
        intarr[ndp]=intarr[i]
        ndp+=1
intarr=intarr[:ndp]
print(f"List without duplicates : {intarr}")
