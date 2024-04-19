n=eval(input("Enter a number: "))
for i in range(n):
    x=1
    for j in range(i+1):
        print(x,end=" ")
        x+=1
    print()