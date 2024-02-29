f=open("numbers.txt")
f=f.read()
for i in range(2,int((num//2)+1)):
		if(num%i!=0):
			flag=0
		else:
			flag=1
if(flag==0):
	print("the number  prime:",f)
else:
    print("the number is note prime")	