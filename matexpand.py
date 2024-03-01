r = int(input("Enter Order of Square matrix : "))
mat=list()

print("Enter Elements of Matrix : ")
for i in range(0,r):
    ls=list()
    for j in range(0,r):
        num=int(input(f"[{i+1}][{j+1}]: "))
        ls.append(num)
    mat.append(ls)

#rowsum
rowsum = list()
for i in range(0,r):
    sum=0
    for j in range(0,r):
        sum+=mat[i][j]
    rowsum.append(sum)

#column sum 
columnsum = list()
for i in range(0,r):
    sum=0
    for j in range(0,r):
        sum+= mat[j][i]
    columnsum.append(sum)
        

#diagonal sum 
diasum=0
for i in range(0,r):
    diasum+=mat[i][i]
    mat[i].append(rowsum[i])

columnsum.append(diasum)
mat.append(columnsum)


print("Expanded Matrix: ")
for i in range(0,r+1):
    for j in range(0,r+1):
        print(f"{mat[i][j]}\t",end=" ")
    print() 