n=eval(input("Enter a number: "))
for i in range(n):
    x=1
    for j in range(i+1):
        print(x,end=" ")
        x+=1
    print()
"""
1   
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
"""