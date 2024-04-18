n=eval(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        if j<=i or j>=n-i-1 or j==0 or j==n-1:
            if j<i and j>n-i-1:
                print("  ",end="")
            else:
                print("* ",end="")
        else:
            print("  ",end="")
    print() 