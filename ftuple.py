""" 
Name : Milan George Mathew
Class : S4 DS
Roll No : 39
Experiment : 8 - Tuple Format
Date : 28 - 02 - 2024
"""


n = int(input("Enter Number of Elements in tuple: "))
print("Enter Elements: ")
intarr=list()
for i in range(0,n):
    num=int(input(f"[{i+1}]: "))
    intarr.append(num)
tup=tuple(intarr)

pevenlist=[]
poddlist=[]
vevenlist=[]
voddlist=[]

for i in range(0,n):
    if i%2==0:
        pevenlist.append(tup[i])
    else: 
        poddlist.append(tup[i])
    if tup[i]%2==0:
        vevenlist.append(tup[i])
    else:
        voddlist.append(tup[i])

peventup=tuple(pevenlist)
poddtup=tuple(poddlist)
veventup=tuple(vevenlist)
voddtup=tuple(voddlist)

print(f"Even tuple (position) : {peventup}")
print(f"Odd tuple (position) : {poddtup}")
print(f"Even tuple (value) : {veventup}")
print(f"Odd tuple (value) : {voddtup}")
