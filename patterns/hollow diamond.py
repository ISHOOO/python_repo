n=eval(input("Enter a number: "))
for i in range(1,n*2):
    if i<=n:                                # upper half
        print(" "*(n-i)+"*",end="")
        if i==1:
            print()
        print(" "*(2*i-3),end="")
        if i>1:
            print("*")
    else:                                   #lower half 
        print(" "*(i-n)+"*",end="")
        print(" "*(4*n-2*i-3),end="")
        if i<(n*2-1):
            print("*")
"""
     *
    * *
   *   *
  *     *
 *       *
*         *
 *       *
  *     *
   *   *
    * *
     *
"""