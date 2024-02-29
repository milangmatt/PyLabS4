upper = int(input("Enter upper Limit: "))
lower = int(input("Enter lower Limit: "))
for i in range(lower, upper+1):
	for j in range(2,i):
		if i%j!=0:
			flag=1
		else:
			flag=0
			break
	if(flag==1):
		print(i, end="  ")

