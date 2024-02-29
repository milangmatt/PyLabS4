def calc(num1,num2,op):
	if op == "+":
		return num1+num2
	elif op == "-":
		return num1-num2
	elif op == "*":
		return num1*num2
	elif op == "/":
		return num1/num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operation (+,-,/,*) : ")
print(f"Result = {calc(num1,num2,op)}")

