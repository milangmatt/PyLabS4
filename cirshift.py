n = int(input("Enter Number of Elements: "))
print("Enter Elements: ")
intarr=list()
for i in range(0,n):
    num=int(input(f"[{i+1}]: "))
    intarr.append(num)
print(f"Entered list is {intarr}\n\n")
shift = int(input("Enter number of elements to shift: "))
lshift=len(intarr)-shift
intarr=intarr[lshift:]+intarr[:lshift]
print(f"New list is {intarr}")