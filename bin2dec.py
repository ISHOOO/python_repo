n=eval(input("Enter a binary number:"))
x=0
sum=0
while(n):
    rem=n%10
    n=n//10
    sum+=rem*(2**x)
    x+=1
print(f"Decimal form: {sum}")