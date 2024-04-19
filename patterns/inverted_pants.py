n=eval(input("Enter a number: "))
for i in range(n-1,-1,-1):
    print("*"*(n-i)+" "*(2*i-1),end="")
    if i==0:
        print("*"*(n-1))
    else:
        print("*"*(n-i))
"""
*       *
**     **
***   ***
**** ****
*********
"""