n=eval(input("Enter a number: "))
x=1
for i in range(n):
    print(" "*(n-i-1)+f"{x} "*(i+1))
    x+=1