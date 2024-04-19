n=eval(input("Enter a number: "))
for i in range(n):
    print("*"*(n-i)+" "*(2*i-1),end="")
    if i==0:
        print("*"*(n-1))
    else:
        print("*"*(n-i)) 
"""
***********
***** *****
****   ****
***     ***
**       **
*         *
"""