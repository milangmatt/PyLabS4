def sumn(n):
    sum = 0
    for i in range(1,n+1):
        sum=sum+i
    print(f"Sum of {n} natural numbers= {sum}")

n = int(input("Enter a number: "))
sumn(n)