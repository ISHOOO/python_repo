n=eval(input("Enter a number: "))
for i in range(2*n-1):
    if i<n:
        print(" "*i+"* "*(n-i))
    else:
        print(" "*(2*n-i-2)+"* "*(i-n+2))
"""
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
    * * 
   * * * 
  * * * * 
 * * * * *
* * * * * *
"""