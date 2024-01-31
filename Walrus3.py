"""Walrus ooperator(':='): 
   Performing assignment to a variable and executing an expression/ function at the same time. 
   Useful to reduce lines of code 
"""
def get_value():
    return None
if var := get_value():
    print(var)
else:
    print("No Value")
"""
Here with the walrus operator two tasks performed are:
1. var= get_value()
2. var==True
"""