n=eval(input("Enter a number: "))
print(" "*i+"* "*(n-i)) if i<n else print(" "*(2*n-i-2)+"* "*(i-n+2)) for i in range(2*n-1)
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
