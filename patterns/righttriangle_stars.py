n=eval(input("Enter a number: "))
for i in range(1,n*2):
    if i<=n:
        print(("* "*i).center(n*2-1))
    else:
        print(("* "*(2*n-i)).center(n*2-1))
"""
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
"""