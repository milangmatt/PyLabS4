def fact(n):
    if n == 1:
        return 1
    else :
        return n*fact(n-1)
num = int(input("Enter a number: "))
print(f"factorial of {num} = {fact(num)}")