n=eval(input("Enter a number: "))
for i in range(n):
    print(" "*(n-i-1)+"*",end="")
    if i==0:
        print()
    print(" "*(2*i-1),end="")
    if (i>0):
       print("*")
"""
    *
   * *
  *   *
 *     *
*       *
"""