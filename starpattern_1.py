n=eval(input("Enter a number: "))
for i in range (n*2-1):
    if(i<n):
        for k in range (n,i,-1):
            print(end=" ")
        for j in range(i+1):
            print("*",end=" ")
    else:
        for k in range (n,i+2):
            print(end=" ")
        for j in range (i,n*2-1):
            print("*",end=" ")
    print()