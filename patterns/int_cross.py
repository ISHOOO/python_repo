n=eval(input("enter a number: "))
for i in range(n):
    for j in range(n):
        if i==j or j==n-i-1:
            if i<n/2:
                print(i+1,end="")
            else:
                print(n-i,end="")
        else:
            print(end=" ")
    print()
"""
enter a number: 9
1       1
 2     2 
  3   3  
   4 4   
    5    
   4 4   
  3   3  
 2     2 
1       1
"""