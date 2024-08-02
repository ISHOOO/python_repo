n=eval(input("Enter a number: "))
x=1
for i in range(n):
    print(" "*(n-i-1)+f"{x} "*(i+1))
    x+=1
"""
    1     
   2 2    
  3 3 3   
 4 4 4 4  
5 5 5 5 5
"""