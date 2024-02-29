num = int(input("Enter a number: "))
temp=num
sum=0
while temp!=0:
	digit = temp%10
	sum += digit**3
	temp = temp//10
if sum == num:
	print(f"{num} is Armstrong Number")
else:
	print(f"{num} is not Armstrong Number")
