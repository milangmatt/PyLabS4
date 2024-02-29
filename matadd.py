""" 
Name : Milan George Mathew
Class : S4 DS
Roll No : 39
Experiment : 7 - Matrix addition
Date : 28 - 02 - 2024
"""


r1 = int(input("Enter Number of rows in matrix 1: "))
c1 = int(input("Enter Number of columns in matrix 1: "))
r2 = int(input("Enter Number of rows in matrix 2: "))
c2 = int(input("Enter Number of columns in matrix 2: "))
if not(r1==r2 and c1==c2):
    print("Matrices not compatible\nExiting...")
    exit()
mat1=list()
mat2=list()


print("Enter Elements of Matrix 1: ")
for i in range(0,r1):
    ls=list()
    for j in range(0,c1):
        num=int(input(f"[{i+1}][{j+1}]: "))
        ls.append(num)
    mat1.append(ls)


print("Enter Elements of Matrix 2: ")
for i in range(0,r2):
    ls=list()
    for j in range(0,c2):
        num=int(input(f"[{i+1}][{j+1}]: "))
        ls.append(num)
    mat2.append(ls)


resmat=list()

for i in range(0,r1):
    ls=list()
    for j in range(0,c1):
        ls.append(mat1[i][j]+mat2[i][j])
    resmat.append(ls)

print("Sum Matrix: ")
for i in range(0,r1):
    for j in range(0,c1):
        print(f"{resmat[i][j]}\t",end=" ")
    print()