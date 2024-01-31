n=eval(input("Enter a number: "))
for i in range(n):
    for k in range(i):
        print(end=" ")
    for j in range(n): 
        print("*",end=" ")
    print()