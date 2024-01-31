"""Walrus ooperator(':='): 
   Performing assignment to a variable and executing an expression/ function at the same time. 
   Useful to reduce lines of code. 
   """
user_input:str =input("Enter a string: ")
if(text:=len(user_input))>5:
    print(text, "\N{slightly smiling face}")
else:
    print(text,"\N{angry face}")
"""
here the two tasks performed in one line using walrus operator are:
1. text=len(user_input)
2. text>5 
"""